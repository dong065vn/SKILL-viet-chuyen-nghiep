---
name: coding
description: >
  Thực thi coding theo kế hoạch đã lập.
  Làm việc theo batches, báo cáo tiến độ sau mỗi batch.
  Sử dụng sau khi planning hoàn thành.
---

# Coding - Thực thi Theo Kế hoạch

## Mục đích
Load plan, execute tasks theo batches, báo cáo progress cho review.

**Core principle:** Batch execution với checkpoints.

---

## Quy trình 5 bước

### Step 1: Load and Review Plan
1. Đọc `task_plan.md`
2. Review critically - xác định questions/concerns
3. Nếu có concerns: Raise với user trước khi bắt đầu
4. Nếu OK: Proceed

### Step 2: Execute Batch
**Default: 3 tasks đầu tiên**

Cho mỗi task:
1. Mark as `in_progress`
2. Follow each step exactly
3. Run verifications as specified
4. Mark as `completed`

### Step 3: Report
Khi batch hoàn thành:
```markdown
## Batch Complete

### Implemented
- [x] Task 1: [What was done]
- [x] Task 2: [What was done]
- [x] Task 3: [What was done]

### Verification Output
[Paste kết quả verify]

### Ready for feedback.
```

### Step 4: Continue
Dựa trên feedback:
- Apply changes nếu cần
- Execute next batch
- Repeat until complete

### Step 5: Complete
Sau khi tất cả tasks hoàn thành:
- Run final verification
- Update task_plan.md status
- Report completion

---

## Khi nào STOP và Hỏi

**STOP ngay khi:**
- Hit blocker giữa batch (missing dependency, test fails)
- Plan có gaps critical
- Không hiểu instruction
- Verification fails repeatedly

**Hỏi clarification thay vì đoán.**

---

## Best Practices

### Trong Batch
- Follow plan steps exactly
- Không skip verifications
- Commit sau mỗi task hoàn thành (nếu dùng git)
- Update progress.md

### Giữa Batches
- Just report và wait
- Không tự động tiếp tục
- Wait for user feedback

### Khi Blocked
- Stop và ask
- Don't guess
- Document blocker

---

## Code Quality Checklist

Trước khi mark task complete:

- [ ] Code runs without errors
- [ ] Follows project conventions
- [ ] Has meaningful variable/function names
- [ ] No hardcoded values (use constants/config)
- [ ] Error handling appropriate
- [ ] Comments for non-obvious logic only

---

## Remember

1. ✅ Review plan critically first
2. ✅ Follow plan steps exactly
3. ✅ Don't skip verifications
4. ✅ Between batches: report and wait
5. ✅ Stop when blocked, don't guess
