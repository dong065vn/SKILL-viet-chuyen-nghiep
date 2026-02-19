# 📥 Input — Mô Tả Mục Tiêu (Ngọn)

Đặt tài liệu mô tả **mục tiêu bạn muốn đạt được** vào folder này.

## Hỗ trợ định dạng

| Định dạng | Ví dụ |
|-----------|-------|
| `.md`, `.txt` | Mô tả mục tiêu bằng text |
| `.png`, `.jpg` | Ảnh chụp, sơ đồ, mindmap |
| `.pdf` | Tài liệu tham khảo |
| `.json` | Dữ liệu có cấu trúc |

## Cách sử dụng

1. Đặt file(s) mô tả mục tiêu vào folder `input/`
2. Chạy workflow `/thanh-cong`
3. Workflow sẽ tự động:
   - Đọc tất cả files
   - Trích xuất mục tiêu chính
   - Phân tích mọi khía cạnh cần thiết
   - Xây dựng lộ trình qua **Tam Giác Thành Công**

## Ví dụ

```
input/
├── muc-tieu.md          # "Tôi muốn trở thành full-stack developer trong 6 tháng"
├── roadmap-reference.png # Ảnh chụp roadmap tham khảo
└── skills-gap.json       # Đánh giá kỹ năng hiện tại
```

> **Lưu ý:** Workflow sẽ hỏi xác nhận mục tiêu trước khi bắt đầu phân tích.
