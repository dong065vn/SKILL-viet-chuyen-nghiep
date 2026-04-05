---
name: dong-goi-vibe-skill
description: Meta-Skill cốt lõi để biến các tác vụ thành công lặp đi lặp lại thành một kỹ năng (Skill) mới nhằm tái sử dụng vĩnh viễn trong tương lai.
---

# Kỹ năng Đóng Gói Tri Thức Vibe Code

## Mục đích
Hỗ trợ Agent tự động chuyển đổi những kinh nghiệm, thói quen và quy trình đã được DONG huấn luyện thành một tệp `SKILL.md` hoặc một thư mục Skill hoàn chỉnh theo chuẩn KWSR. Ngăn chặn việc phải prompt lại cùng một vấn đề trong các hội thoại sau.

## Phạm vi Ứng dụng
- Khi kết quả của một buổi lập trình đôi (Vibe Code) diễn ra thuận lợi, xuất sắc.
- Khi DONG cung cấp một tài liệu chuẩn (Standard Operating Procedure) hoặc cấu trúc Code mẫu và muốn tái chế dài hạn.

## Bộ Nguyên Tắc Đóng Gói
1. **Tinh Lọc (Distillation):** Bỏ qua mọi context rườm rà. Lấy đúng quy luật lõi và tư duy xử lý (IPO). Bốc tách rõ Input expected, Process logic và Output template.
2. **Tuân thủ Vibe Structure:** Lưu file đúng chuẩn vào `.agent/skills/<tên-skill>/SKILL.md`.
3. **Mô tả tường minh (YAML Header):** Yêu cầu bắt buộc phải viết `description` thật chất lượng ở thẻ YAML của skill mới để khi sử dụng sau này, AI Agent của Antigravity có thể (Auto-Retrieve) tìm ra tự động.

## Quy trình Tự Động (Execution Flow)
Khi DONG yêu cầu `/dong-goi-kien-thuc`, Agent tuân thủ 4 bước:

- **Bước 1 (Analyze):** Phân tích 5-10 lượt chat vừa qua, hoặc file source DONG vừa cung cấp. Rút ra cốt lõi logic.
- **Bước 2 (Drafting):** Viết cấu trúc nháp `SKILL.md` cho skill mới. Phải bao gồm các phần: (Mục đích, Phạm Vi, Bộ Nguyên Tắc, Quy trình thực hiện).
- **Bước 3 (Review):** Xuất nội dung nháp cho DONG xem lại. Bắt buộc có thông báo: *"Dưới đây là kỹ năng tôi rút ra. Anh DONG có muốn thêm Rule hay Exception (ngoại lệ) nào không trước khi lưu?"*
- **Bước 4 (Save):** Agent tự động dùng tool `write_to_file` hoặc tương đương lưu vào `.agent/skills/`. Từ thời điểm lưu xong, Skill chính thức có hiệu lực trên toàn cõi Workspace.
