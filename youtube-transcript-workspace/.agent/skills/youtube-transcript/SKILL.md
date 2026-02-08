---
name: youtube-transcript
description: "Skill lấy transcript từ YouTube video và xuất file markdown"
version: 1.0.0
author: Antigravity Assistant
created: 2026-02-08
platforms: [github-copilot-cli, claude-code, gemini-cli]
category: content
tags: [youtube, transcript, video, extraction]
risk: safe
---

# YouTube Transcript Extractor

## Purpose

Skill này giúp lấy transcript (phụ đề) từ video YouTube và xuất thành file markdown. Sử dụng thư viện Python `youtube-transcript-api`.

## When to Use

- Người dùng dán link YouTube và muốn lấy transcript
- Cần trích xuất nội dung text từ video
- Muốn lưu transcript để đọc/nghiên cứu offline

## Prerequisites

```bash
# Kiểm tra Python
python --version

# Cài đặt dependency
pip install youtube-transcript-api
```

## Step 1: Validate YouTube URL

**Định dạng hỗ trợ:**
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

**Regex pattern:**
```python
import re

patterns = [
    r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
]

def extract_video_id(url):
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None
```

## Step 2: Check Transcript Availability

```python
from youtube_transcript_api import YouTubeTranscriptApi

# Liệt kê các transcript có sẵn
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

for transcript in transcript_list:
    print(f"- {transcript.language} ({transcript.language_code})")
    print(f"  Auto-generated: {transcript.is_generated}")
```

## Step 3: Extract Transcript

```python
from youtube_transcript_api import YouTubeTranscriptApi

# Lấy transcript với ngôn ngữ ưu tiên
transcript = YouTubeTranscriptApi.get_transcript(
    video_id,
    languages=['vi', 'en']  # Ưu tiên tiếng Việt, fallback sang English
)

# Ghép các đoạn thành text đầy đủ
full_text = " ".join([entry['text'] for entry in transcript])
```

## Step 4: Save to Markdown

```python
from datetime import datetime

filename = f"transcript_{video_id}_{datetime.now().strftime('%Y-%m-%d')}.md"

content = f"""# YouTube Transcript

**Video ID:** {video_id}
**URL:** https://www.youtube.com/watch?v={video_id}
**Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Transcript

{full_text}
"""

with open(f"output/{filename}", "w", encoding="utf-8") as f:
    f.write(content)
```

## Error Handling

| Error | Message | Action |
|-------|---------|--------|
| TranscriptsDisabled | Video không cho phép transcript | Thông báo user |
| NoTranscriptFound | Không tìm thấy transcript | Thử ngôn ngữ khác |
| Invalid URL | URL không đúng định dạng | Yêu cầu URL hợp lệ |

## Usage Example

```bash
# Chạy script
python .agent/skills/youtube-transcript/scripts/extract_transcript.py https://youtu.be/dQw4w9WgXcQ

# Output
✅ Transcript extracted successfully!
📄 File saved: output/transcript_dQw4w9WgXcQ_2026-02-08.md
```

## Scripts

- `scripts/extract_transcript.py` - Script chính để extract transcript
