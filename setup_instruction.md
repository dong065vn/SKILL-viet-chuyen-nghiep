# Academic Writer Workspace - Hướng dẫn Sử dụng

## Giới thiệu

**Academic Writer Workspace** là workspace chuyên dụng cho việc viết các bài học thuật:
- 📝 Tiểu luận môn học
- 📋 Báo cáo thực tập
- 🎓 Đồ án/Khóa luận tốt nghiệp
- 🔬 Nghiên cứu khoa học sinh viên

### Đặc điểm nổi bật

| Tính năng | Mô tả |
|-----------|-------|
| **Văn phong khoa học** | Chuyên nghiệp - Sáng rõ - Khách quan |
| **Cấu trúc chặt chẽ** | Luận điểm → Luận cứ → Luận chứng |
| **Trích dẫn chuẩn** | Hỗ trợ APA và IEEE |
| **Phân tích sâu** | Đào sâu - So sánh - Phản biện |
| **Brainstorm trước khi viết** | Xác nhận yêu cầu trước khi thực hiện |

---

## Cấu trúc Workspace

```
academic-writer-workspace/
├── .antigravity/
│   ├── agents/                    # 4 AI Agents chuyên biệt
│   │   ├── Academic_Writer.md     # Viết bài học thuật
│   │   ├── Researcher.md          # Nghiên cứu, tổng quan
│   │   ├── Editor.md              # Biên tập, kiểm tra
│   │   └── Advisor.md             # Tư vấn, brainstorm
│   ├── skills/                    # 7 Skills chuyên biệt
│   │   ├── nghien_cuu/            # Research & Literature Review
│   │   ├── dan_bai/               # Outline/Structure
│   │   ├── viet_bai/              # Academic Writing
│   │   ├── trich_dan/             # Citations (APA & IEEE)
│   │   ├── phan_tich/             # Analysis
│   │   ├── bien_tap/              # Review & Edit
│   │   └── brainstorm/            # Brainstorm
│   └── knowledge_base/            # Kiến thức nền tảng
│       ├── apa_style_guide.md     # Hướng dẫn APA
│       ├── ieee_style_guide.md    # Hướng dẫn IEEE
│       └── van_phong_khoa_hoc.md  # Văn phong khoa học
├── .agent/workflows/              # 4 Workflows
│   ├── tieu_luan.md               # /tieu_luan
│   ├── baocao_thuctap.md          # /baocao_thuctap
│   ├── doan_totnghiep.md          # /doan_totnghiep
│   └── nghien_cuu_khoa_hoc.md     # /nckh
├── tailieu_dauvao/                # Thư mục đầu vào
│   ├── sach/                      # Sách tham khảo
│   ├── tapchi/                    # Bài báo, tạp chí
│   └── baocao/                    # Báo cáo, nghiên cứu
└── output/                        # Kết quả đầu ra
```

---

## Cách sử dụng

### 1. Sử dụng Workflows (Khuyến nghị)

Cách nhanh nhất để bắt đầu viết bài:

```
/tieu_luan "Đề tài tiểu luận của bạn"
```

```
/baocao_thuctap "Chuyên đề thực tập tại Công ty ABC"
```

```
/doan_totnghiep "Đề tài đồ án tốt nghiệp"
```

```
/nckh "Đề tài nghiên cứu khoa học"
```

### 2. Sử dụng từng Agent

#### @Advisor - Brainstorm và tư vấn
```
@Advisor brainstorm "Tôi cần viết tiểu luận về AI trong giáo dục"
```

#### @Researcher - Nghiên cứu tài liệu
```
@Researcher tổng quan "AI trong giáo dục" với keyword "AI, EdTech, e-learning"
```

#### @Academic_Writer - Viết nội dung
```
@Academic_Writer viết mở_đầu theo chuẩn APA
@Academic_Writer viết chương_1 với dàn_ý [dàn ý]
```

#### @Editor - Biên tập
```
@Editor kiểm tra tất cả
@Editor kiểm tra trích dẫn
```

### 3. Sử dụng từng Skill

```
@brainstorm "yêu cầu"
@nghien_cuu "đề tài"
@dan_bai tiểu luận "đề tài"
@viet_bai mở_đầu "chủ đề"
@trich_dan APA sách "thông tin"
@phan_tich so_sanh "vấn đề A vs B"
@bien_tap nội dung
```

---

## Quy trình làm việc chuẩn

### Bước 1: Brainstorm
> ⚠️ **QUAN TRỌNG**: Luôn brainstorm và xác nhận trước khi viết

```
@Advisor brainstorm [yêu cầu của bạn]
```

→ AI sẽ hỏi các câu hỏi làm rõ và đề xuất hướng tiếp cận

### Bước 2: Nghiên cứu (nếu cần)
```
@Researcher tổng quan [đề tài]
```

→ AI sẽ tìm và tổng hợp tài liệu tham khảo

### Bước 3: Xây dựng dàn ý
```
@dan_bai [loại bài] [đề tài]
```

→ AI sẽ đề xuất bố cục phù hợp

### Bước 4: Viết nội dung
```
@Academic_Writer viết [phần] theo chuẩn [APA/IEEE]
```

→ AI viết nội dung với văn phong khoa học và trích dẫn

### Bước 5: Biên tập
```
@Editor kiểm tra tất cả
```

→ AI kiểm tra và đề xuất chỉnh sửa

---

## Cách đưa tài liệu đầu vào

1. **Sách tham khảo**: Đặt vào `tailieu_dauvao/sach/`
2. **Bài báo, tạp chí**: Đặt vào `tailieu_dauvao/tapchi/`
3. **Báo cáo có sẵn**: Đặt vào `tailieu_dauvao/baocao/`

Sau đó:
```
@Researcher đọc tài liệu từ tailieu_dauvao/sach
```

---

## Cấu trúc lập luận

Mỗi đoạn văn được viết theo công thức:

```
LUẬN ĐIỂM (câu kết luận chính)
    ↓
LUẬN CỨ (lý lẽ, lập luận)
    ↓
LUẬN CHỨNG (bằng chứng, số liệu + trích dẫn)
    ↓
KẾT LUẬN (tổng hợp)
```

**Ví dụ:**
> **Việc học tốt ngoại ngữ giúp sinh viên có thu nhập cao** (luận điểm). Sinh viên có khả năng ngoại ngữ sẽ có cơ hội làm việc trong doanh nghiệp nước ngoài (luận cứ). Theo Tổng cục Thống kê (2020), mức lương tại doanh nghiệp nước ngoài cao hơn 1.5 lần (luận chứng + trích dẫn).

---

## Kiểu trích dẫn

### APA (Khoa học xã hội, Giáo dục)
```
Trích dẫn trong bài: (Nguyễn, 2020)
DMTLTK: Xếp theo alphabet
```

### IEEE (Kỹ thuật, CNTT)
```
Trích dẫn trong bài: [1], [2], [3]
DMTLTK: Xếp theo số thứ tự
```

Chi tiết xem: `.antigravity/knowledge_base/apa_style_guide.md` và `ieee_style_guide.md`

---

## Mẹo sử dụng hiệu quả

### 💡 Brainstorm kỹ trước khi viết
- AI sẽ không viết nếu chưa được xác nhận
- Điều này giúp đảm bảo sản phẩm đúng yêu cầu

### 💡 Cung cấp đủ thông tin
- Loại bài, số trang, deadline
- Yêu cầu format của trường
- Tài liệu đã có

### 💡 Chia nhỏ công việc
- Viết từng phần thay vì cả bài
- Kiểm tra từng phần trước khi tiếp tục

### 💡 Luôn trích dẫn nguồn
- Mỗi luận điểm cần có trích dẫn
- Ưu tiên trích gián tiếp

---

## Hỗ trợ

Nếu gặp vấn đề, hãy hỏi:
```
@Advisor tôi cần giúp về [vấn đề]
```

Hoặc xem chi tiết từng skill:
```
Mở file: .antigravity/skills/[tên skill]/SKILL.md
```
