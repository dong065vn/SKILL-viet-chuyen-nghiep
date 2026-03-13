# Project Phases - Hướng dẫn Phân chia Dự án

## Nguyên tắc chia Phases

### 1. Mỗi Phase có Goal rõ ràng
- Phase là một milestone có thể demo
- Kết thúc phase = có output cụ thể

### 2. Max 3-5 Phases cho dự án
- Quá nhiều phases = plan quá chi tiết
- Phase nên từ 3-7 ngày

### 3. Tasks trong Phase
- Max 5-10 tasks mỗi phase
- Mỗi task 2-5 phút để complete
- Mỗi task có verification cụ thể

---

## Template

```markdown
# [Project Name] - Implementation Plan

## Goal
[Một câu: Xây dựng gì?]

## Phases

### Phase 1: Foundation
**Goal:** [Kết quả của phase]
**Duration:** [X ngày]
**Status:** Not Started | In Progress | Complete

#### Tasks
- [ ] Task 1: [Action] → Verify: [Check]
- [ ] Task 2: [Action] → Verify: [Check]
- [ ] Task 3: [Action] → Verify: [Check]

### Phase 2: Core Features
**Goal:** [Kết quả của phase]
...

### Phase 3: Polish & Testing
**Goal:** [Kết quả của phase]
...

## Dependencies
- Phase 2 requires Phase 1 complete
- [Other dependencies]

## Done When
- [ ] [Success criteria 1]
- [ ] [Success criteria 2]
```

---

## Ví dụ: Todo App

### Phase 1: Setup & UI Base (3 ngày)
- [ ] Create project với Vite + React
- [ ] Setup Tailwind CSS
- [ ] Create Layout component
- [ ] Create TodoList component (static)

### Phase 2: Core CRUD (5 ngày)
- [ ] Add Todo functionality
- [ ] Display Todos
- [ ] Mark complete/incomplete
- [ ] Delete Todo
- [ ] Edit Todo

### Phase 3: Enhancements (3 ngày)
- [ ] Filter: All/Active/Completed
- [ ] Local Storage persistence
- [ ] Clear completed button

### Phase 4: Polish (2 ngày)
- [ ] Responsive design
- [ ] Animations
- [ ] Error handling
- [ ] Final testing

---

## Anti-patterns

| ❌ Sai | ✅ Đúng |
|--------|---------|
| 20 phases cho 1 project | 3-5 phases max |
| Phase chỉ có 1 task | Combine vào phase khác |
| Tasks không có verify | Mỗi task có cách check |
| Phase kéo dài 2 tuần | Chia nhỏ hơn |
