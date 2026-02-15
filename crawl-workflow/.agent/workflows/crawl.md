---
description: Crawl dữ liệu web - Phân tích, gợi ý trường, xuất Excel/CSV/Word
---

# /crawl - Web Scraping CLI

## Cách dùng
```
/crawl [URL website mục tiêu]
```

## ⚠️ NGUYÊN TẮC VÀNG
> **LUÔN xác nhận với user trước mỗi bước quan trọng.**
> User là người quyết định: trường dữ liệu nào cào, format nào xuất.

## Quy trình 6 Phase

### Phase 1: 🎯 Nhận mục tiêu (Receive Target)
1. **Xác nhận URL từ user:**
   - Hỏi URL website cần crawl
   - Hỏi mục đích crawl (để gợi ý trường phù hợp hơn)
   - Kiểm tra URL hợp lệ, website có truy cập được không
2. **Kiểm tra cơ bản:**
   - Test kết nối: `python scripts/crawl_engine.py --check <URL>`
   - Xác nhận robots.txt (tôn trọng quy tắc crawl)
   - Tự động bypass anti-bot nếu bị chặn (CloudScraper)
   - Báo user nếu website chặn crawl

### Phase 2: 🔍 Phân tích cấu trúc (Analyze)
3. **Quét trang web:**
   - Chạy: `python scripts/crawl_engine.py --analyze <URL>`
   - Script tự động phân tích HTML structure
   - Tìm các repeating elements (tables, lists, cards, articles)
4. **Phát hiện dữ liệu:**
   - Xác định loại trang (tin tức, e-commerce, danh sách...)
   - Liệt kê tất cả data fields phát hiện được
   - Phát hiện pagination pattern (nếu có)

### Phase 3: ✅ Xác nhận trường dữ liệu (Confirm Fields)
5. **Gợi ý trường dữ liệu cho user:**
   - Hiển thị danh sách fields phát hiện được
   - Đánh dấu fields khuyến nghị (★)
   - Ví dụ output:
     ```
     Phát hiện các trường dữ liệu:
     ★ [1] Tiêu đề (title)         - 50 items found
     ★ [2] Đường link (url)         - 50 items found
       [3] Mô tả (description)      - 48 items found
       [4] Ngày đăng (date)         - 50 items found
       [5] Hình ảnh (image_url)     - 45 items found
     
     Chọn trường cần cào (VD: 1,2,4) hoặc nhập trường tùy chỉnh:
     ```
6. **User xác nhận:**
   - User chọn từ danh sách HOẶC tự nhập trường custom
   - Nếu user nhập custom → hướng dẫn chỉ CSS selector hoặc mô tả
   - **⚠️ PHẢI có xác nhận rõ ràng trước khi crawl**

### Phase 4: 🕷️ Thực thi Crawl (Execute)
7. **Chạy crawl:**
   - `python scripts/crawl_engine.py --crawl <URL> --fields "field1,field2" --max-pages <N>`
   - Hiển thị progress: trang đang crawl, số records thu được
   - Rate limiting tự động (1-2 giây/request)
8. **Xử lý lỗi:**
   - Retry 3 lần nếu request failed
   - Skip trang lỗi, tiếp tục crawl
   - Tự động chuyển CloudScraper nếu bị 403
   - Báo cáo tổng kết sau khi crawl xong

### Phase 5: 👀 Preview & Chọn Format (Preview)
9. **Hiển thị preview dữ liệu:**
   - `python scripts/export_data.py --preview <data_file>`
   - Hiện 5-10 dòng đầu dưới dạng bảng
   - Thống kê: tổng records, tổng trang đã crawl
10. **User chọn format xuất:**
    ```
    Chọn định dạng xuất file:
    [1] Excel (.xlsx) - Có format bảng, colors
    [2] CSV (.csv)    - Nhẹ, mở được mọi nơi
    [3] Word (.docx)  - Có format bảng đẹp
    [4] Tất cả        - Xuất cả 3 file
    ```
    - **⚠️ PHẢI có xác nhận của user trước khi xuất**

### Phase 6: 📄 Xuất File (Export)
11. **Render file (tự tạo folder riêng):**
    - `python scripts/export_data.py --export <format> --input <data>`
    - Tự động tạo thư mục: `output/{domain}_{timestamp}/`
    - Excel: Bảng có header bold, auto-width columns, zebra stripes
    - CSV: UTF-8 BOM encoding (mở đúng tiếng Việt trong Excel)
    - Word: Bảng có format, tiêu đề, ngày xuất
    - JSON: Copy dữ liệu gốc vào cùng folder
12. **Báo cáo kết quả:**
    - Đường dẫn folder output
    - Danh sách files đã xuất + kích thước
    - Tổng số records

## Cấu trúc folder
```
crawl-workflow/
├── .agent/workflows/
│   └── crawl.md          # Workflow này
├── scripts/
│   ├── crawl_engine.py   # Engine cào + phân tích
│   ├── export_data.py    # Xuất Excel/CSV/Word
│   └── requirements.txt  # Python dependencies
├── output/               # 📁 Tự động tạo khi xuất
│   └── {domain}_{timestamp}/
│       ├── crawl_data.json
│       ├── crawl_data.xlsx
│       ├── crawl_data.csv
│       └── crawl_data.docx
└── README.md
```

## Dependencies
```bash
pip install -r scripts/requirements.txt
```

## ❌ Anti-patterns (TRÁNH)
- Crawl mà chưa xác nhận trường dữ liệu với user
- Xuất file mà chưa cho user preview
- Crawl quá nhanh (không rate limit) → bị block
- Bỏ qua robots.txt
- Không báo lỗi khi website chặn crawl

## Output
- Folder riêng chứa tất cả file output
- File dữ liệu theo format user chọn (Excel/CSV/Word)
- Preview data trước khi xuất
- Báo cáo crawl (tổng trang, tổng records, lỗi)
