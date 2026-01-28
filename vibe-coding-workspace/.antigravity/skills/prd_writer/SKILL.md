---
name: prd_writer
description: >
  Viết PRD (Product Requirements Document) chuyên nghiệp.
  Bao gồm Problem, Solution, User Stories, Success Metrics.
  Sử dụng sau khi brainstorm hoàn thành.
---

# PRD Writer - Viết Tài liệu Yêu cầu Sản phẩm

## Mục đích
Tạo PRD rõ ràng, đầy đủ từ kết quả brainstorm để định hướng development.

---

## PRD Template

### 1. Overview
```markdown
# [Tên Dự án] - PRD

**Version:** 1.0
**Date:** [Ngày tạo]
**Author:** [Tên]
**Status:** Draft | Review | Approved
```

### 2. Problem Statement
```markdown
## Problem Statement

### The Problem
[Mô tả vấn đề cần giải quyết]

### Current Situation
[Tình trạng hiện tại và pain points]

### Impact
[Ảnh hưởng nếu không giải quyết]
```

### 3. Solution
```markdown
## Proposed Solution

### High-Level Solution
[Tổng quan giải pháp]

### Key Features
| Feature | Description | Priority |
|---------|-------------|----------|
| [Feature 1] | [Mô tả] | Must-have |
| [Feature 2] | [Mô tả] | Should-have |
| [Feature 3] | [Mô tả] | Could-have |
```

### 4. User Stories
```markdown
## User Stories

### Persona: [Tên Persona]
**Background:** [Mô tả]
**Goals:** [Mục tiêu]
**Pain Points:** [Khó khăn]

### Stories
1. As a [role], I want [action] so that [benefit].
2. As a [role], I want [action] so that [benefit].
```

### 5. Success Metrics
```markdown
## Success Metrics

### North Star Metric
[Metric chính đo lường thành công]

### Key Metrics
| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| [Metric 1] | [Now] | [Goal] | [When] |
| [Metric 2] | [Now] | [Goal] | [When] |
```

### 6. Out of Scope
```markdown
## Out of Scope
- [Điều KHÔNG làm trong phiên bản này]
- [Điều KHÔNG làm trong phiên bản này]
```

### 7. Technical Considerations
```markdown
## Technical Considerations

### Dependencies
- [Dependency 1]
- [Dependency 2]

### Risks & Mitigations
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Plan] |
```

### 8. Timeline
```markdown
## Timeline

### Phases
| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Phase 1 | [X weeks] | [Outputs] |
| Phase 2 | [X weeks] | [Outputs] |
```

---

## RICE Prioritization

Cho mỗi feature, tính RICE Score:
```
Score = (Reach × Impact × Confidence) / Effort

- Reach: Số users/quarter
- Impact: Massive=3, High=2, Medium=1, Low=0.5, Minimal=0.25
- Confidence: High=100%, Medium=80%, Low=50%
- Effort: Person-months
```

---

## Best Practices

✅ **Do:**
- Start với problem, không phải solution
- Include clear success metrics
- Explicitly state out of scope
- Use visuals (wireframes, flows)
- Version control changes

❌ **Don't:**
- Skip problem definition
- Vague success criteria
- No out of scope section
- Technical jargon overload
- No stakeholder input

---

## Quy trình viết PRD

1. **Gather Input** - Từ brainstorm session
2. **Draft PRD** - Dùng template trên
3. **Review** - Với stakeholders
4. **Iterate** - Cập nhật theo feedback
5. **Approve** - Chốt version final
6. **Handoff** - Chuyển cho Planning phase
