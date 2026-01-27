---
description: Quy trình viết bài tiểu luận (5-20 trang) - LINH HOẠT theo yêu cầu
---

# Workflow: Viết Tiểu luận

Quy trình viết bài tiểu luận môn học với văn phong khoa học và trích dẫn chuẩn.

## Thông tin cơ bản

| Thuộc tính | Mô tả |
|------------|-------|
| Loại bài | Tiểu luận môn học |
| Độ dài | 5-20 trang |
| Bố cục | Theo mục hoặc theo chương (tùy yêu cầu) |

---

## Quy trình thực hiện

### Bước 1: Brainstorm yêu cầu
// turbo
```
@Advisor brainstorm [đề tài tiểu luận]
```

**Output cần có:**
- Phân tích đề tài
- Xác định phạm vi
- Dàn ý đề xuất
- **Xác nhận từ người dùng**

---

### Bước 2: Nghiên cứu tài liệu (nếu cần)
```
@Researcher tổng quan [đề tài] với keyword [từ khóa]
```

**Output:**
- Danh sách tài liệu tham khảo
- Tóm tắt các nghiên cứu liên quan
- Khoảng trống tri thức (nếu có)

---

### Bước 3: Xây dựng dàn ý chi tiết
```
@dan_bai tiểu luận [đề tài]
```

**Bố cục tiểu luận ngắn (5-10 trang):**
```
ĐẶT VẤN ĐỀ
1. Khái niệm cơ bản
2. Nội dung chính (theo yêu cầu đề bài)
3. Ví dụ/Ứng dụng
4. Đề xuất/Kiến nghị
KẾT LUẬN
DANH MỤC TÀI LIỆU THAM KHẢO
```

**Bố cục tiểu luận dài (10-20 trang):**
```
PHẦN MỞ ĐẦU
CHƯƠNG 1: CƠ SỞ LÝ LUẬN
CHƯƠNG 2: NỘI DUNG CHÍNH
CHƯƠNG 3: VÍ DỤ/ỨNG DỤNG (nếu có)
KẾT LUẬN
DANH MỤC TÀI LIỆU THAM KHẢO
```

---

### Bước 4: Viết nội dung
```
@Academic_Writer viết [phần] với dàn ý [dàn ý] theo chuẩn [APA/IEEE]
```

**Lưu ý khi viết:**
- Mỗi đoạn văn: Luận điểm → Luận cứ → Luận chứng
- Trích dẫn nguồn cho mỗi luận điểm
- Văn phong khoa học, không văn nói

**Viết theo thứ tự:**
1. Phần Đặt vấn đề/Mở đầu
2. Nội dung từng mục/chương
3. Kết luận

---

### Bước 5: Biên tập hoàn thiện
```
@Editor kiểm tra tất cả
```

**Checklist:**
- [ ] Nội dung đáp ứng yêu cầu đề bài
- [ ] Văn phong khoa học
- [ ] Trích dẫn đúng chuẩn
- [ ] Format đúng quy định
- [ ] Không lỗi chính tả

---

## Ví dụ sử dụng

```
/tieu_luan "Phân tích vai trò của công nghệ trong giáo dục hiện đại"
```

Hoặc từng bước:
```
1. @Advisor brainstorm "vai trò công nghệ trong giáo dục"
2. @Researcher tổng quan "công nghệ giáo dục" với keyword "EdTech, e-learning"
3. @Academic_Writer viết mở_đầu theo chuẩn APA
4. @Editor kiểm tra tất cả
```

---

## Lưu ý

> ⚠️ **QUAN TRỌNG**
> - Luôn brainstorm và xác nhận trước khi viết
> - Mỗi luận điểm cần có trích dẫn
> - Kiểm tra kỹ trước khi nộp
