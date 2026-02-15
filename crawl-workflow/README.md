# 🕷️ Crawl Workflow - Công cụ cào dữ liệu web

Workflow CLI chuyên nghiệp crawl dữ liệu từ bất kỳ website nào, với quy trình xác nhận rõ ràng từng bước.

## ⚡ Quick Start

```bash
# 1. Cài đặt dependencies
pip install -r scripts/requirements.txt

# 2. Kiểm tra URL
python scripts/crawl_engine.py --check https://example.com

# 3. Phân tích cấu trúc
python scripts/crawl_engine.py --analyze https://example.com

# 4. Crawl dữ liệu
python scripts/crawl_engine.py --crawl https://example.com --fields fields_config.json --max-pages 10

# 5. Preview dữ liệu
python scripts/export_data.py --preview crawl_output.json

# 6. Xuất file (tự tạo folder output riêng)
python scripts/export_data.py --export all --input crawl_output.json
```

## 📁 Output Structure

Khi xuất file, tự động tạo folder riêng:

```
output/
└── example_com_20260215_140028/
    ├── crawl_data.json   # Dữ liệu gốc
    ├── crawl_data.xlsx   # Excel (formatted)
    ├── crawl_data.csv    # CSV (UTF-8 BOM)
    └── crawl_data.docx   # Word (bảng đẹp)
```

## 🔧 Tính năng

- ✅ Tự động phân tích cấu trúc HTML
- ✅ Gợi ý trường dữ liệu
- ✅ Bypass anti-bot (CloudScraper)
- ✅ Rate limiting tự động
- ✅ Retry logic (3 lần)
- ✅ Tìm pagination tự động
- ✅ Xuất Excel/CSV/Word format đẹp
- ✅ Tự tạo folder output riêng

## 📋 Workflow

Gõ `/crawl [URL]` để bắt đầu quy trình 6 bước:

1. **Nhận URL** → Kiểm tra accessibility
2. **Phân tích** → Detect data fields
3. **Xác nhận** → User chọn trường ⚠️
4. **Crawl** → Thu thập dữ liệu
5. **Preview** → User chọn format ⚠️
6. **Export** → Xuất file vào folder riêng
