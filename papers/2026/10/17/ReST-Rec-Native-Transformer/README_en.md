# 2609.01240 — From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs (ReST)

## Problem
- The LLM Transformer scaling recipe does not transfer directly to production ranking: (1) signal quality — behavior sequences are noisy (accidental clicks), temporally irregular (seconds vs days), sparsely supervised; the main loss is shortcut via the DLRM branch → sequence-starvation effect (the sequence module weakens as it scales); (2) computation asymmetry — one user history vs N candidates: sequence-side compute amortizes, per-candidate compute is the latency bottleneck.

## Contribution
- ReST (Recommendation-native Scalable Transformer): asymmetric encoder–decoder — compute-heavy sequence encoder T (contextualizes history once → reusable memory) + lightweight cross decoder C (projection-free KV attention + token-specific parameterization)
- 3 rec-native designs: Dual-Gated Attention (DGA), RoPE + RoTE (rotary temporal embedding), SRN (Stabilized Residual Normalization); 2 training-only auxiliary objectives; shared-prefix training/serving

## Method
- DGA: a value gate filters unreliable features pre-aggregation + an output gate modulates context post-aggregation, with bounded sigmoid gates (HSTU's unbounded SiLU gate diverges at scale).
- RoTE: attention heads split into two groups — Hpos uses standard RoPE (ordinal positions), Htime uses RoTE (relative time intervals at head-specific granularity τ_h: seconds/minutes fine, days/weeks coarse).
- SRN: Mix-LN-style depth-dependent LN placement + a small learnable scalar on each residual branch.
- Auxiliary objectives (training-only): auxiliary sequence CVR supervision + sequence/non-sequence alignment — fights starvation, no inference overhead.
- ULT (user-level shared-prefix training): 5.8× training throughput; shared-prefix serving: 20× reduction in per-request inference cost.

## Key Findings
- TikTok Shop Ads industrial: ReST +0.92% AUC Δ (Large) over the production DLRM baseline (0.05% AUC Δ is already practically meaningful); a parameter-matched Trans. still trails by 0.20%; encoder-only ReST +0.87%, beating LLaMA by 0.17%.
- Public benchmarks: best AUC + log loss on ML-1M (0.8099), ML-20M (0.8135), Amazon-Books (0.7571).
- Scaling power law: ReST (a,b)=(0.626,0.101) vs LLaMA (0.491,0.090), HSTU (0.461,0.088). Length: ReST keeps improving to 16k tokens (+~0.4%); Depth: ReST +0.59%→+0.76% (LLaMA saturates >8 layers, HSTU >16); Width: ReST +0.67%→+0.80% monotonic (LLaMA/HSTU flatten at d=256).
- Ablation: MoE in T costs +500% params with zero gain; DGA O&V gate +0.12%; SRN +0.12% vs Pre-LN; aux CVR: LLaMA +0.16→+0.22, ReST +0.07→+0.12; alignment +0.05–0.06%.
- Online A/B, 1 week, 20% traffic: AUC +1.31%, Advertiser Value +11.93% (p<0.01), within the 50ms P99 budget; fully deployed in production.

## Actionable Insights
- Fight sequence starvation before scaling: add an auxiliary sequence CVR loss (training-only, no inference overhead) — otherwise the DLRM branch shortcuts the main loss and longer context yields nothing.
- Factorize along asymmetric compute: a heavy encoder runs once per user, a light decoder scores N candidates — shared-prefix serving cuts 20× inference cost and is the precondition for deploying large sequence models.
- Capacity ≠ gains: MoE with +500% params gave nothing; gains come from rec-native design (gates, temporal encoding, normalization) — invest in architecture before parameters.

## Assumptions & Limitations
- Industrial data confidential (only relative AUC Δ reported); public benchmarks cast pointwise via chronological splitting.
- Architecture ablation is observational; the power-law fit is descriptive over the tested compute range.
- Not stated: generalizability beyond ads/e-commerce recommendation; the 50ms P99 budget is TikTok Shop Ads' own.

## Metadata
- 2026, Jie Chen, Xiangqian Yu, Yanchao Lian, Tan Lu, Run Yang, Zhengchun Shang, Xing Wang, Cheng Chen, Ke Hu, Qiang Li, Tianjiu Yin, Xiaobing Liu (ByteDance), cs.IR/cs.AI/cs.LG, https://arxiv.org/pdf/2609.01240
