# 2610.26199 TaQFormer: Treatment-as-Query Transformer with Data-Fusion for Multidimensional Treatment Modeling in Coupon Allocation

## Problem
Coupon allocation on an online marketplace with multiple service categories: need to choose a vector of category-specific discounts, accounting for both direct effects and cross-category demand shifts. Uplift modeling (a model estimating the incremental effect of an intervention vs control) is needed to estimate the response to the full treatment vector. Three challenges: (1) modeling focal response to structured treatment (M-dimensional discount vector), (2) combining large policy-biased observational logs (OBS) with a smaller stream of randomized controlled trial (RCT) data, (3) validating Transformer-based uplift models in production.

## Contribution
- TaQFormer: a treatment-as-query Transformer — each treatment coordinate is represented as a query token, enabling cross-attention (attention mechanism between two sequences) to estimate the response to the full treatment vector.
- Two-stage training pipeline: observational pretraining (OBS pretraining — training on observational data first) learns general outcome patterns, followed by LoRA fine-tuning (low-rank adaptation — efficient parameter fine-tuning) on RCT data with a request-specific fusion gate.
- Production validation: offline uplift metrics, treatment-parallel serving, latency monitoring, and a 14-day online A/B test. At essentially the same subsidy cost rate, TaQFormer increases business value per user by 1.26% over the production baseline and significantly outperforms both the production baseline and the RCT-only model, while meeting the latency budget. Rolled out to all marketplace traffic and operating at full scale as of October 2026.

## Method
Problem: allocate discount coupons across M substitutable service categories offered simultaneously. Each treatment is an M-dimensional vector of discount depths: a = (a₁, ..., a_M). Feasible actions a ∈ A satisfy a business rule: higher-priced categories receive strictly smaller discounts than lower-priced ones (a₁ < · · · < a_M). Causal target: conditional average treatment effect τ(x; a, a₀) = E[Y(a) − Y(a₀) | X = x].

TaQFormer architecture:
- Treatment-independent request path: feature tokenizer converts context into N semantic tokens, a stack of Encoder Blocks (Transformer backbone) encodes them into request representation H(x) ∈ R^{N×d}.
- Treatment-dependent path: each discount dimension is a treatment token, T(a) ∈ R^{M×d}. Treatment tokens act as queries using cross-attention to retrieve relevant information from H(x). A nonlinear readout combines decoded treatment representations to predict scalar completion probability ˆy(x, a) for the focal category.
- Treatment-aware cross-attention: L Treatment Decoder Blocks, each with cross-attention sublayer and feed-forward sublayer. Z⁽⁰⁾ = T(a). At block ℓ, decoded treatment states are queries, H(x) provides keys and values. A two-layer GELU MLP jointly reads all M decoded coordinates to produce the focal response.

Two-stage training:
- Stage I (OBS pretraining): full model trained for one epoch on OBS data using primary binary cross-entropy (BCE) objective plus auxiliary supervision.
- Stage II (RCT randomized fine-tune): retains full OBS-trained model as frozen reference route and builds a distinct RCT route. Tokenizer and first L − L_a Encoder Blocks form a shared prefix evaluated once. Final L_a Encoder Blocks evaluated twice: once with frozen weights producing H_obs(x), once with LoRA updates producing H_rct(x). LoRA: W′ = W + (η/r)AB where A and B are trainable rank-r matrices. Instance-wise gated fusion: small MLP g receives stop-gradient summaries of adapted memory, RCT treatment tokens, the two branch logits, and their absolute difference; α(x,a) = σ(g(...)); final logit s(x,a) = α·s_obs + (1−α)·s_rct.

Treatment-parallel serving: at serving time, encoder runs once producing H(X) for a request batch. Feasible treatment table stored as constant tensor. All B|A| request–treatment pairs flattened into one decoder batch, outputs reshaped into B × |A| response matrix. Reduces per-request computation from |A|(C_enc + C_dec) to C_enc + |A|C_dec.

## KNOWLEDGE — Data & Concepts
- M = 2 service categories, |A| = 33 feasible joint treatments (excluding reference). Encoder dimension d = 64, 4 Transformer blocks, 4 attention heads, feed-forward width 4d. Treatment decoder L = 2 blocks.
- Offline (same held-out RCT week): PEPNet baseline Qini = 0.1612, AUC = 0.6776, PCOC = 1.3737. TaQFormer: Qini = 0.2697, AUC = 0.7393, PCOC = 1.0012.
- 14-day online A/B test: PEPNet index = 100.00, RCT-only = 101.08 (*), Two-stage TaQFormer = 101.26 (*†). Subsidy cost rates: 20.43%, 20.45%, 20.42%. All pairwise comparisons significant (p < 0.05).
- P99 latency = 21 ms at 500 QPS load test, scoring all 33 feasible joint treatments.
- Two-stage pipeline improves Qini and AUC by 0.0033 over conventional sequential full fine-tuning, while bringing PCOC closer to one (1.0114 → 1.0027). RCT-only training keeps PCOC closest to one (1.0012).
- Model rolled out to all marketplace traffic, operating at full scale since October 2026.

## INSIGHT — Mechanism & Why
[Each discount coordinate gets its own treatment token] happens BECAUSE treatments with the same discount for a given category share embedding parameters, while each coordinate still has its own embedding table so the model knows which service category each discount belongs to. This means [related treatments share information while retaining coordinate identity, unlike the PEPNet baseline that fuses coordinate embeddings into one vector before gated prediction].
[The fusion gate combines the two branches' logits under RCT supervision] happens BECAUSE the two routes (frozen OBS and LoRA-adapted RCT) have different training distributions and may produce different prediction errors across request–action pairs. This means [the gate learns to mix per-instance rather than using a fixed weight, preserving useful OBS predictions while adapting to RCT data].

## IDEA — Actionable Applications
1. Apply treatment-as-query to multi-category discount/recommendation systems: first step is to represent each discount dimension as a query token, use cross-attention to estimate response under the full treatment vector.
2. Apply two-stage OBS→RCT training with fusion gate: first step is to pretrain on large observational data, then LoRA fine-tune on smaller RCT data with a per-request gate mixing the two branches' logits.

## WISDOM — General Principle
Principle: In industrial uplift modeling, large observational data provides general predictive information while smaller RCT data provides unbiased adaptation; combining both sources via per-instance fusion gate is better than choosing one source alone. Use when: you have large observational data and smaller RCT data for structured intervention decisions (discounts, promotions). Do NOT use when: no RCT data exists or counterfactual estimation is not needed.

## Assumptions & Limitations
- Plans to extend joint coupon allocation to more than 7 service categories — will require further evaluation of treatment coverage, candidate-action selection, and serving efficiency as the feasible action space grows.
- Business-specific calculations and absolute values withheld for confidentiality.
- Evaluated on one online marketplace with M = 2 service categories.

## Metadata
- Year 2026; authors: Jiahong Li, Zhifan Jiang, Jixing Xu, Zeqin Yang, Jingqi Ma, Jun Wu, Yu Xiang, Enzheng Hua, Fei Wang, Enyun Yu, Jiecheng Guo (all Didi Chuxing, Beijing, China); category: cs.LG; PDF: https://arxiv.org/pdf/2610.26199v1; citation count: [NO DATA — paper 2026-10-19]