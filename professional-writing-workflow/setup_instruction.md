# 📋 Setup Instruction — Professional Writing Workflow

## Cài đặt

### Bước 1: Copy vào workspace
Copy toàn bộ folder `professional-writing-workflow` vào workspace của bạn:

```
your-workspace/
├── .agent/
│   └── workflows/
│       ├── write.md          ← Workflow viết bài chính
│       └── research-write.md ← Workflow nghiên cứu + viết
├── shortcut_guide.md
├── skill_router.md
└── setup_instruction.md     ← File này
```

### Bước 2: Sử dụng
Mở terminal/chat trong workspace và gõ:
- `/write` — khi đã có đủ dữ liệu để viết
- `/research-write` — khi chỉ có ảnh/link/ý tưởng mỏng

## Yêu cầu

### Tools cần có
Workflows sử dụng các tools sau (đã tích hợp sẵn trong hầu hết AI coding assistants):

| Tool | Mục đích |
|------|---------|
| `search_web` | Tìm kiếm thông tin trên web |
| `read_url_content` | Đọc nội dung trang web |
| `view_file` | Đọc ảnh/file input |
| `write_to_file` | Lưu bài viết output |

### Không cần cài thêm
- Không cần API key
- Không cần Python/Node.js
- Không cần database

## Nguồn uy tín được tích hợp

Workflow tự động search trên **30+ nguồn** phân theo loại:

- **Học thuật**: Nature, Science, PubMed, Google Scholar, JSTOR, arXiv
- **Báo quốc tế**: Reuters, AP, BBC, The Guardian, SCMP, The Economist
- **Pháp luật VN**: thuvienphapluat.vn, vanban.chinhphu.vn, quochoi.vn
- **Báo VN**: VnExpress, Tuổi Trẻ, Thanh Niên, Tiền Phong, Dân Trí
- **Thống kê**: World Bank Data, UN Data, GSO, Statista, OWID
- **Chính sách QT**: WTO, IMF, ADB, OECD, WHO, UNESCO

## Chắt lọc từ

Bộ workflow này được tổng hợp từ các skills chất lượng cao:

| Nguồn | Kỹ thuật |
|-------|---------|
| `content-research-writer` (awesome-claude-skills) | Quy trình Outline → Research → Draft → Feedback |
| `copywriting` (antigravity-awesome-skills) | Phase-based workflow, Claim Discipline |
| `social-content` (antigravity-awesome-skills) | Hook Formulas, Facebook strategy |
| `content-creator` (antigravity-awesome-skills) | Content Pillars, Brand Voice |
| `deep-research` (antigravity-awesome-skills) | Autonomous web research |
| `content_frameworks` (antigravity-awesome-skills) | Thought Leadership, Case Study templates |
| `persuasion-principles` (antigravity-awesome-skills) | Authority + Commitment enforcement |
| `seo-content-writer` (antigravity-awesome-skills) | E-E-A-T signals |
