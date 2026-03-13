---
name: brainstorm
description: Requirements gathering and brainstorming with MoSCoW prioritization. Use when starting a new project, exploring requirements, or when the user needs to gather and organize ideas before planning.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch
hooks:
  before:
    - echo "🧠 Starting brainstorming session..."
  after:
    - echo "✅ Brainstorming complete. Ready for PRD writing."
---

# /brain - Brainstorm & Requirements Gathering

## What This Skill Does
Systematic brainstorming to gather requirements, generate ideas, and prioritize features using MoSCoW methodology. Creates structured output ready for PRD writing.

## When to Use This Skill
- Starting a new project from scratch
- Exploring requirements for existing projects
- Feature ideation and prioritization
- When user says "brainstorm", "explore requirements", "generate ideas"
- Before writing PRD or planning phase

## Core Process

### Step 1: Understanding Phase
1. **Problem Discovery**: What problem are we solving?
2. **Stakeholder Analysis**: Who are the users and stakeholders?
3. **Context Gathering**: Current solutions, constraints, requirements
4. **Success Criteria**: How do we measure success?

### Step 2: Idea Generation
5. **Feature Brainstorming**: Generate potential features without filtering
6. **Technical Considerations**: Technology stack, architecture ideas
7. **User Experience**: User flows, interface concepts
8. **Edge Cases**: Potential problems and edge scenarios

### Step 3: Prioritization (MoSCoW)
9. **Must Have**: Core features without which the product fails
10. **Should Have**: Important but not critical features
11. **Could Have**: Nice-to-have features if time permits
12. **Won't Have**: Explicitly excluded features

### Step 4: Output Generation
13. **Requirements Summary**: Structured list of all requirements
14. **Priority Matrix**: MoSCoW categorization with rationale
15. **Questions & Assumptions**: Open questions and assumptions made
16. **Next Steps**: Recommendations for next phase

## Có phối hợp

### Inputs
- Project description or problem statement
- Target users or audience
- Technical constraints or preferences
- Success metrics or goals
- Time/budget constraints

### Outputs
```markdown
## Brainstorm Results

### Problem Statement
[Clear problem description]

### Stakeholder Analysis
- Primary users: [description]
- Secondary users: [description]
- Stakeholders: [description]

### Requirements Summary
#### Must Have (Core Features)
- [Feature 1]: [Description] - Why critical
- [Feature 2]: [Description] - Why critical

#### Should Have (Important Features)
- [Feature 3]: [Description] - Why important

#### Could Have (Nice-to-Have Features)
- [Feature 4]: [Description] - If time permits

#### Won't Have (Explicitly Excluded)
- [Feature 5]: [Description] - Why excluded

### Questions & Assumptions
**Open Questions:**
- [Question 1]: [Context]
- [Question 2]: [Context]

**Assumptions:**
- [Assumption 1]: [Rationale]
- [Assumption 2]: [Rationale]

### Next Steps
1. Validate assumptions with stakeholders
2. Write PRD with detailed requirements
3. Technical planning and architecture design
4. Begin development with core features
```

## Key Principles

### 1. No Filtering During Generation
- Generate all ideas first, then prioritize
- Avoid premature optimization of ideas
- Capture everything, even "crazy" ideas

### 2. Evidence-Based Prioritization
- Use MoSCoW methodology consistently
- Provide clear rationale for each priority
- Consider impact vs effort for each feature

### 3. Stakeholder-Centric
- Always consider user needs and perspectives
- Balance technical feasibility with user value
- Document assumptions about user behavior

### 4. Iterative Process
- Start broad, then narrow down
- Be prepared to revisit decisions
- Welcome new information that changes priorities

## Success Metrics
- **Completeness**: All major requirements captured
- **Clarity**: Requirements are specific and actionable
- **Prioritization**: Clear MoSCoW categorization with rationale
- **Questions**: Open questions identified and documented
- **Assumptions**: Key assumptions made explicit

## Common Pitfalls to Avoid
- **Premature Filtering**: Don't dismiss ideas too early
- **Missing Stakeholders**: Consider all user types
- **Vague Requirements**: Be specific about what features do
- **Skipping Edge Cases**: Consider failure scenarios
- **Ignoring Constraints**: Document technical and business constraints

## Tips for Effective Brainstorming

### 1. Ask the Right Questions
- What problem are we solving?
- Who are the users and what do they need?
- What are the success criteria?
- What constraints exist?
- What's the minimum viable product?

### 2. Use the 5 Whys Technique
For each requirement, ask "why" five times to get to the root need

### 3. Consider Different User Personas
- Technical users vs non-technical users
- Power users vs casual users
- Internal users vs external users
- Admin users vs end users

### 4. Think About Edge Cases
- What happens when things go wrong?
- How do we handle errors and failures?
- What about unusual user behavior?
- How do we scale to many users?

## Example Workflow

### Scenario: Building a Task Management App
```
User: "I want to build a todo app with user authentication"

Brainstorm Process:
1. Problem Discovery: Managing personal tasks efficiently
2. Stakeholders: Individual users, teams
3. Requirements Generation:
   - Must Have: Task creation, completion, basic auth
   - Should Have: Categories, due dates, reminders
   - Could Have: Collaboration, file attachments, analytics
4. MoSCoW Prioritization with rationale
5. Questions: Mobile vs web? Real-time sync?
6. Assumptions: Users prefer simple interface
7. Next Steps: Validate with potential users, write PRD
```

## Output Quality Checklist
- [ ] Clear problem statement
- [ ] All stakeholders identified
- [ ] Features categorized with MoSCoW
- [ ] Rationale provided for each priority
- [ ] Open questions documented
- [ ] Key assumptions stated
- [ ] Next steps defined
- [ ] Requirements are specific and actionable

## Integration with Other Skills
- **PRD Writer**: Takes brainstorm output as input
- **Planner**: Uses requirements for technical planning
- **Coder**: Provides feature specifications for implementation
- **Tester**: Defines test scenarios from requirements

## Error Handling
If blocked during brainstorming:
1. Ask clarifying questions about the problem
2. Request more context about users/stakeholders
3. Propose assumptions to test
4. Suggest starting with simpler scope
5. Recommend user research or stakeholder interviews