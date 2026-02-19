---
name: kien-thuc-dung
description: >
  Skill phân tích Kiến Thức Đúng (10%) — Học Nhanh Nhờ AI Hỗ Trợ.
  Giúp user xác định knowledge gaps, tìm nguồn học chất lượng,
  sử dụng AI để tăng tốc, và hệ thống hóa kiến thức.
---

# 📘 Kiến Thức Đúng (10%) — Học Nhanh Nhờ AI Hỗ Trợ

## Tại sao chỉ chiếm 10%?

Kiến thức quan trọng nhưng **không phải yếu tố quyết định**. Khi đã có tư duy đúng (70%),
việc tìm kiến thức trở nên dễ dàng — đặc biệt khi có AI hỗ trợ.

---

## Quy trình

### 1️⃣ Knowledge Gap Analysis

Xác định khoảng cách giữa hiện tại và mục tiêu:

```markdown
## Knowledge Gap Analysis

### Mục tiêu: [Tên mục tiêu]

#### Kiến thức ĐÃ CÓ:
1. [Kiến thức 1] — Mức độ: ⭐⭐⭐ (3/5)
2. [Kiến thức 2] — Mức độ: ⭐⭐ (2/5)

#### Kiến thức CẦN HỌC:
1. [Kiến thức mới 1] — Độ ưu tiên: 🔴 Cao
2. [Kiến thức mới 2] — Độ ưu tiên: 🟡 Trung bình

#### GAP:
| Lĩnh vực | Hiện tại | Cần đạt | Gap |
|----------|----------|---------|-----|
| [Lĩnh vực 1] | 2/5 | 4/5 | 2 levels |
```

---

### 2️⃣ Tìm Nguồn Học Chất Lượng

Curated resources theo thứ tự ưu tiên:

**Tiêu chí chọn nguồn:**
- ✅ Chính thống, có uy tín
- ✅ Cập nhật, không lỗi thời
- ✅ Phù hợp level hiện tại
- ✅ Có bài tập thực hành
- ❌ Tránh nguồn không rõ xuất xứ

**Template output:**

| Nguồn | Loại | Level | Thời gian | Link |
|-------|------|-------|-----------|------|
| [Nguồn 1] | Khóa học | Beginner | 10h | [URL] |
| [Nguồn 2] | Sách | Intermediate | 20h | [URL] |
| [Nguồn 3] | Documentation | Advanced | 5h | [URL] |

---

### 3️⃣ Sử dụng AI để Tăng tốc Học

**Prompt patterns hiệu quả:**

#### Pattern 1: Explain Like I'm 5 (ELI5)
```
"Giải thích [concept] như thể tôi là một người mới bắt đầu.
Dùng ví dụ thực tế và so sánh dễ hiểu."
```

#### Pattern 2: Feynman Technique
```
"Tôi sẽ giải thích [concept] theo cách hiểu của tôi.
Hãy chỉ ra những chỗ tôi hiểu sai hoặc thiếu:
[Lời giải thích của user]"
```

#### Pattern 3: Spaced Repetition
```
"Tạo 10 câu hỏi flashcard về [concept] với format:
Q: [Câu hỏi]
A: [Câu trả lời ngắn gọn]"
```

#### Pattern 4: Practice Problems
```
"Cho tôi 5 bài tập thực hành về [concept], 
từ dễ đến khó, có lời giải chi tiết."
```

#### Pattern 5: Knowledge Map
```
"Tạo bản đồ kiến thức (knowledge map) cho [topic],
bao gồm: khái niệm chính, mối quan hệ, và thứ tự học."
```

---

### 4️⃣ Hệ thống hóa Kiến thức (Knowledge Mapping)

Tổ chức kiến thức thành cấu trúc rõ ràng:

```markdown
## Knowledge Map: [Chủ đề]

### Core Concepts (Phải biết)
1. **[Concept A]** — [Mô tả ngắn]
   - Sub-concept A1
   - Sub-concept A2

### Supporting Concepts (Nên biết)
1. **[Concept B]** — [Mô tả ngắn]

### Advanced Concepts (Biết thêm)
1. **[Concept C]** — [Mô tả ngắn]

### Mối quan hệ:
- [Concept A] → phụ thuộc → [Concept B]
- [Concept A] → mở rộng → [Concept C]
```

---

### 5️⃣ Self-Assessment (Kiểm tra hiểu biết)

Tự đánh giá sau khi học:

| Tiêu chí | Điểm (1-5) | Bằng chứng |
|----------|-----------|------------|
| Có thể giải thích cho người khác | _/5 | [Ví dụ] |
| Có thể áp dụng vào bài toán mới | _/5 | [Ví dụ] |
| Có thể nhận ra khi nào KHÔNG dùng | _/5 | [Ví dụ] |
| Biết giới hạn của kiến thức này | _/5 | [Ví dụ] |

> **Ngưỡng pass:** Trung bình ≥ 3/5

---

## Output của Skill này

```json
{
  "kien_thuc_dung": {
    "knowledge_gaps": [
      {"field": "Lĩnh vực 1", "current": 2, "target": 4, "gap": 2}
    ],
    "curated_resources": [
      {"name": "Nguồn 1", "type": "course", "hours": 10, "url": "..."}
    ],
    "key_concepts": [
      {"name": "Concept A", "level": "core", "description": "..."}
    ],
    "knowledge_map": "Structured map of concepts and relationships",
    "self_assessment": {"avg_score": 3.5, "passed": true}
  }
}
```

> Dữ liệu này sẽ được sử dụng để xuất DOCX trong bước cuối cùng.
