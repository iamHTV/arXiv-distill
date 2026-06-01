# Skill: FACTS — Table Summarization with Offline Templates
Source: 2510.13920
Type: workflow

## When to use this skill
- When generating natural language summaries from tabular data
- When needing reusable templates for repeated queries
- When privacy compliance is required

## When NOT to use
- Unstructured data
- No SQL database available
- One-off summaries (no reuse needed)

## Required inputs
- Table schema
- SQL-executable database
- User queries to answer
- Jinja2 template support

## Steps

### Step 1 — Analyze Schema
1. Parse table schema: columns, types, relationships
2. Identify key fields for summarization
3. Output: schema specification

### Step 2 — Generate SQL + Template
1. Generate executable SQL queries for data extraction
2. Create Jinja2 templates for natural language rendering
3. LLM Council validates templates
4. Output: reusable offline templates

### Step 3 — Execute & Render
1. Execute SQL on database
2. Render results through Jinja2 templates
3. Generate natural language summary
4. Output: query-focused summary

### Step 4 — Reuse
1. Same schema + different data → reuse templates
2. Update SQL if schema changes
3. Output: fast repeated summarization

## Expected output
- Accurate, privacy-compliant summaries
- Reusable templates for repeated queries
- Fast summarization (templates pre-generated)

## Example application
**Scenario**: Weekly sales report from database.

**Application**:
1. Schema: sales table (date, product, revenue, region)
2. Template: "Total revenue for {{region}} was {{revenue}} in {{period}}"
3. SQL: SELECT region, SUM(revenue) FROM sales WHERE date BETWEEN...
4. Execute weekly: only data changes, template reusable
5. Result: fast, accurate, privacy-compliant reports

## Gotchas
1. **Templates reusable**: Generate once, use across tables with same schema
2. **Privacy**: Only schemas sent to LLM, not raw data
3. **Executable SQL**: Grounds summaries in actual data, fewer hallucinations
4. **Schema changes**: Need to regenerate templates if schema changes
5. **Multi-table joins**: Complex queries may need more sophisticated templates
