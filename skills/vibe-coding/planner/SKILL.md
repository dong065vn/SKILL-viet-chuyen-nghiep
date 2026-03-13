---
name: planner
description: Technical planning and task breakdown. Use when you need to create implementation plans, break down features into tasks, or when the user asks to "plan", "create task breakdown", or "design architecture".
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch
hooks:
  before:
    - echo "🚀 Starting technical planning..."
  after:
    - echo "✅ Planning complete. Ready for implementation."
---

# /plan - Technical Planning & Task Breakdown

## What This Skill Does
Creates comprehensive technical plans from PRDs, requirements, or feature descriptions. Includes architecture design, task breakdown, dependency mapping, and implementation strategy.

## When to Use This Skill
- After PRD completion
- Before starting development
- When breaking down features into tasks
- Designing system architecture
- When user says "plan", "create task breakdown", "design architecture"
- Need to estimate effort and timeline

## Core Process

### Step 1: Analysis Phase
1. **Requirements Review**: Deep dive into PRD/features
2. **Stakeholder Alignment**: Confirm understanding with users
3. **Constraint Identification**: Technical, business, time constraints
4. **Success Criteria**: What defines successful implementation

### Step 2: Architecture Design
5. **System Architecture**: High-level design and components
6. **Data Models**: Database schema and relationships
7. **API Design**: External interfaces and contracts
8. **Technology Stack**: Language, frameworks, tools selection

### Step 3: Task Breakdown
9. **Feature Decomposition**: Break features into implementable tasks
10. **Task Granularity**: Ensure tasks are appropriately sized
11. **Dependencies**: Map task dependencies and critical path
12. **Effort Estimation**: Time/effort estimates for each task

### Step 4: Implementation Strategy
13. **Phase Planning**: Development phases and milestones
14. **Risk Assessment**: Potential risks and mitigation strategies
15. **Quality Gates**: Testing and verification points
16. **Delivery Plan**: How and when features will be delivered

## Có phối hợp

### Inputs
- PRD documents or feature requirements
- Technical constraints or preferences
- Success criteria or acceptance requirements
- Timeline or deadline constraints
- Team size and capabilities

### Outputs
```markdown
## Technical Plan

### Document Overview
**Purpose**: [Why this plan exists]
**Scope**: [What's included/excluded]
**Timeline**: [Target timeline]
**Stakeholders**: [Who's affected]

### Architecture Design
**System Architecture**: [High-level design]
**Components**:
- [Component 1]: [Description and purpose]
- [Component 2]: [Description and purpose]

### Data Models
**Database Schema**: [Key tables and relationships]
**API Contracts**: [External interfaces]

### Task Breakdown
**Feature: [Feature Name]**
- [Task 1]: [Description] - [Estimated effort]
- [Task 2]: [Description] - [Estimated effort]

### Dependencies
**Task Dependencies**:
- Task 1 depends on: [Prerequisite tasks]
- Critical Path: [Sequence of dependent tasks]

### Implementation Strategy
**Phases**:
- Phase 1: [What's delivered]
- Phase 2: [What's delivered]

### Risk Assessment
**Potential Risks**:
- [Risk 1]: [Likelihood] - [Impact] - [Mitigation]

### Quality Gates
**Verification Points**:
- [Milestone 1]: [What's verified]
- [Milestone 2]: [What's verified]

## Conclusion
This plan provides a comprehensive roadmap for implementing [feature/product]. The detailed task breakdown and risk assessment will guide development and ensure successful delivery.
```

## Key Principles

### 1. Decomposition First
- Break complex features into simple, implementable tasks
- Ensure tasks are appropriately sized (1-2 days each)
- Map dependencies clearly

### 2. Architecture-Driven
- Design system architecture before implementation
- Consider scalability and maintainability
- Document technical decisions

### 3. Risk-Aware
- Identify potential risks early
- Plan mitigation strategies
- Include contingency in timelines

### 4. Evidence-Based
- Use data for effort estimation
- Include measurable success criteria
- Plan for verification at each phase

## Success Metrics
- **Completeness**: All features broken down into tasks
- **Clarity**: Tasks are specific and actionable
- **Dependencies**: All task dependencies mapped
- **Feasibility**: Architecture is technically sound
- **Risk Management**: Potential risks identified and mitigated

## Common Pitfalls to Avoid
- **Monolithic Tasks**: Breaking features into too few, too large tasks
- **Missing Dependencies**: Not mapping task relationships
- **Over-Engineering**: Designing for hypothetical future needs
- **Ignoring Constraints**: Not considering technical or business limitations
- **No Verification Plan**: Not planning for testing and validation

## Tips for Effective Planning

### 1. Use the Right Granularity
- Tasks should be 1-2 days of work
- Small enough to complete without blocking
- Large enough to have meaningful progress

### 2. Map Dependencies Carefully
- What needs to happen before what?
- Identify critical path
- Plan for parallel work where possible

### 3. Consider Different Perspectives
- Developer perspective: What's technically feasible?
- User perspective: What delivers value?
- Business perspective: What's the ROI?
- Support perspective: What will users need help with?

### 4. Plan for Verification
- When and how will we test each feature?
- What are the acceptance criteria?
- How do we know when something is complete?

## Example Workflow

### Scenario: Building a Task Management App
```
Input: PRD for todo app with user authentication

Planning Process:
1. Requirements Review: Understand all features and constraints
2. Architecture Design:
   - Frontend: React with TypeScript
   - Backend: Node.js with Express
   - Database: PostgreSQL with Prisma
   - Auth: JWT with refresh tokens
3. Task Breakdown:
   - Setup project structure
   - Configure database and Prisma
   - Implement authentication system
   - Create task CRUD operations
   - Build UI components
   - Add validation and error handling
4. Dependencies:
   - Database setup before API implementation
   - Auth before user-specific features
   - UI components after API endpoints
5. Implementation Strategy:
   - Phase 1: Core functionality (MVP)
   - Phase 2: Enhanced features
   - Phase 3: Polish and optimization
6. Risk Assessment:
   - Database migration risks: Plan for rollback
   - Authentication security: Follow best practices
7. Quality Gates:
   - Unit tests before feature completion
   - Integration tests before deployment
   - User acceptance testing before release
```

## Output Quality Checklist
- [ ] Clear system architecture diagram or description
- [ ] All features broken down into tasks
- [ ] Task dependencies mapped
- [ ] Effort estimates provided
- [ ] Implementation phases defined
- [ ] Risk assessment completed
- [ ] Quality gates identified
- [ ] Success criteria defined

## Integration with Other Skills
- **PRD Writer**: Takes PRD as input for planning
- **Coder**: Provides task specifications for implementation
- **Tester**: Defines test scenarios from plan
- **Verifier**: Uses quality gates for verification
- **Deployer**: Informs deployment strategy

## Error Handling
If blocked during planning:
1. Ask for clarification on requirements
2. Request more information about constraints
3. Propose assumptions to validate
4. Suggest simpler architecture if complex
5. Recommend stakeholder alignment session

## Best Practices
- Always validate plan with stakeholders
- Use data for effort estimation when possible
- Include contingency in timelines
- Plan for both success and failure scenarios
- Update plan as requirements evolve

## Templates and Tools
- **Architecture Decision Records (ADRs)**: Document technical decisions
- **Gantt Charts**: Visualize timeline and dependencies
- **Risk Matrices**: Assess and prioritize risks
- **Effort Estimation Matrices**: Use historical data for estimates
- **Quality Checklists**: Ensure completeness and consistency