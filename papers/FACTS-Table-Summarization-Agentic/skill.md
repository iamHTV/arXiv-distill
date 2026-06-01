# Skill: FACTS — Tóm tắt Bảng với Template Offline
Nguồn: 2510.13920
Loại: workflow

## Khi nào dùng skill này
- Khi generate (tạo) natural language summaries từ tabular data
- Khi cần reusable templates cho repeated queries
- Khi privacy compliance (tuân thủ riêng tư) required

## KHÔNG nên dùng khi
- Unstructured data (không có cấu trúc)
- No SQL database available
- One-off summaries (không cần reuse)

## Input cần có
- Table schema (lược đồ bảng)
- SQL-executable database
- User queries cần answer
- Jinja2 template support

## Các bước thực hiện

### Bước 1 — Analyze Schema (phân tích lược đồ)
1. Parse table schema: columns, types, relationships
2. Identify key fields for summarization
3. Output: schema specification

### Bước 2 — Generate SQL + Template (tạo SQL + mẫu)
1. Generate executable SQL queries for data extraction
2. Create Jinja2 templates for natural language rendering
3. LLM Council validates templates
4. Output: reusable offline templates

### Bước 3 — Execute & Render (thực thi & hiển thị)
1. Execute SQL on database
2. Render results through Jinja2 templates
3. Generate natural language summary
4. Output: query-focused summary

### Step 4 — Reuse (tái sử dụng)
1. Same schema + different data → reuse templates
2. Update SQL if schema changes
3. Output: fast repeated summarization

## Output mong đợi
- Accurate, privacy-compliant summaries
- Reusable templates for repeated queries
- Fast summarization (templates pre-generated)

## Ví dụ áp dụng
**Tình huống**: Weekly sales report from database.

**Áp dụng**:
1. Schema: sales table (date, product, revenue, region)
2. Template: "Total revenue for {{region}} was {{revenue}} in {{period}}"
3. SQL: SELECT region, SUM(revenue) FROM sales WHERE date BETWEEN...
4. Execute weekly: only data changes, template reusable
5. Result: fast, accurate, privacy-compliant reports

## Lưu ý quan trọng
1. **Templates reusable**: Generate once, use across tables with same schema
2. **Privacy**: Only schemas sent to LLM, not raw data
3. **Executable SQL**: Grounds summaries in actual data, fewer hallucinations
4. **Schema changes**: Need to regenerate templates if schema changes
5. **Multi-table joins**: Complex queries may need more sophisticated templates
