#!/usr/bin/env python3
"""
Crawl Engine - Web Scraping CLI Tool
Phân tích cấu trúc web, phát hiện data fields, crawl dữ liệu.

Usage:
    python crawl_engine.py --check <URL>
    python crawl_engine.py --analyze <URL>
    python crawl_engine.py --crawl <URL> --fields "field1,field2" [--max-pages N] [--output data.json]
"""

import argparse
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Thiếu thư viện. Chạy: pip install -r scripts/requirements.txt")
    sys.exit(1)

try:
    import cloudscraper
    HAS_CLOUDSCRAPER = True
except ImportError:
    HAS_CLOUDSCRAPER = False

# ─── Constants ────────────────────────────────────────────────────────────────

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
]

REQUEST_TIMEOUT = 15
RATE_LIMIT_SECONDS = 1.5
MAX_RETRIES = 3
_use_cloudscraper = False  # Auto-switches to True if standard requests get 403

# ─── Helper Functions ─────────────────────────────────────────────────────────


def get_session():
    """Create a requests session with default headers. Auto-uses cloudscraper if needed."""
    global _use_cloudscraper
    if _use_cloudscraper and HAS_CLOUDSCRAPER:
        session = cloudscraper.create_scraper(
            browser={"browser": "chrome", "platform": "windows", "desktop": True}
        )
        print("  🔄 Sử dụng CloudScraper (bypass anti-bot)")
    else:
        session = requests.Session()
    session.headers.update({
        "User-Agent": USER_AGENTS[0],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    })
    return session


def fetch_page(session, url, retries=MAX_RETRIES):
    """Fetch a page with retry logic. Auto-fallback to cloudscraper on 403."""
    global _use_cloudscraper
    for attempt in range(retries):
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            response.encoding = response.apparent_encoding or "utf-8"
            return response
        except requests.exceptions.HTTPError as e:
            if response.status_code == 403 and HAS_CLOUDSCRAPER and not _use_cloudscraper:
                print(f"  ⚠️ 403 Forbidden - Tự động chuyển sang CloudScraper...")
                _use_cloudscraper = True
                session = get_session()
                try:
                    response = session.get(url, timeout=REQUEST_TIMEOUT)
                    response.raise_for_status()
                    response.encoding = response.apparent_encoding or "utf-8"
                    print(f"  ✅ CloudScraper bypass thành công!")
                    return response
                except Exception as e2:
                    print(f"  ❌ CloudScraper cũng thất bại: {e2}")
                    return None
            elif attempt < retries - 1:
                wait = (attempt + 1) * 2
                print(f"  ⚠️ Lỗi lần {attempt + 1}, thử lại sau {wait}s: {e}")
                time.sleep(wait)
            else:
                print(f"  ❌ Không thể truy cập: {e}")
                return None
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                wait = (attempt + 1) * 2
                print(f"  ⚠️ Lỗi lần {attempt + 1}, thử lại sau {wait}s: {e}")
                time.sleep(wait)
            else:
                print(f"  ❌ Không thể truy cập: {e}")
                return None


def clean_text(text):
    """Clean extracted text: strip whitespace, collapse multiple spaces."""
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text.strip())
    return text


# ─── Check URL ────────────────────────────────────────────────────────────────


def check_url(url):
    """Check if URL is accessible and inspect robots.txt."""
    print(f"\n🔍 Kiểm tra URL: {url}")
    print("─" * 50)

    session = get_session()

    # Check main URL
    response = fetch_page(session, url)
    if not response:
        print("❌ Không thể truy cập website này.")
        return False

    print(f"✅ Website truy cập được (Status: {response.status_code})")
    print(f"📄 Content-Type: {response.headers.get('content-type', 'unknown')}")
    print(f"📦 Size: {len(response.content) / 1024:.1f} KB")

    # Check robots.txt
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    try:
        robots_resp = session.get(robots_url, timeout=5)
        if robots_resp.status_code == 200:
            print(f"\n📋 robots.txt tìm thấy tại: {robots_url}")
            # Simple check for Disallow rules
            disallowed = [
                line.split(":", 1)[1].strip()
                for line in robots_resp.text.split("\n")
                if line.strip().lower().startswith("disallow") and line.split(":", 1)[1].strip()
            ]
            if disallowed:
                print(f"⚠️ Có {len(disallowed)} đường dẫn bị giới hạn crawl")
        else:
            print("ℹ️ Không tìm thấy robots.txt (OK để crawl)")
    except Exception:
        print("ℹ️ Không kiểm tra được robots.txt")

    print("\n✅ URL hợp lệ, sẵn sàng phân tích!")
    return True


# ─── Analyze Page ─────────────────────────────────────────────────────────────


def analyze_page(url):
    """Analyze page structure and detect data fields."""
    print(f"\n🔍 Phân tích cấu trúc: {url}")
    print("─" * 50)

    session = get_session()
    response = fetch_page(session, url)
    if not response:
        return None

    soup = BeautifulSoup(response.text, "lxml")

    # Remove script, style, nav, footer
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    result = {
        "url": url,
        "title": clean_text(soup.title.string) if soup.title else "N/A",
        "fields": [],
        "page_type": "unknown",
        "pagination": None,
        "total_elements": 0,
    }

    print(f"📄 Tiêu đề trang: {result['title']}")

    # Detect page type and repeating elements
    fields = []

    # Strategy 1: Detect tables
    tables = soup.find_all("table")
    if tables:
        result["page_type"] = "table"
        print(f"\n📊 Phát hiện {len(tables)} bảng dữ liệu")
        for i, table in enumerate(tables):
            headers = table.find_all("th")
            rows = table.find_all("tr")
            if headers:
                for j, th in enumerate(headers):
                    text = clean_text(th.get_text())
                    if text:
                        fields.append({
                            "name": text,
                            "selector": f"table:nth-of-type({i+1}) td:nth-of-type({j+1})",
                            "type": "table_cell",
                            "count": max(0, len(rows) - 1),
                            "sample": "",
                        })
                # Get sample values from first data row
                first_row = table.find("tbody", recursive=False)
                if first_row:
                    first_row = first_row.find("tr")
                else:
                    data_rows = [r for r in rows if not r.find("th")]
                    first_row = data_rows[0] if data_rows else None
                if first_row:
                    cells = first_row.find_all("td")
                    for j, cell in enumerate(cells):
                        if j < len(fields):
                            fields[j]["sample"] = clean_text(cell.get_text())[:80]

    # Strategy 2: Detect repeating cards/items (articles, products, list items)
    repeating_patterns = [
        ("article", "article"),
        ("div.card", "card"),
        ("div.item", "item"),
        ("div.product", "product"),
        ("li.post", "post"),
        ("div.post", "post"),
        ("div.entry", "entry"),
        ("div.listing", "listing"),
        ("div.result", "result"),
    ]

    if not fields:
        for selector, ptype in repeating_patterns:
            elements = soup.select(selector)
            if len(elements) >= 3:
                result["page_type"] = ptype
                print(f"\n📦 Phát hiện {len(elements)} mục dạng '{ptype}'")
                # Analyze first element structure
                sample = elements[0]
                _extract_fields_from_element(sample, fields, len(elements))
                break

    # Strategy 3: Detect by common class patterns
    if not fields:
        # Find largest group of same-class siblings
        all_divs = soup.find_all(["div", "li", "article", "section"])
        class_groups = defaultdict(list)
        for div in all_divs:
            classes = div.get("class", [])
            if classes:
                key = " ".join(classes)
                class_groups[key].append(div)

        # Find biggest repeating group
        best_group = None
        best_count = 0
        for key, group in class_groups.items():
            if len(group) >= 3 and len(group) > best_count:
                # Check if elements have meaningful content
                sample_text = clean_text(group[0].get_text())
                if len(sample_text) > 20:
                    best_group = group
                    best_count = len(group)

        if best_group:
            result["page_type"] = "list"
            print(f"\n📦 Phát hiện {len(best_group)} mục lặp lại")
            _extract_fields_from_element(best_group[0], fields, len(best_group))

    # Strategy 4: Detect links collection
    if not fields:
        links = soup.find_all("a", href=True)
        meaningful_links = [
            a for a in links
            if clean_text(a.get_text()) and len(clean_text(a.get_text())) > 5
        ]
        if len(meaningful_links) >= 5:
            result["page_type"] = "links"
            fields.append({
                "name": "Tiêu đề (text)",
                "selector": "a",
                "type": "text",
                "count": len(meaningful_links),
                "sample": clean_text(meaningful_links[0].get_text())[:80],
            })
            fields.append({
                "name": "Đường link (href)",
                "selector": "a[href]",
                "type": "attribute:href",
                "count": len(meaningful_links),
                "sample": meaningful_links[0].get("href", "")[:80],
            })

    # Detect pagination
    pagination = _detect_pagination(soup, url)
    if pagination:
        result["pagination"] = pagination
        print(f"\n📑 Phát hiện phân trang: {pagination['type']}")

    # Add universal fields
    _add_universal_fields(soup, fields)

    result["fields"] = fields
    result["total_elements"] = max((f.get("count", 0) for f in fields), default=0)

    # Print summary
    print(f"\n{'═' * 50}")
    print(f"📊 KẾT QUẢ PHÂN TÍCH")
    print(f"{'═' * 50}")
    print(f"  Loại trang: {result['page_type']}")
    print(f"  Số trường phát hiện: {len(fields)}")
    print(f"  Phân trang: {'Có' if pagination else 'Không'}")
    print()

    if fields:
        print(f"{'─' * 50}")
        print(f"  Các trường dữ liệu phát hiện:")
        print(f"{'─' * 50}")
        for i, field in enumerate(fields, 1):
            star = "★" if field.get("count", 0) >= 3 else " "
            name = field["name"][:30].ljust(30)
            count = str(field.get("count", "?")).rjust(5)
            sample = field.get("sample", "")[:40]
            print(f"  {star} [{i:2d}] {name} | {count} items | VD: {sample}")
        print(f"{'─' * 50}")
    else:
        print("  ⚠️ Không phát hiện được trường dữ liệu rõ ràng.")
        print("  💡 Hãy nhập CSS selector hoặc mô tả trường cần cào.")

    return result


def _extract_fields_from_element(element, fields, count):
    """Extract potential data fields from a repeating element."""
    # Headings
    for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        found = element.find(tag)
        if found:
            text = clean_text(found.get_text())
            if text:
                fields.append({
                    "name": f"Tiêu đề ({tag})",
                    "selector": tag,
                    "type": "text",
                    "count": count,
                    "sample": text[:80],
                })
                # Check for link inside heading
                link = found.find("a", href=True)
                if link:
                    fields.append({
                        "name": "Link bài viết",
                        "selector": f"{tag} a[href]",
                        "type": "attribute:href",
                        "count": count,
                        "sample": link.get("href", "")[:80],
                    })
                break

    # Paragraphs (description)
    p_tag = element.find("p")
    if p_tag:
        text = clean_text(p_tag.get_text())
        if text and len(text) > 10:
            fields.append({
                "name": "Mô tả (description)",
                "selector": "p",
                "type": "text",
                "count": count,
                "sample": text[:80],
            })

    # Images
    img = element.find("img", src=True)
    if img:
        fields.append({
            "name": "Hình ảnh (image)",
            "selector": "img[src]",
            "type": "attribute:src",
            "count": count,
            "sample": img.get("src", "")[:80],
        })

    # Time/Date
    time_tag = element.find("time")
    if time_tag:
        fields.append({
            "name": "Ngày đăng (date)",
            "selector": "time",
            "type": "text",
            "count": count,
            "sample": clean_text(time_tag.get_text())[:80],
        })

    # Spans with specific classes
    for span in element.find_all("span"):
        classes = span.get("class", [])
        text = clean_text(span.get_text())
        if text and len(text) > 2:
            class_str = ".".join(classes) if classes else "span"
            if any(kw in class_str.lower() for kw in ["price", "gia", "cost", "amount"]):
                fields.append({
                    "name": "Giá (price)",
                    "selector": f"span.{class_str}",
                    "type": "text",
                    "count": count,
                    "sample": text[:80],
                })
            elif any(kw in class_str.lower() for kw in ["author", "writer", "tac-gia"]):
                fields.append({
                    "name": "Tác giả (author)",
                    "selector": f"span.{class_str}",
                    "type": "text",
                    "count": count,
                    "sample": text[:80],
                })
            elif any(kw in class_str.lower() for kw in ["category", "cat", "danh-muc", "tag"]):
                fields.append({
                    "name": "Danh mục (category)",
                    "selector": f"span.{class_str}",
                    "type": "text",
                    "count": count,
                    "sample": text[:80],
                })


def _add_universal_fields(soup, fields):
    """Add universally detectable fields."""
    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        fields.append({
            "name": "Meta Description",
            "selector": "meta[name=description]",
            "type": "attribute:content",
            "count": 1,
            "sample": meta_desc["content"][:80],
        })


def _detect_pagination(soup, base_url):
    """Detect pagination patterns on the page."""
    # Pattern 1: <a> with page numbers
    page_links = soup.select('a[href*="page="], a[href*="/page/"], a[href*="p="]')
    if page_links:
        hrefs = [urljoin(base_url, a.get("href", "")) for a in page_links]
        return {"type": "query_param", "links": hrefs[:10], "total_found": len(page_links)}

    # Pattern 2: Pagination nav
    pag_nav = soup.select(".pagination a, .pager a, nav.page a, .pages a")
    if pag_nav:
        hrefs = [urljoin(base_url, a.get("href", "")) for a in pag_nav]
        return {"type": "pagination_nav", "links": hrefs[:10], "total_found": len(pag_nav)}

    # Pattern 3: Next button
    next_btn = soup.select('a.next, a[rel="next"], .next a, a:contains("Next"), a:contains("Tiếp")')
    if next_btn:
        href = urljoin(base_url, next_btn[0].get("href", ""))
        return {"type": "next_button", "links": [href], "total_found": 1}

    return None


# ─── Crawl Data ───────────────────────────────────────────────────────────────


def crawl_data(url, fields_config, max_pages=10, output_file="crawl_output.json"):
    """Crawl data from website based on configured fields."""
    print(f"\n🕷️ BẮT ĐẦU CRAWL")
    print(f"{'═' * 50}")
    print(f"  URL: {url}")
    print(f"  Trường: {', '.join(f['name'] for f in fields_config)}")
    print(f"  Tối đa: {max_pages} trang")
    print(f"{'═' * 50}\n")

    session = get_session()
    all_data = []
    urls_to_crawl = [url]
    crawled_urls = set()
    page_count = 0
    error_count = 0

    while urls_to_crawl and page_count < max_pages:
        current_url = urls_to_crawl.pop(0)

        if current_url in crawled_urls:
            continue

        page_count += 1
        crawled_urls.add(current_url)

        print(f"  📄 Trang {page_count}/{max_pages}: {current_url[:70]}...")

        response = fetch_page(session, current_url)
        if not response:
            error_count += 1
            continue

        soup = BeautifulSoup(response.text, "lxml")

        # Remove noise
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        # Extract data based on fields config
        page_data = _extract_data(soup, fields_config, current_url)
        if page_data:
            all_data.extend(page_data)
            print(f"    ✅ Thu được {len(page_data)} records (Tổng: {len(all_data)})")
        else:
            print(f"    ⚠️ Không tìm thấy dữ liệu trên trang này")

        # Find next pages
        if page_count < max_pages:
            pagination = _detect_pagination(soup, current_url)
            if pagination:
                for link in pagination["links"]:
                    if link not in crawled_urls and link not in urls_to_crawl:
                        urls_to_crawl.append(link)

        # Rate limiting
        if urls_to_crawl:
            time.sleep(RATE_LIMIT_SECONDS)

    # Save results
    output = {
        "source_url": url,
        "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_pages": page_count,
        "total_records": len(all_data),
        "errors": error_count,
        "fields": [f["name"] for f in fields_config],
        "data": all_data,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n{'═' * 50}")
    print(f"📊 KẾT QUẢ CRAWL")
    print(f"{'═' * 50}")
    print(f"  ✅ Tổng trang đã crawl: {page_count}")
    print(f"  ✅ Tổng records: {len(all_data)}")
    print(f"  ❌ Trang lỗi: {error_count}")
    print(f"  💾 Dữ liệu lưu tại: {output_file}")
    print(f"{'═' * 50}")

    return output


def _extract_data(soup, fields_config, base_url):
    """Extract data from soup based on field configurations."""
    records = []

    # Determine the repeating container
    # Try to find repeating elements that contain the first field
    first_field = fields_config[0]
    containers = []

    # Try common container patterns
    container_selectors = [
        "table tbody tr",
        "article",
        "div.card", "div.item", "div.product", "div.post",
        "div.entry", "div.listing", "div.result",
        "li",
    ]

    for selector in container_selectors:
        elements = soup.select(selector)
        if len(elements) >= 2:
            # Verify that elements contain the target fields
            test_elem = elements[0]
            if first_field["type"] == "table_cell":
                containers = elements
                break
            elif test_elem.select_one(first_field["selector"]):
                containers = elements
                break

    if not containers:
        # Fallback: extract fields globally (single record per page)
        record = {}
        for field in fields_config:
            value = _extract_field_value(soup, field, base_url)
            record[field["name"]] = value
        if any(record.values()):
            records.append(record)
        return records

    # Extract from each container
    for container in containers:
        record = {}
        for field in fields_config:
            value = _extract_field_value(container, field, base_url)
            record[field["name"]] = value
        if any(v for v in record.values() if v):
            records.append(record)

    return records


def _extract_field_value(element, field, base_url=""):
    """Extract a single field value from an element."""
    selector = field.get("selector", "")
    field_type = field.get("type", "text")

    try:
        if field_type == "table_cell":
            # For table cells, extract by column index
            match = re.search(r"nth-of-type\((\d+)\)", selector)
            if match:
                col_idx = int(match.group(1)) - 1
                cells = element.find_all("td")
                if col_idx < len(cells):
                    return clean_text(cells[col_idx].get_text())
            return ""

        target = element.select_one(selector) if selector else element
        if not target:
            return ""

        if field_type.startswith("attribute:"):
            attr_name = field_type.split(":", 1)[1]
            value = target.get(attr_name, "")
            # Make URLs absolute
            if attr_name in ("href", "src") and value and not value.startswith("http"):
                value = urljoin(base_url, value)
            return value
        else:
            return clean_text(target.get_text())
    except Exception:
        return ""


# ─── CLI ──────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="🕷️ Crawl Engine - Công cụ cào dữ liệu web",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", metavar="URL", help="Kiểm tra URL có truy cập được không")
    group.add_argument("--analyze", metavar="URL", help="Phân tích cấu trúc trang web")
    group.add_argument("--crawl", metavar="URL", help="Crawl dữ liệu từ website")

    parser.add_argument("--fields", help='Cấu hình trường (JSON string hoặc file path)')
    parser.add_argument("--max-pages", type=int, default=10, help="Số trang tối đa (mặc định: 10)")
    parser.add_argument("--output", default="crawl_output.json", help="File output (mặc định: crawl_output.json)")

    args = parser.parse_args()

    if args.check:
        success = check_url(args.check)
        sys.exit(0 if success else 1)

    elif args.analyze:
        result = analyze_page(args.analyze)
        if result:
            # Save analysis result
            analysis_file = "analysis_result.json"
            with open(analysis_file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"\n💾 Kết quả phân tích đã lưu: {analysis_file}")

    elif args.crawl:
        if not args.fields:
            print("❌ Cần chỉ định --fields khi crawl")
            print("   Ví dụ: --fields fields_config.json")
            sys.exit(1)

        # Load fields config
        if os.path.isfile(args.fields):
            with open(args.fields, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
        else:
            try:
                fields_config = json.loads(args.fields)
            except json.JSONDecodeError:
                print(f"❌ Không đọc được cấu hình trường: {args.fields}")
                sys.exit(1)

        crawl_data(args.crawl, fields_config, args.max_pages, args.output)


if __name__ == "__main__":
    main()
