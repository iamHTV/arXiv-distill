# 2608.28649 — Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution? (CIKM '26)

## Problem
- Conversion attribution (allocating credit for a conversion across past user touchpoints) has two aspects: (1) weight allocation (restricted to touchpoints under the same item/shop), (2) touchpoint selection (identifying meaningful touchpoints from the full user behavior sequence — Zeng et al., Meta). Prior selection methods rely on collaborative-filtering heuristics (taxonomy matching + CF similarity) that fail to align with user-perceived semantic intent and miss implicitly-related touchpoints (functional complementarity: camera + memory card; scenario/audience alignment: shared anime IPs).

## Contribution
- SILVA: the first benchmark for touchpoint Selection In fuLl-path conVersion Attribution — 1,000 conversion events + touchpoints within a 3-day lookback window (69,680 touchpoints), multimodal (image, title, shop, category metadata), from a platform with hundreds of millions of DAU.
- Human annotation: 6 annotators, each touchpoint independently labeled by 3 annotators, Fleiss' κ > 0.70 (substantial agreement), majority voting; annotators were NOT shown heuristic baseline outputs. Distribution: explicit 19.09%, implicit 14.91% — implicit signals are non-negligible and invisible to prior approaches.
- Systematic evaluation of 8 LLMs (GPT-5.5, Gemini-3.1-Pro, Claude-Opus-4.7, GLM-5.1, DeepSeek-V4-Pro/Flash, Qwen3.5-27B, Qwen3.5-30B-A3B) with pairwise vs listwise prompting.
- LOTUS (LLM-Oriented Touchpoint Understanding and Selection): internal foundation model + pairwise reasoning at scale → labels used as positive samples for an auxiliary indirect conversion prediction task in a production CVR model.

## Method
- Three-class label space: Irrelevant / Explicit (taxonomy matching: identical item/shop/brand/leaf category; CF-based similar leaf categories) / Implicit (functional complementarity; scenario/audience alignment).
- Pairwise protocol: the model receives user profile + one candidate touchpoint + conversion → 3-way judgment. Listwise: profile + full behavior log + conversion → relevant touchpoints with relation types. Same criteria in prompts for both protocols.
- Metrics: per-conversion precision/recall/F1 per class, macro-averaged; Overall F1 = (F1_Exp + F1_Imp)/2. Random-guessing F1 ≈ 0.1491 (implicit prevalence).

## Key Findings
- Finding 1 — implicit much harder: pairwise explicit F1 0.8979 vs implicit 0.4929; listwise 0.8372 vs 0.4608. Best implicit F1 0.5426 (Gemini-3.1-Pro pairwise) vs best explicit 0.9095 (Claude-Opus-4.7 pairwise).
- Finding 2 — pairwise beats listwise on EVERY model: avg overall F1 0.6490 → 0.6954. Pairwise decomposes a noisy sequence-level selection into candidate-level judgments; listwise over-filters → lower recall.
- Finding 3 — strong open-weight models competitive: GLM-5.1 0.7086, DeepSeek-V4-Pro 0.7056 (pairwise overall) close to GPT-5.5 0.7197; smaller Qwen variants lag (0.6636/0.6703), especially on implicit.
- Finding 4 — model capability narrows the pairwise-listwise gap: 1.3pp Gemini-3.1-Pro, 3.0pp GPT-5.5, but 6.2pp Qwen3.5-27B, 11.9pp Qwen3.5-30B-A3B. Pairwise gain is larger when listwise F1 is lower.
- Thinking-mode ablation: marginal — listwise +0.0196 avg overall gain, pairwise +0.0082; strongest gains from smaller Qwen variants. Current reasoning patterns are not optimized for touchpoint selection.
- LOTUS on a production-scale CVR model: absolute GAUC gains +0.35pp over Base (in-shop heuristic [4]) and +0.15pp over CABB (heuristic cross-shop explicit-only [23]). An absolute 0.1pp GAUC is empirically sufficient to drive substantial growth in online sales/ad revenue.

## Actionable Insights
- Use pairwise prompting (one candidate + conversion + profile) for semantic relevance judgment, not listwise — higher recall at every model scale; the gap narrows to 1.3–3.0pp with flagship models.
- Touchpoint selection should use semantic criteria (functional complementarity, scenario/audience alignment) alongside taxonomy/CF rules — implicit touchpoints are 14.91% of the journey; ignoring them loses ~15% of conversion signal.
- LLM-attributed labels as auxiliary positive samples for CVR training: +0.35pp GAUC offline using only pairwise reasoning with an internal model — no fine-tuning required, just labels.

## Assumptions & Limitations
- Benchmark from a single platform (Alibaba e-commerce, hundreds of millions of DAU) — generalization to other domains untested.
- Implicit F1 remains far below explicit (best 0.5426 vs 0.9095) — semantic relations (functional complementarity, scenario consistency) are still hard even for strong LLMs.
- Thinking mode is marginal (+0.008–0.020) — current reasoning patterns are not optimal; specialized fine-tuning is needed for the nuanced semantic judgments.
- Offline GAUC only — no online A/B test reported; the 0.1pp GAUC threshold rests on prior empirical findings [3,4,24].
- Smaller models (<100B) largely lag — touchpoint selection needs flagship-scale reasoning; not runnable on edge/small deployments.

## Metadata
- 2026 (2026-08-18), Jinqi Wu (NJU), Sishuo Chen (PKU), Zhangming Chan, Yong Bai, Chao Yi, Han Zhu, Shuodian Yu, Lei Zhang, Sheng Chen, Chenghuan Hou, Jian Xu (Taobao & Tmall Group, Alibaba), Chaoyou Fu (NJU); CIKM '26 Rome, Nov 07–11 2026, cs.CL, https://arxiv.org/pdf/2608.28649
