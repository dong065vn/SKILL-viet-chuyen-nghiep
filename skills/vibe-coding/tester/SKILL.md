---
name: tester
description: Comprehensive testing with unit, integration, and e2e tests. Use when you need to write and run tests, ensure code quality, or when the user asks to "test", "write tests", or "run test suite".
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🧪 Starting comprehensive testing..."
  after:
    - echo "✅ Testing complete. Ready for verification."
---

# /test - Comprehensive Testing Suite

## What This Skill Does
Creates and runs comprehensive test suites covering unit, integration, and end-to-end testing. Ensures code quality with coverage targets and systematic test strategies.

## When to Use This Skill
- After implementing features
- Before code review or deployment
- When writing new functionality
- When user says "test", "write tests", "run test suite"
- Need to ensure code quality and reliability
- Following TDD (Test-Driven Development) approach

## Core Process

### Step 1: Analysis Phase
1. **Code Review**: Understand what needs testing
2. **Test Level Selection**: Choose appropriate test types
3. **Test Strategy**: Define testing approach and scope
4. **Coverage Targets**: Set quality goals for testing

### Step 2: Test Creation
5. **Test Structure**: Organize tests by feature/component
6. **Test Writing**: Implement tests following best practices
7. **Test Data**: Create realistic test data and scenarios
8. **Test Cases**: Cover happy paths, error paths, and edge cases

### Step 3: Test Execution
9. **Test Running**: Execute test suite systematically
10. **Result Analysis**: Review test outcomes and failures
11. **Coverage Reporting**: Generate and analyze coverage reports
12. **Performance Testing**: Check test execution performance

### Step 4: Quality Assurance
13. **Test Review**: Ensure tests are meaningful and effective
14. **Flaky Test Detection**: Identify and fix unreliable tests
15. **Documentation**: Update test documentation
16. **Final Report**: Generate comprehensive test results

## Có phối hợp

### Inputs
- Source code to be tested
- Test requirements and specifications
- Testing framework and setup
- Coverage targets and quality goals
- Test data and scenarios

### Outputs
```markdown
## Test Results

### Summary
**Total Tests**: 47
**Passed**: 47
**Failed**: 0
**Skipped**: 0

### Coverage Report
**Statements**: 85% (target: 80%)
**Branches**: 70% (target: 70%)
**Functions**: 80% (target: 80%)
**Lines**: 83% (target: 80%)

### Test Categories
**Unit Tests**: 32 tests - Individual functions and components
**Integration Tests**: 10 tests - API endpoints and database
**E2E Tests**: 5 tests - User workflows

### Results by Feature
**Authentication**: 100% pass rate
**Task Management**: 100% pass rate
**API Endpoints**: 100% pass rate

Ready for verification.
```

## Key Principles

### 1. Test Pyramid Approach
- More unit tests than integration tests
- More integration tests than e2e tests
- Focus on fast, reliable tests first

### 2. Test-Driven Development (TDD)
- Write tests before implementation
- Red-Green-Refactor cycle
- Ensure test coverage from the start

### 3. Comprehensive Coverage
- Happy path testing
- Error path testing
- Edge case testing
- Performance testing

### 4. Quality Over Quantity
- Meaningful tests over test count
- Reliable tests over flaky tests
- Maintainable tests over complex tests

## Success Metrics
- **Test Coverage**: Minimum 80% statement coverage
- **Pass Rate**: 100% test pass rate
- **Test Quality**: No flaky or unreliable tests
- **Test Speed**: Tests complete in under 5 minutes
- **Documentation**: Clear test documentation

## Common Pitfalls to Avoid
- **No Tests**: Shipping code without verification
- **Flaky Tests**: Tests that fail randomly
- **Over-Mocking**: Testing implementation instead of behavior
- **Slow Tests**: Tests that take too long to run
- **Missing Edge Cases**: Not testing failure scenarios

## Tips for Effective Testing

### 1. Follow the AAA Pattern
- **Arrange**: Setup test data and environment
- **Act**: Execute the code being tested
- **Assert**: Verify the expected outcome

### 2. Use Descriptive Test Names
- Clear what is being tested
- Include expected behavior
- Include context or conditions

### 3. Test One Thing at a Time
- Single assertion per test when possible
- Focus on specific behavior
- Avoid testing multiple scenarios in one test

### 4. Cover All Paths
- Happy path: Normal successful execution
- Error path: Expected error handling
- Edge cases: Boundary conditions and extremes
- Performance: Speed and resource usage

## Example Workflow

### Scenario: Testing Task Management App
```
Input: Task management feature implementation

Test Process:
1. Analysis: Review task CRUD operations and authentication
2. Test Strategy:
   - Unit tests for individual functions
   - Integration tests for API endpoints
   - E2E tests for user workflows
3. Test Creation:
   - Unit tests for task service functions
   - Integration tests for API endpoints
   - E2E tests for complete user workflows
4. Test Execution:
   - Run all tests with coverage
   - Analyze results and failures
   - Generate coverage report
5. Quality Assurance:
   - Review test effectiveness
   - Fix any flaky tests
   - Update documentation
6. Final Report:
   - Document test results
   - Highlight coverage metrics
   - Identify any remaining issues
```

## Output Quality Checklist
- [ ] All features have corresponding tests
- [ ] Test coverage meets targets
- [ ] All tests pass consistently
- [ ] No flaky or unreliable tests
- [ ] Tests are well-documented
- [ ] Test data is realistic and comprehensive
- [ ] Performance testing included
- [ ] Ready for verification

## Integration with Other Skills
- **Coder**: Tests code implementation
- **Debugger**: Handles test failures
- **Verifier**: Provides evidence for completion
- **Fixer**: Resolves issues found during testing
- **Deployer**: Ensures tests pass before deployment

## Error Handling
If blocked during testing:
1. Identify the specific test failure
2. Check test data and setup
3. Verify implementation matches requirements
4. If stuck, ask for help with specific error
5. Don't proceed with failing tests

## Best Practices

### 1. Test-Driven Development (TDD)
- Write failing test first
- Implement to make test pass
- Refactor while keeping tests green
- Ensures test coverage from start

### 2. Arrange-Act-Assert Pattern
```javascript
describe('FeatureName', () => {
  it('should [expected behavior] when [condition]', () => {
    // Arrange - Setup data
    const input = { /* test data */ };

    // Act - Execute function
    const result = functionUnderTest(input);

    // Assert - Verify result
    expect(result).toEqual(expectedOutput);
  });
});
```

### 3. Mock External Dependencies
- Isolate unit tests from external systems
- Use mocks for databases, APIs, file systems
- Focus on behavior, not implementation

### 4. Test Data Management
- Use realistic test data
- Cover edge cases and boundary conditions
- Keep test data consistent and reproducible

## Test Categories and Strategies

### Unit Tests
- Test individual functions and classes
- Fast execution (milliseconds)
- High coverage (70%+)
- No external dependencies

### Integration Tests
- Test component interactions
- API endpoints and database queries
- Medium execution time (seconds)
- Some external dependencies

### E2E Tests
- Test complete user workflows
- Browser automation
- Slow execution (minutes)
- Full system testing

### Performance Tests
- Test execution speed
- Memory usage
- Resource consumption
- Scalability testing

## Coverage Targets
- **Statements**: 80% minimum
- **Branches**: 70% minimum
- **Functions**: 80% minimum
- **Lines**: 80% minimum
- **Critical Paths**: 100% coverage

## Testing Tools and Frameworks
- **Jest/Vitest**: Unit and integration testing
- **Playwright/Cypress**: E2E testing
- **Istanbul/NYC**: Coverage reporting
- **Mock Service Worker**: API mocking
- **Testcontainers**: Database testing

## Documentation and Reporting
- **Test Documentation**: What each test covers
- **Coverage Reports**: Visual coverage analysis
- **Test Results**: Pass/fail/skip statistics
- **Performance Metrics**: Test execution times
- **Quality Gates**: Automated quality checks