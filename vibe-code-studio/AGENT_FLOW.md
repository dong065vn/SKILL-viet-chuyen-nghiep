# 🔄 Phương Pháp Vận Hành Tương Tác: Thuyết Vibe Working & KWSR

> **Antigravity Vibe Code Studio** - Cẩm nang tư duy vòng đời dữ liệu & tích lũy tri thức

---

## 📊 Tổng Quan Luồng Vibe Working (1 Chiều)

```text
┌─────────────────────────────────────────────────────────────────┐
│                      👤 USER (DONG) & AI                        │
│                 (Hợp tác đôi - Pair Programming)                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    01_INPUTS (READ-ONLY)                        │
│  • Dữ liệu đầu vào: Yêu cầu, source code chưa hoàn thiện        │
│  • Nguyên tắc: Không ai được ghi đè, làm hỏng bản gốc           │
└────────────────────────────┬────────────────────────────────────┘
                             │
               ┌─────────────┴─────────────┐
               │         IPO PROCESS       │
               ▼                           ▼
    ┌───────────────────┐        ┌──────────────────┐
    │  PHÂN TÍCH NHIỆM VỤ     │  │  KÍCH HOẠT SKILL │
    │ (Brainstorming/Task.md) │  │ (Auto-retrieve)  │
    └─────────┬─────────┘        └────────┬─────────┘
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    02_PROCESS (VÙNG NHÁP)                       │
│  • Môi trường để AI thử nghiệm: Viết code, chạy test, sửa lỗi   │
│  • Áp dụng kỹ thuật: Code generation, Linting, Debugging        │
└────────────────────────────┬────────────────────────────────────┘
                             │ (Xác nhận hoàn thành)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    03_OUTPUTS (SẢN PHẨM)                        │
│  • Kết quả đạt chuẩn: File source code đã verified, Report      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│            ĐÓNG GÓI TRI THỨC (TIẾN HÓA KWSR)                    │
│  • Biến quy trình xử lý vừa rồi thành Skill để tái sử dụng      │
│  • `dong-goi-vibe-skill` được kích hoạt tự động                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Chi tiết Vòng Đời KWSR

KWSR là hệ thống phát triển năng lực AI, từ mức độ "tập sự" đến "chuyên gia kiểm soát". Mọi phiên làm việc Vibe Code đều tuân thủ nguyên lý tiến hóa này.

### 1️⃣ Knowledge (Tri Thức Cơ Bản - Tự Động)
Hệ thống **Brain** tự động ghi nhận hội thoại, lưu vào `knowledge/` dưới dạng các Knowledge Items.
* Áp dụng: Lưu trữ những thói quen nhỏ của DONG (ví dụ: Luôn dùng `const` thay vì `let`, thích thụt đầu dòng 2 space).

### 2️⃣ Workflow (Quy Trình Chuẩn Hóa - Bán Tự Động)
Khi một công việc lặp lại hơn 3 lần, nó được nâng cấp thành **Workflow**.
* Ví dụ: `/thuc-chien-vibe` là một lệnh quy định các bước: (1) Đọc yêu cầu -> (2) Viết code -> (3) Review nội bộ -> (4) Xuất kết quả.

### 3️⃣ Skill (Kỹ Năng Chuyên Môn - Chuyên Sâu)
Skill trả lời câu hỏi: *Làm thế nào để hoàn thành xuất sắc?*
* Ví dụ: Từ kinh nghiệm Frontend, xây dựng `dong-goi-vibe-skill`, biến AI thành chuyên gia tự đóng gói kinh nghiệm.
* Kích hoạt tự động khi nhận diện pattern trong yêu cầu.

### 4️⃣ Rule (Quy Tắc Luật Lệ - Chốt Chặn Bắt Buộc)
Nguyên tắc bất di bất dịch của dự án. AI tuyệt đối không được vi phạm.
* Ví dụ: `.agent/rules/vibe_code_principles.md`. Không tự ý xóa file, giữ giọng điệu phản hồi tự nhiên, ngắn gọn.

---

## 💻 Hệ Lệnh Thực Chiến (Slash Commands)

Để thúc đẩy tiến độ, chúng tôi cung cấp các Workflow gọi tắt thông qua dấu `/`:

| Lệnh | Ý nghĩa (Mục đích theo Vibe Working) |
| --- | --- |
| `/thuc-chien-vibe` | Bắt đầu chu trình Vibe Code chuẩn: Lên kế hoạch -> Chốt Input -> Xử lý |
| `/dong-goi-vibe-skill`| Quét phiên trò chuyện hiện tại, xuất ra file `.md` chuẩn cấu trúc Skill |
| `/brainstorm` | Định hình ý tưởng (Giai đoạn lên Input) |
| `/debug` | Giải quyết lỗi phát sinh (Giai đoạn Process) |

---

## ⚖️ Tiêu Chuẩn Phản Hồi Khi Lập Trình Đôi (Vibe Code)
- **Zero-Bollocks:** Ngắn gọn, không giải thích những khái niệm phổ thông. Chỉ tập trung vào thay đổi trọng tâm.
- **Fail-Fast:** Nếu code sai, AI sẽ đề xuất Rollback hoặc sửa thẳng, không vòng vo xin lỗi lấp liếm.
- **Context-Aware:** Auto đọc `01_Inputs/` để không hỏi lại những thứ đã có sẵn trong file.
