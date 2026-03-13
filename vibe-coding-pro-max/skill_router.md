# Skill Router - Quy Tắc Điều Tiết

## Khi nào dùng skill nào?

### 🎯 Planning Phase
```
/brain → brainstorm (workspace skill)
/prd   → prd_writer (workspace skill)
/flow  → mermaid-expert, brainstorming, docs-architect
/erd   → database-design (integrated skill), prisma-expert, sql-optimization-patterns
```

### 🔧 Development Phase
```
/setup  → nodejs-backend-patterns (integrated skill), docker-expert, environment-setup-guide
/prisma → prisma-expert, database-design, sql-optimization-patterns
/api    → api-patterns (integrated skill), api-design-principles, error-handling-patterns
/docker → docker-expert, backend-dev-guidelines
/code   → coding (workspace skill)
```

### 🔐 Auth Phase
```
/auth   → auth-patterns (integrated skill), error-handling-patterns, security-hardening
/google → auth-patterns, google-oauth-patterns
/clerk  → clerk-auth-patterns, nextjs-patterns
```

### 🧪 Testing Phase
```
/test → javascript-testing-patterns (integrated skill), testing (workspace skill)
/tdd  → testing (workspace skill - TDD discipline)
```

### 🐛 Debug/Fix Phase
```
/debug → debugging (workspace skill - 4 phases + 3-strike protocol)
/fix   → verify (workspace skill), error-handling-patterns
```

### 🎨 UI/UX Phase (NÂNG CẤP)
```
/ui  → ui-ux-pro-max (search engine + database), frontend-design, wcag-audit-patterns
/css → tailwind-design-system, tailwind-patterns, frontend-design
```

### 📦 Release Phase
```
/build   → build-optimization, performance-pro
/exe     → electron-patterns, desktop-app-builder
/save    → git-conventions, pre-commit-automation
/check   → verify (workspace skill), git-conventions
/verify  → verify (workspace skill)
/gh      → github-actions-expert, deployment-patterns
/deploy  → deployment-patterns, vercel-patterns, docker-expert
/postman → api-design-principles, docs-architect
/compact → (built-in context management)
```

---

## ⚡ Quy tắc ưu tiên

1. **Luôn bắt đầu với** `/brain` hoặc `/prd` (Planning trước)
2. **KHÔNG skip** Testing Phase (test trước khi deploy)
3. **Checkpoint** sau mỗi phase → `/check`
4. **Gặp lỗi?** → `/debug` trước, `/fix` sau khi fix xong
5. **Polish** UI last → `/ui` + `/css`
6. **Deploy** chỉ khi tests pass → `/deploy`
7. **UI luôn generate design system** trước khi code

### 🐛 Khi nào dùng /debug vs /fix vs /verify?

| Tình huống | Dùng |
|-----------|------|
| Gặp error, chưa biết nguyên nhân | `/debug` |
| Đã fix xong, cần verify fix đúng | `/fix` |
| Bug phức tạp, nhiều layers | `/debug` → sửa → `/fix` |
| Review code sau khi sửa | `/fix review` |
| Trước khi commit/deploy | `/verify` |
| Cần evidence trước khi claim done | `/verify` |

### 🎨 Khi nào dùng /ui?

| Tình huống | Command |
|-----------|---------|
| Bắt đầu UI mới | `/ui design [mô tả project]` |
| Làm đẹp component | `/ui [component name]` |
| Audit toàn bộ UI | `/ui audit` |
