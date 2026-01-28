---
description: Test - TDD workflow, viết test trước code
---

# /test - Testing

## Khi nào sử dụng
- Viết test cho feature mới (TDD)
- Run tests và check results
- Fix failing tests

## Quy trình TDD
1. 🔴 RED: Viết failing test
2. Verify test fails correctly
3. 🟢 GREEN: Viết minimal code
4. Verify test passes
5. 🔵 REFACTOR: Clean up
6. Repeat

## Cú pháp
```
/test [action và context]
```

## Ví dụ
```
/test viết tests cho function calculateTotal

/test run all tests

/test fix failing tests

/test TDD cho feature login
```

## Test Fixing Flow
1. Run tests → identify failures
2. Group errors by type
3. Prioritize (infrastructure first)
4. Fix systematically
5. Verify từng group
6. Run full suite

## Output
- Test files
- Test results
- Fix reports

## Tips
- Write test FIRST, then code
- Watch test fail before implementing
- One behavior per test
- AAA pattern: Arrange, Act, Assert
