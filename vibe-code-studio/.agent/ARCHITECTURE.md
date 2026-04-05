# Thiết Kế Kiến Trúc: Antigravity Vibe Code Studio

> Cấu trúc hạ tầng Workspace theo nguyên lý Vibe Working (Luồng 1 chiều) và mô hình rèn luyện năng lực AI KWSR. 

---

## 🏗️ Bản Đồ Không Gian Làm Việc (Workspace Structure)

Antigravity Studio tuân thủ định dạng thư mục sau để đảm bảo tính minh bạch và tránh gây hại đến dữ liệu gốc. 

```plaintext
workspace/
├── .agent/                  # [CHỨA LOGIC & QUY TẮC]
│   ├── rules/               # Rule: Quy tắc cao nhất (Vibe Code Principles)
│   ├── workflows/           # Workflow: Quy trình thực chiến Slash Command
│   ├── skills/              # Skill: Kiến thức chuyên môn (React, DevOps)
│   ├── agents/              # Core Personas (20 Specialist Agents)
│   └── scripts/             # Kịch bản Validate kiểm tra chất lượng
├── 01_Inputs/               # [READ-ONLY] Dữ liệu người dùng cung cấp
├── 02_Process/              # [VÙNG NHÁP] AI tạo ra file script chạy thử, log lỗi
└── 03_Outputs/              # [THÀNH PHẨM] Mã nguồn đã duyệt, Report hoàn chỉnh
```

---

## ⚙️ Thứ Tự Ưu Tiên Triển Khai (Mô hình giải quyết xung đột)

Khi DONG (User) hoặc AI Agent xử lý lệnh, hệ thống áp dụng chuỗi ưu tiên từ cao xuống thấp như sau:

```
RULES (.agent/rules) [PHÁP LUẬT]
   ↓
   WORKFLOWS (.agent/workflows) [QUY TRÌNH BAO TRÙM]
      ↓
      SKILLS (.agent/skills) [CHUYÊN MÔN CỤ THỂ]
         ↓
         AGENTS (.agent/agents) [BẢN NĂNG CƠ BẢN]
```

Cụ thể:
- Bất kể Agent chuyên gia nào (Frontend, Backend) cũng phải tuân thủ nghiêm ngặt **Rules** (VD: Quy tắc *vibe_code_principles.md*). 
- Một **Workflow** có thể gọi ra nhiều **Skills**.

---

## 🤖 Agents & Skills Hiện Hữu (Kế Thừa)

Hệ thống vẫn giữ lại bộ lõi 20 Agent chuyên gia và 36 Skill chuyên sâu nhằm phục vụ việc code thực chiến mà không cần "train" lại từ đầu:

### Specialist Agents (Ví dụ)
- `frontend-specialist`: Gánh vác mảng Web UI/UX.
- `backend-specialist`: Gánh vác API, Logic.
- `orchestrator`: Gọi nhiều Agent cùng lúc để lập trình.
- `debugger`: Truy vết dòng code (Root cause analysis).

### Advanced Skills (Quản lý theo KWSR)
Tất cả các thư mục trong `skills/` nay tuân thủ thiết kế:
- `react-best-practices`: Dạy Agent tối ưu React.
- `database-design`: Schema, Prisma optimize.
- **[NEW META-SKILL] `dong-goi-vibe-skill`**: Giúp hệ thống đóng gói các thao tác thường làm của DONG thành một Skill mới (áp dụng bước cuối của tiến trình KWSR).

---

## 🔄 Vòng Đời Tri Thức (Knowledge Lifecycle)

Trình độ của AI trong Studio được tiến hóa theo chu kỳ do DONG làm chủ:

1. **Khám phá (Knowledge):** Auto-lưu lịch sử vào `.gemini/brain/`. AI tự nhớ context dự án.
2. **Quy trình hóa (Workflow):** Gom nhóm lệnh lại vào `.agent/workflows/`
3. **Chuyên môn hóa (Skill):** Gọi lệnh `/dong-goi-vibe-skill` để trích xuất tinh hoa thành chuẩn mực.
4. **Kiểm soát (Rule):** Nếu có rủi ro lớn (Xóa nhầm db), thiết lập ngay vào `.agent/rules/`.

## 📜 Mã Lệnh Xác Minh (Scripts Validation)

Thay vì phó mặc trực giác, bộ KIT sử dụng script validate chéo (ở mục 03_Outputs):
- `checklist.py`: Kiểm tra tĩnh (Lint, Types, Security, Schema).
- `verify_all.py`: Kiểm tra động (E2E, Lighthouse, Audit).
