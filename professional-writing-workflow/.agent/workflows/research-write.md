---
description: Viết bài chuyên nghiệp từ ảnh/screenshot/link/ý tưởng mỏng. Tự động nghiên cứu web sâu rồi viết bài hoàn chỉnh.
---

# /research-write — Nghiên cứu & Viết từ Ảnh/Ý tưởng

Workflow đặc biệt cho trường hợp người dùng chỉ cung cấp **input tối thiểu** (1 bức ảnh, 1 link, hoặc 1 câu ý tưởng) và muốn có bài viết chuyên nghiệp hoàn chỉnh.

> **Ví dụ thực tế:** Người dùng gửi 1 ảnh chụp bài báo về "Trung Quốc cải cách giáo dục" → Workflow tự nghiên cứu → Output bài 1500+ từ có đầy đủ số liệu, so sánh quốc tế, phân tích chính sách.

---

## STEP 1 — Phân tích Input (5 phút)

### Nếu input là ẢNH/SCREENSHOT:
1. Đọc nội dung ảnh (OCR nếu cần)
2. Trích xuất: tiêu đề, keywords, tên nguồn, ngày tháng
3. Xác định ngôn ngữ gốc (Việt/Anh/Trung/...)
4. Tóm tắt nội dung chính trong 3-5 câu

### Nếu input là LINK:
1. Đọc nội dung trang web bằng `read_url_content`
2. Trích xuất thông tin chính
3. Ghi nhận nguồn gốc

### Nếu input là Ý TƯỞNG NGẮN:
1. Phân tích ý tưởng → xác định chủ đề cốt lõi
2. Mở rộng thành 3-5 câu hỏi nghiên cứu
3. Xác định góc nhìn/angle phù hợp

### Output Step 1:
```
📋 PHÂN TÍCH INPUT
- Chủ đề: [...]
- Keywords chính: [kw1], [kw2], [kw3]
- Keywords mở rộng (EN): [kw1_en], [kw2_en]
- Loại bài phù hợp: [Phê phán / Kiến thức / Motivational / Bán hàng]
- Câu hỏi nghiên cứu:
  1. [...]
  2. [...]
  3. [...]
```

**→ Hỏi người dùng xác nhận hướng đi trước khi research.**

---

## STEP 2 — Deep Research (15-30 phút)

### 2.1 Vòng 1: Research rộng
Sử dụng `search_web` với keywords đã xác định:

```
search_web("[keyword chính] [năm]")
search_web("[keyword chính tiếng Anh] [year] research")
search_web("[keyword] site:nature.com OR site:reuters.com")
search_web("[keyword] thống kê số liệu site:vnexpress.net OR site:tuoitre.vn")
search_web("[keyword] nghị định luật site:thuvienphapluat.vn")
```

### 2.2 Vòng 2: Research sâu
Từ kết quả vòng 1, đọc chi tiết các nguồn quan trọng nhất:

```
read_url_content("[URL bài báo/nghiên cứu quan trọng 1]")
read_url_content("[URL bài báo/nghiên cứu quan trọng 2]")
read_url_content("[URL văn bản pháp luật liên quan]")
read_url_content("[URL số liệu thống kê]")
```

### 2.3 Vòng 3: Cross-verify & Bổ sung
- Số liệu quan trọng → search thêm nguồn thứ 2 xác minh
- Quote/phát biểu → tìm nguồn gốc
- So sánh quốc tế → tìm case tương tự ở nước khác

### 2.4 Tiêu chí chất lượng nghiên cứu

| Tiêu chí | Yêu cầu tối thiểu |
|----------|-------------------|
| Số nguồn tham khảo | ≥ 5 nguồn |
| Nguồn quốc tế | ≥ 2 nguồn |
| Nguồn Việt Nam | ≥ 2 nguồn |
| Số liệu cụ thể | ≥ 3 con số/thống kê |
| Quote chuyên gia | ≥ 1 quote |
| Văn bản pháp luật (nếu liên quan) | ≥ 1 |
| Cross-verify | Số liệu chính xác nhận ≥ 2 nguồn |

### Output Step 2: Research Brief
```markdown
## 📚 RESEARCH BRIEF: [Chủ đề]

### Bối cảnh
[Tóm tắt 3-5 câu]

### Số liệu chính
1. [Số liệu] — Nguồn: [A] (MM/YYYY), xác nhận bởi [B]
2. [Số liệu] — Nguồn: [A]
3. [Số liệu] — Nguồn: [A]

### Quote / Phát biểu
- "[Quote]" — [Người], [Chức vụ] | [Nguồn]

### Timeline
- [Năm 1]: [Sự kiện]
- [Năm 2]: [Sự kiện]

### Chính sách / Pháp luật
- [Tên văn bản] ([Số hiệu], [Ngày])
- Nội dung chính: [...]

### So sánh quốc tế
| Tiêu chí | [Nước A] | [Nước B/VN] |
|----------|---------|-------------|
| [Tiêu chí 1] | [Data] | [Data] |

### Case Study nổi bật
[Câu chuyện cụ thể với tên, địa điểm, chi tiết]

### Nguồn tham khảo đầy đủ
1. [Tác giả/Tổ chức]. ([Năm]). "[Tiêu đề]". [Nguồn]. URL
2. ...
```

---

## STEP 3 — Xác nhận hướng viết

Trình bày cho người dùng:
1. **Research Brief** (tóm tắt ngắn)
2. **Đề xuất loại bài**: Phê phán? Kiến thức? Motivational?
3. **Đề xuất outline** sơ bộ (5-8 section)
4. **3 biến thể tiêu đề/hook**

**→ Chờ người dùng xác nhận hoặc điều chỉnh.**

---

## STEP 4 — Viết bài hoàn chỉnh

Sau khi người dùng xác nhận hướng đi → Chạy workflow `/write` với đầy đủ dữ liệu:

- **Input cho /write**: Research Brief + Loại bài + Outline đã duyệt
- **Bỏ qua Phase 1.5** (vì đã research xong)
- **Chạy từ Phase 2** → Phase 5

### Lưu ý đặc biệt khi viết từ research:
- PHẢI dẫn nguồn trong bài (tự nhiên, không academic)
- Số liệu cụ thể hơn tốt hơn (47.329 thay vì "gần 50.000")
- Kể case study chi tiết (tên người, địa điểm, thời gian)
- So sánh quốc tế → tạo contrast mạnh
- Kết bài: câu hỏi tu từ kích thích suy nghĩ

---

## STEP 5 — Output hoàn chỉnh

Bàn giao cho người dùng:

### 1. Bài viết hoàn chỉnh
- Copy-paste ready cho Facebook
- 1200-2000 từ
- Đã format mobile-friendly

### 2. File nguồn tham khảo
```markdown
---
Tham khảo: [Nguồn 1] (MM/YYYY), [Nguồn 2], [Nguồn 3], ...
```

### 3. Vị trí chèn ảnh
```
[VỊ TRÍ ẢNH 1]: [Mô tả ảnh cần chèn]
[VỊ TRÍ ẢNH 2]: [Mô tả ảnh cần chèn]
```

### 4. Biến thể A/B Test
- Tiêu đề A: [...]
- Tiêu đề B: [...]
- Tiêu đề C: [...]

### 5. Gợi ý đăng bài
- **Thời gian tốt nhất**: 7-9h sáng, 12-13h, 20-22h (giờ VN)
- **Group/Page phù hợp**: [Gợi ý dựa trên chủ đề]
- **Hashtag**: [3-5 hashtag phù hợp]

---

## Ví dụ thực tế: Từ ảnh → Bài viết

**Input:** 1 ảnh chụp bài báo "Trung Quốc cải cách giáo dục: Xóa bỏ luận án giấy"

**Step 1:** Trích xuất → Keywords: "Trung Quốc", "tiến sĩ sản phẩm", "cải cách giáo dục", "luận án", "practice-based PhD"

**Step 2:** Research → Tìm được: Ngụy Liên Phong (Cáp Nhĩ Tân), Trịnh Hạ Huy (Đại học Đông Nam), Luật Học vị 2024, 10.000 bài báo bị rút lại (Nature), NQ 57-NQ/TW, Luật KH,CN&ĐMST 2025

**Step 4:** Viết theo nhánh Phê phán Xã hội → Bài 1800 từ so sánh TQ-VN

**Output:** Bài viết "KHI TIẾN SĨ TRUNG QUỐC BẢO VỆ LUẬN ÁN BẰNG... MỘT CÂY CẦU" + 8 nguồn tham khảo
