---
name: literature_review_table
description: Academic literature review table generator for systematic knowledge organization. Creates structured literature review tables with thematic grouping and citation formatting.
---
## Purpose
1. **Systematic knowledge overview** - Group research by theme rather than author
2. **Research clustering** - Organize studies by approach/methods/results
3. **Knowledge gaps identification** - Highlight unexplored areas
4. **Writing support** - Work with EndNote for citation management

## Template
### Basic Template (10 columns)
| STT | Tác giả | Năm | Tiêu đề | Tạp chí | Số/Trang | Kết quả NC | Phương pháp NC | Mẫu | PP Phân tích |
|-----|---------|-----|---------|---------|----------|------------|----------------|-----|--------------|
| 1   |         |     |         |         |          |            |                |     |              |
| 2   |         |     |         |         |          |            |                |     |              |

**Column explanations:**
| Column | English | Description | Example |
|--------|---------|-------------|---------|
| STT | No | Sequential number | 1, 2, 3... |
| Tác giả | Authors | Author(s) name (Last, Year) | Nguyễn Văn A |
| Năm | Year | Publication year | 2022 |
| Tiêu đề | Title | Article title | "Factors affecting..." |
| Tạp chí | Journal | Publication journal | Child Abuse & Neglect |
| Số/Trang | Volume/Page | Journal volume/page | 131/105710 |
| Kết quả NC | Findings | Main findings | "Identified 4 key themes..." |
| Phương pháp NC | Research Methods | Research methodology | Quantification, structured interviews |
| Mẫu | Sample | Sample size and population | 25 MDT members |
| PP Phân tích | Method of data analysis | Analysis approach | Thematic analysis |

### Enhanced Template (14 columns) - Nguyễn Văn Thắng 2022
Additional columns to add to Basic Template:
| Added Column | English | Description |
|--------------|---------|-------------|
| Câu hỏi/Mục tiêu NC | Research Questions/Objectives | Specific research questions or objectives |
| Cơ sở lý thuyết | Theoretical Framework | Research framework/theoretical models |
| Hạn chế | Limitations | Study limitations and future research directions |
| Bình luận cá nhân | Personal Notes | Personal thoughts on application |

**Complete template:**
```markdown
| STT | Tác giả | Năm | Tiêu đề | Tạp chí | Số/Trang | Câu hỏi NC | Cơ sở lý thuyết | Phương pháp | Mẫu | PP Phân tích | Kết quả | Hạn chế | Ghi chú |
|-----|---------|-----|---------|---------|----------|-----------|------------------|--------------|-----|--------------|---------|---------|---------|
| 1   |         |     |         |         |          |           |                  |              |     |              |         |         |         |
```

## Workflow Instructions
### 1. Information Collection
- Read materials via Scanning → Skimming → Intensive Reading
- Fill literature review table with collected data

### 2. Coding Process
- Add "Mã" column for categorization
- Common coding criteria:
  - By **methodology**: Quantitative (DT), Qualitative (DL), Mixed (HH)
  - By **approach**: Identify research schools
  - By **results**: Positive/negative/neutral outcomes
  - By **population**: Students, businesses, civil servants...

### 3. Grouping & Sorting
- Use Excel's **Sort** function on "Mã" column
- Group studies with similar approaches together

### 4. Thematic Writing
- Write by sections, NOT by authors
- Use EndNote to cite multiple authors with shared perspectives

## Article Summary Format
```
Generally, we can group studies on [theme] into [N] clusters.
Cluster 1 approaches from perspective of [A], examining issues like [list]
Cluster 2 focuses on [B], emphasizing [content]. Core solutions include [list] (Author 4, year; Author 5, year).
Comparing clusters reveals [commonalities/differences]...
```

## Practical Examples
> Generally, literature on organizational learning and knowledge transfer can be grouped into three categories. **First cluster** analyzes from cognitive perspective examining issues like reception, distribution, innovation and knowledge storage (Huber, 1991). This cluster emphasizes content and institutional/institutional factors affecting knowledge updating (Grant, 1996; Spender, 1996; Cohen and Levinthal, 1990). Basic solutions include database establishment, training enhancement...
> *(From: Nguyễn Văn Thắng, 2022)*

## Export Formats
### Markdown Table
```markdown
| STT | Tác giả | Năm | Tiêu đề | ... |
|-----|---------|-----|---------|-----|
| 1   | ...     | ... | ...     | ... |
```

### CSV (for Excel)
```csv
STT,Tác giả,Năm,Tiêu đề,Tạp chí,Số/Trang,Kết quả,Phương pháp,Mẫu,PP Phân tích
1,Nguyễn A,2022,Tiêu đề bài,Tạp chí A,Vol1/p1-10,Kết quả...,Định lượng,200 SV,Hồi quy
```

## Usage Instructions
### Create new table
```
@literature_review_table tạo [type: cơ bản/chi tiết/khái niệm]
```

### Add document to table
```
@literature_review_table thêm [document information]
```

### Group documents
```
@literature_review_table phân_nhóm theo [criteria]
```

### Export table
```
@literature_review_table xuất [format: md/csv/docx]
```

## Usage Examples
```
@literature_review_table tạo chi_tiết cho đề tài "Các yếu tố ảnh hưởng đến quyết định mua hàng online"
```

## References
- Combine with skill `@nghien_cuu` for literature search
- Combine with skill `@trich_dan` for citation formatting
- Additional reference: [Literature Review Table Guide](../knowledge_base/literature_review_table/)