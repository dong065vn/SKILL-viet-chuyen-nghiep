---
name: debugging
description: >
  Fix lỗi có hệ thống - tìm root cause trước khi fix.
  4 phases: Root Cause → Pattern → Hypothesis → Implementation.
  Sử dụng khi gặp bug, test failure, hoặc unexpected behavior.
---

# Debugging - Fix Lỗi Có Hệ Thống

## The Iron Law

```
KHÔNG FIX NẾU CHƯA TÌM ROOT CAUSE
```

Random fixes waste time và tạo bugs mới. Symptom fixes = failure.

---

## Khi nào sử dụng

Sử dụng cho MỌI technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**ĐẶC BIỆT khi:**
- Under time pressure (đừng đoán)
- "Just one quick fix" có vẻ obvious
- Đã thử nhiều fixes rồi
- Previous fix không work
- Không fully understand issue

---

## 4 Phases

### Phase 1: Root Cause Investigation

**TRƯỚC KHI attempt ANY fix:**

1. **Đọc Error Messages Kỹ**
   - Đừng skip errors/warnings
   - Đọc stack traces completely
   - Note line numbers, file paths, error codes

2. **Reproduce Consistently**
   - Trigger được reliably không?
   - Exact steps là gì?
   - Happens every time không?

3. **Check Recent Changes**
   - What changed?
   - Git diff, recent commits
   - New dependencies, config changes

4. **Trace Data Flow**
   - Where does bad value originate?
   - What called this with bad value?
   - Trace up until source

### Phase 2: Pattern Analysis

1. **Find Working Examples**
   - Similar working code trong same codebase?
   
2. **Compare Against References**
   - Read reference implementation COMPLETELY
   - Đừng skim

3. **Identify Differences**
   - What's different between working và broken?
   - List EVERY difference

### Phase 3: Hypothesis and Testing

1. **Form Single Hypothesis**
   - State clearly: "I think X is root cause because Y"
   - Write it down

2. **Test Minimally**
   - SMALLEST possible change
   - One variable at a time

3. **Verify**
   - Worked? → Phase 4
   - Didn't work? → NEW hypothesis (không add more fixes)

### Phase 4: Implementation

1. **Create Failing Test Case**
   - Simplest reproduction
   - MUST have before fixing

2. **Implement Single Fix**
   - Address root cause
   - ONE change at a time
   - No "while I'm here" improvements

3. **Verify Fix**
   - Test passes?
   - No other tests broken?
   - Issue actually resolved?

4. **If Fix Doesn't Work**
   - STOP
   - Count: How many fixes tried?
   - If < 3: Return to Phase 1
   - **If ≥ 3: Question architecture**

---

## 3-Strike Error Protocol

```
ATTEMPT 1: Diagnose & Fix
  → Root cause analysis
  → Targeted fix

ATTEMPT 2: Alternative Approach
  → Different method
  → NEVER repeat failing action

ATTEMPT 3: Broader Rethink
  → Question assumptions
  → Consider updating approach

AFTER 3 FAILURES: Escalate
  → Discuss với user
  → Maybe architectural problem
```

---

## Red Flags - STOP

Nếu bạn đang nghĩ:
- "Quick fix for now, investigate later"
- "Just try changing X"
- "Add multiple changes, run tests"
- "I don't fully understand but this might work"
- "One more fix attempt" (khi đã thử 2+)

**→ STOP. Return to Phase 1.**

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple" | Simple issues có root causes too |
| "Emergency, no time" | Systematic FASTER than thrashing |
| "Just try this first" | First fix sets pattern. Do it right |
| "I'm confident" | Confidence ≠ evidence |

---

## Quick Reference

| Phase | Activities | Success Criteria |
|-------|------------|------------------|
| 1. Root Cause | Read errors, reproduce, trace | Understand WHAT and WHY |
| 2. Pattern | Find examples, compare | Identify differences |
| 3. Hypothesis | Form theory, test minimal | Confirmed or new hypothesis |
| 4. Implementation | Create test, fix, verify | Bug resolved, tests pass |
