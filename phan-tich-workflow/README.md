# 🏆 Phân Tích Workflow — Tam Giác Thành Công

Framework giúp đạt **bất kỳ mục tiêu nào** thông qua phương pháp luận "Tam Giác Thành Công":

- 🧠 **Tư Duy Đúng (70%)** — Thuận Nguyên Lý
- 📘 **Kiến Thức Đúng (10%)** — Học Nhanh Nhờ AI Hỗ Trợ
- 🔧 **Công Cụ Đúng (20%)** — Luyện Kỹ Năng 20H

Kèm theo **Công Thức Tiến Bộ:** HỌC (50%) → DẠY LẠI (90%) → KIẾM TIỀN (100%)

## Quick Start

1. Đặt tài liệu mô tả mục tiêu vào `input/`
2. Gọi `/thanh-cong` hoặc invoke `SKILL.md`
3. Workflow phân tích → hướng dẫn → xuất DOCX

## Cấu trúc

```
phan-tich-workflow/
├── SKILL.md                    # Orchestrator chính
├── input/                      # 📥 Đặt tài liệu mục tiêu vào đây
├── skills/
│   ├── tu-duy-dung/            # 🧠 70% — First Principles
│   ├── kien-thuc-dung/         # 📘 10% — AI-Assisted Learning
│   ├── cong-cu-dung/           # 🔧 20% — Tool Mastery 20H
│   ├── hoc-hanh/               # 📚 HỌC + HÀNH = 50%
│   ├── day-lai/                # 🎓 DẠY LẠI = 90%
│   ├── kiem-tien/              # 💰 KIẾM TIỀN = 100%
│   └── danh-gia-tien-bo/       # 📊 Progress Assessment
├── scripts/
│   ├── export_docx.py          # Xuất DOCX
│   └── requirements.txt
├── templates/
│   └── tam-giac-thanh-cong.json
└── resources/
    └── framework-overview.md
```

## Xuất DOCX

Khi đã thu thập đủ kiến thức từ 3 cạnh Tam Giác:

```bash
pip install -r scripts/requirements.txt
python scripts/export_docx.py --input knowledge.json --output output.docx
# Hoặc tạo sample:
python scripts/export_docx.py --sample
```
