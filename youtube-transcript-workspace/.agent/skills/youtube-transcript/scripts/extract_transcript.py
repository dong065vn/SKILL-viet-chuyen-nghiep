#!/usr/bin/env python3
"""
YouTube Transcript Extractor
Lấy transcript từ video YouTube và xuất file markdown

Usage:
    python extract_transcript.py <YouTube_URL> [--output <folder>] [--lang <language_code>]
    
Examples:
    python extract_transcript.py https://youtu.be/dQw4w9WgXcQ
    python extract_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ --output ./output
    python extract_transcript.py https://youtu.be/dQw4w9WgXcQ --lang vi
"""

import sys
import re
import argparse
from datetime import datetime
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("❌ Chưa cài đặt youtube-transcript-api")
    print("   Chạy: pip install youtube-transcript-api")
    sys.exit(1)


def extract_video_id(url: str) -> str | None:
    """Extract video ID từ YouTube URL"""
    patterns = [
        r'(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'(?:youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'(?:youtube\.com/v/)([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    # Nếu input chỉ là video ID (11 ký tự)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url):
        return url
    
    return None


def extract_transcript(video_id: str, languages: list = None) -> str | None:
    """Lấy transcript từ video sử dụng youtube-transcript-api v1.2.x"""
    if languages is None:
        languages = ['vi', 'en']
    
    try:
        # API v1.2.x: tạo instance trước, sau đó gọi fetch()
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=languages)
        
        # Kết hợp tất cả các đoạn text
        full_text = "\n".join([entry.text for entry in transcript])
        return full_text
    except Exception as e:
        error_msg = str(e).lower()
        if "disabled" in error_msg:
            print(f"❌ Transcripts bị tắt cho video {video_id}")
        elif "no transcript" in error_msg or "not found" in error_msg:
            print(f"❌ Không tìm thấy transcript cho video {video_id}")
            print(f"   Thử các ngôn ngữ khác bằng --lang")
        else:
            print(f"❌ Lỗi: {e}")
        return None


def save_to_markdown(video_id: str, transcript: str, output_folder: str = "output") -> str:
    """Lưu transcript thành file markdown"""
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"transcript_{video_id}_{date_str}.md"
    filepath = output_path / filename
    
    content = f"""# YouTube Transcript

**Video ID:** {video_id}
**URL:** https://www.youtube.com/watch?v={video_id}
**Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Transcript

{transcript}
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return str(filepath)


def main():
    parser = argparse.ArgumentParser(
        description="Lấy transcript từ YouTube video và xuất file markdown"
    )
    parser.add_argument("url", help="YouTube URL hoặc video ID")
    parser.add_argument("--output", "-o", default="output", help="Thư mục lưu file (default: output)")
    parser.add_argument("--lang", "-l", default="vi,en", help="Ngôn ngữ ưu tiên (default: vi,en)")
    
    args = parser.parse_args()
    
    video_id = extract_video_id(args.url)
    if not video_id:
        print("❌ URL không hợp lệ!")
        print("   Định dạng hỗ trợ:")
        print("   - https://www.youtube.com/watch?v=VIDEO_ID")
        print("   - https://youtu.be/VIDEO_ID")
        sys.exit(1)
    
    print(f"📹 Video ID: {video_id}")
    
    languages = [lang.strip() for lang in args.lang.split(",")]
    print(f"🔍 Đang lấy transcript (ngôn ngữ: {', '.join(languages)})...")
    
    transcript = extract_transcript(video_id, languages)
    if not transcript:
        sys.exit(1)
    
    filepath = save_to_markdown(video_id, transcript, args.output)
    print(f"✅ Đã lưu transcript!")
    print(f"📄 File: {filepath}")


if __name__ == "__main__":
    main()
