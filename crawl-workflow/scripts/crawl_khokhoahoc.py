"""
Crawl khokhoahoc.org - Lọc khóa học theo chủ đề.
Tìm tất cả khóa học liên quan đến: AI, Python, SEO, Veo 3, Affiliate, TikTok, YouTube
Trường: Tên khóa học, Giá gốc, Giá sale, Link khóa học
"""
import cloudscraper
from bs4 import BeautifulSoup
import json
import time
import re
from urllib.parse import urljoin

# Keywords to filter
KEYWORDS = [
    "ai", "chatgpt", "gpt", "gemini", "copilot", "midjourney", "claude",
    "python",
    "seo",
    "veo 3", "veo3", "veo",
    "affiliate", "affilate", "tiếp thị liên kết",
    "tiktok", "tik tok",
    "youtube",
]

BASE_URL = "https://khokhoahoc.org/"

def match_keywords(title):
    """Check if title matches any keyword."""
    title_lower = title.lower()
    matched = []
    for kw in KEYWORDS:
        if kw in title_lower:
            matched.append(kw)
    return matched


def crawl_page(scraper, url):
    """Crawl a single page for products."""
    print(f"  📄 Đang crawl: {url[:70]}...")
    
    try:
        r = scraper.get(url, timeout=15)
        r.raise_for_status()
    except Exception as e:
        print(f"  ❌ Lỗi: {e}")
        return [], []
    
    soup = BeautifulSoup(r.text, "lxml")
    products = soup.select(".product-small.box")
    
    results = []
    for product in products:
        # Title + Link
        title_el = product.select_one(".box-text .title-wrapper a")
        if not title_el:
            title_el = product.select_one(".name a")
        if not title_el:
            continue
        
        title = title_el.get_text().strip()
        link = title_el.get("href", "")
        if link and not link.startswith("http"):
            link = urljoin(url, link)
        
        # Check keywords
        matched = match_keywords(title)
        if not matched:
            continue
        
        # Prices
        price_wrapper = product.select_one(".price-wrapper, .price")
        old_price = ""
        new_price = ""
        
        if price_wrapper:
            del_el = price_wrapper.select_one("del")
            ins_el = price_wrapper.select_one("ins")
            
            if del_el and ins_el:
                old_price = del_el.get_text().strip()
                new_price = ins_el.get_text().strip()
            else:
                # Single price only
                amounts = price_wrapper.select(".amount")
                if amounts:
                    new_price = amounts[0].get_text().strip()
                else:
                    new_price = price_wrapper.get_text().strip()
        
        # Clean price text
        old_price = re.sub(r'\s+', '', old_price).replace('Giá gốc:', '').replace('Giá hiện tại:', '')
        new_price = re.sub(r'\s+', '', new_price).replace('Giá gốc:', '').replace('Giá hiện tại:', '')
        
        results.append({
            "Tên khóa học": title,
            "Giá gốc": old_price,
            "Giá sale": new_price,
            "Link khóa học": link,
            "Chủ đề": ", ".join(matched),
        })
    
    # Find pagination links (next pages)
    next_pages = []
    pag_links = soup.select(".page-numbers a, a.next, a[rel='next']")
    for a in pag_links:
        href = a.get("href", "")
        if href and href not in next_pages:
            next_pages.append(href)
    
    return results, next_pages


def find_category_pages(scraper):
    """Find category/search pages that might have more courses."""
    print("\n🔍 Tìm trang danh mục liên quan...")
    
    # Try category pages and search
    extra_urls = []
    
    # Search by each keyword group
    search_terms = ["ai", "python", "seo", "veo", "affiliate", "tiktok", "youtube"]
    for term in search_terms:
        search_url = f"{BASE_URL}?s={term}&post_type=product"
        extra_urls.append((search_url, term))
    
    return extra_urls


def main():
    print("🕷️ CRAWL KHOKHOAHOC.ORG")
    print("═" * 60)
    print("  Chủ đề: AI, Python, SEO, Veo 3, Affiliate, TikTok, YouTube")
    print("  Trường: Tên khóa học, Giá gốc, Giá sale, Link khóa học")
    print("═" * 60)
    
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "desktop": True}
    )
    
    all_results = []
    seen_titles = set()
    
    # Step 1: Crawl main page
    print("\n📌 Bước 1: Crawl trang chủ...")
    results, _ = crawl_page(scraper, BASE_URL)
    for r in results:
        if r["Tên khóa học"] not in seen_titles:
            seen_titles.add(r["Tên khóa học"])
            all_results.append(r)
    print(f"  ✅ Tìm thấy {len(results)} khóa học phù hợp trên trang chủ")
    
    # Step 2: Search by keywords for more results
    print("\n📌 Bước 2: Tìm kiếm thêm theo từ khóa...")
    search_urls = find_category_pages(scraper)
    
    for search_url, term in search_urls:
        time.sleep(1.5)  # Rate limit
        print(f"\n  🔎 Tìm kiếm: '{term}'")
        results, next_pages = crawl_page(scraper, search_url)
        
        new_count = 0
        for r in results:
            if r["Tên khóa học"] not in seen_titles:
                seen_titles.add(r["Tên khóa học"])
                all_results.append(r)
                new_count += 1
        
        if results:
            print(f"    ✅ {len(results)} kết quả, {new_count} mới")
        
        # Follow pagination
        crawled_pages = {search_url}
        pages_to_crawl = [p for p in next_pages if p not in crawled_pages]
        page_num = 1
        
        while pages_to_crawl and page_num < 5:  # Max 5 pages per search
            page_num += 1
            next_url = pages_to_crawl.pop(0)
            if next_url in crawled_pages:
                continue
            crawled_pages.add(next_url)
            
            time.sleep(1.5)
            results, more_pages = crawl_page(scraper, next_url)
            
            new_count = 0
            for r in results:
                if r["Tên khóa học"] not in seen_titles:
                    seen_titles.add(r["Tên khóa học"])
                    all_results.append(r)
                    new_count += 1
            
            if results:
                print(f"    ✅ Trang {page_num}: {len(results)} kết quả, {new_count} mới")
            
            for p in more_pages:
                if p not in crawled_pages and p not in pages_to_crawl:
                    pages_to_crawl.append(p)
    
    # Save results
    output_file = "crawl_output.json"
    output = {
        "source_url": BASE_URL,
        "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "keywords": "AI, Python, SEO, Veo 3, Affiliate, TikTok, YouTube",
        "total_records": len(all_results),
        "fields": ["Tên khóa học", "Giá gốc", "Giá sale", "Link khóa học", "Chủ đề"],
        "data": all_results,
    }
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print(f"\n{'═' * 60}")
    print(f"📊 KẾT QUẢ CRAWL")
    print(f"{'═' * 60}")
    print(f"  ✅ Tổng khóa học tìm được: {len(all_results)}")
    print(f"  💾 Dữ liệu lưu tại: {output_file}")
    
    # Show breakdown by topic
    topic_count = {}
    for r in all_results:
        for topic in r["Chủ đề"].split(", "):
            topic_count[topic] = topic_count.get(topic, 0) + 1
    
    print(f"\n  📋 Phân theo chủ đề:")
    for topic, count in sorted(topic_count.items(), key=lambda x: -x[1]):
        print(f"    • {topic}: {count} khóa học")
    
    # Preview first 5
    print(f"\n{'─' * 60}")
    print(f"  Preview 5 khóa học đầu tiên:")
    print(f"{'─' * 60}")
    for i, r in enumerate(all_results[:5], 1):
        print(f"  {i}. {r['Tên khóa học'][:60]}")
        print(f"     Giá: {r['Giá gốc']} → {r['Giá sale']} | [{r['Chủ đề']}]")
    
    print(f"{'═' * 60}")


if __name__ == "__main__":
    main()
