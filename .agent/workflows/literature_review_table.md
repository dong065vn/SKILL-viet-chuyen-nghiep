---
description: Quy trình tạo và sử dụng bảng tổng quan tài liệu (Literature Review Table)
---

# Workflow: Literature Review Table

Quy trình tạo và sử dụng **LITERATURE REVIEW TABLE** để tổng quan tài liệu một cách có hệ thống trong nghiên cứu khoa học.

## Thông tin cơ bản

| Thuộc tính | Mô tả |
|------------|-------|
| Mục đích | Tổng quan tài liệu theo chủ đề, không liệt kê từng tác giả |
| Công cụ hỗ trợ | Excel, Google Sheets, EndNote |
| Nguồn tham khảo | Tailieukhoahoc.md (ThS. Đặng Văn Phong), Nguyễn Văn Thắng (2022) |

---

## Quy trình thực hiện

### Giai đoạn 1: Chuẩn bị

```
@literature_review_table tạo [loại bảng]
```

**Chọn loại bảng phù hợp:**

| Loại bảng | Khi nào sử dụng | Số cột |
|-----------|-----------------|--------|
| **Cơ bản** | Tổng quan nhanh, tiểu luận | 10 |
| **Chi tiết** | NCKH, khóa luận, luận văn | 14 |
| **Khái niệm** | Tổng hợp định nghĩa, quan điểm | 6 |

**Tạo file Excel/Google Sheets với các cột:**
- Template cơ bản: STT, Tác giả, Năm, Tiêu đề, Tạp chí, Số/Trang, Kết quả, Phương pháp, Mẫu, PP Phân tích
- Template chi tiết: + Câu hỏi NC, Cơ sở lý thuyết, Hạn chế, Ghi chú

---

### Giai đoạn 2: Thu thập tài liệu

```
@nghien_cuu tìm kiếm [keyword]
```

**Quy trình đọc tài liệu:**

1. **Scanning** - Tìm keyword trong bài
   - Đọc tiêu đề, abstract, keywords
   - Xác định bài có liên quan không

2. **Skimming** - Đọc lướt
   - Đọc đoạn đầu, cuối mỗi phần
   - Đọc kết luận
   - Nắm ý chính

3. **Intensive Reading** - Đọc kỹ
   - Đọc toàn bài nếu phù hợp
   - Ghi chú thông tin vào bảng

---

### Giai đoạn 3: Điền thông tin vào bảng

**Với mỗi tài liệu, điền đầy đủ:**

```markdown
| Cột | Nội dung cần điền |
|-----|-------------------|
| Tác giả | Họ tên đầy đủ hoặc theo format trích dẫn |
| Năm | Năm xuất bản |
| Tiêu đề | Tên đầy đủ của bài báo/sách |
| Tạp chí | Tên tạp chí, nhà xuất bản |
| Số/Trang | Volume, Issue, Pages |
| Kết quả | TÓM TẮT kết quả chính (2-3 câu) |
| Phương pháp | Định tính/Định lượng/Hỗn hợp + chi tiết |
| Mẫu | Số lượng + đối tượng (VD: 200 sinh viên) |
| PP Phân tích | SPSS, SmartPLS, Thematic analysis... |
```

**Ví dụ một dòng đã điền:**

| STT | Tác giả | Năm | Tiêu đề | Tạp chí | Kết quả | PP NC | Mẫu |
|-----|---------|-----|---------|---------|---------|-------|-----|
| 1 | Westphal et al. | 2022 | Facilitators and barriers to Children's Advocacy Center-based multidisciplinary teamwork | Child Abuse & Neglect | Xác định 4 chủ đề chính ảnh hưởng đến teamwork theo mô hình socioecological | Định tính, phỏng vấn bán cấu trúc | 25 thành viên MDT từ 1 CAC |

---

### Giai đoạn 4: Phân nhóm và Mã hóa

```
@literature_review_table phân_nhóm theo [tiêu chí]
```

**Bước 1: Thêm cột Mã hóa**

| Tiêu chí phân nhóm | Ví dụ mã |
|-------------------|----------|
| Phương pháp NC | ĐT (định tính), ĐL (định lượng), HH (hỗn hợp) |
| Góc nhìn/Tiếp cận | LT (lý thuyết), TT (thực tiễn), KT (kinh tế) |
| Kết quả | (+) tích cực, (-) tiêu cực, (0) trung lập |
| Đối tượng | SV (sinh viên), DN (doanh nghiệp), CC (công chức) |

**Bước 2: Sắp xếp theo Mã**
- Trong Excel: Data → Sort → Chọn cột Mã
- Các nghiên cứu cùng nhóm sẽ nằm cạnh nhau

**Bước 3: Đặt tên nhóm**
- Xác định đặc điểm chung của mỗi nhóm
- Đặt tên nhóm phản ánh góc tiếp cận

---

### Giai đoạn 5: Viết tổng quan theo chủ đề

```
@viet_bai tổng quan từ literature_review_table
```

**Template viết tổng quan:**

```markdown
Nhìn chung, có thể nhóm các nghiên cứu về [CHỦ ĐỀ] thành [N] nhóm chính.

**Nhóm thứ nhất** tiếp cận từ góc độ [GÓC NHÌN 1], tập trung nghiên cứu 
[NỘI DUNG]. Đại diện cho nhóm này là các nghiên cứu của (Tác giả A, năm; 
Tác giả B, năm; Tác giả C, năm). Các nghiên cứu này chỉ ra rằng [KẾT QUẢ 
CHUNG].

**Nhóm thứ hai** tiếp cận từ góc độ [GÓC NHÌN 2], nhấn mạnh đến [NỘI DUNG]. 
Theo hướng này, (Tác giả D, năm) và (Tác giả E, năm) đã chứng minh [KẾT QUẢ].

**So sánh** giữa các nhóm nghiên cứu, có thể thấy [ĐIỂM CHUNG]. Tuy nhiên, 
[ĐIỂM KHÁC BIỆT]. Điều này cho thấy [NHẬN XÉT].

Từ tổng quan trên, có thể xác định **khoảng trống tri thức**: [CHỈ RA NHỮNG 
GÌ CHƯA ĐƯỢC NGHIÊN CỨU]. Đây chính là cơ sở để nghiên cứu này tiến hành...
```

---

## Ví dụ sử dụng đầy đủ

### Bước 1: Tạo bảng
```
/literature_review_table "Các yếu tố ảnh hưởng đến quyết định mua hàng online"
```

### Bước 2: Thu thập và điền thông tin
- Tìm 30-50 tài liệu liên quan
- Điền vào bảng Literature Review Table

### Bước 3: Mã hóa
- Thêm cột Mã với các giá trị: TAM, TPB, UTAUT, OTHER (theo mô hình lý thuyết)

### Bước 4: Viết tổng quan

> Nhìn chung, các nghiên cứu về quyết định mua hàng online có thể nhóm thành 3 hướng tiếp cận chính.
>
> **Hướng thứ nhất** dựa trên mô hình TAM (Technology Acceptance Model), tập trung vào nhận thức hữu ích và nhận thức dễ sử dụng (Davis, 1989; Venkatesh & Davis, 2000; Nguyễn & Trần, 2020). Các nghiên cứu này chỉ ra rằng...
>
> **Hướng thứ hai** áp dụng TPB (Theory of Planned Behavior), nhấn mạnh vai trò của thái độ, chuẩn chủ quan và kiểm soát hành vi (Ajzen, 1991; Lê & Phạm, 2019)...
>
> **Hướng thứ ba** sử dụng UTAUT, tích hợp nhiều yếu tố từ các mô hình trước...
>
> Tuy nhiên, các nghiên cứu trên chủ yếu thực hiện tại các thành phố lớn, **chưa có nghiên cứu nào** khảo sát đối tượng sinh viên tại [địa phương cụ thể]. Đây là khoảng trống mà nghiên cứu này hướng đến.

---

## Lưu ý quan trọng

> ⚠️ **KHÔNG viết theo kiểu liệt kê:**
> ~~"Theo Nguyễn (2018)... Theo Trần (2019)... Theo Lê (2020)..."~~

> ✅ **PHẢI viết theo chủ đề/nhóm:**
> "Các nghiên cứu về X có thể chia thành 2 nhóm. Nhóm 1... (Nguyễn, 2018; Trần, 2019). Nhóm 2... (Lê, 2020; Phạm, 2021)"

---

## Công cụ hỗ trợ

| Công cụ | Mục đích |
|---------|----------|
| **Excel/Google Sheets** | Tạo và quản lý bảng, Sort, Filter |
| **EndNote 20** | Quản lý trích dẫn, tạo DMTLTK tự động |
| **Connected Papers** | Tìm các bài liên quan |
| **Paper Digest** | Tóm tắt tự động |

---

## Liên kết workflow

- Sử dụng sau: `/nghien_cuu_khoa_hoc` (Giai đoạn 2: Tổng quan tài liệu)
- Kết hợp với: `@nghien_cuu`, `@trich_dan`
- Output: Phần "Tổng quan nghiên cứu" trong báo cáo
