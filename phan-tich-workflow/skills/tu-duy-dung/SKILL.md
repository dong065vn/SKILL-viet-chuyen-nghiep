---
name: tu-duy-dung
description: >
  Skill phân tích Tư Duy Đúng (70%) — Thuận Nguyên Lý.
  Giúp user hiểu đúng nguyên lý nền tảng của mục tiêu thông qua
  First Principles, Pareto 80/20, Mental Models, và 5 Whys.
---

# 🧠 Tư Duy Đúng (70%) — Thuận Nguyên Lý

## Tại sao chiếm 70%?

Tư duy đúng là nền tảng quan trọng nhất. Nếu hiểu sai nguyên lý, mọi nỗ lực
học tập và luyện tập đều lãng phí. **Thuận Nguyên Lý** = đi đúng hướng từ đầu.

---

## Quy trình

### 1️⃣ Phân tích First Principles

Bẻ gãy mục tiêu thành các nguyên lý nền tảng nhỏ nhất:

1. Mục tiêu tổng thể là gì?
2. Những giả định nào đang có?
3. Bỏ hết giả định → còn lại **sự thật cốt lõi** nào?
4. Từ sự thật cốt lõi, xây dựng lại logic từ dưới lên

**Template output:**

```markdown
## First Principles Analysis

### Mục tiêu: [Tên mục tiêu]

#### Giả định hiện tại:
1. [Giả định 1] — Đúng/Sai/Cần kiểm tra
2. [Giả định 2] — Đúng/Sai/Cần kiểm tra

#### Sự thật cốt lõi:
1. [Sự thật 1]
2. [Sự thật 2]

#### Logic xây dựng lại:
Từ [sự thật] → cần [hành động] → dẫn đến [kết quả]
```

---

### 2️⃣ Phân tích Pareto 80/20

Xác định **20% yếu tố** tạo ra **80% kết quả**:

1. Liệt kê tất cả yếu tố ảnh hưởng đến mục tiêu
2. Đánh giá tác động của mỗi yếu tố (1-10)
3. Xếp hạng theo tác động
4. Chọn top 20% quan trọng nhất

**Template output:**

| Yếu tố | Tác động (1-10) | Độ ưu tiên | Ghi chú |
|---------|----------------|------------|---------|
| [Yếu tố 1] | 9 | 🔴 Cao | [Lý do] |
| [Yếu tố 2] | 7 | 🟡 Trung bình | [Lý do] |

---

### 3️⃣ Mental Models Checklist

Áp dụng các mô hình tư duy phù hợp:

- [ ] **Inversion** — Nghĩ ngược: "Điều gì khiến tôi THẤT BẠI?" → Tránh nó
- [ ] **Second-Order Thinking** — Hệ quả kế tiếp: "Nếu làm A, sẽ dẫn đến gì?"
- [ ] **Circle of Competence** — Tôi giỏi gì? Tôi yếu gì? Tập trung vào đâu?
- [ ] **Map vs Territory** — Bản đồ ≠ thực tế. Kiểm tra giả thiết bằng thực hành
- [ ] **Occam's Razor** — Giải pháp đơn giản nhất thường đúng nhất
- [ ] **Hanlon's Razor** — Đừng quy cho ác ý những gì giải thích được bằng sai lầm
- [ ] **Opportunity Cost** — Chọn A nghĩa là bỏ B. Chi phí cơ hội là gì?

---

### 4️⃣ Phân tích 5 Whys

Đào sâu đến gốc rễ vấn đề:

```
MỤC TIÊU: [Mô tả mục tiêu]

WHY 1: Tại sao mục tiêu này quan trọng?
→ [Trả lời]

WHY 2: Tại sao [trả lời 1]?
→ [Trả lời]

WHY 3: Tại sao [trả lời 2]?
→ [Trả lời]

WHY 4: Tại sao [trả lời 3]?
→ [Trả lời]

WHY 5: Tại sao [trả lời 4]?
→ [GỐC RỄ - NGUYÊN LÝ NỀN TẢNG]
```

---

### 5️⃣ Loại bỏ Assumptions sai

Kiểm tra mỗi assumption:

| Assumption | Nguồn gốc | Bằng chứng | Kết luận |
|-----------|------------|------------|----------|
| [Assumption 1] | Nghe người khác nói | Không có | ❌ **Loại bỏ** |
| [Assumption 2] | Kinh nghiệm bản thân | Có dữ liệu | ✅ **Giữ lại** |

---

## Output của Skill này

Khi hoàn thành, skill này cung cấp:

```json
{
  "tu_duy_dung": {
    "nguyen_ly": ["Nguyên lý 1", "Nguyên lý 2"],
    "mental_models": ["Inversion", "Pareto"],
    "first_principles": ["Sự thật cốt lõi 1", "Sự thật cốt lõi 2"],
    "five_whys": ["Why 1", "Why 2", "Why 3", "Why 4", "Gốc rễ"],
    "removed_assumptions": ["Assumption sai 1"],
    "pareto_top20": ["Yếu tố quan trọng 1", "Yếu tố quan trọng 2"]
  }
}
```

> Dữ liệu này sẽ được sử dụng để xuất DOCX trong bước cuối cùng.
