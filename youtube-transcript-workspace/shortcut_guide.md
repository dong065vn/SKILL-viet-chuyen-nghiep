# YouTube Transcript Workspace - Shortcuts

## Danh sách Commands

| Command | Mô tả |
|---------|-------|
| `/yt-transcript` | Lấy transcript từ YouTube video và xuất file markdown |

## Cách sử dụng

### `/yt-transcript`

**Mục đích:** Trích xuất transcript (phụ đề) từ video YouTube

**Input:** Link YouTube video

**Output:** File markdown trong thư mục `output/`

**Ví dụ:**
```
> /yt-transcript

Vui lòng dán link YouTube video:
> https://www.youtube.com/watch?v=dQw4w9WgXcQ

📹 Video ID: dQw4w9WgXcQ
🔍 Đang lấy transcript...
✅ Đã lưu transcript!
📄 File: output/transcript_dQw4w9WgXcQ_2026-02-08.md
```

## Định dạng URL hỗ trợ

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

## Ngôn ngữ hỗ trợ

Script tự động ưu tiên:
1. Tiếng Việt (`vi`)
2. Tiếng Anh (`en`)

Có thể chỉ định ngôn ngữ khác bằng flag `--lang`.
