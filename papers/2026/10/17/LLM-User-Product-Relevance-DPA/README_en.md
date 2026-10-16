# 2610.14550 — LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising

## Problem
- Dynamic Product Advertising (DPA) retrieval lacks a reliable offline metric: engagement metrics suffer selection bias and sparsity; online evaluation is costly. Search has explicit queries; ads do not — prior work cannot infer user-level relevance from heterogeneous engagement histories.

## Contribution
- Query-free relevance metric: compress engagement history into an intent set via Semantic ID (SID) grouping + event-stratified segmentation; an LLM judge scores each intent–candidate pair, aggregated into a user-level score
- Scalable pipeline: SID compression cuts LLM calls 30×; agentic guideline discovery + human alignment + teacher-student distillation
- Validated against real online KPIs: ranks 6 retrieval sources consistently with conversion precision/recall; directionally aligned with CTR/CVR deltas across 4 A/B tests

## Method
- Intent representation: RQ-kmeans (L=3 stages, 512-entry codebooks) over multimodal product embeddings → SID; group by (SID prefix, event type), representative = most recent product; weight w_g = log(1+|g|)·β(e_g), β(purchase)=3, add-to-cart=2, others=1.
- Judge: Phase A agentic rule discovery — seed prompt with 5-tier taxonomy (Exact/Similar/Substitute/Complementary/Irrelevant), Gemini-2.5-Pro labels a calibration split, loop: cluster errors → propose ≤3 sub-rules → accept iff paired-bootstrap 95% CI on Δaccuracy excludes zero, no per-class F1 regression >0.5pp; keep rules recurring across trials. Phase B human alignment: audit business-critical mismatches (demographic gender/age, regulated categories, advertiser exclusions) — demographic mismatch promoted to a hard Irrelevant override.
- Distillation: teacher Gemini-2.5-Pro + GPT-5 verification agent; disagreements → human auditors; student Gemini-2.5-Flash fine-tuned with LoRA rank 16, lr multiplier 2, 5 epochs. Metric: MicroRel/MacroRel under threshold-k aggregation (k=7).

## Key Findings
- SID grouping + event stratification: 0.99 Spearman fidelity vs full sequence at 3.4% of pairwise cost (~30× reduction); weighted variant reaches P(CVR)=0.50, P(CR)=0.29, P(CP)=0.35, beating Random baseline (+0.24 CVR, +0.16 CP) which itself costs 7× more.
- Student Flash-ft matches teacher F1 0.869 vs 0.860; +2.9% precision, +3.0% recall over prompt-only; beats SigLIP-2-mm by 9% precision, 12% recall (with 10× less training data).
- Latency: Flash-ft 751ms p50 / 1,117ms p95 / 18 QPS vs teacher 6,963ms / 10,840ms / 2 QPS (~9× faster). Prompt-only Flash keeps teacher-like long-tail p95 (8,807ms) — fine-tuning compresses both p50 and p95 by an order of magnitude.
- Threshold k peaks in [5,7]; at k=7 all 95% bootstrap CIs strictly positive: P(CVR) [+0.29,+0.68].

## Actionable Insights
- Compress history before LLM judging: semantic grouping + event-strength weighting cuts cost 30× while keeping 0.99 fidelity — apply to any content evaluation pipeline: judge intent representatives, not every event.
- The guideline matters more than the model: the guideline carries most of the lift (unguided Pro loses to a guided student) — invest in taxonomy + rules before switching models.
- Fine-tune, don't just prompt: prompt-only keeps teacher-like p95 tail; fine-tuning compresses p95 by an order of magnitude — when latency matters, distillation is mandatory.

## Assumptions & Limitations
- Engagement-based iteration mixes ranker alignment with engagement signal → weaker, noisier correlation.
- The metric is a gate before A/B, not a replacement for online evaluation; demographic rules are too rare in the calibration set for the agentic loop to discover — human pass is load-bearing.
- Not stated: Figure 2 validation covers only 2 retrieval sources; threshold-k peaks may shift on other catalogs.

## Metadata
- 2026, Wen Zhang, Xiao Bai, Hsiang-wei Chao, Mengfan Zhu, Tong Zhao, Mingxuan Ju, Xiaodong Liu, Congfei Zhang, Yunzhi Zhou, Yajun Wang, Jinchao Li, Yu Zhang (Snap Inc.), cs.IR, CIKM '26, https://arxiv.org/pdf/2610.14550
