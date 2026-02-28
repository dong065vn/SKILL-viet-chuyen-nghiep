# 🔤 Image OCR Workspace

Workspace chuyên nghiệp để trích xuất văn bản từ ảnh (OCR).

## 🚀 Cách dùng nhanh

```bash
# 1. Đặt ảnh vào thư mục input/
copy your-image.png input/

# 2. Chạy OCR
python .agent/skills/image-ocr/scripts/ocr_engine.py batch \
    --input input/ --output output/ --lang vi --engine paddleocr

# 3. Xem kết quả trong output/md/
```

## 📁 Cấu trúc

```
image-ocr-workspace/
├── input/              ← ĐẶT ẢNH VÀO ĐÂY
├── output/
│   ├── text/           ← Văn bản thuần (.txt)
│   ├── md/             ← Markdown với metadata (.md)
│   ├── json/           ← Dữ liệu JSON structured (.json)
│   └── logs/           ← Báo cáo batch
└── .agent/
    ├── workflows/
    │   └── image-ocr.md       ← Workflow hướng dẫn
    └── skills/image-ocr/
        ├── SKILL.md           ← Mô tả skill
        └── scripts/
            └── ocr_engine.py  ← Script OCR chính
```

## 🔧 Cài đặt

```bash
# Option 1: PaddleOCR (Khuyến dùng - tốt nhất cho tiếng Việt)
pip install paddlepaddle paddleocr pillow opencv-python rich

# Option 2: EasyOCR
pip install easyocr pillow opencv-python rich

# Option 3: Tesseract (cần cài thêm binary)
pip install pytesseract pillow rich
winget install UB-Mannheim.TesseractOCR
```

## 📖 Xem workflow đầy đủ

→ [.agent/workflows/image-ocr.md](.agent/workflows/image-ocr.md)
