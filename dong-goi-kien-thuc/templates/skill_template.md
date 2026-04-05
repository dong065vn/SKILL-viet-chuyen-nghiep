# Template Skill Chuẩn Antigravity

> Người dùng có thể cung cấp file này hoặc file tương tự để skill đóng gói theo cấu trúc riêng.
> Nếu không cung cấp template, skill sẽ sử dụng cấu trúc mặc định bên dưới.

---

```markdown
---
name: {{TEN_SKILL}}
description: {{MO_TA_NGAN}}
---

# {{TEN_SKILL_DAY_DU}}

## Mục đích
{{MO_TA_MUC_DICH}}

## Phạm vi Ứng dụng
- {{TINH_HUONG_1}}
- {{TINH_HUONG_2}}
- {{TINH_HUONG_3}}

## Bộ Nguyên tắc Cốt lõi
1. **{{NGUYEN_TAC_1}}:** {{CHI_TIET_1}}
2. **{{NGUYEN_TAC_2}}:** {{CHI_TIET_2}}
3. **{{NGUYEN_TAC_3}}:** {{CHI_TIET_3}}

## Quy trình Thực hiện
1. **{{BUOC_1}}:** {{CHI_TIET_BUOC_1}}
2. **{{BUOC_2}}:** {{CHI_TIET_BUOC_2}}
3. **{{BUOC_3}}:** {{CHI_TIET_BUOC_3}}

## Ví dụ Mẫu (Few-shot)

### Input mẫu
{{VI_DU_INPUT}}

### Output mẫu
{{VI_DU_OUTPUT}}

## Điều kiện & Ngoại lệ
- {{NGOAI_LE_1}}
- {{NGOAI_LE_2}}
```

---

## Hướng dẫn sử dụng Template

| Placeholder | Ý nghĩa | Ví dụ |
|-------------|---------|-------|
| `{{TEN_SKILL}}` | Tên kebab-case | `phan-tich-hop-dong` |
| `{{MO_TA_NGAN}}` | Mô tả 1-2 câu, ngôi thứ ba | "Chuyên gia phân tích hợp đồng..." |
| `{{TEN_SKILL_DAY_DU}}` | Tên đầy đủ tiếng Việt | "Kỹ năng Phân tích Hợp đồng" |
| `{{MO_TA_MUC_DICH}}` | Mục tiêu chính của Skill | "Hỗ trợ rà soát và phân tích..." |
| `{{TINH_HUONG_N}}` | Khi nào dùng Skill | "Khi nhận hợp đồng mới cần rà soát" |
| `{{NGUYEN_TAC_N}}` | Quy tắc cốt lõi | "Luôn kiểm tra điều khoản phạt" |
| `{{BUOC_N}}` | Các bước thực hiện | "Đọc tổng quan hợp đồng" |
| `{{VI_DU_INPUT}}` | Ví dụ đầu vào | "File hợp đồng 10 trang..." |
| `{{VI_DU_OUTPUT}}` | Ví dụ đầu ra kỳ vọng | "Bảng 5 rủi ro pháp lý..." |
| `{{NGOAI_LE_N}}` | Giới hạn/ngoại lệ | "Không áp dụng cho hợp đồng quốc tế" |

## Lưu ý

- Người dùng KHÔNG BẮT BUỘC phải dùng template này
- Có thể cung cấp template riêng với cấu trúc khác hoàn toàn
- Skill đóng gói sẽ linh hoạt theo cấu trúc được cung cấp
- Phần `Ví dụ Mẫu` rất quan trọng — giúp Agent học tốt nhất
