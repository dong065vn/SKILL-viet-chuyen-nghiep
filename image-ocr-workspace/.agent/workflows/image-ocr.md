---
description: Trích xuất văn bản từ ảnh chuyên nghiệp - OCR với thư mục input/output, hỗ trợ batch, AI cleanup và xuất nhiều định dạng
---

# Workflow: Image OCR Text Extractor

// turbo-all

## Tổng quan

Workflow trích xuất văn bản từ ảnh (JPG, PNG, WEBP, PDF scan, BMP, TIFF) bằng OCR đa engine với hỗ trợ:
- 📁 **Input folder**: Tự động quét và xử lý batch tất cả ảnh
- 📤 **Output folder**: Tổ chức kết quả với timestamp, metadata, nhiều format
- 🤖 **AI Cleanup**: Sử dụng Claude/LLM để hiệu chỉnh văn bản sau OCR
- 🌏 **Đa ngôn ngữ**: Tiếng Việt, Anh, Nhật, Trung, Hàn, và 100+ ngôn ngữ

---

## Bước 0: Kiểm tra môi trường (Auto-detect OCR Engines)

**Mục tiêu:** Phát hiện các engine OCR đã cài, không cần cấu hình thủ công.

```powershell
# Kiểm tra Tesseract (open-source OCR engine)
tesseract --version 2>$null && Write-Host "✅ Tesseract OCR đã cài" || Write-Host "❌ Chưa cài Tesseract"

# Kiểm tra Python + pytesseract, easyocr, paddleocr
python -c "import pytesseract; print('✅ pytesseract OK')" 2>$null
python -c "import easyocr; print('✅ EasyOCR OK')" 2>$null
python -c "import paddleocr; print('✅ PaddleOCR OK')" 2>$null

# Kiểm tra Pillow (image processing)
python -c "from PIL import Image; print('✅ Pillow OK')" 2>$null
```

**Nếu chưa cài, tự động lên plan cài đặt:**

```powershell
# Option A: Cài nhanh với pip (Windows)
pip install pytesseract pillow easyocr opencv-python rich

# Cài Tesseract OCR cho Windows:
winget install UB-Mannheim.TesseractOCR
# HOẶC tải từ: https://github.com/UB-Mannheim/tesseract/wiki

# Thêm language pack Tiếng Việt (sau khi cài Tesseract):
# Download vie.traineddata → C:\Program Files\Tesseract-OCR\tessdata\

# Option B: Cài đầy đủ với PaddleOCR (tốt nhất cho tiếng Việt)
pip install paddlepaddle paddleocr pillow rich
```

**Bảng so sánh engine:**

| Engine | Tiếng Việt | Tốc độ | Độ chính xác | Dùng khi |
|--------|-----------|--------|---------------|---------|
| EasyOCR | ⭐⭐⭐⭐ | Trung bình | Cao | Ảnh thực tế, scan |
| PaddleOCR | ⭐⭐⭐⭐⭐ | Nhanh | Rất cao | Default khuyến dùng |
| Tesseract | ⭐⭐⭐ | Rất nhanh | Trung bình | Batch lớn, text rõ |
| Azure Vision | ⭐⭐⭐⭐⭐ | Nhanh | Rất cao | Cần API key |

---

## Bước 1: Chuẩn bị thư mục Input/Output

**Mục tiêu:** Tạo cấu trúc thư mục chuẩn và quét ảnh đầu vào.

```powershell
# Script: Tạo cấu trúc thư mục
$PROJECT_ROOT = ".\ocr-workspace"

New-Item -ItemType Directory -Force -Path @(
    "$PROJECT_ROOT\input",        # Đặt ảnh vào đây
    "$PROJECT_ROOT\output\text",  # Kết quả .txt
    "$PROJECT_ROOT\output\md",    # Kết quả .md (có metadata)
    "$PROJECT_ROOT\output\json",  # Kết quả .json (structured)
    "$PROJECT_ROOT\logs"          # Log xử lý
)

Write-Host "📁 Cấu trúc thư mục:"
Write-Host "  ocr-workspace/"
Write-Host "  ├── input/          ← Đặt ảnh cần OCR vào đây"
Write-Host "  └── output/"
Write-Host "      ├── text/       ← Văn bản thuần"
Write-Host "      ├── md/         ← Markdown với metadata"
Write-Host "      └── json/       ← Dữ liệu structured"
```

**Quét và liệt kê ảnh trong input:**

```powershell
# Liệt kê tất cả ảnh được hỗ trợ
$SUPPORTED_EXT = @("jpg","jpeg","png","webp","bmp","tiff","tif","pdf")
$images = Get-ChildItem "$PROJECT_ROOT\input" -Recurse | 
    Where-Object { $SUPPORTED_EXT -contains $_.Extension.TrimStart('.').ToLower() }

Write-Host "📊 Tìm thấy $($images.Count) file ảnh trong input:"
$images | ForEach-Object { Write-Host "  - $($_.Name) ($([math]::Round($_.Length/1KB, 1)) KB)" }
```

---

## Bước 2: Cấu hình OCR

**Mục tiêu:** Xác định ngôn ngữ, engine, và chất lượng xử lý.

Hỏi người dùng (hoặc dùng mặc định):

```
🔧 Cấu hình OCR:
  [1] Ngôn ngữ: Tiếng Việt (vi) - mặc định
  [2] Engine: PaddleOCR - mặc định
  [3] AI Cleanup: Bật (dùng Claude để sửa lỗi OCR) - mặc định
  [4] Output format: TXT + MD + JSON - mặc định
  [5] Xử lý ảnh trước (pre-processing): Tự động - mặc định

  → Nhấn Enter để dùng mặc định, hoặc chỉnh sửa
```

**Map ngôn ngữ phổ biến:**
- `vi` = Tiếng Việt
- `en` = English  
- `zh-cn` = 简体中文
- `ja` = 日本語
- `ko` = 한국어
- `vi+en` = Tiếng Việt + English (mixed)

---

## Bước 3: Tiền xử lý ảnh (Image Pre-processing)

**Mục tiêu:** Tăng chất lượng ảnh trước khi OCR để có kết quả tốt hơn.

```bash
python .agent/skills/image-ocr/scripts/ocr_engine.py preprocess \
    --input "ocr-workspace/input/" \
    --output "ocr-workspace/input/processed/" \
    --enhance  # Tăng độ sharp, contrast, denoise
```

**Các bước tiền xử lý tự động:**
1. **Resize**: Scale lên nếu ảnh < 300 DPI
2. **Grayscale**: Chuyển về ảnh xám
3. **Denoise**: Loại bỏ nhiễu (Gaussian/Median filter)
4. **Contrast**: Tăng độ tương phản (CLAHE)
5. **Deskew**: Tự động xoay thẳng ảnh nghiêng
6. **Binarize**: Ngưỡng thích ứng (Otsu/Adaptive threshold)

---

## Bước 4: Thực hiện OCR

**Mục tiêu:** Trích xuất văn bản từ tất cả ảnh trong input.

```bash
# Single file
python .agent/skills/image-ocr/scripts/ocr_engine.py extract \
    --input "ocr-workspace/input/document.png" \
    --output "ocr-workspace/output/" \
    --lang vi \
    --engine paddleocr

# Batch processing (toàn bộ thư mục)
python .agent/skills/image-ocr/scripts/ocr_engine.py batch \
    --input "ocr-workspace/input/" \
    --output "ocr-workspace/output/" \
    --lang vi \
    --engine paddleocr \
    --format txt,md,json \
    --ai-cleanup  # Bật AI cleanup với Claude
```

**Progress output mẫu:**

```
📦 Batch OCR Mode - 5 files found
──────────────────────────────────────────
  📄 [1/5] invoice-2026-01.png        (342 KB)
     🔍 Pre-processing...  ✅
     🔤 OCR (PaddleOCR)... ✅ (1.2s)
     🤖 AI Cleanup...      ✅
     💾 Saved: output/md/invoice-2026-01_20260222.md

  📄 [2/5] contract-scan.jpg          (1.2 MB)
     🔍 Pre-processing...  ✅
     🔤 OCR (PaddleOCR)... ✅ (3.4s)
     🤖 AI Cleanup...      ✅
     💾 Saved: output/md/contract-scan_20260222.md

  ...

──────────────────────────────────────────
✅ Batch Complete! 5/5 thành công
⏱️  Tổng thời gian: 18.3s | Trung bình: 3.7s/file
```

---

## Bước 5: AI Text Cleanup (Tùy chọn)

**Mục tiêu:** Dùng Claude/LLM để sửa lỗi OCR, chuẩn hóa văn bản.

```bash
# Nếu bật --ai-cleanup, script tự động gọi Claude:
echo "
Bạn là chuyên gia hiệu đính văn bản OCR tiếng Việt.

Văn bản OCR dưới đây có thể có lỗi nhận dạng ký tự, lỗi dấu thanh,
từ bị tách sai, hoặc ký tự bị nhầm. Hãy:
1. Sửa các lỗi OCR rõ ràng (ví dụ: 'l' thành '1', 'O' thành '0')
2. Chuẩn hóa dấu câu và khoảng trắng
3. Giữ nguyên cấu trúc, bảng biểu, số liệu
4. KHÔNG thêm/bớt nội dung, chỉ sửa lỗi kỹ thuật

Văn bản OCR:
---
{OCR_RAW_TEXT}
---

Trả về văn bản đã hiệu chỉnh:
" | claude -
```

---

## Bước 6: Kiểm tra và xác nhận Output

**Mục tiêu:** Đảm bảo tất cả file đã được xử lý và output đầy đủ.

```powershell
# Kiểm tra output
$output_files = Get-ChildItem "ocr-workspace\output" -Recurse -File
Write-Host "`n📊 Kết quả xuất ra:"
Write-Host "  📁 output/text/  - $((Get-ChildItem 'ocr-workspace\output\text').Count) files .txt"
Write-Host "  📁 output/md/    - $((Get-ChildItem 'ocr-workspace\output\md').Count) files .md"
Write-Host "  📁 output/json/  - $((Get-ChildItem 'ocr-workspace\output\json').Count) files .json"
```

**Xem nội dung mẫu một file output `.md`:**

```markdown
# OCR Result: invoice-2026-01.png

## 📊 Metadata

| Field | Value |
|-------|-------|
| **File gốc** | invoice-2026-01.png |
| **Kích thước** | 342 KB (1920×1080 px) |
| **Engine** | PaddleOCR v2.7 |
| **Ngôn ngữ** | Tiếng Việt (vi) |
| **Độ tin cậy** | 94.3% |
| **Thời gian xử lý** | 1.2s |
| **AI Cleanup** | ✅ Claude claude-3-5-sonnet |
| **Ngày xử lý** | 2026-02-22 21:22 |

---

## 📝 Văn bản trích xuất

[Nội dung văn bản đã OCR và cleanup...]

---

## 🔢 Dữ liệu bổ sung

- **Số dòng**: 47
- **Số từ**: 312
- **Số ký tự**: 1,847
```

---

## Bước 7: Tổng kết và báo cáo

**Mục tiêu:** Xuất báo cáo tổng hợp của batch.

```powershell
python .agent/skills/image-ocr/scripts/ocr_engine.py report \
    --output "ocr-workspace/output/" \
    --report "ocr-workspace/logs/summary_$(Get-Date -Format 'yyyyMMdd_HHmmss').md"
```

**Báo cáo tổng hợp mẫu:**

```
╔══════════════════════════════════════════╗
║         OCR BATCH REPORT                ║
║         2026-02-22 21:22:19             ║
╠══════════════════════════════════════════╣
║  Tổng file xử lý     :  5               ║
║  Thành công          :  5 (100%)        ║
║  Thất bại            :  0               ║
║  Tổng thời gian      :  18.3s           ║
║  Trung bình/file     :  3.7s            ║
║  Độ tin cậy TB       :  91.8%           ║
║  Tổng từ trích xuất  :  1,423           ║
╠══════════════════════════════════════════╣
║  Engine: PaddleOCR | Lang: vi           ║
║  AI Cleanup: Claude ✅                   ║
╚══════════════════════════════════════════╝

📁 Output:
  - output/text/  → 5 files .txt
  - output/md/    → 5 files .md (với metadata)
  - output/json/  → 5 files .json (structured)
  - logs/summary_20260222_212219.md
```

---

## Xử lý lỗi

| Lỗi | Nguyên nhân | Giải pháp |
|-----|-------------|-----------|
| `TesseractNotFound` | Chưa cài hoặc chưa add PATH | Cài Tesseract, thêm vào PATH |
| `Low confidence (<50%)` | Ảnh quá mờ/nhỏ | Bật pre-processing, tăng DPI |
| `UnicodeError` | Encoding output | Dùng `--encoding utf-8` |
| `MemoryError` | Ảnh quá lớn | Chia nhỏ ảnh, giảm batch size |
| `PDF not supported` | Cần pdf2image | `pip install pdf2image poppler` |

---

## Ví dụ sử dụng nhanh

```bash
# 1. Chụp ảnh hóa đơn/tài liệu → đặt vào ocr-workspace/input/

# 2. Chạy OCR một lệnh
python .agent/skills/image-ocr/scripts/ocr_engine.py batch \
    --input ocr-workspace/input/ \
    --output ocr-workspace/output/ \
    --lang vi --engine paddleocr --ai-cleanup

# 3. Xem kết quả trong ocr-workspace/output/md/
```

---

## Cấu trúc thư mục hoàn chỉnh

```
image-ocr-workspace/
├── .agent/
│   ├── workflows/
│   │   └── image-ocr.md          ← Workflow này
│   └── skills/
│       └── image-ocr/
│           ├── SKILL.md
│           └── scripts/
│               └── ocr_engine.py  ← Script OCR chính
├── input/                         ← ĐẶT ẢNH VÀO ĐÂY
│   ├── document1.png
│   ├── invoice.jpg
│   └── contract-scan.pdf
└── output/                        ← KẾT QUẢ XUẤT RA
    ├── text/
    │   ├── document1_20260222.txt
    │   └── invoice_20260222.txt
    ├── md/
    │   ├── document1_20260222.md
    │   └── invoice_20260222.md
    ├── json/
    │   └── document1_20260222.json
    └── logs/
        └── summary_20260222_212219.md
```
