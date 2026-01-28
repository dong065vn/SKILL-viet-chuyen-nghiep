---
description: Debug - Fix lỗi có hệ thống, tìm root cause trước
---

# /debug - Debugging

## Khi nào sử dụng
- Gặp bug hoặc unexpected behavior
- Test failures
- Performance problems
- Build/integration issues

## Quy trình 4 Phases
### Phase 1: Root Cause Investigation
- Đọc error messages kỹ
- Reproduce consistently
- Check recent changes
- Trace data flow

### Phase 2: Pattern Analysis
- Find working examples
- Compare differences
- Understand dependencies

### Phase 3: Hypothesis Testing
- Form single hypothesis
- Test minimally (1 change)
- Verify or form new hypothesis

### Phase 4: Implementation
- Create failing test
- Implement fix
- Verify fix works

## Cú pháp
```
/debug [mô tả bug]
```

## Ví dụ
```
/debug login không hoạt động sau khi deploy

/debug test user.spec.js failing

/debug app crash khi load data lớn
```

## 3-Strike Rule
- Attempt 1: Diagnose & Fix
- Attempt 2: Alternative approach
- Attempt 3: Broader rethink
- After 3 fails: Escalate

## Tips
- NEVER fix mà không tìm root cause
- One change at a time
- Log mọi error và attempt
- 3 lần fail → hỏi user
