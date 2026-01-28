---
description: Tạo mục lục cho đồ án tốt nghiệp - LINH HOẠT theo quy định trường
---

# Workflow: Tạo Mục Lục Đồ Án Tốt Nghiệp

Quy trình CHI TIẾT để tạo mục lục cho đồ án/luận văn tốt nghiệp.

---

## ⚠️ LƯU Ý QUAN TRỌNG

Đồ án tốt nghiệp là tài liệu QUAN TRỌNG NHẤT trong quá trình học.
- Mỗi trường có quy định riêng về format
- Phải hỏi KỸ về yêu cầu từ giáo viên hướng dẫn
- KHÔNG được bỏ qua bất kỳ yêu cầu đặc biệt nào

---

## Bước 1: Brainstorm KỸ LƯỠNG (Bắt buộc)

```
@TOC_Architect /brainstorm tạo mục lục đồ án tốt nghiệp
```

**Agent sẽ hỏi TỪNG CÂU MỘT về:**

### Thông tin cơ bản:
- [ ] Đề tài đồ án là gì?
- [ ] Ngành học và chuyên ngành?
- [ ] Trường/Khoa?
- [ ] Tên giáo viên hướng dẫn?

### Yêu cầu từ trường:
- [ ] **CÓ MẪU ĐỒ ÁN CHUẨN KHÔNG?** (rất quan trọng!)
- [ ] Số trang tối thiểu/tối đa?
- [ ] Số chương yêu cầu?
- [ ] Yêu cầu về phần Tổng quan / Cơ sở lý thuyết?
- [ ] Chuẩn trích dẫn nào? (APA, hay chuẩn riêng?)

### Yêu cầu từ GVHD:
- [ ] GVHD có yêu cầu đặc biệt gì không?
- [ ] Có phải gửi outline trước để duyệt không?

### Nội dung:
- [ ] Đồ án lý thuyết hay có phần thực hành/code?
- [ ] Có sản phẩm demo không?
- [ ] Tài liệu tham khảo chính?

**⚠️ CHỈ tiến hành khi người dùng XÁC NHẬN đã đủ thông tin!**

---

## Bước 2: Phân tích tài liệu nghiên cứu

```
@Research_Analyst /analyze phân tích các tài liệu tham khảo
```

---

## Bước 3: Đề xuất dàn ý (2-3 phương án)

```
@TOC_Architect /outline đề xuất các phương án dàn ý
```

**Cấu trúc GỢI Ý (PHỤ THUỘC vào quy định trường):**

```
LỜI CAM ĐOAN
LỜI CẢM ƠN
TÓM TẮT (Tiếng Việt)
ABSTRACT (Tiếng Anh)
DANH MỤC HÌNH ẢNH
DANH MỤC BẢNG BIỂU
DANH MỤC TỪ VIẾT TẮT

MỞ ĐẦU
   1. Lý do chọn đề tài
   2. Mục tiêu nghiên cứu
   3. Đối tượng và phạm vi nghiên cứu
   4. Phương pháp nghiên cứu
   5. Ý nghĩa khoa học và thực tiễn
   6. Bố cục đồ án

CHƯƠNG 1: TỔNG QUAN VỀ [LĨNH VỰC]
   1.1. Giới thiệu chung
   1.2. Tình hình nghiên cứu trong nước
   1.3. Tình hình nghiên cứu nước ngoài
   1.4. Các công trình liên quan
   1.5. Đánh giá và hướng tiếp cận

CHƯƠNG 2: CƠ SỞ LÝ THUYẾT
   2.1. [Lý thuyết nền tảng 1]
   2.2. [Lý thuyết nền tảng 2]
   2.3. Công nghệ và công cụ sử dụng
   2.4. Kết luận chương

CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ
   3.1. Phân tích yêu cầu
   3.2. Thiết kế tổng quan
   3.3. Thiết kế chi tiết
   3.4. Kết luận chương

CHƯƠNG 4: TRIỂN KHAI VÀ KẾT QUẢ
   4.1. Môi trường triển khai
   4.2. Kết quả đạt được
   4.3. Đánh giá và so sánh
   4.4. Kết luận chương

KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
   1. Kết luận
   2. Hạn chế
   3. Hướng phát triển

TÀI LIỆU THAM KHẢO
PHỤ LỤC
```

---

## Bước 4: Điều chỉnh theo phản hồi

Lặp lại cho đến khi người dùng hài lòng:

```
@TOC_Architect /outline điều chỉnh theo phản hồi
```

---

## Bước 5: Tạo mục lục hoàn chỉnh

```
@TOC_Architect /structure tạo mục lục chi tiết với đánh số chuẩn
```

---

## Bước 6: Tạo danh mục TLTK

```
@Academic_Advisor /cite tạo danh mục TLTK theo chuẩn [APA/chuẩn trường]
```

---

## Kết quả

Mục lục được lưu tại: `ketqua/mucluc_doan_totnghiep_[ten].md`

---

## Shortcut

```
/doan về [đề tài]
```

---

## Phụ lục: Template câu hỏi brainstorm

Danh sách câu hỏi gợi ý (hỏi từng câu một):

1. "Đề tài đồ án của anh/chị là gì?"
2. "Ngành học và chuyên ngành?"
3. "Trường và khoa nào?"
4. "Giáo viên hướng dẫn có yêu cầu gì đặc biệt không?"
5. "Trường có mẫu đồ án chuẩn không? Xin chia sẻ nếu có."
6. "Số trang tối thiểu và tối đa?"
7. "Đồ án có phần thực hành/demo không?"
8. "Chuẩn trích dẫn yêu cầu là gì?"
9. "Deadline nộp là khi nào?"
10. "Có gì khác cần lưu ý không?"
