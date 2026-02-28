---
name: image-ocr
description: Skill trích xuất văn bản từ ảnh chuyên nghiệp - OCR đa engine (PaddleOCR, EasyOCR, Tesseract) với thư mục input/output chuẩn hóa, hỗ trợ batch processing, AI text cleanup và xuất nhiều định dạng (TXT, MD, JSON). Dùng khi user cần OCR ảnh, hóa đơn scan, tài liệu chụp, ảnh chứa văn bản.
version: 1.0.0
category: document-processing
tags: [ocr, image, text-extraction, vietnamese, batch, pdf, scan]
platforms: [windows, mac, linux]
risk: safe
---

# Image OCR - Trích xuất văn bản từ ảnh

## Mục đích

Skill này tự động hóa việc trích xuất văn bản từ ảnh với workflow chuẩn hóa gồm:
1. **Input folder** → đặt ảnh cần OCR
2. **Pre-processing** → tăng chất lượng ảnh
3. **Multi-engine OCR** → PaddleOCR, EasyOCR, Tesseract  
4. **AI Cleanup** → Claude sửa lỗi OCR
5. **Output folder** → TXT, Markdown, JSON với metadata

## Khi nào dùng skill này

Invoke skill này khi:
- User muốn trích xuất văn bản từ ảnh, hình chụp, scan
- User cần OCR hóa đơn, hợp đồng, tài liệu scan
- User có batch nhiều ảnh cần xử lý hàng loạt
- User hỏi: "copy text từ ảnh", "scan văn bản", "trích xuất chữ từ hình"
- User cần convert ảnh → văn bản có thể chỉnh sửa

## Cách sử dụng

### Sử dụng script chính

```bash
# Single file
python .agent/skills/image-ocr/scripts/ocr_engine.py extract \
    --input "path/to/image.png" \
    --output "output/" \
    --lang vi \
    --engine paddleocr

# Batch (toàn bộ folder)
python .agent/skills/image-ocr/scripts/ocr_engine.py batch \
    --input "input/" \
    --output "output/" \
    --lang vi \
    --engine paddleocr \
    --format txt,md,json \
    --ai-cleanup

# Chỉ tiền xử lý ảnh
python .agent/skills/image-ocr/scripts/ocr_engine.py preprocess \
    --input "input/" \
    --output "input/processed/"
```

### Tham số dòng lệnh

| Tham số | Mô tả | Mặc định |
|---------|-------|---------|
| `--input` | File ảnh hoặc thư mục input | Bắt buộc |
| `--output` | Thư mục output | `./output` |
| `--lang` | Ngôn ngữ OCR | `vi` |
| `--engine` | paddleocr / easyocr / tesseract | `paddleocr` |
| `--format` | txt,md,json | `txt,md` |
| `--ai-cleanup` | Bật AI cleanup với Claude | Tắt |
| `--no-preprocess` | Tắt tiền xử lý ảnh | Tắt |
| `--dpi` | DPI tối thiểu (upscale nếu ảnh nhỏ) | `300` |

## Output Format

### Markdown (`.md`) — Khuyến dùng

```markdown
# OCR Result: filename.png

## 📊 Metadata
| Field | Value |
|-------|-------|
| Engine | PaddleOCR v2.7 |
| Ngôn ngữ | Tiếng Việt |
| Độ tin cậy | 94.3% |
| AI Cleanup | ✅ |
| Ngày xử lý | 2026-02-22 21:22 |

## 📝 Văn bản trích xuất
[nội dung...]
```

### JSON (`.json`) — Cho lập trình

```json
{
  "source_file": "document.png",
  "engine": "paddleocr",
  "language": "vi",
  "confidence": 0.943,
  "ai_cleaned": true,
  "text": "Nội dung văn bản...",
  "words": 312,
  "processed_at": "2026-02-22T21:22:19"
}
```

## Cấu trúc thư mục workspace

```
image-ocr-workspace/
├── input/          ← Đặt ảnh cần OCR vào đây
└── output/
    ├── text/       ← .txt thuần
    ├── md/         ← .md với metadata  
    ├── json/       ← .json structured
    └── logs/       ← Báo cáo batch
```

## Lưu ý quan trọng

- Script `scripts/ocr_engine.py` chứa toàn bộ logic OCR
- Yêu cầu cài đặt ít nhất 1 engine: `pip install paddlepaddle paddleocr pillow`
- Với Tesseract: cần cài riêng + language pack tiếng Việt
- AI Cleanup yêu cầu Claude CLI (`claude`) được cài sẵn trong PATH
- File output đặt tên theo format: `{tên_gốc}_{YYYYMMDD_HHMMSS}.{ext}`
