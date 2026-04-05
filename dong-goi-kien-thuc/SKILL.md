---
name: dong-goi-kien-thuc
description: Chuyên gia đóng gói kiến thức, quy trình, và tài liệu thành Skill chuẩn Antigravity. Áp dụng khung tư duy IPO, phương pháp tương tác Vibe Working, và mô hình phát triển KWSR để tạo ra các Skill thực chiến, linh hoạt, có thể tái sử dụng cho mọi ngành nghề.
---

# 🧠 Skill: Đóng Gói Kiến Thức (Knowledge Packager)

## Mục đích

Hỗ trợ người dùng **đóng gói** kiến thức chuyên môn, quy trình làm việc, hoặc tài liệu tham khảo thành một **Skill chuẩn Antigravity** — có cấu trúc rõ ràng, có thể tái sử dụng, và sẵn sàng triển khai cho AI Agent.

Skill này giải quyết bài toán cốt lõi: **"Làm sao chuyển đổi tri thức ngầm (tacit knowledge) trong đầu chuyên gia hoặc trong tài liệu thành năng lực có hệ thống cho AI Agent?"**

## Khi nào sử dụng Skill này

- Người dùng muốn đóng gói kiến thức chuyên môn thành Skill tái sử dụng
- Người dùng có tài liệu (PDF, TXT, MD, DOCX) và muốn chuyển thành Skill
- Người dùng muốn chuẩn hóa quy trình làm việc thành Workflow rồi nâng cấp thành Skill
- Người dùng cung cấp file cấu trúc/template để đóng gói theo yêu cầu riêng
- Người dùng muốn tạo Skill cho một domain/ngành nghề cụ thể

## Nền tảng phương pháp luận

### IPO — Phương pháp Tư duy

Mọi quá trình đóng gói kiến thức đều tuân theo khung IPO:

| Thành phần | Vai trò trong đóng gói | Chi tiết |
|------------|----------------------|----------|
| **Input** | Nguyên liệu đầu vào | Tài liệu gốc, file kiến thức, yêu cầu người dùng, template (nếu có) |
| **Process** | Logic xử lý và chuyển đổi | Phân tích → Trích xuất → Cấu trúc hóa → Đóng gói → Review |
| **Output** | Skill hoàn chỉnh | SKILL.md + examples/ + templates/ (nếu cần) |

### Vibe Working — Phương pháp Tương tác

- **Kiến trúc 2 cấp:** Skill tạo ra có thể đặt ở Global (`~/.gemini/antigravity/skills/`) hoặc Workspace (`.agent/skills/`)
- **Luồng dữ liệu một chiều:** Input (tài liệu gốc) → Process (phân tích, chuyển đổi) → Output (Skill hoàn chỉnh)
- **Review trước triển khai:** LUÔN LUÔN gửi bản nháp Skill cho người dùng review trước khi đóng gói chính thức

### KWSR — Phương pháp Phát triển

Skill này tự bản thân là minh chứng cho mô hình KWSR:
- **Knowledge:** Thu thập, phân tích tài liệu và kiến thức đầu vào
- **Workflow:** Tuân theo quy trình đóng gói 6 bước chuẩn
- **Skill:** Đảm bảo chất lượng chuyên môn trong mỗi Skill tạo ra
- **Rule:** Tuân thủ các quy tắc an toàn và chuẩn mực đầu ra

---

## QUY TRÌNH ĐÓNG GÓI — 6 BƯỚC

### Bước 1: Thu thập & Phân tích đầu vào (INPUT)

**Hỏi người dùng các câu hỏi sau:**

1. **Nguồn kiến thức là gì?**
   - [ ] Tài liệu có sẵn (file PDF, TXT, MD, DOCX, v.v.)
   - [ ] Kiến thức trong đầu (mô tả bằng lời)
   - [ ] Quy trình làm việc đang dùng (SOP hiện tại)
   - [ ] Kết hợp nhiều nguồn

2. **Skill này phục vụ mục đích gì?**
   - Tóm tắt trong 1-2 câu mục tiêu chính

3. **Đối tượng sử dụng Skill là ai?**
   - Cá nhân / Team / Toàn tổ chức

4. **Phạm vi áp dụng?**
   - Global (mọi dự án) hay Workspace (dự án cụ thể)

5. **Có file template/cấu trúc riêng không?**
   - [ ] Có → Người dùng cung cấp file template
   - [ ] Không → Sử dụng cấu trúc chuẩn Antigravity

**Xử lý đầu vào:**
- Nếu người dùng cung cấp **file tài liệu** → Đọc toàn bộ, trích xuất nội dung cốt lõi
- Nếu người dùng cung cấp **file template** → Đọc cấu trúc template, áp dụng làm khung
- Nếu người dùng **mô tả bằng lời** → Đặt câu hỏi làm rõ cho đến khi đủ chi tiết

### Bước 2: Xác định cấu trúc Skill (PROCESS)

**Dựa trên đầu vào, xác định:**

| Thành phần | Quyết định |
|------------|-----------|
| **Tên Skill** | kebab-case, ngắn gọn, mô tả rõ chức năng |
| **Loại Skill** | Chuyên môn kỹ thuật / Quy trình nghiệp vụ / Sáng tạo nội dung / Phân tích dữ liệu |
| **Phạm vi** | Global / Workspace |
| **Cấu trúc thư mục** | SKILL.md + thư mục phụ cần thiết |
| **Cơ chế kích hoạt** | Mô tả ngắn trong YAML header để Agent tự nhận diện |

**Cấu trúc thư mục chuẩn:**

```
[tên-skill]/
├── SKILL.md              ← File chính (BẮT BUỘC)
├── examples/             ← Ví dụ mẫu (few-shot examples)
│   ├── example_input.md
│   └── example_output.md
└── templates/            ← Template đầu ra (nếu cần)
    └── output_template.md
```

### Bước 3: Soạn thảo bản nháp SKILL.md (PROCESS)

**Cấu trúc SKILL.md chuẩn:**

```markdown
---
name: [tên-skill-kebab-case]
description: [Mô tả ngắn 1-2 câu, viết ở ngôi thứ ba]
---

# [Tên Skill đầy đủ]

## Mục đích
[Mô tả rõ ràng Skill này giải quyết vấn đề gì]

## Phạm vi Ứng dụng
- [Tình huống 1]
- [Tình huống 2]
- [Tình huống 3]

## Bộ Nguyên tắc Cốt lõi
1. [Nguyên tắc 1]
2. [Nguyên tắc 2]
3. [Nguyên tắc 3]

## Quy trình Thực hiện
1. **[Bước 1]:** [Chi tiết]
2. **[Bước 2]:** [Chi tiết]
3. **[Bước 3]:** [Chi tiết]

## Ví dụ Mẫu (Few-shot)
### Input mẫu
[Ví dụ đầu vào]

### Output mẫu
[Ví dụ đầu ra kỳ vọng]

## Điều kiện & Ngoại lệ
- [Trường hợp đặc biệt cần xử lý]
- [Giới hạn của Skill]
```

**Nguyên tắc soạn thảo:**
- Mỗi phần phải **cụ thể và có thể hành động** — không viết chung chung
- Cung cấp **ít nhất 1 ví dụ mẫu** (few-shot) cho Input → Output
- Nội dung trung thực theo tài liệu gốc — **KHÔNG bịa đặt, thêm bớt**
- Sử dụng **ngôn ngữ phù hợp** với đối tượng sử dụng Skill
- Giữ SKILL.md dưới **2000 từ** — nội dung chi tiết chuyển vào thư mục phụ

### Bước 4: GỬI REVIEW (BẮT BUỘC — KHÔNG ĐƯỢC BỎ QUA)

> ⚠️ **QUY TẮC VÀNG:** LUÔN LUÔN gửi bản nháp SKILL.md cho người dùng review TRƯỚC KHI triển khai đóng gói. KHÔNG BAO GIỜ tự ý tạo file chính thức mà chưa được chấp nhận.

**Quy trình Review:**

1. **Xuất bản nháp** — Hiển thị toàn bộ nội dung SKILL.md dự kiến cho người dùng
2. **Yêu cầu phản hồi** — Hỏi người dùng:
   - "Nội dung có chính xác không?"
   - "Có cần bổ sung hoặc chỉnh sửa gì không?"
   - "Cấu trúc có phù hợp với yêu cầu không?"
3. **Xử lý phản hồi:**
   - Nếu **CHẤP NHẬN** → Chuyển sang Bước 5
   - Nếu **YÊU CẦU SỬA** → Chỉnh sửa theo phản hồi → Gửi review lại
   - Nếu **TỪ CHỐI** → Quay lại Bước 1 hoặc Bước 2

### Bước 5: Đóng gói chính thức (OUTPUT)

**Chỉ thực hiện SAU KHI người dùng đã CHẤP NHẬN bản review.**

1. **Tạo cấu trúc thư mục:**
   ```
   [phạm-vi]/skills/[tên-skill]/
   ├── SKILL.md
   ├── examples/
   └── templates/
   ```

2. **Ghi file SKILL.md** với nội dung đã được review và chấp nhận

3. **Tạo file examples** (nếu có ví dụ mẫu)

4. **Tạo file templates** (nếu có template đầu ra)

**Vị trí lưu trữ:**
- **Global:** `~/.gemini/antigravity/skills/[tên-skill]/`
- **Workspace:** `[project]/.agent/skills/[tên-skill]/`

### Bước 6: Xác nhận & Hướng dẫn sử dụng

Sau khi đóng gói xong, thông báo:

```
✅ Skill "[tên-skill]" đã được đóng gói thành công!

📁 Vị trí: [đường dẫn]
📋 Cấu trúc:
   ├── SKILL.md ([số từ] từ)
   ├── examples/ ([số file] file)
   └── templates/ ([số file] file)

🚀 Cách sử dụng:
   - Agent sẽ tự động kích hoạt khi nhận diện yêu cầu phù hợp
   - Hoặc gọi trực tiếp: "Sử dụng skill [tên-skill] để..."

💡 Lưu ý:
   - Cập nhật Skill khi kiến thức thay đổi
   - Bổ sung thêm examples khi có case mới
   - Chia sẻ với team bằng cách copy thư mục Skill
```

---

## CÁC CHẾ ĐỘ ĐÓNG GÓI

### Chế độ 1: Đóng gói từ Tài liệu

**Khi người dùng cung cấp file tài liệu:**
1. Đọc toàn bộ file → Phân loại nội dung (kiến thức, quy trình, quy tắc)
2. Trích xuất thông tin cốt lõi, loại bỏ nội dung thừa
3. Cấu trúc hóa theo format SKILL.md chuẩn
4. Tạo ví dụ mẫu từ case thực tế trong tài liệu (nếu có)
5. Gửi review → Đóng gói

### Chế độ 2: Đóng gói từ Mô tả

**Khi người dùng mô tả bằng lời:**
1. Đặt câu hỏi chi tiết để làm rõ kiến thức
2. Ghi nhận nguyên tắc, quy trình, ví dụ từ người dùng
3. Tổng hợp thành format SKILL.md chuẩn
4. Gửi review → Đóng gói

### Chế độ 3: Đóng gói theo Template

**Khi người dùng cung cấp file cấu trúc/template riêng:**
1. Đọc file template → Hiểu cấu trúc yêu cầu
2. Thu thập nội dung từ người dùng (tài liệu hoặc mô tả)
3. Đổ nội dung vào cấu trúc template
4. Bổ sung thông tin thiếu (nếu template yêu cầu)
5. Gửi review → Đóng gói

### Chế độ 4: Nâng cấp Workflow thành Skill

**Khi người dùng muốn nâng cấp Workflow hiện có:**
1. Đọc file Workflow hiện tại
2. Phân tích: bước nào cần nâng cao chất lượng?
3. Bổ sung nguyên tắc cốt lõi, tiêu chuẩn chất lượng, ví dụ mẫu
4. Chuyển đổi format từ Workflow → Skill
5. Gửi review → Đóng gói

---

## QUY TẮC AN TOÀN (RULES)

1. **KHÔNG BAO GIỜ** đóng gói chính thức mà chưa qua review của người dùng
2. **KHÔNG bịa đặt** nội dung — chỉ sử dụng thông tin từ nguồn đầu vào
3. **KHÔNG ghi đè** file Skill đã tồn tại mà không xin phép
4. **BẢO TOÀN** file gốc — không sửa đổi tài liệu nguồn
5. **THÔNG BÁO** rõ ràng khi phát hiện nội dung mâu thuẫn hoặc thiếu
6. **GHI RÕ** nguồn trích xuất khi đóng gói từ tài liệu

## Điều kiện & Giới hạn

- Skill phù hợp nhất với kiến thức có thể cấu trúc hóa được
- Kiến thức quá trừu tượng hoặc phụ thuộc nhiều ngữ cảnh → nên giữ ở dạng Knowledge thay vì Skill
- File đầu vào thuộc Nhóm 1 (TXT, CSV, MD, JSON) cho kết quả tốt nhất
- File Nhóm 2-3 (Excel, PDF, ảnh) cần kiểm tra kỹ sau khi trích xuất
