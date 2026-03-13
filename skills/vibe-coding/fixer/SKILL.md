---
name: fixer
description: Evidence-based fix verification. Use when you need to verify fixes, ensure changes don't introduce new bugs, or when the user asks to "fix review", "verify fix", or "check changes". Implements the verify-before-claim principle.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🔍 Starting fix verification..."
  after:
    - echo "✅ Fix verified. No regressions detected."
---

# /fix - Evidence-Based Fix Verification

## What This Skill Does
Implements evidence-based verification of fixes to ensure they resolve the root cause without introducing new bugs. Follows the "verify before claim" principle and uses systematic testing to confirm fixes work as intended.

## When to Use This Skill
- After implementing bug fixes
- When reviewing changes to ensure quality
- Before claiming work is complete
- When user says "fix review", "verify fix", "check changes"
- Need to ensure fixes don't introduce regressions
- Following up on debug findings

## Core Process

### Step 1: Fix Analysis
**Objective**: Understand what was changed and why

1. **Change Review**
   - Examine code changes made
   - Review fix implementation details
   - Understand the intended solution
   - Check against original requirements

2. **Root Cause Alignment**
   - Verify fix addresses the identified root cause
   - Ensure solution matches the proposed fix
   - Check if fix is minimal and targeted
   - Confirm no over-engineering

3. **Side Effect Assessment**
   - Identify potential unintended impacts
   - Check for breaking changes
   - Assess performance implications
   - Consider security implications

4. **Test Plan Development**
   - Define verification tests
   - Identify regression scenarios
   - Plan edge case testing
   - Prepare test data and environment

### Step 2: Verification Testing
**Objective**: Confirm fix works and doesn't break other things

1. **Original Issue Reproduction**
   - Attempt to reproduce the original issue
   - Verify the issue is resolved
   - Test under various conditions
   - Document success criteria

2. **Regression Testing**
   - Test unaffected functionality
   - Verify no new bugs introduced
   - Check related features
   - Test performance characteristics

3. **Edge Case Testing**
   - Test boundary conditions
   - Verify error handling
   - Test extreme cases
   - Check data validation

4. **Integration Testing**
   - Test with other system components
   - Verify API contracts
   - Check database interactions
   - Test user workflows

### Step 3: Evidence Collection
**Objective**: Gather proof that fix works correctly

1. **Test Results Documentation**
   - Record test outcomes
   - Capture success metrics
   - Document verification steps
   - Note any issues found

2. **Performance Metrics**
   - Measure execution time
   - Check resource usage
   - Verify scalability
   - Document performance impact

3. **Security Assessment**
   - Check for security vulnerabilities
   - Verify data validation
   - Test authentication/authorization
   - Assess potential attack vectors

4. **Quality Gates Verification**
   - Run linting and style checks
   - Verify code coverage
   - Check documentation updates
   - Ensure build success

### Step 4: Final Assessment
**Objective**: Make evidence-based conclusion about fix quality

1. **Success Criteria Evaluation**
   - Did the fix resolve the original issue?
   - Are all tests passing?
   - Is there any regression?
   - Does it meet quality standards?

2. **Risk Assessment**
   - Any remaining concerns?
   - Potential future issues?
   - Maintenance implications?
   - Deployment readiness?

3. **Recommendations**
   - Additional tests needed?
   - Documentation updates?
   - Monitoring requirements?
   - Deployment strategy?

4. **Final Decision**
   - Fix approved for deployment?
   - Additional work needed?
   - Rollback plan if needed?
   - Next steps defined?

## Có phối hợp

### Inputs
- Code changes to be verified
- Original issue description and root cause
- Proposed fix implementation
- Test requirements and success criteria
- Environment and data setup

### Outputs
```markdown
## Fix Verification Report

### Fix Analysis
**Changes Reviewed**: [Summary of changes made]
**Root Cause Alignment**: [How fix addresses root cause]
**Side Effects Assessed**: [Potential impacts identified]

### Verification Testing
**Original Issue Reproduction**:
- [ ] Issue successfully reproduced
- [ ] Fix implemented correctly
- [ ] Issue resolved verified

**Regression Testing**:
- [ ] Unaffected functionality intact
- [ ] No new bugs introduced
- [ ] Related features working

**Edge Case Testing**:
- [ ] Boundary conditions handled
- [ ] Error handling verified
- [ ] Performance acceptable

### Evidence Collected
**Test Results**: [Summary of outcomes]
**Performance Metrics**: [Before/after comparison]
**Security Assessment**: [Any concerns identified]

### Final Assessment
**Fix Status**: [Approved/Rejected/Requires Work]
**Success Criteria Met**: [Yes/No/Partially]
**Risk Level**: [Low/Medium/High]

### Recommendations
**Next Steps**: [What to do next]
**Additional Work**: [Any remaining tasks]
**Deployment Readiness**: [Ready/Not Ready]

Ready for deployment.
```

## Key Principles

### 1. Evidence Before Claims
- Never claim fix works without proof
- Base conclusions on test results
- Document all verification steps
- Use objective metrics

### 2. Minimal Verification
- Test only what's necessary
- Focus on critical paths
- Avoid over-testing
- Efficient verification process

### 3. Regression Prevention
- Ensure no new bugs introduced
- Verify related functionality
- Test edge cases and boundaries
- Check performance implications

### 4. Risk-Aware
- Identify potential risks
- Plan for mitigation
- Document concerns
- Provide recommendations

## Success Metrics
- **Fix Effectiveness**: Original issue resolved
- **Regression Rate**: No new bugs introduced
- **Test Coverage**: All critical paths tested
- **Documentation Quality**: Clear verification evidence
- **Risk Assessment**: Potential issues identified

## Common Pitfalls to Avoid
- **Incomplete Verification**: Not testing all scenarios
- **Assumption-Based**: Believing fix works without testing
- **Over-Testing**: Wasting time on unnecessary tests
- **Missing Regressions**: Not checking related functionality
- **No Documentation**: Not recording verification results

## Tips for Effective Fix Verification

### 1. Use the Scientific Method
- Form hypothesis about fix
- Design experiment to test it
- Collect data from tests
- Draw evidence-based conclusions

### 2. Test in Isolation First
- Verify fix in controlled environment
- Test with minimal dependencies
- Ensure basic functionality works
- Then test in integrated environment

### 3. Think Like an Attacker
- Try to break the fix
- Test with invalid data
- Check for security vulnerabilities
- Verify error handling

### 4. Automate Where Possible
- Create repeatable test scripts
- Use continuous integration
- Automate regression testing
- Document test procedures

## Verification Techniques

### 1. Black Box Testing
- Test functionality without knowing implementation
- Focus on inputs and outputs
- Verify behavior matches requirements
- No assumptions about internal workings

### 2. White Box Testing
- Test with knowledge of implementation
- Check code coverage
- Verify internal logic
- Test edge cases and boundaries

### 3. Mutation Testing
- Introduce small changes to test robustness
- Verify tests catch the changes
- Ensure tests are meaningful
- Improve test quality

### 4. Property-Based Testing
- Test with random inputs
- Verify invariants hold
- Test edge cases automatically
- Find unexpected failures

## Common Fix Verification Scenarios

### Scenario 1: Bug Fix Verification
```
Fix: Resolved null pointer exception in user service
Verification Steps:
1. Reproduce original bug: Confirm null pointer occurs
2. Apply fix: Verify null check prevents exception
3. Test related functionality: User registration, login still work
4. Edge cases: Empty user data, invalid inputs
5. Performance: Check service response time
6. Security: Verify no injection vulnerabilities
7. Documentation: Update API docs if needed
```

### Scenario 2: Performance Fix Verification
```
Fix: Optimized database query to reduce response time
Verification Steps:
1. Measure original performance: Record baseline metrics
2. Apply fix: Verify query optimization
3. Performance testing: Test under load
4. Regression testing: Ensure other queries still work
5. Memory usage: Check for memory leaks
6. Scalability: Test with larger datasets
7. Documentation: Update performance expectations
```

### Scenario 3: Security Fix Verification
```
Fix: Added input validation to prevent XSS attacks
Verification Steps:
1. Security testing: Try various attack vectors
2. Input validation: Test with valid and invalid inputs
3. Output encoding: Verify proper encoding applied
4. Regression testing: Ensure legitimate inputs still work
5. Performance: Check validation overhead
6. Documentation: Update security guidelines
7. Monitoring: Add logging for suspicious activities
```

## Output Quality Checklist
- [ ] Original issue successfully reproduced and resolved
- [ ] Regression testing completed
- [ ] Edge case testing performed
- [ ] Performance verified
- [ ] Security assessment completed
- [ ] All tests documented
- [ ] Evidence collected and recorded
- [ ] Final assessment provided
- [ ] Recommendations included

## Integration with Other Skills
- **Debugger**: Takes debug findings for verification
- **Tester**: Uses verification tests for regression
- **Coder**: Implements fixes based on requirements
- **Verifier**: Provides evidence for completion claims
- **Deployer**: Ensures fixes ready for deployment

## Advanced Verification Strategies

### 1. Continuous Integration Integration
- Automated verification in CI pipeline
- Regression tests run on every commit
- Performance benchmarks tracked over time
- Security scans automated

### 2. A/B Testing for Critical Fixes
- Deploy fix to subset of users
- Compare behavior with control group
- Monitor for unexpected issues
- Gradual rollout with monitoring

### 3. Canary Releases
- Deploy fix to small percentage of traffic
- Monitor for issues
- Gradual increase based on success
- Quick rollback capability

### 4. Feature Flags
- Deploy fix behind feature flag
- Enable for specific users/groups
- Quick disable if issues found
- Gradual rollout strategy

## Post-Verification Activities

### 1. Documentation Updates
- Update API documentation
- Add troubleshooting guides
- Record known issues and solutions
- Update runbooks

### 2. Monitoring and Alerting
- Add monitoring for fixed issue
- Set up alerts for recurrence
- Track performance metrics
- Log important events

### 3. Knowledge Sharing
- Document the fix and verification
- Share with team
- Add to knowledge base
- Train others on similar issues

### 4. Process Improvement
- Could this issue have been prevented?
- Should we add more tests?
- Can we improve our development process?
- What monitoring would help catch this earlier?

## Error Handling and Escalation

### When to Reject a Fix
- Fix doesn't address root cause
- Fix introduces new bugs
- Fix has unacceptable performance impact
- Fix creates security vulnerabilities
- Fix is over-engineered or incomplete

### Rejection Process
1. Document specific issues found
2. Provide clear evidence of problems
3. Suggest alternative approaches
4. Offer to help find better solution
5. Keep communication constructive

## Best Practices
- Always verify before claiming fix works
- Use objective evidence, not assumptions
- Test both success and failure scenarios
- Consider performance and security implications
- Document everything for future reference
- Think about long-term maintenance
- Plan for monitoring and alerting