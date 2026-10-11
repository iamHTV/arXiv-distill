# 2506.00549 MSumBench: Towards Multi-dimensional Evaluation of LLM Summarization

## Problem

Existing summarization benchmarks lack domain-specific assessment criteria, are predominantly English-centric, and face human annotation challenges due to reasoning complexity. LLM-generated summaries still face hallucinations, omission of critical information, and redundancy. No benchmark evaluates summarization across multiple domains + multiple languages + domain-specific criteria simultaneously.

## Contribution

1. MSumBench — multi-dimensional, multi-domain benchmark for summarization in English and Chinese, with specialized assessment criteria per domain.
2. Multi-agent debate annotation framework — 3 LLM agents (Advocate, Skeptic, Adjudicator) create structured arguments with contrasting viewpoints, reducing annotator dependence on single viewpoints.
3. Discovery: systematic bias in LLM evaluation — LLMs systematically rate self-generated summaries higher.

## Method (core summary)

(1) Multi-domain documents with domain-specific key-fact categories; (2) Bilingual: English and Chinese; (3) Multi-agent debate: Advocate argues for quality, Skeptic argues against, Adjudicator finalizes; (4) Human annotation: scores on faithfulness, completeness, conciseness (%); (5) LLM-as-evaluator: test 8 models, analyze correlation with human judgment.

## Key Findings

- 8 models evaluated, distinct patterns across domains/languages
- Multi-agent debate improves annotation quality
- Domain-specific criteria essential
- Systematic bias: LLMs rate self-generated summaries higher
- LLM evaluator correlation varies by domain

## Actionable Insights

1. Don't use single metric (ROUGE, BERTScore) — need domain-specific criteria. Example: medical summaries need "captured all contraindications?"
2. LLM-as-evaluator has self-bias — don't use same model to generate and evaluate. Example: if GPT-4 generates, use Claude to evaluate.
3. Multi-agent debate improves annotation quality — applicable to any evaluation task. Example: code review — Agent A argues clean, Agent B finds issues, Agent C adjudicates.

## Assumptions & Limitations

- Assumption: debate produces higher quality annotations — depends on LLM capability
- Limitation: English and Chinese only
- Limitation: Domain coverage limited
- Limitation: Human annotation still needed
- Limitation (observed): Self-bias only tested on summarization

## Metadata

- Year: 2026
- Authors: Hyangsuk Min, Yuho Lee, Minjeong Ban, Jiaqi Deng, Nicole Hee-Yeon Kim, Taewon Yun, Hang Su, Jason Cai, Hwanjun Song
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2506.00549
- Citation count: N/A
- Classification: [applied]
- Skill: multi-agent-debate-annotation
