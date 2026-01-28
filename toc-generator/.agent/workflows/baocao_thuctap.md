---
description: Tạo mục lục cho báo cáo thực tập - LINH HOẠT theo format trường/khoa
---

# Workflow: Tạo Mục Lục Báo Cáo Thực Tập

Quy trình từng bước để tạo mục lục cho báo cáo thực tập.

---

## Bước 1: Brainstorm CHI TIẾT

```
@TOC_Architect /brainstorm tạo mục lục báo cáo thực tập
```

**Agent sẽ hỏi từng câu về:**
- [ ] Tên công ty/đơn vị thực tập
- [ ] Vị trí thực tập
- [ ] Thời gian thực tập
- [ ] Trường/Khoa của bạn
- [ ] **MẪU BÁO CÁO CÓ SẴN KHÔNG?** (quan trọng!)
- [ ] Yêu cầu đặc biệt từ giáo viên hướng dẫn
- [ ] Số trang yêu cầu

**⚠️ Mỗi trường/khoa có format riêng - phải hỏi kỹ!**

---

## Bước 2: Phân tích tài liệu công ty (nếu có)

```
@Research_Analyst /analyze đọc tài liệu về công ty trong tailieudauvao
```

---

## Bước 3: Đề xuất dàn ý

```
@TOC_Architect /outline đề xuất dàn ý phù hợp với mẫu trường
```

**Cấu trúc GỢI Ý (thay đổi theo mẫu trường):**
```
LỜI CẢM ƠN
DANH MỤC HÌNH ẢNH
DANH MỤC BẢNG BIỂU
DANH MỤC TỪ VIẾT TẮT

PHẦN MỞ ĐẦU
- Lý do chọn đơn vị thực tập
- Mục tiêu thực tập

CHƯƠNG 1: GIỚI THIỆU VỀ ĐƠN VỊ THỰC TẬP
1.1. Thông tin chung
1.2. Lịch sử hình thành
1.3. Cơ cấu tổ chức
1.4. Lĩnh vực hoạt động

CHƯƠNG 2: NỘI DUNG THỰC TẬP
2.1. Vị trí và nhiệm vụ được giao
2.2. Các công việc thực hiện
2.3. Kỹ năng và kiến thức áp dụng

CHƯƠNG 3: KẾT QUẢ VÀ ĐÁNH GIÁ
3.1. Kết quả đạt được
3.2. Thuận lợi và khó khăn
3.3. Bài học kinh nghiệm

KẾT LUẬN VÀ KIẾN NGHỊ
TÀI LIỆU THAM KHẢO
PHỤ LỤC
```

---

## Bước 4: Tùy chỉnh theo yêu cầu

Nếu người dùng có mẫu riêng → Điều chỉnh theo mẫu đó.

```
@TOC_Architect /structure tạo mục lục theo mẫu người dùng cung cấp
```

---

## Bước 5: Hoàn thiện

```
@Academic_Advisor /cite tạo danh mục TLTK
```

---

## Kết quả

Mục lục được lưu tại: `ketqua/mucluc_baocao_thuctap_[ten].md`

---

## Shortcut

```
/thuctap về công ty [tên công ty]
```

---

## Lưu ý đặc biệt

> **QUAN TRỌNG:** Báo cáo thực tập thường có mẫu cố định từ trường.
> Luôn hỏi người dùng có mẫu sẵn không trước khi đề xuất cấu trúc.
