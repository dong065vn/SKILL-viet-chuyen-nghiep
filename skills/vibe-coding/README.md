# Vibe Coding Pro Max - Skill Reference

## Overview
Complete vibe coding workflow orchestrator with 13+ specialized skills for end-to-end development from ideation to deployment.

## Available Skills

### 1. workflow-orchestrator
**Purpose:** Complete vibe coding workflow orchestrator. Use when you need end-to-end development from ideation to deployment, or when you want to follow structured development workflows like brainstorm → PRD → plan → code → test → deploy.

**Commands:**
```
/vibe-coding brainstorm "topic or requirement"
/vibe-coding prd "from requirements"
/vibe-coding plan "with PRD"
/vibe-coding code "Phase X: implementation"
/vibe-coding test "all features"
/vibe-coding debug "issue description"
/vibe-coding fix "after implementing fix"
/vibe-coding verify "before deployment"
/vibe-coding deploy "to production"
```

**Example:**
```
/vibe-coding brainstorm "todo app with user authentication"
/vibe-coding prd "from brainstorm results"
/vibe-coding plan "with PRD"
/vibe-coding code "Phase 1: setup and authentication"
/vibe-coding test "all features"
/vibe-coding debug "if any issues found"
/vibe-coding verify "before deployment"
/vibe-coding deploy "to production"
```

---

### 2. brainstorm
**Purpose:** Requirements gathering and brainstorming with MoSCoW prioritization. Use when starting a new project, exploring requirements, or when the user needs to gather and organize ideas before planning.

**Commands:**
```
/brainstorm "topic or requirement"
```

**Example:**
```
/brainstorm "I need to build a todo app with user authentication"
```

---

### 3. prd-writer
**Purpose:** Product Requirements Document (PRD) writing with RICE prioritization. Use when you need to document product requirements, create structured specifications, or when the user asks to "write PRD", "document requirements", or "create product spec".

**Commands:**
```
/prd-writer "from requirements"
```

**Example:**
```
/prd-writer "from brainstorm results"
```

---

### 4. planner
**Purpose:** Technical planning and task breakdown. Use when you need to create implementation plans, break down features into tasks, or when the user asks to "plan", "create task breakdown", or "design architecture".

**Commands:**
```
/planner "with PRD"
```

**Example:**
```
/planner "create task breakdown for todo app"
```

---

### 5. coder
**Purpose:** Progressive batch-based coding implementation. Use when you need to implement features, write code in batches, or when the user asks to "code", "implement", or "write code".

**Commands:**
```
/coder "Phase X: implementation"
```

**Example:**
```
/coder "Phase 1: setup and authentication"
```

---

### 6. tester
**Purpose:** Comprehensive testing with unit, integration, and e2e tests. Use when you need to write and run tests, ensure code quality, or when the user asks to "test", "write tests", or "run test suite".

**Commands:**
```
/tester "all features"
```

**Example:**
```
/tester "test authentication and task features"
```

---

### 7. debugger
**Purpose:** Systematic 4-phase debugging protocol. Use when you encounter errors, unexpected behavior, or when the user asks to "debug", "find root cause", or "troubleshoot".

**Commands:**
```
/debugger "issue description"
```

**Example:**
```
/debugger "login failure issue"
```

---

### 8. fixer
**Purpose:** Evidence-based fix verification. Use when you need to verify fixes, ensure changes don't introduce new bugs, or when the user asks to "fix review", "verify fix", or "check changes".

**Commands:**
```
/fixer "after implementing fix"
```

**Example:**
```
/fixer "verify login fix"
```

---

### 9. ui-designer
**Purpose:** UI/UX design intelligence with search engine. Use when you need to design user interfaces, create design systems, or when the user asks to "design UI", "create interface", or "build UI with specific style".

**Commands:**
```
/ui-designer "design description"
```

**Example:**
```
/ui-designer "modern dashboard with dark mode"
```

---

### 10. deployer
**Purpose:** Cloud deployment with rollback strategy. Use when you need to deploy applications, manage releases, or when the user asks to "deploy", "release to production", or "push to cloud".

**Commands:**
```
/deployer "to production"
```

**Example:**
```
/deployer "deploy to Vercel"
```

---

### 11. api-designer
**Purpose:** RESTful API design with validation and error handling. Use when you need to design API endpoints, create API documentation, or when the user asks to "design API", "create endpoints", or "build API".

**Commands:**
```
/api-designer "API requirements"
```

**Example:**
```
/api-designer "user management API"
```

---

### 12. database-designer
**Purpose:** Database schema design and optimization. Use when you need to design database schemas, create ERD diagrams, or when the user asks to "design database", "create schema", or "plan database".

**Commands:**
```
/database-designer "database requirements"
```

**Example:**
```
/database-designer "task management database"
```

---

## Key Features

### 1. Evidence-Based Development
- Never claim completion without verification
- Run commands, read outputs, then make claims
- No "should", "probably", "seems to" - only verified facts

### 2. Systematic Approach
- Follow structured workflows
- No skipping phases
- Checkpoint after each major phase

### 3. Progressive Disclosure
- Start with planning before coding
- Build incrementally with verification
- Polish UI last

### 4. Error Handling Protocol
- `/debug` for systematic error analysis
- `/fix` for verification after fixes
- `/verify` before any deployment

## Prerequisites
- Git repository for version control
- Node.js runtime for backend development
- Python (for UI/UX Pro Max features)
- Docker for containerization

## Success Metrics
- **Verification Rate**: All claims backed by evidence
- **Test Coverage**: Minimum 80% statement coverage
- **Deployment Success**: Zero rollback rate
- **User Satisfaction**: Functional requirements met
- **Code Quality**: Linting and best practices followed

## Best Practices
1. **Start with Planning**: Never skip the brainstorm/PRD phase
2. **Follow the Workflow**: Don't jump ahead or skip phases
3. **Verify Everything**: No claims without evidence
4. **Ask for Help**: Use `/debug` when blocked
5. **Progressive Disclosure**: Build incrementally, polish last
6. **Evidence-Based**: Always verify before claiming done

## Error Handling
When you encounter errors:
1. Use `/debug` to systematically analyze the issue
2. Implement fixes based on root cause analysis
3. Use `/fix` to verify the fix worked
4. Use `/verify` before continuing
5. If still blocked, ask for help with specific error details

## Integration with Other Skills
All skills work together seamlessly:
- **Planning Skills**: Brainstorm → PRD Writer → Planner
- **Development Skills**: Coder → API Designer → Database Designer
- **Testing Skills**: Tester → Debugger → Fixer → Verifier
- **Release Skills**: UI Designer → Deployer
- **Orchestration**: Workflow Orchestrator coordinates all phases