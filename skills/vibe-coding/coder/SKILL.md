---
name: coder
description: Progressive batch-based coding implementation. Use when you need to implement features, write code in batches, or when the user asks to "code", "implement", or "write code".
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🚀 Starting batch-based coding..."
  after:
    - echo "✅ Coding batch complete. Ready for verification."
---

# /code - Progressive Batch-Based Coding

## What This Skill Does
Implements features in progressive batches with continuous verification and progress reporting. Follows technical plans and ensures code quality at each step.

## When to Use This Skill
- After technical planning completion
- When implementing features from task breakdown
- For progressive development with verification
- When user says "code", "implement", "write code"
- Need to build features in manageable chunks

## Core Process

### Step 1: Preparation Phase
1. **Plan Review**: Load and analyze task_plan.md
2. **Environment Setup**: Ensure development environment ready
3. **Dependencies Check**: Verify all required packages/tools available
4. **Configuration**: Load project settings and conventions

### Step 2: Batch Execution
5. **Batch Selection**: Choose 3-5 tasks for current batch
6. **Task Implementation**: Code each task following specifications
7. **Progress Tracking**: Update progress.md with current status
8. **Verification**: Run tests and checks for completed tasks

### Step 3: Quality Assurance
9. **Code Review**: Self-review for quality and consistency
10. **Testing**: Run unit tests for implemented features
11. **Linting**: Check code style and conventions
12. **Build**: Verify successful compilation/build

### Step 4: Reporting & Handoff
13. **Progress Report**: Generate batch completion report
14. **Verification Results**: Document test outcomes
15. **Next Steps**: Identify next batch of tasks
16. **Feedback Loop**: Wait for review before continuing

## Có phối hợp

### Inputs
- task_plan.md with detailed task breakdown
- Technical specifications and requirements
- Project configuration and conventions
- Testing framework and setup
- Development environment details

### Outputs
```markdown
## Batch Complete

### Implemented
- [x] Task 1: [Description] - [File location]
- [x] Task 2: [Description] - [File location]
- [x] Task 3: [Description] - [File location]

### Verification
**Tests**:
- [x] Unit tests: 12/12 passed
- [x] Integration tests: 5/5 passed

**Build**:
- [x] TypeScript compilation: Success
- [x] Linting: No errors

**Quality**:
- [x] Code coverage: 85%
- [x] No security issues

Ready for feedback.
```

## Key Principles

### 1. Progressive Disclosure
- Build in small, manageable batches
- Verify at each step before proceeding
- Don't move forward with broken code

### 2. Quality at Speed
- Write tests alongside code
- Follow established conventions
- Self-review before completion

### 3. Evidence-Based Progress
- Only mark tasks complete when verified
- Document verification results
- Provide clear progress reports

### 4. Feedback-Driven
- Stop when blocked, ask for help
- Wait for review before continuing
- Incorporate feedback into next batch

## Success Metrics
- **Task Completion**: All planned tasks implemented
- **Verification Rate**: All tests pass at each batch
- **Code Quality**: Linting and style compliance
- **Progress Reporting**: Clear status updates
- **Feedback Integration**: Issues resolved before continuing

## Common Pitfalls to Avoid
- **Big Bang Development**: Trying to implement everything at once
- **Skipping Verification**: Moving forward with broken code
- **Over-Engineering**: Adding features not in plan
- **Ignoring Conventions**: Not following project standards
- **No Progress Tracking**: Losing track of what's been done

## Tips for Effective Batch Coding

### 1. Choose the Right Batch Size
- 3-5 tasks per batch is optimal
- Small enough to complete in 1-2 hours
- Large enough to make meaningful progress

### 2. Follow the Plan Exactly
- Don't deviate from task specifications
- Implement exactly what's described
- Ask for clarification if unclear

### 3. Verify Before Moving On
- Run tests after each task
- Check linting and build
- Ensure no regressions

### 4. Document Everything
- Update progress.md regularly
- Comment code clearly
- Note any deviations from plan

## Example Workflow

### Scenario: Building Task Management App
```
Input: task_plan.md with authentication and task features

Batch 1 Process:
1. Review plan: Setup project, implement auth, create task CRUD
2. Batch Selection: Choose project setup and authentication tasks
3. Implementation:
   - Setup Node.js project with Express
   - Configure Prisma and database
   - Implement JWT authentication
   - Create user registration/login endpoints
4. Verification:
   - Run unit tests for auth functions
   - Test API endpoints with Postman
   - Check database migrations
5. Progress Report:
   - Document completed tasks
   - Show test results
   - Identify next batch
6. Handoff: Wait for review before proceeding
```

## Output Quality Checklist
- [ ] All selected tasks completed
- [ ] Tests pass for implemented features
- [ ] Code follows project conventions
- [ ] Progress.md updated
- [ ] Verification results documented
- [ ] No regressions introduced
- [ ] Ready for review/feedback

## Integration with Other Skills
- **Planner**: Takes task breakdown as input
- **Tester**: Runs tests for verification
- **Debugger**: Handles issues found during testing
- **Verifier**: Provides evidence for completion claims
- **Fixer**: Resolves issues found during verification

## Error Handling
If blocked during coding:
1. Identify the specific issue
2. Try to resolve using documentation
3. If stuck, stop and ask for help
4. Don't proceed with broken code
5. Document the issue in progress.md

## Best Practices

### 1. Write Tests First (TDD Approach)
- Define test cases before implementation
- Write failing tests, then make them pass
- Ensures test coverage from the start

### 2. Follow SOLID Principles
- Single responsibility for functions/classes
- Open/closed for extensibility
- Liskov substitution for polymorphism
- Interface segregation for clean APIs
- Dependency inversion for testability

### 3. Use Meaningful Names
- Variables describe their purpose
- Functions describe their action
- Classes describe their responsibility
- Avoid abbreviations and magic numbers

### 4. Keep Functions Small
- Single responsibility principle
- Under 20 lines when possible
- Easy to test and understand
- Reusable across the codebase

## Templates and Patterns
- **API Endpoint Template**: Standard CRUD structure
- **Service Layer Pattern**: Business logic separation
- **Repository Pattern**: Data access abstraction
- **Middleware Pattern**: Request processing pipeline
- **Error Handling Pattern**: Consistent error responses

## Development Workflow
1. **Setup**: Ensure environment ready
2. **Plan Review**: Understand what needs to be done
3. **Batch Selection**: Choose manageable chunk
4. **Implementation**: Write code following specs
5. **Verification**: Test and validate
6. **Documentation**: Update progress and comments
7. **Review**: Wait for feedback
8. **Iterate**: Continue with next batch