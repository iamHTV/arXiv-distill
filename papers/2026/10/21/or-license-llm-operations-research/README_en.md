# 2610.24087 OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners

## Problem
- Existing OR (operations research) benchmarks start from self-contained problem descriptions or predefined tasks — they skip the hardest real-world step: translating original, incomplete client materials into professionally validated solutions.

## Contribution
- OR-License: an end-to-end benchmark of 31 instances across 10 industrial scenarios, drawn from paid OR engagements totaling $3.68M (fees $67.1k–$131.6k, mean duration 4.7 months, 2.16 experts).
- ORSim: a controlled client simulator that discloses business facts (max 3 non-brief facts per query) while withholding OR expertise.
- DAQ (Deployment-Adjusted Quality): zero credit for infeasible deliveries; DAQ = Feasibility × conditional quality.
- Hidden verifiers check feasibility; objective quality is independently recomputed from the agent's submitted decisions.

## Method
- The agent receives a de-identified brief + input files, may query ORSim throughout formulation, solving, and refinement, and must output executable decisions for every test case.
- 11 frontier LLMs evaluated with the Claude Code harness, 5 runs per model-task pair, tasks weighted equally; a Codex harness comparison is in the appendix.
- HCAEU chain analysis: Hypothesis → mechanistic explanation (C) → executed diagnostic experiment (A) → evidence interpretation (E) → evidence-grounded update (U).

## Key Findings
- Feasibility spans 43.23 percentage points: Hy3 45.16% → Grok 4.6 88.39%. Conditional quality spans only 4.09 points (96.92%–101.01%).
- Several models exceed the expert reference (100%) on conditional quality, but ALL fall below the expert on DAQ. Best: Grok 4.6 DAQ 86.55% — the 13.45-point gap decomposes into 11.61 points from infeasible deliveries + 1.84 from objective shortfall, so ~86% of the deficit comes from failed delivery, not weak math.
- GPT-5.6 Sol: feasibility 84.52%, DAQ 85.02%. Gemini 3.8 Flash: 82.58% / 82.94%. Claude Opus 5: 77.42% / 77.44%.
- Task-equalized complete HCAEU chain rates: 24% (Muse Spark 1.3) → 45% (Grok 4.6); every model below 50%.
- GPT-5.6 Sol forms no testable hypothesis in 41% of opportunities; Qwen3.8-Max stops at HC and HCAE 21% each.

## Actionable Insights
1. Score agents by "feasible × quality", not "quality when feasible". Example: when grading an agent's delivery schedule, any deliverable violating a constraint scores 0 before quality is multiplied in.
2. Information acquisition must continue past initial clarification. Example: build business agents with mid-task client check-ins (max 3 facts per query, like ORSim) during modeling and validation stages.
3. Measure H-C-A-E-U chain completion in logs, not just the final answer. Example: flag an agent that stops at "explanation" without an evidence-grounded update — its research chain is open.

## Assumptions & Limitations
- Requires client-accepted expert reference solutions plus a programmatic verifier per instance — hard to build for fuzzy business tasks like content writing.
- De-identification may remove information a real practitioner would have; ORSim facts are expert-curated, not live clients.
- 5 runs per model-task; spreads are within-task, not standard errors of the benchmark mean.
- No agent-vs-expert time/cost comparison in the body → [NO BENCHMARK] on cost.

## Metadata
- 2026; authors: Peisong Wang (HKUST-GZ), Feixue Liu (HKU), Yize Meng (Qingzhi Optimization), Bowen Liu (HKUST-GZ/Tencent Hunyuan), ... Zuo-Jun Max Shen, Yong-Hong Kuo (HKU), Jia Li (HKUST-GZ); categories: cs.CL, cs.AI; PDF: https://arxiv.org/pdf/2610.24087; citation count: [NO DATA — published 2026-10-16]
