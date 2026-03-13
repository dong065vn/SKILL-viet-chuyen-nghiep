---
name: vibe-coding
description: Complete vibe coding workflow orchestrator. Use when you need end-to-end development from ideation to deployment, or when you want to follow structured development workflows like brainstorm → PRD → plan → code → test → deploy.
model: opus
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch
hooks:
  before:
    - echo "🎯 Starting Vibe Coding workflow..."
  after:
    - echo "✅ Vibe Coding workflow completed."
---

# Vibe Coding - Complete Workflow Orchestrator

## What This Skill Does
This skill orchestrates the complete vibe coding workflow, combining the best practices from the analyzed workflows. It provides structured development from ideation to deployment with proper verification at each stage.

## When to Use This Skill
- Starting a new project from scratch
- Following structured development workflows
- Need end-to-end development with verification
- Want to use the brainstorm → PRD → plan → code → test → deploy workflow
- Need systematic debugging and verification

## Core Workflow Phases

### Phase 1: Ideation & Planning
```
/brain → /prd → /flow → /erd
```
- **Brainstorm**: Requirements gathering with MoSCoW prioritization
- **PRD Writing**: Problem statement, user stories, RICE prioritization
- **Flowchart**: Mermaid diagrams for system architecture
- **Database Design**: ERD, schema design, indexing strategy

### Phase 2: Development
```
/setup → /prisma → /api → /auth → /code
```
- **Backend Setup**: Node.js + Docker + project structure
- **Database Schema**: Prisma migrations + validation
- **API Creation**: CRUD endpoints + validation + error handling
- **Authentication**: JWT/Session/OAuth setup
- **Batch Coding**: Progressive implementation with progress reporting

### Phase 3: Testing & Quality
```
/test → /debug → /fix → /verify
```
- **Testing**: Unit/integration/e2e with coverage targets
- **Systematic Debugging**: 4-phase debugging protocol
- **Fix Verification**: Evidence-based fix validation
- **Verification**: Pre-commit/pre-deploy checks

### Phase 4: UI/UX & Release
```
/ui → /css → /check → /save → /deploy
```
- **UI/UX Pro Max**: Design intelligence with 50+ styles, 97 palettes
- **Tailwind CSS**: Design system and dark mode
- **Checkpoint**: Pre-release verification
- **Git Operations**: Conventional commits + push
- **Deployment**: Cloud deployment with rollback strategy

## Key Principles

### 1. Evidence Before Claims
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

## Usage Examples

### New Project Workflow
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

### Bug Fix Workflow
```
/vibe-coding debug "login failure issue"
/vibe-coding fix "after implementing fix"
/vibe-coding verify "login functionality"
/vibe-coding check "before commit"
```

### UI Enhancement Workflow
```
/vibe-coding design "modern dashboard with dark mode"
/vibe-coding css "tailwind design system"
/vibe-coding verify "UI functionality"
/vibe-coding check "before merge"
```

## Skills This Orchestrates

### Planning Skills
- **Brainstorm**: Requirements gathering with MoSCoW
- **PRD Writer**: Product requirements document creation
- **Planner**: Technical planning and task breakdown
- **Mermaid Expert**: Flowchart and diagram creation
- **Database Design**: Schema design and optimization

### Development Skills
- **Coder**: Batch-based progressive implementation
- **Setup Expert**: Backend setup with Node.js + Docker
- **API Designer**: RESTful API creation with validation
- **Auth Specialist**: Authentication system setup
- **Docker Expert**: Containerization and deployment

### Testing & Quality Skills
- **Tester**: Unit/integration/e2e testing
- **Debugger**: Systematic 4-phase debugging
- **Fixer**: Evidence-based fix verification
- **Verifier**: Pre-commit/pre-deploy checks
- **Quality Gate**: Automated quality checks

### UI/UX & Release Skills
- **UI Designer**: Design intelligence with search engine
- **CSS Specialist**: Tailwind design system
- **Deployer**: Cloud deployment with rollback
- **Git Expert**: Conventional commits and workflows
- **Release Manager**: Build optimization and packaging

## Success Metrics
- **Verification Rate**: All claims backed by evidence
- **Test Coverage**: Minimum 80% statement coverage
- **Deployment Success**: Zero rollback rate
- **User Satisfaction**: Functional requirements met
- **Code Quality**: Linting and best practices followed

## Prerequisites
- Git repository for version control
- Node.js runtime for backend development
- Python (for UI/UX Pro Max features)
- Docker for containerization

## Tips for Success
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

## Best Practices
- Always run tests before deployment
- Use conventional commits for Git operations
- Keep PRDs updated with changing requirements
- Document decisions in code comments
- Follow the "stop when blocked" principle

## Output Format
This skill provides structured outputs at each phase:
- **Planning**: Complete PRD documents with user stories
- **Development**: Working code with progress reports
- **Testing**: Test results with coverage reports
- **Verification**: Evidence-based completion reports
- **Deployment**: Deployment logs and rollback procedures