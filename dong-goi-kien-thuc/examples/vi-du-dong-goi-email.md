# Ví dụ: Đóng gói kiến thức "Viết Email Chuyên Nghiệp" thành Skill

## Input mẫu

**Yêu cầu người dùng:**
> "Tôi muốn đóng gói kiến thức viết email công việc cho team marketing. 
> Chúng tôi có quy tắc: tiêu đề phải có action keyword, nội dung theo cấu trúc Pyramid, 
> không quá 200 từ, và luôn có call-to-action rõ ràng."

---

## Output mẫu — SKILL.md được tạo ra

```markdown
---
name: viet-email-marketing
description: Chuyên gia soạn thảo email công việc chuẩn mực cho team marketing, áp dụng cấu trúc Pyramid và quy tắc brand voice.
---

# Kỹ năng Viết Email Marketing

## Mục đích
Hỗ trợ team marketing soạn email công việc chuyên nghiệp, đảm bảo nhất quán về văn phong và cấu trúc.

## Phạm vi Ứng dụng
- Email gửi khách hàng (follow-up, proposal, cảm ơn)
- Email nội bộ (báo cáo, yêu cầu, thông báo)
- Email outreach (giới thiệu sản phẩm, mời hợp tác)

## Bộ Nguyên tắc Cốt lõi
1. **Tiêu đề = [Action] + [Chủ đề] + [Deadline/Context]**
   - ✅ "[Cần phản hồi] Đề xuất chiến dịch Q2 - trước thứ 6"
   - ❌ "Về vấn đề chiến dịch"
2. **Cấu trúc Pyramid:** Yêu cầu chính ở dòng đầu tiên, chi tiết bên dưới
3. **Giới hạn 200 từ:** Ngắn gọn, mỗi đoạn tối đa 3 câu
4. **Call-to-action rõ ràng:** Cuối email phải nêu rõ hành động cần, người chịu trách nhiệm, deadline
5. **Giọng điệu:** Thân thiện nhưng chuyên nghiệp, xưng hô "anh/chị" với khách, "mình" với team

## Quy trình Thực hiện
1. **Xác định:** Ai nhận? Mục đích? Mức độ khẩn cấp?
2. **Soạn tiêu đề:** Theo công thức [Action] + [Chủ đề] + [Context]
3. **Viết dòng đầu:** Tóm tắt yêu cầu chính (1 câu)
4. **Triển khai nội dung:** Chi tiết hỗ trợ (2-3 đoạn ngắn)
5. **Kết thúc:** Call-to-action + deadline + chữ ký
6. **Rà soát:** Kiểm tra độ dài, lỗi chính tả, giọng điệu

## Ví dụ Mẫu

### Input
> "Viết email gửi khách hàng Công ty ABC cảm ơn đã mua 100 sản phẩm X, đề xuất ưu đãi 10% cho đơn tiếp theo trong tháng."

### Output
**Tiêu đề:** [Ưu đãi đặc biệt] Cảm ơn Công ty ABC - Giảm 10% đơn hàng tiếp theo

Kính gửi anh/chị,

Team [Tên công ty] xin chân thành cảm ơn Công ty ABC đã tin tưởng đặt mua 100 sản phẩm X trong tuần qua.

Để tri ân sự hợp tác, chúng tôi xin gửi tặng mã giảm giá **10% cho đơn hàng tiếp theo**, áp dụng đến hết tháng này. Anh/chị chỉ cần sử dụng mã **VIP10ABC** khi đặt hàng.

**Bước tiếp theo:** Vui lòng xác nhận nhu cầu đơn hàng tiếp theo qua email này trước ngày [deadline] để chúng tôi chuẩn bị hàng sớm nhất.

Trân trọng,
[Chữ ký]
```

---

## Ghi chú

- Ví dụ này minh họa Chế độ 2 (Đóng gói từ Mô tả)
- Người dùng mô tả quy tắc → Skill trích xuất thành Bộ Nguyên tắc Cốt lõi
- Ví dụ mẫu (few-shot) giúp Agent hiểu rõ tiêu chuẩn đầu ra mong đợi
