# Academic Writing Skills - Command Reference

All skills produce output in Vietnamese with proper academic style for the research topic being analyzed.

## Available Skills

### 1. literature_review_table
**Purpose:** Create structured literature review tables for systematic knowledge organization

**Commands:**
```
@literature_review_table create [type: basic/detailed/concept] "research topic"
@literature_review_table add "document information"
@literature_review_table group_by "criteria"
@literature_review_table export [format: md/csv/docx]
```

**Example:**
```
@literature_review_table create detailed "Factors affecting online shopping decisions"
```

---

### 2. dan_bai
**Purpose:** Build academic outlines and content structure

**Commands:**
```
@dan_bai [type: essay/report/project/thesis] "topic"
```

**Example:**
```
@dan_bai thesis "The impact of AI on higher education"
```

---

### 3. brainstorm
**Purpose:** Requirements analysis and idea generation before writing

**Commands:**
```
@brainstorm "topic or requirement"
```

**Example:**
```
@brainstorm "I need to write about digital transformation in Vietnam"
```

---

### 4. bien_tap
**Purpose:** Systematic academic editing and polishing

**Commands:**
```
@bien_tap [type: content/format/citation/all] "file or content"
```

**Example:**
```
@bien_tap all "my essay draft"
```

---

### 5. nghien_cuu
**Purpose:** Research planning and academic literature review

**Commands:**
```
@nghien_cuu "keyword or research topic"
```

**Example:**
```
@nghien_cuu "các yếu tố ảnh hưởng đến sự hài lòng khách hàng"
```

---

### 6. phan_tich
**Purpose:** Academic problem analysis using deep, comparative, and critical methods

**Commands:**
```
@phan_tich [method: dao_sau/so_sanh/phan_bien] "issue to analyze"
```

**Examples:**
```
@phan_tich so_sanh "Phương pháp giáo dục truyền thống và hiện đại"
@phan_tich phan_bien "Hiệu quả chính sách đổi mới giáo dục"
@phan_tich dao_sau "Nguyên nhân thất bại của doanh nghiệp khởi nghiệp"
```

---

## Notes

- All skill outputs are in **Vietnamese** with proper academic formatting
- Skills follow Vietnamese academic standards (NCKH - Nghiên cứu Khoa học)
- All citations support APA and IEEE formats
- Outputs are structured for thesis, journal articles, and research papers

## Vibe Coding Pro Max Integration

For software development workflows, use the **vibe-coding** skill directory instead:

```
cd ~/.claude/skills/vibe-coding
```

This provides complete development workflows from ideation to deployment with systematic verification at each phase.