---
description: Compact tiến trình làm việc và xuất context snapshot để reset context phiên realtime
---

# /compact - Compact Tiến trình

## Khi nào sử dụng
- Cần reset context window
- Chuyển sang phiên làm việc mới
- Context đã sử dụng quá nhiều

## Quy trình
1. Xác nhận với user
2. Đọc artifacts (task.md, implementation_plan.md, walkthrough.md)
3. Trích xuất completed tasks
4. Tạo context_snapshot.md
5. Hướng dẫn user copy để dùng phiên mới

## Cú pháp
```
/compact
```

## Ví dụ
```
/compact

/compact tổng hợp progress hiện tại

/compact xuất context để chuyển phiên mới
```

## Output
- `context_snapshot.md`:
  - Tóm tắt công việc đã hoàn thành
  - Trạng thái hiện tại (phase, status)
  - Completed tasks
  - Pending tasks (nếu có)
  - Quyết định quan trọng
  - Files đã tạo/sửa

## Context Snapshot Format
```markdown
# Context Snapshot - [Project]
Generated: [Timestamp]

## Tóm tắt đã hoàn thành
...

## Trạng thái hiện tại
- Phase: [X]
- Status: [Completed/In Progress]

## Tasks đã complete
[x] Task 1
[x] Task 2

## Tasks còn lại
[ ] Pending task

## Quyết định quan trọng
| Quyết định | Lý do |
|...        |...    |
```

## Tips
- **CHỈ chạy khi user xác nhận** - Không tự động
- Giữ ngắn gọn, chỉ thông tin cốt lõi
- Không xóa file gốc, chỉ tạo snapshot
- Copy nội dung snapshot để paste vào phiên mới
