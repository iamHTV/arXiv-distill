# [2609.06438v1] InsightChain: Optimized Chain-of-Insight Analytics for LLM-driven Data Visualization

## Problem
- Existing LLM-driven visualization approaches frame visualization generation as a single-step mapping from user query to figure or code, overlooking the iterative analytical reasoning process of expert analysts. Existing approaches have an evaluation gap for complex data visualization — a table may support multiple valid analytical directions, leaving no unique reference insight or visualization, while final-output metrics cannot determine whether intermediate hypotheses are grounded in executed evidence.

## Contribution
- InsightChain — a four-stage visualization prompting pipeline (Explore–Focus–Test–Present) that emulates expert analytical workflows, together with VG-COPRO, a vision-guided automatic prompt optimization (APO) method adapted to jointly optimize such multi-stage, executable pipelines.
- Insight Progression Metric (IPM) — a rubric combining four text-based dimensions with a vision-based dimension, for evaluating both the analytical trajectory and the final visualization.
- IPM assessed through a 100-chain human pilot and an expanded 300-chain agent-based evaluation spanning all ten domains.

## Method (core summary)
- Task formulation: Given a single tabular dataset D without a predefined analytical question or visualization intent, the system must identify a worthwhile analytical direction, test the resulting hypothesis through executable analysis, and communicate the supported finding in a visualization. Output is a multi-stage reasoning-and-execution trace together with a final figure.
- InsightChain implements this through a four-stage pipeline S = (t1, t2, t3, t4) corresponding to Explore, Focus, Test, Present. At each stage t, a predictor πt implemented as a DSPy chain-of-thought module with a typed signature produces structured output ot = πt(xt; θt), where xt denotes input context and θt denotes stage-specific prompt.
- Each output ot contains an executable Python program pyt, executed by a sandboxed executor with retry budget B = 2. If error trace is non-empty, the error is fed back to the predictor, guiding regeneration of ot, forming a self-correcting execution loop.
- Downstream stages condition on prior outputs and execution traces. Running context C<t = (o1, e1, ..., ot−1, et−1). Input to every predictor is xt = (σ(D), C<t) where σ(D) is a fixed dataset profile.
- IPM(c) = sum over d in D of wd · ϕd(c), where D = {EXPLORATION BREADTH, FOCUS RELEVANCE, HYPOTHESIS RIGOR, INSIGHT COMMUNICATION, VISUAL QUALITY}, ϕd ∈ [1, 10] is LLM-as-judge score, and w = (0.20, 0.25, 0.20, 0.25, 0.10).
- VG-COPRO: built on COPRO outer loop for per-predictor optimization, with OPRO proposer for inner loop, plus three modifications: per-dimension diagnostic critique, leave-one-domain-out (LODO) objective, vision-aware compile signal.

## Key Findings
- 5 authors from Huawei Technologies Co., Ltd., arXiv category: cs.CL.
- 285 tabular datasets spanning 10 domains from 7 public sources. Leave-five-domains-out protocol: 5 domains supply 150 datasets for compilation (train n=95, validation n=20, in-domain test n=35), other 5 domains provide cross-domain test set (n=135).
- IPM achieves Spearman ρ = 0.88 agreement with human ratings in the 100-chain human pilot.
- InsightChain consistently outperforms single-shot baselines (Single-shot 4-prompt and LIDA) across task models (Gemini 3 Flash, GPT-4.1).
- Existing APO methods fail to yield consistent gains; VG-COPRO improves performance in both in-domain and cross-domain settings.
- Table 1: Gemini 3 Flash — InsightChain pre-APO IPM 7.24 → VG-COPRO IPM 8.56 (+1.31); GPT-4.1 — 7.90 → 8.54 (+1.16). Single-shot 4-prompt: Gemini 6.38 (−1.00), GPT-4.1 6.92 (−1.09); LIDA: Gemini 5.79 (−1.46), GPT-4.1 4.29 (−3.62).

## Actionable Insights
1. Instead of one-step mapping from query to chart, use a four-stage pipeline (Explore–Focus–Test–Present) to emulate expert analytical workflows. Application: split data visualization tasks into four separate stages, each generating executable Python code that is executed and validated before proceeding to the next stage.
2. Use a multi-dimensional metric (IPM) combining text-based and vision-based evaluation to assess multi-stage visualization pipelines. Application: evaluate both the analytical trajectory and the final visualization, not just final output metrics.

## Assumptions & Limitations
- IPM construct validity: full five-dimensional human ratings limited to the 100-chain pilot; expanded 300-chain evaluation relies on repeated agent-based ratings and one expert's audit of three binary criteria.
- 91.9% of datasets from real public sources, with small synthetic-template fallback for underrepresented demographics and energy domains.
- Experiments use specific models (Gemini 3 Flash, GPT-4.1).

## Metadata
- Year: 2026, authors: Hanya Sun, Chen Zhang, Sheng Liang, Yongyue Zhang, Yong Liu (Huawei Technologies Co., Ltd.), arXiv category: cs.CL, PDF link: https://arxiv.org/pdf/2609.06438v1
