---
name: debugger
description: Systematic 4-phase debugging protocol. Use when you encounter errors, unexpected behavior, or when the user asks to "debug", "find root cause", or "troubleshoot". Implements the diagnose-analyze-resolve-verify workflow.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🐛 Starting systematic debugging..."
  after:
    - echo "✅ Debugging complete. Root cause identified and fix provided."
---

# /debug - Systematic 4-Phase Debugging Protocol

## What This Skill Does
Implements a structured 4-phase debugging methodology: DARV (Diagnose → Analyze → Resolve → Verify). Systematically identifies root causes, provides actionable solutions, and ensures fixes are properly verified.

## When to Use This Skill
- Encountering runtime errors or exceptions
- Unexpected application behavior
- Performance issues or bottlenecks
- System failures or crashes
- When user says "debug", "troubleshoot", "find root cause"
- Need structured approach to problem-solving

## The DARV Protocol

### Phase 1: Diagnose
**Objective**: Understand the problem's symptoms and scope

1. **Symptom Collection**
   - Error messages and stack traces
   - Unexpected behaviors observed
   - System state information
   - Context of the issue

2. **Impact Assessment**
   - Who is affected?
   - How severe is the impact?
   - When does it occur?
   - Frequency of occurrence

3. **Reproduction Steps**
   - Steps to reproduce the issue
   - Prerequisites required
   - Expected vs actual outcomes
   - Screenshots or logs if available

4. **Initial Hypothesis**
   - Formulate initial theories
   - List potential causes
   - Prioritize likely causes
   - Document assumptions

### Phase 2: Analyze
**Objective**: Investigate and identify the true root cause

1. **Data Collection**
   - Examine logs and error reports
   - Review recent code changes
   - Check system metrics and performance
   - Gather diagnostic information

2. **Hypothesis Testing**
   - Test each potential cause systematically
   - Eliminate impossible causes
   - Validate or refute hypotheses
   - Narrow down possibilities

3. **Root Cause Identification**
   - Identify the fundamental cause
   - Distinguish symptoms from causes
   - Verify the root cause with evidence
   - Document the causal chain

4. **Evidence Documentation**
   - Capture proof of root cause
   - Note specific code or configuration issues
   - Record environment conditions
   - Document investigation findings

### Phase 3: Resolve
**Objective**: Design and implement a solution

1. **Solution Design**
   - Propose fixes addressing root cause
   - Consider multiple solutions
   - Evaluate trade-offs
   - Select optimal solution

2. **Implementation Plan**
   - Break fix into implementable steps
   - Identify code changes needed
   - Consider side effects and impacts
   - Plan for verification

3. **Solution Documentation**
   - Document what will be changed
   - Explain why this solution works
   - Note any assumptions or risks
   - Provide implementation details

4. **Validation Strategy**
   - How to confirm the fix works
   - What tests to run
   - What to monitor after fix
   - Rollback plan if needed

### Phase 4: Verify
**Objective**: Confirm the fix resolves the issue

1. **Fix Implementation**
   - Apply the proposed solution
   - Make minimal necessary changes
   - Document changes made
   - Update relevant documentation

2. **Verification Testing**
   - Test the fix in controlled environment
   - Verify problem is resolved
   - Check for unintended side effects
   - Run regression tests

3. **Edge Case Testing**
   - Test related functionality
   - Verify no new issues introduced
   - Test performance implications
   - Test under various conditions

4. **Final Confirmation**
   - Confirm issue is fully resolved
   - Verify in production if applicable
   - Document final status
   - Provide closure summary

## Có phối hợp

### Inputs
- Error messages and stack traces
- System logs and diagnostic data
- Code under investigation
- Environment information
- User descriptions of issues

### Outputs
```markdown
## Debugging Report

### Diagnosis Summary
**Issue Description**: [What's happening]
**Impact**: [Who/what's affected]
**Symptom**: [Observed behaviors]
**Initial Hypotheses**: [Potential causes considered]

### Root Cause Analysis
**Investigation Steps**:
1. [Step 1]: [Finding]
2. [Step 2]: [Finding]
3. [Step 3]: [Finding]

**Root Cause Identified**: [Fundamental issue]
**Evidence**: [Proof locating the cause]

### Solution Proposed
**Fix Description**: [What to change]
**Implementation Steps**:
1. [Step 1]: [Action]
2. [Step 2]: [Action]
3. [Step 3]: [Action]

**Expected Outcome**: [What should happen after fix]
**Side Effects**: [Potential impacts to consider]

### Verification Plan
**Test Steps**:
1. [Test 1]: [Procedure] - [Expected result]
2. [Test 2]: [Procedure] - [Expected result]

**Rollback Plan**: [How to revert if needed]

### Status
- [ ] Fix implemented
- [ ] Tests executed
- [ ] Issue resolved verified
- [ ] No regressions detected

Ready for /fix verification.
```

## Key Principles

### 1. Systematic Approach
- Follow the DARV protocol strictly
- Don't skip phases
- Document everything

### 2. Evidence-Based
- Base conclusions on data
- Log all observations
- Avoid assumptions without verification

### 3. Focus on Root Cause
- Distinguish symptoms from causes
- Identify fundamental issues
- Don't just patch symptoms

### 4. Minimal Fixes
- Change only what's necessary
- Avoid over-engineering solutions
- Keep changes reversible

## Success Metrics
- **Root Cause Accuracy**: Correctly identifying fundamental cause
- **Fix Effectiveness**: Issue permanently resolved
- **Investigation Time**: Reasonable time spent on diagnosis
- **Documentation Quality**: Clear, comprehensive findings
- **No Regressions**: Fix doesn't introduce new issues

## Common Pitfalls to Avoid
- **Shooting in Dark**: Guessing without data
- **Treating Symptoms**: Fixing appearances, not root causes
- **Over-Fixing**: Changing more than necessary
- **Assumption-Based**: Making changes based on guesses
- **Skipping Verification**: Not confirming fixes work

## Tips for Effective Debugging

### 1. Start Broad, Then Narrow
- Begin with general investigation
- Systematically eliminate possibilities
- Focus on most likely causes first
- Use binary search approach when possible

### 2. Use the Right Tools
- Debuggers for step-through analysis
- Logs for historical context
- Profilers for performance issues
- Network tools for connectivity issues

### 3. Isolate the Problem
- Reproduce in controlled environment
- Minimize variables
- Test one hypothesis at a time
- Use feature flags to isolate components

### 4. Document Everything
- Record what you tried
- What worked and what didn't
- What you learned
- Final conclusions

## Debugging Techniques

### 1. Rubber Duck Debugging
Explain the problem to someone (or something) else to find your own blind spots

### 2. Binary Search Debugging
Divide the codebase or data set to isolate where problems occur

### 3. Divide and Conquer
Split the system into components and test each independently

### 4. Trace Analysis
Follow execution flow through logs or debuggers to find where things go wrong

### 5. Known Good State
Compare working system with broken system to find differences

## Common Debugging Scenarios

### Scenario 1: Application Crash
```
Symptom: Application crashes with "Unhandled exception"
1. Diagnostic: Examine stack trace and error message
2. Investigation: Check recent code changes, null references
3. Root Cause: Typically null pointer or invalid memory access
4. Solution: Add null checks, validate inputs, fix memory leak
5. Verification: Run crash scenarios safely
```

### Scenario 2: Performance Degradation
```
Symptom: Application slower than expected
1. Diagnostic: Profile CPU, memory, I/O usage
2. Investigation: Identify bottleneck resources or operations
3. Root Cause: N+1 query, memory leak, blocking operation
4. Solution: Optimize algorithm, add caching, fix leak
5. Verification: Benchmark before and after
```

### Scenario 3: Incorrect Behavior
```
Symptom: Wrong results or unexpected output
1. Diagnostic: Identify incorrect assumptions or logic
2. Investigation: Add logging, inspect intermediate values
3. Root Cause: Algorithm error, incorrect condition, wrong data
4. Solution: Fix algorithm, correct condition, validate data
5. Verification: Add tests covering the scenario
```

## Output Quality Checklist
- [ ] Problem symptoms clearly documented
- [ ] Impact assessment completed
- [ ] Reproduction steps provided
- [ ] Multiple hypotheses considered
- [ ] Systematic investigation performed
- [ ] Root cause identified with evidence
- [ ] Solution proposed addresses root cause
- [ ] Verification plan defined
- [ ] Rollback plan available
- [ ] All steps documented

## Integration with Other Skills
- **Tester**: Uses debug findings to write better tests
- **Fixer**: Takes debug analysis for fix verification
- **Verifier**: Uses debug insights for comprehensive verification
- **Coder**: Implements fixes based on debug findings
- **Planner**: Updates plans based on discovered issues

## Advanced Debugging Strategies

### 1. Pattern Recognition
- Look for patterns in failures
- Compare with similar past issues
- Identify systemic problems

### 2. Timeline Analysis
- When did the problem start?
- What changed around that time?
- Is it related to recent deployments?

### 3. Environment Differences
- Does it happen in all environments?
- Are there configuration differences?
- Does it affect all users or only some?

### 4. Data Investigation
- Are there common data patterns in failures?
- Does specific data trigger issues?
- Are there data validation gaps?

## Post-Debugging Activities

### 1. Prevent Recurrence
- Add tests for the discovered issue
- Improve error handling
- Add monitoring and alerting
- Update documentation

### 2. Knowledge Sharing
- Document the issue and solution
- Share with team
- Update runbooks or troubleshooting guides
- Train others on similar issues

### 3. Process Improvement
- Identify why issue occurred
- What could have prevented it?
- Can we catch similar issues earlier?
- Should we add more tests or monitoring?

## Error Handling and Escalation

### When to Escalate
- Issue outside your expertise
- Requires infrastructure changes
- Needs cross-team coordination
- Legal or compliance implications
- Critical production issues

### Escalation Process
1. Document all investigation steps
2. Provide clear problem statement
3. Share evidence and analysis
4. State specific help needed
5. Keep stakeholders informed

## Best Practices
- Always start with diagnosis, not guessing
- Use data, not assumptions
- Document investigation path
- Focus on root cause, not symptoms
- Implement minimal, targeted fixes
- Verify thoroughly before closing
- Learn and improve processes