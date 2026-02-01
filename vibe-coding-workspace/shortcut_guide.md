# Vibe Coding Workspace - Shortcut Guide

## Quy trình phát triển

```
/brainstorm → /prd → /plan → /code → /test → /debug → /verify → /compact
```

---

## Danh sách Shortcuts

| Shortcut | Mục đích | Khi nào dùng |
|----------|----------|--------------|
| `/brainstorm` | Thu thập yêu cầu | Bắt đầu dự án/feature mới |
| `/prd` | Viết PRD | Sau brainstorm |
| `/plan` | Lập kế hoạch | Sau PRD approve |
| `/code` | Coding | Có task_plan.md |
| `/test` | Testing/TDD | Viết tests, fix failures |
| `/debug` | Fix lỗi | Gặp bug/error |
| `/verify` | Xác minh hoàn thành | Trước commit/deploy |
| `/compact` | Reset context | Cần chuyển phiên mới |

---

## Chi tiết từng Shortcut

### /brainstorm
```
/brainstorm Tôi muốn làm app quản lý task cho team
```
**Output:** Understanding Summary, Assumptions, Design options

---

### /prd
```
/prd viết PRD từ kết quả brainstorm
```
**Output:** Full PRD document với Problem, Solution, User Stories, Metrics

---

### /plan
```
/plan lập kế hoạch từ PRD
```
**Output:** task_plan.md với Phases, Tasks, Verifications

---

### /code
```
/code implement Phase 1
/code continue với batch tiếp theo
```
**Output:** Code + Updated progress.md

---

### /test
```
/test viết tests cho feature login
/test run tests và fix failures
/test TDD cho function calculateTotal
```
**Output:** Test files + Test results

---

### /debug
```
/debug login không hoạt động
/debug app crash khi load data lớn
```
**Output:** Root cause analysis + Fix

---

### /verify
```
/verify kiểm tra trước deploy
/verify all tests pass
```
**Output:** Verification report với evidence

---

## Agents

| Agent | Role | Skill chính |
|-------|------|-------------|
| `@Brainstormer` | Thu thập yêu cầu | brainstorm |
| `@Product_Manager` | Viết PRD | prd_writer |
| `@Planner` | Lập kế hoạch | planning |
| `@Developer` | Coding | coding, testing |
| `@QA_Engineer` | Test & Debug | testing, debugging, verify |

### Ví dụ Multi-Agent
```
@Brainstormer thu thập requirements,
rồi chuyển cho @Product_Manager viết PRD
```

---

## Tips

1. **Luôn bắt đầu với /brainstorm** - Không skip bước này
2. **Confirm understanding** - Trả lời từng câu hỏi chi tiết  
3. **Theo quy trình** - brainstorm → prd → plan → code → test → verify
4. **Stop khi blocked** - Hỏi thay vì đoán
5. **Evidence before claims** - Luôn verify trước khi claim done
