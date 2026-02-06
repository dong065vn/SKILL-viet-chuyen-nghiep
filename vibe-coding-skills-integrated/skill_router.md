# Skill Router - Quy Tắc Điều Tiết

## Khi nào dùng skill nào?

### 🎯 Planning Phase
```
/flow → mermaid-expert
/erd  → database-design, mermaid-expert
/brain → brainstorming
```

### 🔧 Development Phase
```
/setup  → nodejs-patterns, docker-expert
/prisma → prisma-expert
/api    → api-patterns
```

### 🔐 Auth Phase
```
/auth   → auth-patterns
/google → auth-patterns (OAuth2)
/clerk  → clerk-auth
```

### ✅ Testing Phase
```
/test → testing-patterns
/tdd  → testing-patterns
```

### 💅 Polish Phase
```
/ui  → ui-ux-expert, frontend-design
/css → frontend-design
```

### 📦 Release Phase
```
/save   → git-workflows
/check  → git-workflows
/deploy → deployment
```

## Priority Rules

1. **Luôn bắt đầu với** `/brain` hoặc `/flow`
2. **Không skip** testing phase
3. **Checkpoint sau mỗi phase** với `/check`
4. **UI polish** chỉ sau khi code hoạt động
5. **Deploy** chỉ sau khi test pass
