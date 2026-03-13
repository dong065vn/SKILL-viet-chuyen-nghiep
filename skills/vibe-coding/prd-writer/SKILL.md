---
name: prd-writer
description: Product Requirements Document (PRD) writing with RICE prioritization. Use when you need to document product requirements, create structured specifications, or when the user asks to "write PRD", "document requirements", or "create product spec".
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch
hooks:
  before:
    - echo "📝 Starting PRD writing..."
  after:
    - echo "✅ PRD complete. Ready for planning phase."
---

# /prd - Product Requirements Document Writing

## What This Skill Does
Creates comprehensive Product Requirements Documents (PRDs) from requirements, brainstorming outputs, or user inputs. Includes problem statements, solution definitions, user stories, success metrics, and RICE prioritization.

## When to Use This Skill
- After brainstorming sessions
- When starting new features or products
- Documenting requirements for stakeholders
- Creating specifications for development teams
- When user says "write PRD", "create product spec", "document requirements"
- Before technical planning or development begins

## Core Structure

### Section 1: Overview
- **Document Purpose**: Why this PRD exists
- **Scope**: What's included and excluded
- **Timeline**: Target release or development timeline
- **Stakeholders**: Who this affects

### Section 2: Problem Statement
- **Current State**: What problem exists now
- **User Pain Points**: Specific frustrations or needs
- **Business Impact**: Why this matters to the business
- **Success Vision**: What success looks like

### Section 3: Solution & Features
- **High-Level Solution**: How we'll solve the problem
- **Feature Breakdown**: Detailed features with descriptions
- **Technical Approach**: High-level architecture or implementation
- **Dependencies**: What we need from other teams/systems

### Section 4: User Stories
- **Role-Based Stories**: User stories organized by user type
- **Acceptance Criteria**: How we know each story is complete
- **Priority**: Business priority for each story
- **Effort Estimates**: Rough development effort

### Section 5: Success Metrics
- **Key Performance Indicators**: What we'll measure
- **Success Criteria**: Specific targets for success
- **Baseline Metrics**: Current state for comparison
- **Monitoring Plan**: How we'll track progress

### Section 6: Out of Scope
- **Explicit Exclusions**: Features we won't build
- **Future Considerations**: Potential future enhancements
- **Constraints**: Technical or business limitations
- **Assumptions**: What we're assuming about the solution

### Section 7: RICE Prioritization
- **Reach**: How many users will be affected
- **Impact**: How much will it help users
- **Confidence**: How sure are we about our estimates
- **Effort**: How much work it will take
- **RICE Score**: Calculated priority score

### Section 8: Technical Considerations
- **Architecture**: High-level system design
- **Data Models**: Key data structures and relationships
- **API Design**: External interfaces if applicable
- **Performance**: Key performance considerations
- **Security**: Security requirements and concerns

### Section 9: Timeline & Milestones
- **Phases**: Development phases or releases
- **Key Milestones**: Important delivery points
- **Dependencies**: What needs to happen first
- **Risks**: Potential timeline risks

## Có phối hợp

### Inputs
- Brainstorm outputs or requirements
- Problem statements or user needs
- Success metrics or goals
- Technical constraints or preferences
- Stakeholder information

### Outputs
```markdown
## Product Requirements Document

### Document Overview
**Purpose**: [Why this PRD exists]
**Scope**: [What's included/excluded]
**Timeline**: [Target timeline]
**Stakeholders**: [Who's affected]

### Problem Statement
**Current State**: [Problem description]
**User Pain Points**: [Specific frustrations]
**Business Impact**: [Why it matters]
**Success Vision**: [What success looks like]

### Solution & Features
**High-Level Solution**: [How we'll solve it]
**Feature Breakdown**:
- [Feature 1]: [Description] - [User benefit]
- [Feature 2]: [Description] - [User benefit]

### User Stories
**Role-Based Stories**:
**Admin Users**:
- [Story 1]: [Description] - [Acceptance criteria]
- [Priority]: [High/Medium/Low]

### Success Metrics
**Key Performance Indicators**:
- [Metric 1]: [Target] - [How measured]
- [Metric 2]: [Target] - [How measured]

### Out of Scope
**Explicit Exclusions**:
- [Feature 3]: [Why excluded]

### RICE Prioritization
**Feature Prioritization**:
| Feature | Reach | Impact | Confidence | Effort | RICE Score |
|---------|-------|--------|------------|--------|------------|
| Feature 1 | [Score] | [Score] | [Score] | [Score] | [Score] |

### Technical Considerations
**Architecture**: [High-level design]
**Data Models**: [Key structures]

### Timeline & Milestones
**Phases**:
- Phase 1: [What's delivered]
- Phase 2: [What's delivered]

## Conclusion
This PRD provides a comprehensive foundation for building [product name]. The prioritized features and clear success metrics will guide development and ensure we deliver value to users.
```

## Key Principles

### 1. Problem-First Approach
- Always start with the problem, not the solution
- Understand user pain points before proposing features
- Focus on why before how

### 2. Evidence-Based Decisions
- Use data to support feature decisions
- Include metrics for success
- Provide rationale for priorities

### 3. Stakeholder Alignment
- Consider all affected parties
- Document assumptions and constraints
- Create shared understanding

### 4. Clarity and Specificity
- Avoid vague requirements
- Use concrete examples
- Define acceptance criteria clearly

## Success Metrics
- **Completeness**: All major aspects covered
- **Clarity**: Requirements are specific and actionable
- **Alignment**: Stakeholders understand and agree
- **Feasibility**: Technical considerations addressed
- **Measurability**: Success metrics are specific and trackable

## Common Pitfalls to Avoid
- **Solution-First**: Jumping to solutions without understanding problems
- **Vague Requirements**: Using ambiguous language
- **Missing Success Metrics**: Not defining how to measure success
- **No Prioritization**: Listing features without priority
- **Ignoring Constraints**: Not considering technical or business limitations

## Tips for Effective PRD Writing

### 1. Start with the Problem
- What's wrong with the current state?
- Who is affected and how?
- What's the business impact?
- What does success look like?

### 2. Use the 5 Whys Technique
For each feature, ask "why" five times to get to the root need

### 3. Consider Different Perspectives
- User perspective: What do they need?
- Business perspective: What's the ROI?
- Technical perspective: What's feasible?
- Support perspective: What will users need help with?

### 4. Define Clear Acceptance Criteria
- What makes each feature complete?
- How do we know it works?
- What are the edge cases?
- What's the minimum viable implementation?

## Example Workflow

### Scenario: Building a Task Management App
```
Input: Brainstorm results for todo app

PRD Process:
1. Problem Statement: Users struggle to manage personal tasks
2. Solution: Simple, intuitive task management app
3. Features:
   - Must Have: Task creation, completion, basic auth
   - Should Have: Categories, due dates, reminders
4. User Stories:
   - As a user, I want to create tasks so I can track my work
   - As a user, I want to mark tasks complete so I can see progress
5. Success Metrics:
   - Task completion rate increases by 50%
   - User retention improves by 30%
6. RICE Prioritization:
   - Task creation: High reach, high impact, medium effort
   - Collaboration: Medium reach, high impact, high effort
7. Technical Considerations: Mobile-first design, offline support
8. Timeline: MVP in 6 weeks, full feature set in 12 weeks
```

## Output Quality Checklist
- [ ] Clear problem statement with user pain points
- [ ] Specific success metrics with targets
- [ ] RICE scores calculated for all features
- [ ] Acceptance criteria defined for user stories
- [ ] Out of scope clearly documented
- [ ] Technical considerations addressed
- [ ] Timeline with phases and milestones
- [ ] All assumptions and constraints stated

## Integration with Other Skills
- **Brainstorm**: Takes brainstorm output as input
- **Planner**: Uses PRD for technical planning
- **Coder**: Provides specifications for implementation
- **Tester**: Defines test scenarios from user stories
- **Verifier**: Uses success metrics for verification

## Error Handling
If blocked during PRD writing:
1. Ask for clarification on problem statement
2. Request more information about users/stakeholders
3. Propose assumptions to validate
4. Suggest starting with simpler scope
5. Recommend stakeholder interviews or user research

## Best Practices
- Always validate problem statement with stakeholders
- Use concrete examples in user stories
- Include both business and user success metrics
- Be specific about technical constraints
- Update PRD as requirements evolve