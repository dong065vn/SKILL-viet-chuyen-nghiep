# Vibe Coding Pro Max - Setup Instructions

## Giới thiệu

**Vibe Coding Pro Max** là bộ skill vibe coding tốt nhất, kết hợp từ 2 bộ skill:
- **vibe-coding-skills-integrated** (23 workflows + 6 skills chuyên sâu)
- **vibe-coding-workspace** (7 skills methodology-driven + 5 agents + knowledge_base)
- **Nâng cấp** UI/UX skill với `ui-ux-pro-max` search engine (50+ styles, 97 palettes, 57 fonts)

```
Brainstorm → PRD → Plan → Code → Test → Debug → Fix → Verify → UI → Deploy
```

---

## Cấu trúc Workspace

```
vibe-coding-pro-max/
├── .agent/
│   └── workflows/            # 27 workflow commands
├── .antigravity/
│   ├── agents/               # 5 AI Agents
│   ├── skills/               # 13+ Skills (merged best of both)
│   │   ├── api/              # API & Testing patterns
│   │   ├── auth/             # Authentication patterns
│   │   ├── backend/          # Node.js backend patterns
│   │   ├── brainstorm/       # Brainstorm methodology (7 bước)
│   │   ├── coding/           # Batch-based coding execution
│   │   ├── debugging/        # Systematic debugging (4 phases)
│   │   ├── planning/         # Planning + Database design
│   │   ├── prd_writer/       # PRD writing (RICE prioritization)
│   │   ├── testing/          # TDD (Red-Green-Refactor)
│   │   ├── uiux/             # UI/UX Pro Max (search engine)
│   │   └── verify/           # Evidence-first verification
│   └── knowledge_base/       # Templates & Guides
├── setup_instruction.md       # File này
├── shortcut_guide.md          # Quick reference
└── skill_router.md            # Routing rules
```

---

## Cách sử dụng

### 1. Copy vào project
```
Copy folder `.agent/workflows/` và `.antigravity/` vào project của bạn.
```

### 2. Sử dụng Shortcuts
Gõ `/command` để kích hoạt workflow tương ứng.

### 3. Gọi Agents
```
@Brainstormer /brainstorm [yêu cầu]
@Product_Manager /prd [context]
@Planner /plan [PRD]
@Developer /code [phase]
@QA_Engineer /test [scope]
```

---

## Danh sách 27 Commands

### 🎯 Planning
| Command | Description |
|---------|-------------|
| `/brain` | Brainstorm & thu thập requirements (MoSCoW) |
| `/prd` | Viết PRD (Problem → Solution → User Stories → Metrics) |
| `/flow` | Vẽ Flowchart bằng Mermaid |
| `/erd` | Thiết kế Database Schema + indexing strategy |

### 🔧 Development
| Command | Description |
|---------|-------------|
| `/setup` | Setup Backend (Node.js + Docker + project structure) |
| `/prisma` | Tạo Prisma Schema + Migration |
| `/docker` | Docker containerization (multi-stage build) |
| `/api` | Tạo CRUD API + validation + error handling |
| `/postman` | Generate Postman collection + test scripts |
| `/code` | Coding theo batches, report progress |

### 🔐 Auth
| Command | Description |
|---------|-------------|
| `/auth` | Setup Authentication (JWT/Session/OAuth) |
| `/google` | Google OAuth integration |
| `/clerk` | Clerk authentication integration |

### 🧪 Testing
| Command | Description |
|---------|-------------|
| `/test` | Viết và chạy tests (unit/integration/e2e) |
| `/tdd` | TDD workflow (red-green-refactor) |

### 🐛 Debug/Fix
| Command | Description |
|---------|-------------|
| `/debug` | Debug có hệ thống (4 pha: Phân tích → Root Cause → Fix → Verify) |
| `/fix` | Fix review - Xác minh fix đúng root cause, không tạo bug mới |

### 🎨 UI/UX (NÂNG CẤP - Pro Max)
| Command | Description |
|---------|-------------|
| `/ui` | **UI/UX Pro Max** - Design intelligence với search engine (50+ styles, 97 palettes) |
| `/css` | Tailwind CSS (design system, dark mode) |

### 📦 Release
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

## Quy trình làm việc

```
/brain → /prd → /flow → /erd → /setup → /prisma → /api → /auth → /code → /test
                                                                          ↓
                                                                 có lỗi? → /debug → /fix
                                                                          ↓
                                                      /ui → /css → /verify → /check → /save → /deploy
```

### Khi gặp lỗi:
1. `/debug` - Phân tích lỗi, tìm root cause
2. Sửa code theo đề xuất
3. `/fix` - Verify fix đúng, không tạo bug mới
4. `/check` - Checkpoint trước khi tiếp tục

---

## UI/UX Pro Max (Prerequisites)

Skill `/ui` sử dụng Python search engine. Đảm bảo Python đã cài:

```bash
python3 --version || python --version
```

Nếu chưa có:
- **Windows:** `winget install Python.Python.3.12`
- **macOS:** `brew install python3`
- **Ubuntu:** `sudo apt install python3`
