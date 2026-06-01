# [2510.13920] FACTS: Tóm tắt Bảng qua Tạo Template Offline với Quy trình Tác nhân

## Vấn đề
Query-focused table summarization (tóm tắt bảng theo truy vấn) cần generate natural language summaries từ tabular data (dữ liệu bảng) conditioned on user query. Existing approaches: table-to-text models cần costly fine-tuning; prompt-based LLM methods suffer token-limit và efficiency issues, expose sensitive data; prior agentic pipelines lack robustness và scalability.

## Đóng góp
1. **FACTS framework**: Fast, Accurate, Privacy-Compliant Table Summarization qua Offline Template Generation
2. **Offline templates**: SQL queries + Jinja2 templates — reusable across multiple tables với same schema
3. **Privacy compliance**: Chỉ gửi table schemas cho LLMs, không expose data

## Phương pháp (tóm tắt cốt lõi)
FACTS: (1) Schema-guided specifications — analyze table schema; (2) SQL synthesis — generate executable SQL queries cho data extraction; (3) Jinja2 rendering — create natural language templates; (4) LLM Council — iterative validation với multiple LLMs. Templates reusable: generate once, use across tables với same schema.

## Kết quả chính
- Consistently outperforms baselines trên FeTaQA, QTSumm, QFMTS benchmarks
- Outperforms prompt-based: CoT, ReFactor, DirectSumm
- Outperforms agentic: Binder, Dater, TaPERA
- Competitive with SPaGe, outperforms on most metrics
- GPT-Only variant competitive — core workflow effective without cross-model diversity
- Reusable templates: fast summarization
- Privacy: only schemas sent to LLMs

## Insight có thể áp dụng ngay
1. **Offline templates cho repeated queries**: Generate templates once, reuse across tables. Ví dụ: khi generate weekly reports từ database, create SQL + template once → reuse every week, chỉ update data.

2. **Privacy compliance**: Chỉ send table schemas cho LLM, không expose raw data. Ví dụ: khi build analytics chatbot for sensitive data, use FACTS — LLM chỉ see schema, SQL executes locally.

3. **Executable SQL = accuracy**: SQL queries ground summaries trong actual data. Ví dụ: khi generate financial summaries, use executable SQL thay vì free-form generation — fewer hallucinations.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Structured tabular data
- SQL-executable databases
- Jinja2 templates support

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- Schema complexity limits
- SQL generation accuracy
- Template maintenance overhead
- Multi-table joins complexity

## Metadata
- Năm: 2025
- Tác giả: Ye Yuan, Mohammad Amin Shabani, Siqi Liu
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2510.13920
- Citation count: [EXTRACTION FAILED]
