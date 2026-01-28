---
description: Verify - Xác minh hoàn thành trước khi commit/deploy
---

# /verify - Verification

## Khi nào sử dụng
- Trước khi claim "done"
- Trước khi commit/push/PR
- Trước khi deploy
- Sau khi fix bug

## The Iron Law
```
KHÔNG CLAIM HOÀN THÀNH NẾU CHƯA CÓ EVIDENCE MỚI
```

## Quy trình
1. IDENTIFY: Command nào prove claim?
2. RUN: Execute full command
3. READ: Full output, check exit code
4. VERIFY: Output confirms claim?
5. REPORT: With evidence

## Cú pháp
```
/verify [scope để verify]
```

## Ví dụ
```
/verify kiểm tra trước deploy

/verify all tests pass

/verify requirements met từ PRD

/verify bug đã được fix
```

## Verification Checklist
- [ ] All tests pass (fresh run)
- [ ] No linter errors
- [ ] Build succeeds
- [ ] Requirements met (checklist)
- [ ] Edge cases handled
- [ ] Documentation updated

## Output Format
```markdown
## Verification Results

### Tests
✅ npm test → 47/47 passed

### Build
✅ npm run build → exit 0

### Requirements
- [x] Feature 1: Verified by [how]
- [x] Feature 2: Verified by [how]

## Conclusion
All verifications passed.
```

## Tips
- Run command, read output, THEN claim
- No "should", "probably", "seems to"
- Evidence before claims
- No shortcuts
