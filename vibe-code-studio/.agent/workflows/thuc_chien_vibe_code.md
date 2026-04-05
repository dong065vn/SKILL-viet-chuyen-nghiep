---
description: Quy trình lập trình đôi chuẩn Vibe Working - Thiết kế riêng để tăng hiệu suất.
---

# Workflow: Thực Chiến Vibe Code

## 📌 Chuẩn Bị (Input Check)
**Mục tiêu:** Bắt buộc AI và DONG phải có chung ngữ cảnh trước khi vào code.
1. AI sẽ kiểm tra xem DONG đã cung cấp các tài liệu cơ sở tại thư mục `01_Inputs/` chưa. 
   - *Nếu chưa có:* AI hỏi DONG muốn bắt đầu file mới hay cần cấp thông tin đầu vào (API docs, Design mockup...).
2. AI chốt yêu cầu bài toán (Sử dụng tư duy IPO):
   - **Input:** Cần nguyên liệu cấu trúc nào?
   - **Process:** Tư duy thuật toán ra sao? Component này làm việc thế nào?
   - **Output:** DONG muốn ra Component React, API Python hay script chạy thẳng?

## ⚙️ Thiết Kế Trạm Nháp (Process Draft)
**Mục tiêu:** Thử sai trên môi trường nháp tự do.
1. AI sẽ di chuyển và làm việc trong `02_Process/`.
2. Tạo file code `.draft.tsx` hoặc script thử nghiệm nhanh.
3. Chạy các tiến trình Fix Lỗi vòng lặp (Loop TDD).
4. Phản hồi với DONG dưới mô hình (Zero-Bollocks): *"Tôi đã thử A, gặp lỗi B, đã tự động fix thành C. Mọi thứ đang chạy ổn."*

## 🛠 Duyệt & Triển Khai (Output Delivery)
**Mục tiêu:** Ra sản phẩm đưa vào hệ sinh thái.
1. Sau khi DONG "Vibe Check" (Nghĩa là đồng ý với kết quả). AI đổi tên file từ Draft thành Clean.
2. Di dời file đã hoàn chỉnh vào cấu trúc `03_Outputs/` hoặc merge trực tiếp vào source code chính trên nhánh master.
3. Chạy `checklist.py`. Đảm bảo chuẩn chỉnh.

## 🧠 Gợi ý Tiến Hóa Tri Thức
- Kết thúc thao tác, AI quét lại xem hôm nay DONG có dặn dò thói quen gì mới (ví dụ "lần sau bỏ cái export default đi").
- AI đưa thói quen đó vào `.gemini/brain/` thành Knowledge. Hoặc đề nghị dùng `/dong-goi-vibe-skill`.
