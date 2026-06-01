# [2605.31433v1] SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks

## Problem
Self-play can train language models without external supervision. But existing methods require rule-checkable answers, leaving open-ended tasks dependent on curated prompts or frontier-model judges. Prior work has no data-free self-play framework for open-ended tasks.

## Contribution
1. **SCOPE framework**: Data-free self-play for open-ended tasks. Co-evolves 2 policies: Challenger (generates document-grounded tasks) and Solver (answers via multi-turn retrieval).
2. **Self-judge with rubrics**: Frozen copy of initial model as self-judge, writes task-specific rubrics from source document, grades Solver responses.
3. **Results**: +10.4 points on 8 benchmarks, matches/exceeds GRPO_data on ~9K curated prompts. Also improves held-out short-form QA by +13.8 points.

## Method (core summary)
SCOPE: (1) Challenger generates document-grounded tasks from source documents; (2) Solver answers tasks via multi-turn retrieval; (3) Frozen self-judge writes task-specific rubrics from source document, grades Solver responses against rubrics; (4) Co-evolve: update Challenger based on Solver performance, keep tasks near Solver's frontier. Quality gates filter ill-formed tasks. Iterative: 3 iterations improve progressively.

## Key Findings
- Qwen2.5-7B: baseline 24.4 → SCOPE iter3 34.9 (+10.5 points)
- GRPO_data (9K curated): 33.4 → SCOPE iter3 34.9 (match/exceed)
- Qwen3-8B: +10.4 points improvement
- OLMo-3: +5.4 points
- Held-out short-form QA: +13.8 points improvement (transfer beyond training domain)
- Co-evolution necessary: frozen Challenger fails to propose learning-value tasks
- Rubric generation quality is bottleneck, not grading capacity

## Actionable Insights
1. **Data-free self-play for open-ended tasks**: When lacking curated training data, use self-play with co-evolving policies. Challenger generates tasks, Solver answers, self-judge evaluates. Example: train AI customer service — Challenger generates customer questions from product docs, Solver answers, self-judge evaluates quality.

2. **Rubrics from source documents**: Self-judge writes rubrics from source documents — task-specific, grounded. No human-written rubrics needed. Example: when training AI report writer, self-judge creates rubrics from source data: "Does response include Q3 revenue? Does response cite source?"

3. **Co-evolution is necessary**: Frozen Challenger doesn't adapt → tasks have no learning value. Must update Challenger based on Solver performance. Example: when training AI tutor, if student improves → increase task difficulty. Frozen difficulty = no learning.

## Assumptions & Limitations
**Conditions for method to work:**
- Source documents available for task generation
- Models 7-8B — larger scale unclear
- Multi-stage pipeline needs more compute than single-stage GRPO

**Limitations the paper acknowledges:**
- Compute overhead: multi-stage pipeline > single-stage GRPO
- Limited to 7-8B models — larger scales untested
- Self-play targets post-data regime

**Limitations the paper does NOT mention:**
- Rubric generation quality bottleneck — no solution proposed
- Content safety risk: Challenger may generate harmful tasks
- 3 iterations arbitrary — optimal iteration count unclear
- Domain transfer not deeply addressed
- Quality gates don't screen harmful content explicitly

## Metadata
- Year: 2026
- Authors: Wai-Chung Kwan, Aryo Pradipta Gema, Joshua Ong Jun Leang, Pasquale Minervini
- Category: cs.CL
- PDF: https://arxiv.org/pdf/2605.31433v1
- Citation count: [EXTRACTION FAILED]
