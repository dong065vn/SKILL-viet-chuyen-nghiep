---
name: planning
description: >
  Lập kế hoạch chi tiết: chia phases, break down tasks.
  Tạo task_plan.md và progress.md để track tiến độ.
  Sử dụng sau khi PRD được approve.
---

# Planning - Lập Kế hoạch Dự án

## Mục đích
Biến PRD thành **kế hoạch hành động cụ thể** với phases, tasks và verification criteria.

---

## Core Pattern

```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Mọi thứ quan trọng phải ghi ra file.
```

---

## Files cần tạo

| File | Mục đích | Khi cập nhật |
|------|----------|--------------|
| `task_plan.md` | Phases, progress, decisions | Sau mỗi phase |
| `progress.md` | Session log, test results | Trong session |
| `findings.md` | Research, discoveries | Sau mỗi discovery |

---

## Nguyên tắc lập kế hoạch

### 1. Keep It SHORT
| ❌ Sai | ✅ Đúng |
|--------|---------|
| 50 tasks với sub-sub-tasks | 5-10 tasks rõ ràng max |
| List mọi micro-step | Chỉ actionable items |
| Mô tả dài dòng | Một dòng mỗi task |

> **Rule:** Plan dài hơn 1 trang = quá dài. Simplify.

### 2. Be SPECIFIC
| ❌ Sai | ✅ Đúng |
|--------|---------|
| "Set up project" | "Run `npx create-next-app`" |
| "Add authentication" | "Install next-auth, create `/api/auth`" |
| "Style the UI" | "Add Tailwind classes to `Header.tsx`" |

### 3. Tasks có Verification
Mỗi task phải có cách verify:
```markdown
- [ ] Task: [Action cụ thể] → Verify: [Cách kiểm tra]
```

---

## Template: task_plan.md

```markdown
# [Tên Dự án] - Implementation Plan

## Goal
[Một câu: Xây dựng/fix gì?]

## Phases

### Phase 1: [Tên Phase]
**Status:** Not Started | In Progress | Complete
**Duration:** [X days/hours]

#### Tasks
- [ ] Task 1: [Action] → Verify: [Check]
- [ ] Task 2: [Action] → Verify: [Check]
- [ ] Task 3: [Action] → Verify: [Check]

### Phase 2: [Tên Phase]
...

## Dependencies
- Phase 2 depends on Phase 1 completion
- [Other dependencies]

## Done When
- [ ] [Main success criteria 1]
- [ ] [Main success criteria 2]

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| [Error] | [#] | [Fix] |
```

---

## Template: progress.md

```markdown
# Progress Log

## Session: [Date]

### Completed
- [x] [What was done]

### In Progress
- [/] [What's ongoing]

### Blocked
- [ ] [What's blocked and why]

### Notes
- [Important observations]
```

---

## Critical Rules

### 1. Create Plan First
Không bắt đầu task phức tạp nếu chưa có `task_plan.md`. Non-negotiable.

### 2. 2-Action Rule
> "Sau mỗi 2 view/browser/search, IMMEDIATELY save findings ra file."

### 3. Read Before Decide
Trước quyết định lớn, đọc lại plan file để keep goals in attention.

### 4. Update After Act
Sau mỗi phase:
- Mark status: `in_progress` → `complete`
- Log errors
- Note files created/modified

### 5. Never Repeat Failures
```
if action_failed:
    next_action != same_action
```

---

## 3-Strike Error Protocol

```
ATTEMPT 1: Diagnose & Fix
  → Đọc error kỹ
  → Xác định root cause
  → Apply targeted fix

ATTEMPT 2: Alternative Approach
  → Same error? Try different method
  → NEVER repeat exact failing action

ATTEMPT 3: Broader Rethink
  → Question assumptions
  → Search for solutions
  → Consider updating plan

AFTER 3 FAILURES: Escalate to User
  → Explain what you tried
  → Share specific error
  → Ask for guidance
```

---

## Quick Reference

| Question | Answer Source |
|----------|---------------|
| Where am I? | Current phase in task_plan.md |
| Where am I going? | Remaining phases |
| What's the goal? | Goal statement in plan |
| What have I learned? | findings.md |
| What have I done? | progress.md |
