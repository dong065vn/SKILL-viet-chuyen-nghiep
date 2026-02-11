# Skill Router - Quy Tắc Điều Tiết

## Khi nào dùng skill nào?

### 🎯 Planning Phase
```
/brain → brainstorming, concise-planning, product-manager-toolkit
/flow  → mermaid-expert, brainstorming, docs-architect
/erd   → database-design, mermaid-expert, prisma-expert, sql-optimization-patterns
```

### 🔧 Development Phase
```
/setup  → nodejs-backend-patterns, docker-expert, environment-setup-guide
/prisma → prisma-expert, database-design, sql-optimization-patterns
/api    → api-patterns, api-design-principles, error-handling-patterns
/docker → docker-expert, backend-dev-guidelines
```

### 🔐 Auth Phase
```
/auth   → auth-patterns, error-handling-patterns, security-hardening
/google → auth-patterns, google-oauth-patterns
/clerk  → clerk-auth-patterns, nextjs-patterns
```

### 🧪 Testing Phase
```
/test → javascript-testing-patterns, testing-patterns
/tdd  → testing-patterns, tdd-orchestrator
```

### 🐛 Debug/Fix Phase (MỚI)
```
/debug → error-detective, debugging-strategies, debugger, error-handling-patterns
/fix   → fix-review, verification-before-completion, error-handling-patterns
```

### 🎨 Polish Phase
```
/ui  → ui-ux-pro-max, frontend-design, wcag-audit-patterns
/css → tailwind-design-system, tailwind-patterns, frontend-design
```

### 📦 Release Phase
```
/build   → build-optimization, performance-pro
/exe     → electron-patterns, desktop-app-builder
/save    → git-conventions, pre-commit-automation
/check   → verification-before-completion, git-conventions
/gh      → github-actions-expert, deployment-patterns
/deploy  → deployment-patterns, vercel-patterns, docker-expert
/postman → api-design-principles, docs-architect
```

---

## ⚡ Quy tắc ưu tiên

1. **Luôn bắt đầu với** `/brain` hoặc `/flow` (Planning trước)
2. **KHÔNG skip** Testing Phase (test trước khi deploy)
3. **Checkpoint** sau mỗi phase → `/check`
4. **Gặp lỗi?** → `/debug` trước, `/fix` sau khi fix xong
5. **Polish** UI last → `/ui` + `/css`
6. **Deploy** chỉ khi tests pass → `/deploy`

### 🐛 Khi nào dùng /debug vs /fix?

| Tình huống | Dùng |
|-----------|------|
| Gặp error, chưa biết nguyên nhân | `/debug` |
| Đã fix xong, cần verify | `/fix` |
| Bug phức tạp, nhiều layers | `/debug` → sửa → `/fix` |
| Review code sau khi sửa | `/fix review` |
