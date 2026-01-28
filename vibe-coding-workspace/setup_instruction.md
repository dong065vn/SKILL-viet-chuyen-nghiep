# Vibe Coding Workspace - Setup Instructions

## Giới thiệu

**Vibe Coding Workspace** là môi trường phát triển phần mềm có cấu trúc với quy trình hoàn chỉnh:

```
Brainstorm → PRD → Planning → Coding → Testing → Debugging → Verification
```

---

## Cấu trúc Workspace

```
vibe-coding-workspace/
├── .antigravity/
│   ├── agents/          # 5 AI Agents
│   ├── skills/          # 7 Skills
│   └── knowledge_base/  # Templates & Guides
├── .agent/
│   └── workflows/       # 7 Workflow shortcuts
├── shortcut_guide.md    # Hướng dẫn shortcuts
└── setup_instruction.md # File này
```

---

## Cách sử dụng

### 1. Mở workspace trong VS Code/Cursor
```
Mở folder: vibe-coding-workspace
```

### 2. Sử dụng Shortcuts
Gõ slash command để kích hoạt workflow:
- `/brainstorm` - Thu thập yêu cầu
- `/prd` - Viết PRD
- `/plan` - Lập kế hoạch
- `/code` - Coding
- `/test` - Testing
- `/debug` - Fix lỗi
- `/verify` - Xác minh

### 3. Gọi Agents
```
@Brainstormer /brainstorm [yêu cầu]
@Product_Manager /prd [context]
@Planner /plan [PRD]
@Developer /code [phase]
@QA_Engineer /test [scope]
```

---

## Quy trình làm việc

### Bước 1: Brainstorm
```
/brainstorm Tôi muốn làm app quản lý task
```
→ AI sẽ hỏi câu hỏi, xác nhận requirements

### Bước 2: PRD
```
/prd viết PRD từ brainstorm
```
→ Tạo PRD document đầy đủ

### Bước 3: Plan
```
/plan lập kế hoạch từ PRD
```
→ Tạo task_plan.md với phases và tasks

### Bước 4: Code
```
/code implement Phase 1
```
→ Coding theo batches, report progress

### Bước 5: Test
```
/test run tests
```
→ TDD workflow, fix failures

### Bước 6: Debug (nếu cần)
```
/debug [mô tả bug]
```
→ Systematic debugging

### Bước 7: Verify
```
/verify kiểm tra trước deploy
```
→ Verification checklist với evidence

---

## Tips

1. **Không skip brainstorm** - Đây là bước quan trọng nhất
2. **Answer questions carefully** - AI hỏi từng câu một
3. **Confirm understanding** - Trước khi tiếp tục phase mới
4. **Follow the plan** - Không tự ý thêm features
5. **Stop when blocked** - Hỏi thay vì đoán

---

## Tài liệu tham khảo

- `shortcut_guide.md` - Chi tiết tất cả shortcuts
- `.antigravity/knowledge_base/prd_template.md` - Template PRD
- `.antigravity/knowledge_base/project_phases.md` - Hướng dẫn chia phases
