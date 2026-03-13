---
description: Code - Implement theo kế hoạch, làm việc theo batches
---

# /code - Coding

## Khi nào sử dụng
- Sau khi planning hoàn thành
- Có task_plan.md rõ ràng
- Sẵn sàng implement

## Quy trình
1. Load và review task_plan.md
2. Execute batch (3 tasks đầu)
3. Mark tasks as in_progress → complete
4. Report progress
5. Wait for feedback
6. Continue với batch tiếp theo

## Cú pháp
```
/code [phase hoặc task cụ thể]
```

## Ví dụ
```
/code implement Phase 1 theo task_plan.md

/code continue với batch tiếp theo

/code task 5: setup routing
```

## Output
- Working code
- Updated progress.md
- Verification results sau mỗi batch

## Batch Report Format
```markdown
## Batch Complete

### Implemented
- [x] Task 1: [Description]
- [x] Task 2: [Description]
- [x] Task 3: [Description]

### Verification
[Results]

Ready for feedback.
```

## Tips
- Follow plan exactly
- Don't skip verifications
- Stop when blocked, ask for help
- Commit sau mỗi task
