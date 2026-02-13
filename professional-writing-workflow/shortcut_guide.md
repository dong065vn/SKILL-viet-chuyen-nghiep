# 🚀 Shortcut Guide — Professional Writing Workflow

## Workflows Viết Bài Chuyên Nghiệp

| Lệnh | Mô tả | Input cần có |
|-------|--------|-------------|
| `/write` | Viết bài Facebook chuyên nghiệp 1200-2000 từ | Chủ đề + loại bài + dữ liệu |
| `/research-write` | Nghiên cứu web sâu + viết bài từ input tối thiểu | Ảnh/link/ý tưởng ngắn |

## Cách sử dụng

### `/write` — Khi đã có đủ dữ liệu
```
/write
→ Chọn loại bài: bán hàng / phê phán / kiến thức / motivational
→ Cung cấp: chủ đề, khán giả, nguyên liệu
→ AI viết theo 6 phases chuyên nghiệp
```

### `/research-write` — Khi chỉ có ảnh hoặc ý tưởng mỏng
```
/research-write
→ Gửi: 1 ảnh chụp bài báo / 1 link / 1 câu ý tưởng
→ AI tự động nghiên cứu 30+ nguồn uy tín
→ Trình bày Research Brief để duyệt
→ Viết bài hoàn chỉnh 1200-2000 từ
```

## Ví dụ thực tế

| Tình huống | Dùng lệnh | Kết quả |
|-----------|-----------|---------|
| Có câu chuyện bán hàng, ảnh before-after | `/write` | Bài PAS/AIDA + CTA |
| Chụp 1 ảnh bài báo về giáo dục TQ | `/research-write` | Bài phê phán 1800 từ + 8 nguồn |
| Muốn viết về AI thay đổi ngành Y | `/research-write` | Bài kiến thức + số liệu quốc tế |
| Có đầy đủ case study + số liệu | `/write` | Bài kiến thức/motivational |

## 4 Loại bài viết được hỗ trợ

| Loại | Framework | Phong cách | Đặc điểm |
|------|-----------|------------|----------|
| **Bán hàng Storytelling** | PAS/AIDA | Friend + Guide | Hook → Nỗi đau (60-70%) → Giải pháp → CTA |
| **Phê phán Xã hội** | Problem-Contrast-Hope | Expert + Innovator | Case quốc tế → So sánh VN → Câu hỏi tu từ |
| **Kiến thức Chia sẻ** | List+Story+Takeaway | Guide + Expert | Insight + Ví dụ cụ thể + Actionable |
| **Motivational** | Hero's Journey+Lesson | Motivator + Friend | Đáy sâu → Vượt qua → Bài học |

## 🎨 Hệ thống Phong cách Viết

### Cách hoạt động
- Mỗi loại bài có **phong cách viết riêng** (Voice, Rhythm, Language, Emotion)
- Phong cách được định nghĩa trong `writing_styles.md`
- Khi gặp bài mẫu xuất sắc → lưu vào `reference_styles/` để tái sử dụng

### Thêm Reference Style mới
```
1. Phân tích bài viết mẫu → trích xuất đặc trưng phong cách
2. Tạo file: reference_styles/[loai-bai]-[chu-de]-v1.md
3. Lần sau gặp bài tương tự → workflow tự động load reference style
```

### Cấu trúc folder
```
professional-writing-workflow/
├── writing_styles.md           ← 4 phong cách mặc định
├── reference_styles/           ← Phong cách đã "học" từ bài thực tế
│   └── phe-phan-xa-hoi-v1.md  ← Từ bài Tiến sĩ TQ
├── .agent/workflows/
│   ├── write.md                ← Workflow chính (có PHASE 2.3)
│   └── research-write.md      ← Workflow nghiên cứu + viết
├── skill_router.md
├── shortcut_guide.md
└── setup_instruction.md
```
