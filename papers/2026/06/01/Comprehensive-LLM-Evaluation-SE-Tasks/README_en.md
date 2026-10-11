# [2602.07079] Comprehensive Evaluation of LLMs on Software Engineering Tasks: A Multi-Task Benchmark

## Problem
LLMs have remarkable capabilities in software engineering, but comprehensive benchmarks covering diverse SE activities remain limited. Prior benchmarks focus on code correctness — missing efficiency metrics. Need to evaluate both quality and efficiency across multiple SE tasks.

## Contribution
1. **Multi-task evaluation**: 11 LLMs across 5 SE tasks: bug fixing, feature development, code refactoring, technical copywriting, research synthesis.
2. **Automated verification framework**: Measures output quality AND completion efficiency.
3. **Efficiency variance discovery**: 22× speed, 49× tool efficiency, 53× cost variation among models achieving identical perfect scores.

## Method (core summary)
Evaluates 11 frontier LLMs (GPT-5.1, Gemini-3 Pro, Deepseek-Chat, GLM-4.7, etc.) across 5 tasks. Automated verification: quality scores + completion time + tool calls + estimated cost. Statistical analysis: Pearson correlation, efficiency metrics. Releases all data + scripts for reproducibility.

## Key Findings
- 4 models achieved perfect scores: GPT-5.1, Gemini-3 Pro, Deepseek-Chat, GLM-4.7
- Efficiency variance: 22× speed (33s vs 732s), 49× tool calls (3.8 vs 188 avg), 53× cost
- No correlation between tool usage and success (r=0.077, p=0.575)
- GPT-5.1: 18.8s, 3 tools. Gemini-3 Flash: 625s, 917 tools — SAME SCORE
- Two inefficiency patterns: loop inefficiency (repeat tool sequences), inference inefficiency (slow correct solutions)
- Coding tasks: 100% success. Research tasks: 90.9%
- OpenAI models: consistently fastest (avg 54s), best speed-quality tradeoff

## Actionable Insights
1. **Efficiency > accuracy when choosing LLM**: Models with same accuracy have 49× tool efficiency difference. Choose based on efficiency, not just accuracy. Example: when deploying code assistant, compare models on tool calls + cost, not just task success.

2. **More tools ≠ better results**: Tool usage count doesn't correlate with success. Avoid models with loop inefficiency. Example: when monitoring AI agent, track tool call count — if >100 calls for simple task → loop inefficiency, consider switching model.

3. **Loop vs inference inefficiency**: Loop = agent repeats tool sequences without recognizing failure. Inference = model generates correct solutions slowly. Example: when debugging slow AI agent, identify type — loop needs stopping logic, inference needs faster model.

## Assumptions & Limitations
**Conditions for benchmark to work:**
- 5 SE tasks representative
- Automated verification accurate
- Cost estimation reliable

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- 5 tasks may not cover all SE activities
- Cost estimation may differ from real costs
- Model versions change rapidly
- Task complexity may vary

## Metadata
- Year: 2026
- Authors: Go Frendi Gunawan, Mukhlis Amien
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2602.07079
- Citation count: [EXTRACTION FAILED]
