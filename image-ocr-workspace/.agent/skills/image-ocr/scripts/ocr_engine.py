#!/usr/bin/env python3
"""
ocr_engine.py - Professional OCR Engine cho Image Text Extraction
Version: 1.0.0
Skill: image-ocr
Hỗ trợ: PaddleOCR, EasyOCR, Tesseract
Output: TXT, Markdown, JSON với metadata đầy đủ
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ─── RICH UI (optional, fallback to plain print) ───────────────────────────────
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
    console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    class Console:
        def print(self, *args, **kwargs):
            text = " ".join(str(a) for a in args)
            print(text)
    console = Console()

# ─── SUPPORTED FORMATS ─────────────────────────────────────────────────────────
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".tif", ".gif"}
SUPPORTED_FORMATS_DISPLAY = "JPG, PNG, WEBP, BMP, TIFF"


# ══════════════════════════════════════════════════════════════════════════════
#  ENGINE DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def detect_engines() -> dict:
    """Auto-detect available OCR engines."""
    engines = {}
    
    # PaddleOCR
    try:
        import paddleocr  # noqa: F401
        engines["paddleocr"] = True
    except ImportError:
        engines["paddleocr"] = False

    # EasyOCR
    try:
        import easyocr  # noqa: F401
        engines["easyocr"] = True
    except ImportError:
        engines["easyocr"] = False

    # Tesseract
    try:
        import pytesseract  # noqa: F401
        pytesseract.get_tesseract_version()
        engines["tesseract"] = True
    except Exception:
        engines["tesseract"] = False

    return engines


def print_engine_status(engines: dict):
    """Print detected engine status."""
    console.print("\n🔍 [bold]Kiểm tra OCR Engines:[/bold]" if HAS_RICH else "\n🔍 Kiểm tra OCR Engines:")
    for name, available in engines.items():
        status = "✅" if available else "❌"
        label = name.upper()
        console.print(f"  {status} {label}")
    
    if not any(engines.values()):
        console.print("\n⚠️  Chưa cài engine nào! Chạy:")
        console.print("  pip install paddlepaddle paddleocr pillow")
        sys.exit(1)


# ══════════════════════════════════════════════════════════════════════════════
#  IMAGE PRE-PROCESSING
# ══════════════════════════════════════════════════════════════════════════════

def preprocess_image(image_path: Path, min_dpi: int = 300) -> Path:
    """
    Tiền xử lý ảnh để tăng chất lượng OCR:
    - Chuyển Grayscale
    - Denoise
    - Tăng Contrast (CLAHE)
    - Deskew (xoay thẳng)
    - Binarize (Otsu threshold)
    Returns: Path to processed image
    """
    try:
        import cv2
        import numpy as np
        from PIL import Image

        img = cv2.imread(str(image_path))
        if img is None:
            # Try PIL for formats OpenCV can't handle
            pil_img = Image.open(image_path).convert("RGB")
            img = np.array(pil_img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # 1. Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. Denoise
        denoised = cv2.fastNlMeansDenoising(gray, h=10)

        # 3. CLAHE contrast enhancement
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(denoised)

        # 4. Adaptive thresholding
        binary = cv2.adaptiveThreshold(
            enhanced, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )

        # 5. Check DPI / upscale if needed
        pil_img = Image.fromarray(binary)
        dpi_info = pil_img.info.get("dpi", (72, 72))
        current_dpi = dpi_info[0] if isinstance(dpi_info, tuple) else 72
        if current_dpi < min_dpi:
            scale = min_dpi / max(current_dpi, 72)
            new_w = int(pil_img.width * scale)
            new_h = int(pil_img.height * scale)
            pil_img = pil_img.resize((new_w, new_h), Image.LANCZOS)

        # Save processed image
        processed_dir = image_path.parent / "processed"
        processed_dir.mkdir(exist_ok=True)
        processed_path = processed_dir / f"{image_path.stem}_processed{image_path.suffix}"
        pil_img.save(str(processed_path))
        return processed_path

    except ImportError:
        console.print("⚠️  cv2/PIL không được cài. Bỏ qua pre-processing.")
        return image_path
    except Exception as e:
        console.print(f"⚠️  Pre-processing lỗi: {e}. Dùng ảnh gốc.")
        return image_path


# ══════════════════════════════════════════════════════════════════════════════
#  OCR ENGINES
# ══════════════════════════════════════════════════════════════════════════════

def ocr_paddleocr(image_path: Path, lang: str = "vi") -> tuple[str, float]:
    """OCR bằng PaddleOCR. Returns (text, confidence)."""
    from paddleocr import PaddleOCR
    
    # Map language codes
    lang_map = {"vi": "vi", "en": "en", "zh-cn": "ch", "ja": "japan", "ko": "korean"}
    paddle_lang = lang_map.get(lang, "vi")
    
    ocr = PaddleOCR(use_angle_cls=True, lang=paddle_lang, show_log=False)
    result = ocr.ocr(str(image_path), cls=True)
    
    lines = []
    confidences = []
    if result and result[0]:
        for line in result[0]:
            if line and len(line) >= 2:
                text_info = line[1]
                if isinstance(text_info, (list, tuple)) and len(text_info) >= 2:
                    lines.append(text_info[0])
                    confidences.append(text_info[1])
    
    text = "\n".join(lines)
    avg_conf = sum(confidences) / len(confidences) if confidences else 0.0
    return text, avg_conf


def ocr_easyocr(image_path: Path, lang: str = "vi") -> tuple[str, float]:
    """OCR bằng EasyOCR. Returns (text, confidence)."""
    import easyocr
    
    # EasyOCR language codes
    lang_map = {"vi": ["vi", "en"], "en": ["en"], "zh-cn": ["ch_sim", "en"], "ja": ["ja", "en"]}
    languages = lang_map.get(lang, ["vi", "en"])
    
    reader = easyocr.Reader(languages, gpu=False, verbose=False)
    result = reader.readtext(str(image_path))
    
    lines = [r[1] for r in result]
    confidences = [r[2] for r in result]
    
    text = "\n".join(lines)
    avg_conf = sum(confidences) / len(confidences) if confidences else 0.0
    return text, avg_conf


def ocr_tesseract(image_path: Path, lang: str = "vi") -> tuple[str, float]:
    """OCR bằng Tesseract. Returns (text, confidence)."""
    import pytesseract
    from PIL import Image
    
    # Tesseract language codes
    lang_map = {"vi": "vie", "en": "eng", "zh-cn": "chi_sim", "ja": "jpn", "ko": "kor"}
    tess_lang = lang_map.get(lang, "vie")
    
    img = Image.open(image_path)
    
    # Get confidence data
    data = pytesseract.image_to_data(img, lang=tess_lang, output_type=pytesseract.Output.DICT)
    
    # Filter and build text
    words = []
    confs = []
    for i, word in enumerate(data["text"]):
        if word.strip():
            words.append(word)
            conf = data["conf"][i]
            if conf > 0:
                confs.append(conf / 100.0)
    
    text = " ".join(words)
    avg_conf = sum(confs) / len(confs) if confs else 0.0
    return text, avg_conf


def run_ocr(image_path: Path, engine: str, lang: str) -> tuple[str, float]:
    """Dispatch OCR to appropriate engine."""
    dispatch = {
        "paddleocr": ocr_paddleocr,
        "easyocr": ocr_easyocr,
        "tesseract": ocr_tesseract,
    }
    func = dispatch.get(engine)
    if not func:
        raise ValueError(f"Engine không hỗ trợ: {engine}. Dùng: paddleocr, easyocr, tesseract")
    return func(image_path, lang)


# ══════════════════════════════════════════════════════════════════════════════
#  AI CLEANUP
# ══════════════════════════════════════════════════════════════════════════════

def ai_cleanup_text(raw_text: str, lang: str = "vi") -> str:
    """
    Dùng Claude CLI để hiệu chỉnh văn bản OCR.
    Yêu cầu: claude CLI được cài trong PATH
    """
    lang_name = {"vi": "Tiếng Việt", "en": "English", "zh-cn": "Tiếng Trung"}.get(lang, lang)
    
    prompt = f"""Bạn là chuyên gia hiệu đính văn bản OCR {lang_name}.

Văn bản OCR dưới đây có thể có lỗi nhận dạng ký tự, lỗi dấu thanh, từ bị tách sai, hoặc ký tự bị nhầm lẫn.

Nhiệm vụ:
1. Sửa các lỗi OCR rõ ràng (ví dụ: 'l' → '1', 'O' → '0', thiếu dấu thanh)
2. Chuẩn hóa dấu câu và khoảng trắng
3. Giữ nguyên cấu trúc đoạn văn, bảng biểu, số liệu
4. KHÔNG thêm bớt nội dung, chỉ sửa lỗi kỹ thuật OCR

Văn bản OCR gốc:
---
{raw_text}
---

Trả về CHÍNH XÁC văn bản đã hiệu chỉnh, không giải thích thêm:"""

    try:
        result = subprocess.run(
            ["claude", "-"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            return raw_text  # Fallback về raw nếu Claude lỗi
    except FileNotFoundError:
        console.print("⚠️  claude CLI không tìm thấy. Bỏ qua AI cleanup.")
        return raw_text
    except subprocess.TimeoutExpired:
        console.print("⚠️  AI cleanup timeout. Dùng văn bản gốc.")
        return raw_text


# ══════════════════════════════════════════════════════════════════════════════
#  OUTPUT GENERATORS
# ══════════════════════════════════════════════════════════════════════════════

def get_image_info(image_path: Path) -> dict:
    """Lấy thông tin ảnh (kích thước, định dạng)."""
    info = {
        "size_bytes": image_path.stat().st_size,
        "size_kb": round(image_path.stat().st_size / 1024, 1),
        "width": 0,
        "height": 0,
        "format": image_path.suffix.upper().lstrip(".")
    }
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            info["width"], info["height"] = img.size
            info["format"] = img.format or info["format"]
    except Exception:
        pass
    return info


def save_txt(text: str, output_path: Path):
    """Xuất văn bản thuần."""
    output_path.write_text(text, encoding="utf-8")


def save_markdown(
    text: str,
    source_file: Path,
    output_path: Path,
    engine: str,
    lang: str,
    confidence: float,
    processing_time: float,
    ai_cleaned: bool,
    img_info: dict
):
    """Xuất file Markdown với metadata đầy đủ."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word_count = len(text.split())
    char_count = len(text)
    line_count = len(text.splitlines())
    
    lang_display = {
        "vi": "Tiếng Việt (vi)",
        "en": "English (en)",
        "zh-cn": "简体中文 (zh-cn)",
        "ja": "日本語 (ja)",
        "ko": "한국어 (ko)"
    }.get(lang, lang)
    
    ai_status = "✅ Claude AI" if ai_cleaned else "❌ Tắt"
    engine_display = {
        "paddleocr": "PaddleOCR",
        "easyocr": "EasyOCR",
        "tesseract": "Tesseract OCR"
    }.get(engine, engine)
    
    md_content = f"""# OCR Result: {source_file.name}

## 📊 Metadata

| Field | Value |
|-------|-------|
| **File gốc** | `{source_file.name}` |
| **Kích thước** | {img_info['size_kb']} KB ({img_info['width']}×{img_info['height']} px) |
| **Định dạng** | {img_info['format']} |
| **Engine OCR** | {engine_display} |
| **Ngôn ngữ** | {lang_display} |
| **Độ tin cậy** | {confidence*100:.1f}% |
| **AI Cleanup** | {ai_status} |
| **Thời gian xử lý** | {processing_time:.2f}s |
| **Ngày xử lý** | {now} |

---

## 📝 Văn bản trích xuất

{text}

---

## 🔢 Thống kê

| Chỉ số | Giá trị |
|--------|--------|
| Số dòng | {line_count:,} |
| Số từ | {word_count:,} |
| Số ký tự | {char_count:,} |

---
*Generated by image-ocr skill v1.0.0 | Engine: {engine_display} | {now}*
"""
    output_path.write_text(md_content, encoding="utf-8")


def save_json(
    text: str,
    source_file: Path,
    output_path: Path,
    engine: str,
    lang: str,
    confidence: float,
    processing_time: float,
    ai_cleaned: bool,
    img_info: dict
):
    """Xuất file JSON structured."""
    data = {
        "source_file": source_file.name,
        "source_path": str(source_file.absolute()),
        "image": {
            "width": img_info["width"],
            "height": img_info["height"],
            "format": img_info["format"],
            "size_kb": img_info["size_kb"]
        },
        "ocr": {
            "engine": engine,
            "language": lang,
            "confidence": round(confidence, 4),
            "processing_time_s": round(processing_time, 2)
        },
        "ai_cleanup": {
            "enabled": ai_cleaned,
            "model": "claude" if ai_cleaned else None
        },
        "text": text,
        "stats": {
            "lines": len(text.splitlines()),
            "words": len(text.split()),
            "chars": len(text)
        },
        "processed_at": datetime.now().isoformat()
    }
    output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ══════════════════════════════════════════════════════════════════════════════
#  CORE PROCESSING FUNCTION
# ══════════════════════════════════════════════════════════════════════════════

def process_single_image(
    image_path: Path,
    output_dir: Path,
    engine: str,
    lang: str,
    formats: list,
    ai_cleanup: bool,
    preprocess: bool,
    min_dpi: int
) -> dict:
    """
    Xử lý một ảnh: preprocess → OCR → AI cleanup → save output.
    Returns: result dict
    """
    result = {
        "file": image_path.name,
        "success": False,
        "confidence": 0.0,
        "time": 0.0,
        "outputs": [],
        "error": None
    }
    
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    stem = image_path.stem

    try:
        # Step 1: Pre-processing
        working_image = image_path
        if preprocess:
            working_image = preprocess_image(image_path, min_dpi)

        # Step 2: OCR
        raw_text, confidence = run_ocr(working_image, engine, lang)
        
        # Step 3: AI Cleanup
        final_text = raw_text
        ai_cleaned = False
        if ai_cleanup and raw_text.strip():
            final_text = ai_cleanup_text(raw_text, lang)
            ai_cleaned = True

        elapsed = time.time() - start_time
        img_info = get_image_info(image_path)

        # Step 4: Save outputs
        for fmt in formats:
            fmt = fmt.strip().lower()
            if fmt == "txt":
                out_path = output_dir / "text" / f"{stem}_{timestamp}.txt"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                save_txt(final_text, out_path)
                result["outputs"].append(str(out_path))
            elif fmt == "md":
                out_path = output_dir / "md" / f"{stem}_{timestamp}.md"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                save_markdown(final_text, image_path, out_path, engine, lang,
                              confidence, elapsed, ai_cleaned, img_info)
                result["outputs"].append(str(out_path))
            elif fmt == "json":
                out_path = output_dir / "json" / f"{stem}_{timestamp}.json"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                save_json(final_text, image_path, out_path, engine, lang,
                         confidence, elapsed, ai_cleaned, img_info)
                result["outputs"].append(str(out_path))

        result["success"] = True
        result["confidence"] = confidence
        result["time"] = elapsed
        result["word_count"] = len(final_text.split())

    except Exception as e:
        result["error"] = str(e)
        result["time"] = time.time() - start_time

    return result


# ══════════════════════════════════════════════════════════════════════════════
#  COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def cmd_preprocess(args):
    """Chỉ tiền xử lý ảnh, không OCR."""
    input_path = Path(args.input)
    output_dir = Path(args.output) if args.output else input_path / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if input_path.is_file():
        images = [input_path]
    else:
        images = [f for f in input_path.rglob("*") if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    
    console.print(f"\n🔍 Tiền xử lý {len(images)} ảnh...")
    for i, img in enumerate(images, 1):
        console.print(f"  [{i}/{len(images)}] {img.name}...", end=" ")
        processed = preprocess_image(img, args.dpi)
        console.print(f"✅ → {processed.name}")
    
    console.print(f"\n✅ Hoàn thành! Output: {output_dir}")


def cmd_extract(args):
    """OCR một file ảnh."""
    image_path = Path(args.input)
    if not image_path.exists():
        console.print(f"❌ File không tồn tại: {image_path}")
        sys.exit(1)
    
    output_dir = Path(args.output) if args.output else Path("output")
    formats = args.format.split(",") if args.format else ["txt", "md"]
    
    console.print(f"\n📄 OCR: {image_path.name}")
    console.print(f"   Engine : {args.engine}")
    console.print(f"   Ngôn ngữ: {args.lang}")
    
    result = process_single_image(
        image_path, output_dir, args.engine, args.lang,
        formats, args.ai_cleanup, not args.no_preprocess, args.dpi
    )
    
    if result["success"]:
        console.print(f"\n✅ Hoàn thành!")
        console.print(f"   Độ tin cậy : {result['confidence']*100:.1f}%")
        console.print(f"   Số từ      : {result.get('word_count', 0):,}")
        console.print(f"   Thời gian  : {result['time']:.2f}s")
        console.print(f"\n📁 Output files:")
        for out in result["outputs"]:
            console.print(f"   - {out}")
    else:
        console.print(f"\n❌ Lỗi: {result['error']}")
        sys.exit(1)


def cmd_batch(args):
    """Batch OCR toàn bộ thư mục."""
    input_dir = Path(args.input)
    output_dir = Path(args.output) if args.output else Path("output")
    formats = args.format.split(",") if args.format else ["txt", "md"]
    
    # Tạo thư mục output
    for subdir in ["text", "md", "json", "logs"]:
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    # Quét ảnh
    if input_dir.is_file():
        images = [input_dir]
    else:
        images = sorted([f for f in input_dir.rglob("*") if f.suffix.lower() in SUPPORTED_EXTENSIONS
                        and "processed" not in str(f)])
    
    if not images:
        console.print(f"❌ Không tìm thấy ảnh nào trong: {input_dir}")
        console.print(f"   Hỗ trợ: {SUPPORTED_FORMATS_DISPLAY}")
        sys.exit(1)
    
    console.print(f"\n📦 Batch OCR Mode - {len(images)} files")
    console.print("─" * 50)
    
    results = []
    total_start = time.time()
    
    for i, image_path in enumerate(images, 1):
        console.print(f"\n  📄 [{i}/{len(images)}] {image_path.name}")
        
        if not args.no_preprocess:
            console.print("     🔍 Pre-processing...", end=" ")
        
        result = process_single_image(
            image_path, output_dir, args.engine, args.lang,
            formats, args.ai_cleanup, not args.no_preprocess, args.dpi
        )
        results.append(result)
        
        if result["success"]:
            conf_pct = result["confidence"] * 100
            console.print(f"     ✅ OCR ({args.engine}): {conf_pct:.1f}% tin cậy | {result['time']:.1f}s")
            for out in result["outputs"]:
                console.print(f"     💾 {Path(out).name}")
        else:
            console.print(f"     ❌ Lỗi: {result['error']}")
    
    # Summary
    total_time = time.time() - total_start
    success_count = sum(1 for r in results if r["success"])
    avg_conf = sum(r["confidence"] for r in results if r["success"]) / max(success_count, 1)
    total_words = sum(r.get("word_count", 0) for r in results if r["success"])
    
    console.print("\n" + "─" * 50)
    console.print(f"""
╔══════════════════════════════════════════╗
║         OCR BATCH REPORT                ║
║  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}              ║
╠══════════════════════════════════════════╣
║  Tổng file xử lý     :  {len(images):<3}              ║
║  Thành công          :  {success_count}/{len(images)} ({(success_count/len(images)*100):.0f}%)         ║
║  Tổng thời gian      :  {total_time:.1f}s            ║
║  Trung bình/file     :  {total_time/max(len(images),1):.1f}s            ║
║  Độ tin cậy TB       :  {avg_conf*100:.1f}%           ║
║  Tổng từ trích xuất  :  {total_words:,}           ║
╠══════════════════════════════════════════╣
║  Engine: {args.engine:<10} | Lang: {args.lang:<5}      ║
║  AI Cleanup: {'Claude ✅' if args.ai_cleanup else 'Tắt ❌'}                  ║
╚══════════════════════════════════════════╝
""")
    
    # Save summary report
    try:
        report_path = output_dir / "logs" / f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report = {
            "batch_summary": {
                "total_files": len(images),
                "success": success_count,
                "failed": len(images) - success_count,
                "total_time_s": round(total_time, 2),
                "avg_confidence": round(avg_conf, 4),
                "total_words": total_words,
                "engine": args.engine,
                "language": args.lang,
                "ai_cleanup": args.ai_cleanup
            },
            "results": results,
            "generated_at": datetime.now().isoformat()
        }
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        console.print(f"📊 Báo cáo: {report_path}")
    except Exception as e:
        console.print(f"⚠️  Không lưu được báo cáo: {e}")


# ══════════════════════════════════════════════════════════════════════════════
#  CLI ENTRYPOINT
# ══════════════════════════════════════════════════════════════════════════════

def build_parser():
    parser = argparse.ArgumentParser(
        prog="ocr_engine.py",
        description="🔤 Professional OCR Engine - Image Text Extraction",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  # Single file
  python ocr_engine.py extract --input photo.png --lang vi --engine paddleocr

  # Batch processing
  python ocr_engine.py batch --input input/ --output output/ --lang vi --ai-cleanup

  # Chỉ tiền xử lý ảnh
  python ocr_engine.py preprocess --input input/ --output input/processed/
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Shared arguments
    def add_common_args(p):
        p.add_argument("--input", "-i", required=True, help="File ảnh hoặc thư mục input")
        p.add_argument("--output", "-o", help="Thư mục output (mặc định: ./output)")
        p.add_argument("--lang", "-l", default="vi",
                       help="Ngôn ngữ OCR: vi, en, zh-cn, ja, ko (mặc định: vi)")
        p.add_argument("--engine", "-e", default="paddleocr",
                       choices=["paddleocr", "easyocr", "tesseract"],
                       help="OCR engine (mặc định: paddleocr)")
        p.add_argument("--format", "-f", default="txt,md",
                       help="Output format: txt,md,json (mặc định: txt,md)")
        p.add_argument("--ai-cleanup", action="store_true",
                       help="Bật AI cleanup với Claude")
        p.add_argument("--no-preprocess", action="store_true",
                       help="Tắt tiền xử lý ảnh")
        p.add_argument("--dpi", type=int, default=300,
                       help="DPI tối thiểu (mặc định: 300)")
    
    # extract command
    extract_p = subparsers.add_parser("extract", help="OCR một file ảnh")
    add_common_args(extract_p)
    
    # batch command
    batch_p = subparsers.add_parser("batch", help="Batch OCR toàn bộ thư mục")
    add_common_args(batch_p)
    
    # preprocess command
    pre_p = subparsers.add_parser("preprocess", help="Chỉ tiền xử lý ảnh (không OCR)")
    pre_p.add_argument("--input", "-i", required=True, help="File hoặc thư mục ảnh")
    pre_p.add_argument("--output", "-o", help="Thư mục output")
    pre_p.add_argument("--dpi", type=int, default=300, help="DPI tối thiểu")
    
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    
    console.print("\n🔤 [bold]Image OCR Engine v1.0.0[/bold]" if HAS_RICH 
                  else "\n🔤 Image OCR Engine v1.0.0")
    console.print("=" * 50)
    
    if args.command == "preprocess":
        cmd_preprocess(args)
    elif args.command == "extract":
        cmd_extract(args)
    elif args.command == "batch":
        cmd_batch(args)


if __name__ == "__main__":
    main()
