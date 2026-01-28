---
name: testing
description: >
  Test-Driven Development: Write test first, watch fail, write code.
  Red-Green-Refactor cycle.
  Sử dụng khi implement features hoặc fix bugs.
---

# Testing - Test-Driven Development

## The Iron Law

```
KHÔNG VIẾT PRODUCTION CODE NẾU CHƯA CÓ FAILING TEST
```

Viết code trước test? Delete. Start over.

---

## Red-Green-Refactor Cycle

```
🔴 RED → Write failing test
    ↓
🟢 GREEN → Write minimal code to pass
    ↓
🔵 REFACTOR → Improve code quality
    ↓
   Repeat...
```

---

## 3 Laws of TDD

1. Write production code only to make a failing test pass
2. Write only enough test to demonstrate failure
3. Write only enough code to make the test pass

---

## RED Phase - Write Failing Test

**Good Test:**
```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };

  const result = await retryOperation(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```

**Requirements:**
- One behavior
- Clear name
- Real code (no mocks unless unavoidable)

### Verify RED

```bash
npm test path/to/test.test.ts
```

Confirm:
- ✅ Test fails (not errors)
- ✅ Failure message expected
- ✅ Fails because feature missing

**Test passes?** Testing existing behavior. Fix test.

---

## GREEN Phase - Minimal Code

Write simplest code to pass.

**Good:**
```typescript
async function retryOperation<T>(fn: () => Promise<T>): Promise<T> {
  for (let i = 0; i < 3; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === 2) throw e;
    }
  }
  throw new Error('unreachable');
}
```

**BAD:** Over-engineered với options không cần.

### Verify GREEN

```bash
npm test path/to/test.test.ts
```

Confirm:
- ✅ Test passes
- ✅ Other tests still pass
- ✅ Output pristine

---

## REFACTOR Phase

**After green only:**
- Remove duplication
- Improve names
- Extract helpers

Keep tests green. Don't add behavior.

---

## AAA Pattern

| Step | Purpose |
|------|---------|
| **Arrange** | Set up test data |
| **Act** | Execute code under test |
| **Assert** | Verify expected outcome |

---

## Test Fixing Workflow

Khi có nhiều failing tests:

### 1. Run Tests
```bash
npm test
```
Analyze: total failures, error types, affected files

### 2. Group Errors
- By error type: ImportError, AttributeError, AssertionError
- By module/file
- By root cause

### 3. Prioritize
- Highest impact first
- Infrastructure before functionality

### 4. Fix Systematically
For each group:
1. Identify root cause
2. Implement fix
3. Verify subset passes
4. Move to next group

### 5. Final Verification
```bash
npm test  # All pass ✓
```

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "TDD slows me down" | TDD faster than debugging. |

---

## Red Flags - Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- "Just this once"
- "Keep as reference"

**→ Delete code. Start with TDD.**

---

## Verification Checklist

Before marking complete:

- [ ] Every new function has a test
- [ ] Watched each test fail first
- [ ] Each test failed for expected reason
- [ ] Wrote minimal code to pass
- [ ] All tests pass
- [ ] Output pristine
- [ ] Edge cases covered
