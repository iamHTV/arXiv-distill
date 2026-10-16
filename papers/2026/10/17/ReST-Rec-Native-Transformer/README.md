# 2609.01240 — From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs (ReST)

## Problem
- Scale Transformer recipe của LLM không transfer trực tiếp sang production ranking: (1) signal quality — behavior sequence noisy (accidental click), temporal irregular (giây vs ngày), supervision thưa; main loss bị shortcut qua DLRM branch → sequence-starvation effect (module sequence yếu đi khi scale); (2) computation asymmetry — 1 user history cho N candidates: sequence-side compute amortize được, per-candidate compute là latency bottleneck.

## Contribution
- ReST (Recommendation-native Scalable Transformer): asymmetric encoder–decoder — compute-heavy sequence encoder T (contextualize history 1 lần → reusable memory) + lightweight cross decoder C (projection-free KV attention + token-specific parameterization)
- 3 rec-native design: Dual-Gated Attention (DGA), RoPE + RoTE (rotary temporal embedding), SRN (Stabilized Residual Normalization); 2 training-only auxiliary objectives; shared-prefix training/serving

## Method
- DGA: value gate lọc feature unreliable trước aggregation + output gate điều chế context sau aggregation, bounded sigmoid (HSTU dùng unbounded SiLU gate — diverge ở scale).
- RoTE: chia attention heads làm 2 nhóm — Hpos dùng RoPE (ordinal position), Htime dùng RoTE (relative time interval, granularity τ_h: giây/phút fine, ngày/tuần coarse).
- SRN: Mix-LN-style depth-dependent LN placement + learnable scalar nhỏ trên mỗi residual branch.
- Aux objectives (training-only): auxiliary sequence CVR supervision + sequence/non-sequence alignment — chống starvation, không overhead inference.
- ULT (user-level shared-prefix training): 5.8× training throughput; shared-prefix serving: 20× reduction per-request inference cost.

## Key Findings
- TikTok Shop Ads industrial: ReST +0.92% AUC Δ (Large) vs production DLRM baseline (0.05% AUC Δ đã practical meaningful); parameter-matched Trans. vẫn thua 0.20%; encoder-only ReST +0.87%, hơn LLaMA 0.17%.
- Public: best AUC + log loss trên ML-1M (0.8099), ML-20M (0.8135), Amazon-Books (0.7571).
- Scaling power law: ReST (a,b)=(0.626,0.101) vs LLaMA (0.491,0.090), HSTU (0.461,0.088). Length: ReST cải thiện đến 16k tokens (+~0.4%); Depth: ReST +0.59%→+0.76% (LLaMA saturate >8 layers, HSTU >16); Width: ReST +0.67%→+0.80% monotonic (LLaMA/HSTU flatten d=256).
- Ablation: MoE trong T +500% params nhưng 0 gain; DGA O&V gate +0.12%; SRN +0.12% vs Pre-LN; aux CVR: LLaMA +0.16→+0.22, ReST +0.07→+0.12; alignment +0.05–0.06%.
- Online A/B 1 tuần (20% traffic): AUC +1.31%, Advertiser Value +11.93% (p<0.01), trong 50ms P99 budget; deployed production.

## Actionable Insights
- Chống sequence starvation trước khi scale: thêm auxiliary sequence CVR loss (training-only, không inference overhead) — nếu không, sequence module bị DLRM branch shortcut và context dài thêm không lợi.
- Factorize theo asymmetric compute: encoder nặng chạy 1 lần/user, decoder nhẹ decode N candidate — shared-prefix serving giảm 20× inference cost, là điều kiện để deploy sequence model lớn.
- Capacity ≠ gains: MoE +500% params không lợi; gains đến từ rec-native design (gate, temporal, normalization) — đầu tư kiến trúc trước khi đầu tư parameter.

## Assumptions & Limitations
- Industrial data confidential (chỉ report relative AUC Δ); public benchmarks cast pointwise qua chronological split.
- Ablation architecture observational; power-law fit descriptive trên tested compute range.
- Không nói: generalizability ngoài ads/e-commerce recommendation; latency budget 50ms P99 là của TikTok Shop Ads.

## Metadata
- 2026, Jie Chen, Xiangqian Yu, Yanchao Lian, Tan Lu, Run Yang, Zhengchun Shang, Xing Wang, Cheng Chen, Ke Hu, Qiang Li, Tianjiu Yin, Xiaobing Liu (ByteDance), cs.IR/cs.AI/cs.LG, https://arxiv.org/pdf/2609.01240
