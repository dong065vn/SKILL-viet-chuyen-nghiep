---
name: phan-tich-workflow
description: >
  Workflow phân tích mục tiêu dựa trên framework "Tam Giác Thành Công".
  Đọc tài liệu mô tả mục tiêu (ngọn) từ folder input/, phân tích mọi khía cạnh,
  dẫn user qua Tư Duy Đúng → Kiến Thức Đúng → Công Cụ Đúng,
  tracking tiến độ và xuất DOCX khi hoàn thành.
---

# 🏆 Phân Tích Workflow — Tam Giác Thành Công

## Overview

Workflow này giúp user đạt được **bất kỳ mục tiêu nào** thông qua framework "Tam Giác Thành Công":

| Yếu tố | Tỷ trọng | Mô tả |
|---------|----------|-------|
| 🧠 **Tư Duy Đúng** | **70%** | Thuận Nguyên Lý — hiểu đúng nguyên lý nền tảng |
| 📘 **Kiến Thức Đúng** | **10%** | Học Nhanh Nhờ AI Hỗ Trợ |
| 🔧 **Công Cụ Đúng** | **20%** | Luyện Kỹ Năng 20H |

Và "Công Thức Tiến Bộ":

| Level | Công thức | Tỷ lệ |
|-------|-----------|--------|
| 1 | HỌC + HÀNH | 50% |
| 2 | HỌC + HÀNH + DẠY LẠI | 90% |
| 3 | HỌC + HÀNH + DẠY LẠI + KIẾM ĐƯỢC TIỀN | 100% |

---

## Luồng Hoạt Động

### Bước 0: Đọc Input (Bắt buộc)

Đọc tất cả files trong folder `input/`:

1. Liệt kê tất cả files trong `input/` (hỗ trợ: `.md`, `.txt`, `.png`, `.jpg`, `.pdf`, `.json`)
2. Đọc từng file và trích xuất nội dung
3. Tổng hợp thành **Mô tả Mục Tiêu (Ngọn)**

> **Output:** Một bản tóm tắt rõ ràng về mục tiêu user muốn đạt được.
> Hỏi user xác nhận: "Mục tiêu của bạn là [X]. Đúng không?"
> **Không tiếp tục nếu chưa được xác nhận.**

---

### Bước 1: 🧠 Tư Duy Đúng (70%) — Thuận Nguyên Lý

**Invoke skill:** `skills/tu-duy-dung/SKILL.md`

Phân tích mục tiêu từ góc nhìn nguyên lý nền tảng:
- Xác định First Principles
- Phân tích Pareto 80/20
- Áp dụng Mental Models
- 5 Whys analysis
- Loại bỏ assumptions sai

> **Output:** Tài liệu phân tích tư duy, nguyên lý nền tảng cần nắm.

---

### Bước 2: 📘 Kiến Thức Đúng (10%) — Học Nhanh Nhờ AI

**Invoke skill:** `skills/kien-thuc-dung/SKILL.md`

Xác định và hệ thống hóa kiến thức cần học:
- Knowledge Gap Analysis
- Tìm nguồn học chất lượng
- Prompt patterns để học hiệu quả với AI
- Knowledge mapping
- Self-assessment

> **Output:** Bản đồ kiến thức, danh sách nguồn học, key concepts.

---

### Bước 3: 🔧 Công Cụ Đúng (20%) — Luyện Kỹ Năng 20H

**Invoke skill:** `skills/cong-cu-dung/SKILL.md`

Chọn và luyện công cụ phù hợp:
- Tool Selection Matrix
- Kế hoạch luyện 20 giờ
- Deliberate practice framework
- Milestone tracking

> **Output:** Danh sách công cụ, kế hoạch luyện tập, milestones.

---

### Bước 4: 📄 Xuất DOCX

Khi **cả 3 bước trên đã hoàn thành** và có đủ tài liệu:

1. Tổng hợp output từ 3 skills vào JSON format
2. Chạy script: `python scripts/export_docx.py --input knowledge.json --output output.docx`
3. Thông báo user file DOCX đã sẵn sàng

> **Điều kiện kích hoạt:** Cả 3 phần Tư Duy Đúng, Kiến Thức Đúng, Công Cụ Đúng đều đã có output.

---

### Bước 5 (Tùy chọn): Công Thức Tiến Bộ

Sau khi hoàn thành Tam Giác Thành Công, user có thể tiếp tục:

1. **📚 HỌC + HÀNH (50%)** → `skills/hoc-hanh/SKILL.md`
2. **🎓 DẠY LẠI (90%)** → `skills/day-lai/SKILL.md`
3. **💰 KIẾM TIỀN (100%)** → `skills/kiem-tien/SKILL.md`

Sử dụng `skills/danh-gia-tien-bo/SKILL.md` để đánh giá tiến độ tại mỗi level.

---

## Routing Logic

```
User invoke /thanh-cong hoặc đề cập đến mục tiêu học tập
    │
    ├─ Có files trong input/ ?
    │   ├─ CÓ → Đọc & phân tích → Xác nhận mục tiêu
    │   └─ KHÔNG → Hỏi user mô tả mục tiêu, lưu vào input/
    │
    ├─ Bước 1: Tư Duy Đúng (70%)
    ├─ Bước 2: Kiến Thức Đúng (10%)
    ├─ Bước 3: Công Cụ Đúng (20%)
    │
    ├─ Đủ output từ 3 bước? → Xuất DOCX
    │
    └─ Tiếp tục Công Thức Tiến Bộ?
        ├─ HỌC + HÀNH (50%)
        ├─ DẠY LẠI (90%)
        └─ KIẾM TIỀN (100%)
```

---

## Nguyên Tắc Hoạt Động

- **Luôn đọc input/ trước** khi bắt đầu bất kỳ phân tích nào
- **Xác nhận mục tiêu** với user trước khi tiến hành
- **Tuần tự:** Tư Duy Đúng → Kiến Thức Đúng → Công Cụ Đúng
- **Không bỏ qua bước nào** — mỗi bước đều quan trọng
- **Xuất DOCX tự động** khi đủ dữ liệu từ 3 bước
- **Hỏi trước khi tiếp tục** sang Công Thức Tiến Bộ
