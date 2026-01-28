---
description: Plan - Lập kế hoạch chi tiết với phases và tasks
---

# /plan - Lập Kế hoạch

## Khi nào sử dụng
- Sau khi PRD được approve
- Trước khi bắt đầu coding
- Khi cần chia nhỏ công việc

## Quy trình
1. Đọc PRD
2. Chia thành phases
3. Break down tasks trong mỗi phase (max 10)
4. Xác định dependencies
5. Tạo verification criteria
6. Output task_plan.md

## Cú pháp
```
/plan [nguồn PRD hoặc context]
```

## Ví dụ
```
/plan lập kế hoạch từ PRD app todo

/plan chia phases cho feature payment

/plan update plan sau iteration 1
```

## Output
- `task_plan.md`:
  - Goal
  - Phases với status
  - Tasks với verification
  - Dependencies
  - Done When criteria
- `progress.md`:
  - Session logs
- `findings.md`:
  - Research notes

## Tips
- Max 5-10 tasks mỗi phase
- Mỗi task có action cụ thể
- Mỗi task có cách verify
- Keep plan ngắn gọn (1 trang max)
