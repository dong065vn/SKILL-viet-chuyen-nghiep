# YouTube Transcript Workspace - Setup

## Giới thiệu

Workspace này cung cấp workflow và skill để lấy transcript từ video YouTube và xuất thành file markdown.

## Cài đặt

### 1. Yêu cầu hệ thống

- Python 3.8+
- pip (Python package manager)

### 2. Cài đặt dependencies

```bash
pip install youtube-transcript-api
```

### 3. Kiểm tra cài đặt

```bash
python -c "import youtube_transcript_api; print('✅ OK')"
```

## Cách sử dụng

### Sử dụng trực tiếp script Python

```bash
# Lấy transcript từ URL
python .agent/skills/youtube-transcript/scripts/extract_transcript.py https://youtu.be/VIDEO_ID

# Chỉ định thư mục output
python .agent/skills/youtube-transcript/scripts/extract_transcript.py https://youtu.be/VIDEO_ID --output ./my-transcripts

# Chỉ định ngôn ngữ
python .agent/skills/youtube-transcript/scripts/extract_transcript.py https://youtu.be/VIDEO_ID --lang en

# Liệt kê các transcript có sẵn
python .agent/skills/youtube-transcript/scripts/extract_transcript.py https://youtu.be/VIDEO_ID --list
```

### Sử dụng workflow `/yt-transcript`

Trong AI assistant, gọi:
```
/yt-transcript
```

Sau đó dán link YouTube video.

## Cấu trúc thư mục

```
youtube-transcript-workspace/
├── .agent/
│   ├── workflows/
│   │   └── youtube-transcript.md
│   └── skills/
│       └── youtube-transcript/
│           ├── SKILL.md
│           └── scripts/
│               └── extract_transcript.py
├── output/                    # Transcript files được lưu ở đây
├── setup_instruction.md
└── shortcut_guide.md
```

## Troubleshooting

| Vấn đề | Giải pháp |
|--------|-----------|
| `ModuleNotFoundError: youtube_transcript_api` | Chạy `pip install youtube-transcript-api` |
| Video không có transcript | Video chưa được thêm phụ đề |
| Video private | Chỉ hoạt động với video public |
