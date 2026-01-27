# Academic Writer Workspace - Shortcut Guide

## 🚀 Quick Reference

### Workflows (Slash Commands)

| Shortcut | Mô tả | Ví dụ |
|----------|-------|-------|
| `/tieu_luan` | Viết tiểu luận (5-20 trang) | `/tieu_luan "Vai trò của AI trong giáo dục"` |
| `/baocao_thuctap` | Viết báo cáo thực tập (30-50 trang) | `/baocao_thuctap "Công tác tuyển dụng tại Công ty ABC"` |
| `/doan_totnghiep` | Viết đồ án tốt nghiệp (50-100+ trang) | `/doan_totnghiep "Nâng cao chất lượng nhân lực..."` |
| `/nckh` | Viết NCKH sinh viên | `/nckh "Các yếu tố ảnh hưởng đến..."` |

---

## 🤖 Agents

| Agent | Chức năng | Cách gọi |
|-------|-----------|----------|
| **Advisor** | Brainstorm, tư vấn | `@Advisor brainstorm [yêu cầu]` |
| **Researcher** | Nghiên cứu, tổng quan | `@Researcher tổng quan [đề tài]` |
| **Academic_Writer** | Viết nội dung | `@Academic_Writer viết [phần]` |
| **Editor** | Biên tập, kiểm tra | `@Editor kiểm tra [loại]` |

### Chi tiết Agent commands

#### @Advisor
```
@Advisor brainstorm "yêu cầu"
@Advisor phản biện "nội dung"
@Advisor tư vấn dàn ý "đề tài"
```

#### @Researcher
```
@Researcher tổng quan "đề tài" với keyword "từ khóa"
@Researcher tìm tài liệu "chủ đề"
@Researcher phân tích khoảng trống "lĩnh vực"
```

#### @Academic_Writer
```
@Academic_Writer viết mở_đầu theo chuẩn APA
@Academic_Writer viết chương_1 với dàn_ý [dàn ý]
@Academic_Writer viết kết_luận
```

#### @Editor
```
@Editor kiểm tra tất cả
@Editor kiểm tra nội dung
@Editor kiểm tra văn phong
@Editor kiểm tra trích dẫn
@Editor kiểm tra format
```

---

## 🛠️ Skills

| Skill | Chức năng | Cách gọi |
|-------|-----------|----------|
| `brainstorm` | Khai thác yêu cầu | `@brainstorm [yêu cầu]` |
| `nghien_cuu` | Nghiên cứu tài liệu | `@nghien_cuu [đề tài]` |
| `dan_bai` | Xây dựng dàn ý | `@dan_bai [loại] [đề tài]` |
| `viet_bai` | Viết nội dung | `@viet_bai [phần] [chủ đề]` |
| `trich_dan` | Trích dẫn | `@trich_dan [APA/IEEE] [loại] [thông tin]` |
| `phan_tich` | Phân tích | `@phan_tich [phương pháp] [vấn đề]` |
| `bien_tap` | Biên tập | `@bien_tap [loại]` |

### Chi tiết Skill commands

#### @brainstorm
```
@brainstorm "Tôi muốn viết về AI trong giáo dục"
```

#### @nghien_cuu
```
@nghien_cuu "công nghệ giáo dục"
@nghien_cuu keyword "AI, e-learning, EdTech"
```

#### @dan_bai
```
@dan_bai tiểu luận "Vai trò của công nghệ"
@dan_bai báo cáo "Công tác tuyển dụng"
@dan_bai đồ_án "Nâng cao chất lượng..."
```

#### @viet_bai
```
@viet_bai mở_đầu "chủ đề"
@viet_bai chương_1 "cơ sở lý luận"
@viet_bai thực_trạng với số_liệu [data]
@viet_bai kết_luận
```

#### @trich_dan
```
@trich_dan APA sách "Nguyễn A, 2020, Tên sách, NXB"
@trich_dan APA bài_báo "Tác giả, Năm, Tên bài, Tạp chí, Vol, Trang"
@trich_dan IEEE sách "Thông tin"
```

#### @phan_tich
```
@phan_tich dao_sau "Công tác tuyển dụng"
@phan_tich so_sanh "Phương pháp A vs Phương pháp B"
@phan_tich phan_bien "Quan điểm của tác giả X"
```

#### @bien_tap
```
@bien_tap content "nội dung"
@bien_tap format "bài viết"
@bien_tap citation "kiểm tra trích dẫn"
@bien_tap all "kiểm tra tất cả"
```

---

## 📚 Quick Access - Knowledge Base

| File | Nội dung |
|------|----------|
| `apa_style_guide.md` | Hướng dẫn trích dẫn APA |
| `ieee_style_guide.md` | Hướng dẫn trích dẫn IEEE |
| `van_phong_khoa_hoc.md` | Hướng dẫn văn phong |

Đường dẫn: `.antigravity/knowledge_base/`

---

## 📁 Thư mục đầu vào

| Thư mục | Đặt gì? |
|---------|---------|
| `tailieu_dauvao/sach/` | Sách tham khảo |
| `tailieu_dauvao/tapchi/` | Bài báo, tạp chí |
| `tailieu_dauvao/baocao/` | Báo cáo, nghiên cứu |
| `output/` | Kết quả đầu ra |

---

## ⚡ Quy trình nhanh

### Viết tiểu luận trong 5 bước:

```
1. @Advisor brainstorm "đề tài"
   → Xác nhận yêu cầu

2. @dan_bai tiểu luận "đề tài"
   → Xây dựng bố cục

3. @Academic_Writer viết theo dàn ý
   → Viết nội dung

4. @Editor kiểm tra tất cả
   → Biên tập

5. Hoàn thành! 🎉
```

### Hoặc dùng workflow:

```
/tieu_luan "đề tài"
→ Hệ thống tự động chạy qua các bước
```

---

## 🔥 Tips

| Tip | Mô tả |
|-----|-------|
| ✅ Brainstorm trước | Luôn xác nhận yêu cầu trước khi viết |
| ✅ Chia nhỏ công việc | Viết từng phần thay vì cả bài |
| ✅ Trích dẫn đầy đủ | Mỗi luận điểm cần có nguồn |
| ✅ Kiểm tra cuối cùng | Dùng @Editor trước khi nộp |

---

## ❓ Khi cần trợ giúp

```
@Advisor tôi cần giúp về [vấn đề]
```

Hoặc mở file hướng dẫn chi tiết:
```
setup_instruction.md
```
