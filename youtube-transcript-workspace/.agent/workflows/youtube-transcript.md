---
description: Lấy transcript từ YouTube video và xuất file markdown
---

# Workflow: YouTube Transcript Extractor

// turbo-all

## Bước 1: Nhận link YouTube

Người dùng cung cấp link YouTube video. Ví dụ:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

## Bước 2: Kiểm tra dependencies

```bash
python -c "import youtube_transcript_api; print('✅ youtube-transcript-api đã cài đặt')" 2>nul || echo "❌ Chưa cài youtube-transcript-api"
```

Nếu chưa cài, chạy:
```bash
pip install youtube-transcript-api
```

## Bước 3: Extract Video ID

Từ URL người dùng, extract video ID:
- `https://www.youtube.com/watch?v=dQw4w9WgXcQ` → `dQw4w9WgXcQ`
- `https://youtu.be/dQw4w9WgXcQ` → `dQw4w9WgXcQ`

## Bước 4: Lấy transcript

Sử dụng script Python:
```bash
python .agent/skills/youtube-transcript/scripts/extract_transcript.py VIDEO_ID --output output/
```

## Bước 5: Xác nhận output

Kiểm tra file markdown đã được tạo trong thư mục `output/`:
```
output/
└── transcript_VIDEO_ID_YYYY-MM-DD.md
```

## Xử lý lỗi

| Lỗi | Giải pháp |
|-----|-----------|
| URL không hợp lệ | Yêu cầu user cung cấp URL đúng định dạng |
| Video không có transcript | Thông báo video không hỗ trợ |
| Video private | Yêu cầu video public |

## Output mẫu

```markdown
# YouTube Transcript

**Video ID:** dQw4w9WgXcQ
**URL:** https://www.youtube.com/watch?v=dQw4w9WgXcQ
**Extracted:** 2026-02-08

---

## Transcript

[Nội dung transcript đầy đủ...]
```
