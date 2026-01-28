---
description: Tạo mục lục cho bài tiểu luận (5-20 trang) - LINH HOẠT theo yêu cầu
---

# Workflow: Tạo Mục Lục Tiểu Luận

Quy trình từng bước để tạo mục lục cho bài tiểu luận.

---

## Bước 1: Brainstorm với người dùng

```
@TOC_Architect /brainstorm tạo mục lục tiểu luận
```

**Agent sẽ hỏi từng câu về:**
- [ ] Chủ đề tiểu luận
- [ ] Môn học / Giảng viên
- [ ] Yêu cầu đặc biệt từ giảng viên (số trang, số chương...)
- [ ] Có mẫu sẵn không?

**⚠️ KHÔNG tiến hành bước 2 nếu chưa xác nhận đầy đủ thông tin!**

---

## Bước 2: Phân tích tài liệu (nếu có)

Nếu người dùng có tài liệu tham khảo:

```
@Research_Analyst /analyze đọc tài liệu trong tailieudauvao
```

---

## Bước 3: Đề xuất dàn ý

```
@TOC_Architect /outline đề xuất 2-3 phương án dàn ý
```

**Agent sẽ:**
- [ ] Đề xuất 2-3 phương án phù hợp với tiểu luận
- [ ] Giải thích ưu/nhược điểm
- [ ] Chờ người dùng chọn

**Cấu trúc GỢI Ý (có thể thay đổi theo yêu cầu):**
```
LỜI MỞ ĐẦU
1. Chương 1: Tổng quan / Giới thiệu
2. Chương 2: Nội dung chính
3. Chương 3: Phân tích / Bàn luận (tuỳ chọn)
KẾT LUẬN
TÀI LIỆU THAM KHẢO
```

---

## Bước 4: Tạo mục lục hoàn chỉnh

```
@TOC_Architect /structure tạo mục lục chi tiết
```

---

## Bước 5: Kiểm tra format và TLTK

```
@Academic_Advisor /cite tạo danh mục TLTK theo chuẩn yêu cầu
```

---

## Kết quả

Mục lục hoàn chỉnh được lưu tại: `ketqua/mucluc_tieuluan_[ten].md`

---

## Shortcut

Dùng lệnh tắt để bắt đầu nhanh:
```
/tieuluan về [chủ đề]
```
