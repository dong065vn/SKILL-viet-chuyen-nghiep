---
name: verify
description: >
  Xác minh trước khi claim hoàn thành. Evidence before claims.
  Chạy verification command, đọc output, rồi mới claim.
  Sử dụng trước khi commit, PR, hoặc claim done.
---

# Verify - Xác minh Trước Khi Hoàn thành

## The Iron Law

```
KHÔNG CLAIM HOÀN THÀNH NẾU CHƯA CÓ EVIDENCE MỚI
```

Claiming complete mà không verify = dishonesty, không efficiency.

---

## The Gate Function

```
TRƯỚC KHI claim any status:

1. IDENTIFY: Command nào prove claim này?
2. RUN: Execute FULL command (fresh, complete)
3. READ: Full output, check exit code
4. VERIFY: Output confirms claim?
   - Nếu NO: State actual status with evidence
   - Nếu YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, không verifying
```

---

## Common Claims và Requirements

| Claim | Requires | NOT Sufficient |
|-------|----------|----------------|
| Tests pass | Test output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check |
| Build succeeds | Build: exit 0 | Linter passing |
| Bug fixed | Test symptom: passes | Code changed |
| Requirements met | Line-by-line checklist | Tests passing |

---

## Red Flags - STOP

- Using "should", "probably", "seems to"
- Expressing satisfaction before verification
- About to commit/push/PR without verification
- Relying on partial verification
- "Just this once"
- **ANY wording implying success without running verification**

---

## Key Patterns

### Tests
```
✅ [Run test] [See: 34/34 pass] "All tests pass"
❌ "Should pass now"
```

### Regression Tests (TDD Red-Green)
```
✅ Write → Run (pass) → Revert fix → Run (MUST FAIL) → Restore → Run (pass)
❌ "I've written a regression test" (without red-green verification)
```

### Build
```
✅ [Run build] [See: exit 0] "Build passes"
❌ "Linter passed" (linter ≠ build)
```

### Requirements
```
✅ Re-read PRD → Create checklist → Verify each → Report
❌ "Tests pass, done"
```

---

## Final Verification Checklist

Before claiming work complete:

### Code Quality
- [ ] All tests pass (fresh run)
- [ ] No linter errors
- [ ] Build succeeds
- [ ] No console errors/warnings

### Functionality
- [ ] All requirements met (checklist từ PRD)
- [ ] Edge cases handled
- [ ] Error states handled

### Documentation
- [ ] Code comments for non-obvious logic
- [ ] README updated if needed
- [ ] CHANGELOG updated if applicable

---

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Linter passed" | Linter ≠ compiler |
| "I'm tired" | Exhaustion ≠ excuse |
| "Partial check enough" | Partial proves nothing |

---

## Evidence Format

Khi report completion:

```markdown
## Verification Results

### Tests
✅ npm test → 47/47 passed (0 failures)

### Build
✅ npm run build → exit 0

### Linter
✅ npm run lint → 0 errors, 0 warnings

### Requirements Checklist
- [x] Feature 1: Verified by [how]
- [x] Feature 2: Verified by [how]
- [x] Feature 3: Verified by [how]

## Conclusion
All verifications passed. Ready for review.
```

---

## The Bottom Line

**No shortcuts for verification.**

Run the command. Read the output. THEN claim the result.

This is non-negotiable.
