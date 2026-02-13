# 🔀 Skill Router — Professional Writing Workflow

## Routing Rules

Khi người dùng yêu cầu viết bài, sử dụng bảng routing sau:

| Trigger từ khóa | Workflow | Điều kiện |
|-----------------|----------|-----------|
| "viết bài", "write", "bài Facebook", "post" | `/write` | Có đủ dữ liệu (chủ đề + khán giả + nguyên liệu) |
| "viết từ ảnh", "research", "nghiên cứu", "tìm tài liệu" | `/research-write` | Input tối thiểu (ảnh/link/ý tưởng ngắn) |
| Gửi ảnh/screenshot kèm "viết bài" | `/research-write` | Tự động detect ảnh input |
| Gửi link kèm "phân tích" hoặc "viết" | `/research-write` | Tự động detect URL input |
| "bán hàng", "CTA", "lead" | `/write` → Nhánh Bán hàng | Có sản phẩm/dịch vụ |
| "phê phán", "so sánh quốc tế", "chính sách" | `/write` → Nhánh Phê phán | Có chủ đề xã hội |
| "chia sẻ kiến thức", "tips", "bài học" | `/write` → Nhánh Kiến thức | Có expertise/insight |
| "truyền cảm hứng", "câu chuyện", "motivational" | `/write` → Nhánh Motivational | Có story cá nhân |

## Decision Tree

```
Người dùng muốn viết bài
│
├── Có đủ dữ liệu? (chủ đề + số liệu + câu chuyện)
│   ├── CÓ → /write
│   │   ├── Mục tiêu bán hàng? → Nhánh Bán hàng (PAS/AIDA)
│   │   ├── Phê phán/so sánh? → Nhánh Phê phán (Problem-Contrast-Hope)
│   │   ├── Chia sẻ kiến thức? → Nhánh Kiến thức (List+Story+Takeaway)
│   │   └── Truyền cảm hứng? → Nhánh Motivational (Hero's Journey)
│   │
│   └── KHÔNG (chỉ có ảnh/link/ý tưởng mỏng) → /research-write
│       ├── Step 1: Phân tích input
│       ├── Step 2: Deep research 30+ nguồn
│       ├── Step 3: Xác nhận hướng viết
│       ├── Step 4: Gọi /write với dữ liệu đầy đủ
│       └── Step 5: Output hoàn chỉnh
```

## Quy tắc ưu tiên

1. **Nếu nghi ngờ** → Hỏi người dùng chọn loại bài
2. **Nếu thiếu dữ liệu** → Luôn chọn `/research-write`
3. **Nếu có ảnh/screenshot** → Mặc định `/research-write`
4. **Nếu có đủ dữ liệu** → Mặc định `/write`
