---
name: analyze
description: >
  Phân tích tài liệu đầu vào (sách, tạp chí, bài báo) để rút ra nội dung chính,
  các điểm quan trọng cần đưa vào mục lục.
---

# Phân Tích Tài Liệu

## Mục đích

Đọc và phân tích tài liệu đầu vào để xác định:
- Các chủ điểm chính và phụ
- Cấu trúc logic của nội dung
- Các khái niệm cần đề cập trong mục lục

---

## Quy trình phân tích

### 1. Tiếp nhận tài liệu

Kiểm tra thư mục `tailieudauvao/` để xem tài liệu có sẵn:
- `tailieudauvao/sach/` - Sách tham khảo
- `tailieudauvao/tapchi/` - Tạp chí, bài báo
- `tailieudauvao/taiLieuKhac/` - Tài liệu khác

---

### 2. Đọc và tóm tắt

Với mỗi tài liệu:
1. Đọc tiêu đề, mục lục (nếu có)
2. Xác định các phần chính
3. Tóm tắt nội dung cốt lõi (3-5 câu/tài liệu)
4. Ghi nhận các keyword quan trọng

---

### 3. Phân loại nội dung

Phân loại theo các nhóm:
- **Lý thuyết/Khái niệm**: Định nghĩa, khái niệm cơ bản
- **Phương pháp**: Cách tiếp cận, phương pháp nghiên cứu
- **Ứng dụng/Thực tiễn**: Ví dụ, case study
- **Kết quả/Số liệu**: Dữ liệu, thống kê

---

### 4. Output

Tạo bản tóm tắt phân tích:

```markdown
## Tóm tắt tài liệu

### Tài liệu 1: [Tên]
- Nội dung chính: 
- Các điểm có thể đưa vào mục lục:
  - ...
  - ...

### Tài liệu 2: [Tên]
...

## Đề xuất cấu trúc dựa trên phân tích
- Chương về lý thuyết: từ tài liệu 1, 3
- Chương về phương pháp: từ tài liệu 2
- Chương về kết quả: từ tài liệu 4
```

---

## Lưu ý

- Không copy nguyên văn - chỉ phân tích và tóm tắt
- Ghi nguồn rõ ràng cho mỗi thông tin
- Đề xuất nhưng không áp đặt cấu trúc
