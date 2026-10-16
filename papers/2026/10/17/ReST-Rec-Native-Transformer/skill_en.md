# Skill: ReST Rec-Native Transformer Scaling
Source: 2609.01240
Type: framework (architecture + system co-design for production ranking sequence models)

## When to use this skill
- Scaling behavior-sequence Transformers for production ranking (CVR/CTR prediction) under a tight latency budget (P99 ~50ms)
- Your current sequence module saturates early when scaling depth/width, or longer context does not help (sequence-starvation symptom)
- Do NOT use: tasks without behavior sequences (static features only); retrieval-stage models that are not discriminative ranking

## Inputs required
- Behavior sequence S_u = [(item, timestamp)] per user + non-sequential user/context features
- A production DLRM ranker as baseline (already optimized: fused kernels, mixed precision)
- Latency budget (P99) + offline AUC Δ measurement (0.05% is already meaningful)

## Steps
1. Fight sequence starvation first: add auxiliary sequence CVR loss + sequence/non-sequence alignment objective (training-only, zero inference overhead) — otherwise the main loss is shortcut via the non-sequential branch.
2. Build the rec-native encoder T (LLaMA-style base): (a) DGA — value gate σ(XW_gv)⊙(XW_V) before attention + output gate σ(XW_go) after, bounded sigmoid (do NOT use unbounded SiLU — diverges at scale); (b) RoPE+RoTE — split heads: Hpos RoPE for ordinal, Htime RoTE for bucketized timestamps τ_h (seconds→minutes→days→weeks); (c) SRN — Mix-LN depth-dependent placement + small learnable scalar α_l on each residual branch.
3. Factorize asymmetrically: heavy encoder T runs once per user history → memory; lightweight cross decoder C: projection-free KV attention + token-specific parameterization for N candidates.
4. System co-design: user-level shared-prefix training (amortize prefix computation across samples from the same user → ~5.8× throughput) + shared-prefix serving (T executed once per request, reused across candidates → ~20× inference cost reduction).
5. Verify scaling on 3 axes: length (to 16k tokens), depth (ReST keeps improving to 32 layers; LLaMA saturates >8, HSTU >16), width (d=512 still monotonic; baselines flatten at d=256). Fit a power law ΔAUC=a·F^b to compare compute efficiency.
6. Deploy: configure to satisfy the P99 budget, A/B test for a week with a revenue metric (Advv) + streaming AUC + guardrails.

## Expected output
- Offline AUC Δ +0.9% (Large) over the production baseline; online AUC +1.31%, revenue +11.93% within the P99 budget; 5.8× training throughput, 20× inference cost reduction.

## Example application
- E-commerce ads ranking: replace the DLRM sequence component with ReST, keep the rest fixed; A/B on 20% traffic for a week → measure Advv lift; if +revenue within the latency budget → full rollout.

## Gotchas
- MoE in the encoder: +500% params, zero AUC gain — encoder capacity is not the bottleneck; the candidate-conditioned decoder is what helps (+0.03% @ +0.2% FLOPs).
- Unbounded output gates (SiLU) diverge at scale — always use bounded sigmoid.
- Auxiliary supervision helps more as the module grows (LLaMA +0.06% vs ReST +0.05%) — bigger modules need aux more.
- RoTE must shift timestamps by sequence start (t̃_i = t_i − t_1) to avoid huge bucket indices.
- Public benchmarks must be cast pointwise with chronological splits to align with the CVR task.
