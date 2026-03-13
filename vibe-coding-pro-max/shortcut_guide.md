# Shortcut Guide

## Quick Reference

### 🎯 Planning (Module 1)
| Command | Description |
|---------|-------------|
| `/brain` | Brainstorm ý tưởng, thu thập requirements (MoSCoW) |
| `/prd` | Viết PRD (Problem → Solution → User Stories → RICE) |
| `/flow` | Vẽ Flowchart bằng Mermaid (multi diagram types) |
| `/erd` | Thiết kế Database Schema/ERD + indexing strategy |

### 🔧 Backend (Module 2)
| Command | Description |
|---------|-------------|
| `/setup` | Setup Backend (Node.js + Docker + project structure) |
| `/prisma` | Tạo Prisma Schema + Migration + validation |
| `/docker` | Docker containerization (multi-stage build) |

### 🔌 API (Module 3)
| Command | Description |
|---------|-------------|
| `/api` | Tạo CRUD API + validation + error handling |
| `/postman` | Generate Postman collection + test scripts |
| `/code` | Coding theo batches, report progress |

### 🔐 Auth (Module 4)
| Command | Description |
|---------|-------------|
| `/auth` | Setup Authentication (JWT/Session/OAuth) |
| `/google` | Google OAuth integration |
| `/clerk` | Clerk authentication integration |

### 🧪 Testing (Module 5)
| Command | Description |
|---------|-------------|
| `/test` | Viết và chạy tests (unit/integration/e2e) |
| `/tdd` | TDD workflow (red-green-refactor) |

### 🐛 Debug/Fix (Module 6)
| Command | Description |
|---------|-------------|
| `/debug` | **Debug có hệ thống** - 4 pha: Phân tích → Root Cause → Fix → Verify |
| `/fix` | **Fix review** - Xác minh fix đúng root cause, không tạo bug mới |

### 🎨 UI/UX Pro Max (Module 7 - NÂNG CẤP)
| Command | Description |
|---------|-------------|
| `/ui` | **UI/UX Pro Max** - Design intelligence (50+ styles, 97 palettes, 57 fonts, 9+ stacks) |
| `/css` | Tailwind CSS (design system, dark mode) |

### 📦 Release (Module 8)
| Command | Description |
|---------|-------------|
| `/build` | Build production bundle + optimization |
| `/exe` | Đóng gói .exe (Electron/Inno Setup) |
| `/save` | Git commit + push (conventional commits) |
| `/check` | Checkpoint - verify trước khi tiếp tục |
| `/verify` | Xác minh hoàn thành (evidence before claims) |
| `/gh` | GitHub Actions CI/CD setup |
| `/deploy` | Deploy to cloud (rollback strategy) |
| `/compact` | Reset context, tạo snapshot cho phiên mới |

---

## ⚡ Typical Workflow

```
/brain → /prd → /flow → /erd → /setup → /prisma → /api → /auth → /code → /test
                                                                          ↓
                                                                 có lỗi? → /debug → /fix
                                                                          ↓
                                                     /ui → /css → /verify → /check → /save → /deploy
```

## 🐛 Debug Flow

```
Gặp lỗi → /debug (tìm root cause) → sửa code → /fix (verify fix) → /check (checkpoint)
```

## 🎨 UI/UX Pro Max Flow

```
/ui design [mô tả] → Generate Design System → Detailed Searches → Stack Guidelines → Polish → /verify
```

## 👥 Agents

| Agent | Role | Skill chính |
|-------|------|-------------|
| `@Brainstormer` | Thu thập yêu cầu | brainstorm |
| `@Product_Manager` | Viết PRD | prd_writer |
| `@Planner` | Lập kế hoạch | planning |
| `@Developer` | Coding | coding, testing |
| `@QA_Engineer` | Test & Debug | testing, debugging, verify |

---

## Tips

1. **Luôn bắt đầu với /brain** - Không skip bước này
2. **Confirm understanding** - Trả lời từng câu hỏi chi tiết
3. **Theo quy trình** - brain → prd → plan → code → test → verify
4. **Stop khi blocked** - Hỏi thay vì đoán
5. **Evidence before claims** - Luôn verify trước khi claim done
6. **UI luôn generate design system trước** - `/ui design [mô tả]`
