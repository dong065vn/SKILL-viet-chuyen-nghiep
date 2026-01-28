# Hướng Dẫn Sử Dụng Workspace Tạo Mục Lục 📚

Workspace này giúp bạn tạo **mục lục** cho các tài liệu học thuật:
- 📝 Bài tiểu luận
- 📋 Báo cáo thực tập
- 🎓 Đồ án tốt nghiệp

---

## 🚀 CÁCH SỬ DỤNG NHANH (Shortcut)

| Lệnh | Mô tả | Ví dụ |
|------|-------|-------|
| `/tieuluan` | Tạo mục lục tiểu luận | `/tieuluan về Marketing số` |
| `/thuctap` | Tạo mục lục báo cáo thực tập | `/thuctap về công ty FPT` |
| `/doan` | Tạo mục lục đồ án tốt nghiệp | `/doan về ứng dụng AI trong y tế` |
| `/toc` | Tạo mục lục tổng quát | `/toc cho báo cáo nghiên cứu` |
| `/brainstorm` | Chỉ brainstorm, chưa tạo | `/brainstorm ý tưởng luận văn` |
| `/cite` | Hướng dẫn trích dẫn | `/cite theo chuẩn APA` |

---

## 📁 CẤU TRÚC THƯ MỤC

```
toc-generator/
├── tailieudauvao/          ← Đặt tài liệu tham khảo vào đây
│   ├── sach/               ← Sách
│   ├── tapchi/             ← Tạp chí, bài báo
│   └── taiLieuKhac/        ← Tài liệu khác
├── ketqua/                 ← Mục lục hoàn thành sẽ ở đây
├── .antigravity/
│   ├── agents/             ← Các AI Agent
│   └── skills/             ← Các kỹ năng AI
└── .agent/workflows/       ← Các quy trình
```

---

## 👥 CÁC AGENT

### @TOC_Architect (Agent chính)
- **Vai trò:** Điều phối brainstorm và tạo mục lục
- **Dùng khi:** Bắt đầu tạo mục lục mới
- **Ví dụ:** `@TOC_Architect /brainstorm tạo mục lục đồ án`

### @Research_Analyst
- **Vai trò:** Phân tích tài liệu tham khảo
- **Dùng khi:** Cần tóm tắt sách, bài báo
- **Ví dụ:** `@Research_Analyst /analyze đọc tài liệu trong tailieudauvao`

### @Academic_Advisor
- **Vai trò:** Kiểm tra format và trích dẫn
- **Dùng khi:** Cần tạo danh mục TLTK
- **Ví dụ:** `@Academic_Advisor /cite theo chuẩn APA`

---

## 🔧 CÁC SKILL

| Skill | Mô tả |
|-------|-------|
| `/brainstorm` | Hỏi kỹ về yêu cầu trước khi tạo mục lục |
| `/analyze` | Phân tích tài liệu đầu vào |
| `/outline` | Tạo dàn ý với 2-3 phương án |
| `/structure` | Cấu trúc mục lục hoàn chỉnh |
| `/cite` | Trích dẫn và danh mục TLTK |

---

## 📋 QUY TRÌNH HOẠT ĐỘNG

```
┌─────────────────┐
│  1. BRAINSTORM  │  ← Hỏi kỹ về yêu cầu
└────────┬────────┘
         │ Xác nhận đủ thông tin
         ▼
┌─────────────────┐
│  2. OUTLINE     │  ← Đề xuất 2-3 phương án
└────────┬────────┘
         │ Chọn phương án
         ▼
┌─────────────────┐
│  3. STRUCTURE   │  ← Tạo mục lục chi tiết
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  4. CITE        │  ← Danh mục TLTK
└─────────────────┘
```

---

## ⚠️ NGUYÊN TẮC QUAN TRỌNG

1. **BRAINSTORM TRƯỚC** - AI sẽ hỏi kỹ trước khi tạo mục lục
2. **HỎI TỪNG CÂU MỘT** - Không hỏi nhiều câu cùng lúc
3. **LINH HOẠT** - Không áp đặt cấu trúc cứng
4. **ƯU TIÊN YÊU CẦU TRƯỜNG** - Nếu có mẫu sẵn, AI sẽ tuân theo

---

## 💡 VÍ DỤ SỬ DỤNG

### Tạo mục lục tiểu luận:
```
User: /tieuluan về tác động của mạng xã hội đến giới trẻ

AI: Chào anh/chị! Tôi sẽ giúp tạo mục lục cho bài tiểu luận.
    Trước hết, cho tôi hỏi: Môn học này là gì ạ?

User: Môn Xã hội học

AI: Giảng viên có yêu cầu đặc biệt gì về số chương hoặc format không ạ?

User: Phải có 3 chương, 15-20 trang

AI: Hiểu rồi! Có mẫu tiểu luận sẵn mà anh/chị phải tuân theo không?

User: Không có mẫu

AI: Tóm tắt: Tiểu luận Xã hội học, 3 chương, 15-20 trang.
    Anh/chị xác nhận để tôi đề xuất dàn ý nhé?

User: Đúng rồi

AI: [Đề xuất 2-3 phương án dàn ý...]
```

---

## 📞 CẦN HỖ TRỢ?

- Xem hướng dẫn chi tiết trong thư mục `.agent/workflows/`
- Mỗi loại tài liệu có quy trình riêng:
  - `tieu_luan.md` - Tiểu luận
  - `baocao_thuctap.md` - Báo cáo thực tập
  - `doan_totnghiep.md` - Đồ án tốt nghiệp
  - `general_toc.md` - Tài liệu khác

---

*TOC Generator Workspace Ready.* 📚✨
