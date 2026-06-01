# [2510.13920] FACTS: Table Summarization via Offline Template Generation with Agentic Workflows

## Problem
Query-focused table summarization needs to generate natural language summaries from tabular data conditioned on user query. Existing approaches: table-to-text models need costly fine-tuning; prompt-based LLM methods suffer token-limit and efficiency issues, expose sensitive data; prior agentic pipelines lack robustness and scalability.

## Contribution
1. **FACTS framework**: Fast, Accurate, Privacy-Compliant Table Summarization via Offline Template Generation.
2. **Offline templates**: SQL queries + Jinja2 templates — reusable across multiple tables with same schema.
3. **Privacy compliance**: Only table schemas sent to LLMs, data not exposed.

## Method (core summary)
FACTS: (1) Schema-guided specifications — analyze table schema; (2) SQL synthesis — generate executable SQL queries for data extraction; (3) Jinja2 rendering — create natural language templates; (4) LLM Council — iterative validation with multiple LLMs. Templates reusable: generate once, use across tables with same schema.

## Key Findings
- Consistently outperforms baselines on FeTaQA, QTSumm, QFMTS benchmarks
- Outperforms prompt-based: CoT, ReFactor, DirectSumm
- Outperforms agentic: Binder, Dater, TaPERA
- Competitive with SPaGe, outperforms on most metrics
- GPT-Only variant competitive — core workflow effective without cross-model diversity
- Reusable templates: fast summarization
- Privacy: only schemas sent to LLMs

## Actionable Insights
1. **Offline templates for repeated queries**: Generate templates once, reuse across tables. Example: when generating weekly reports from database, create SQL + template once → reuse every week, only update data.

2. **Privacy compliance**: Only send table schemas to LLM, don't expose raw data. Example: when building analytics chatbot for sensitive data, use FACTS — LLM only sees schema, SQL executes locally.

3. **Executable SQL = accuracy**: SQL queries ground summaries in actual data. Example: when generating financial summaries, use executable SQL instead of free-form generation — fewer hallucinations.

## Assumptions & Limitations
**Conditions for method to work:**
- Structured tabular data
- SQL-executable databases
- Jinja2 templates support

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- Schema complexity limits
- SQL generation accuracy
- Template maintenance overhead
- Multi-table joins complexity

## Metadata
- Year: 2025
- Authors: Ye Yuan, Mohammad Amin Shabani, Siqi Liu
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2510.13920
- Citation count: [EXTRACTION FAILED]
