# Skill: Treatment-as-query architecture for multi-treatment uplift modeling (TaQFormer)
Source: 2610.26199
Type: framework

## When to use this skill
- Need to estimate causal uplift for structured intervention decisions (e.g. multi-category discount allocation, promotions).
- Have large observational data (OBS) and smaller randomized controlled trial data (RCT).
- Do NOT use when no RCT data exists or counterfactual estimation is not needed.

## Input needed
- Request context with features available online at decision time.
- M-dimensional treatment vector (each dimension is a discount level for a service category).
- Observational data (large OBS logs) and RCT data (smaller randomized stream).
- Target subsidy cost rate.

## Steps
1. Build the treatment-independent request path: tokenizer converts context into N semantic tokens, Encoder Block stack encodes into request representation H(x).
2. Build the treatment-dependent path: each discount dimension is a treatment token, use cross-attention to retrieve relevant information from H(x).
3. Train Stage I: full model on OBS data for one epoch using primary binary cross-entropy objective.
4. Train Stage II: keep full OBS-trained model as frozen reference route, build distinct RCT route with LoRA (rank r = 16, scaling η = 16) on final L_a = 2 Encoder blocks.
5. Add per-instance fusion gate: small MLP mixes the two branches' logits (frozen OBS and LoRA-adapted RCT) based on stop-gradient summaries of adapted memory, RCT treatment tokens, the two logits, and their absolute difference.
6. Optimize serving: encoder runs once per request batch, all request–treatment pairs flattened into one decoder batch.

## Expected output
- Qini improves from 0.1612 (PEPNet baseline) to 0.2697, AUC from 0.6776 to 0.7393, PCOC from 1.3737 to 1.0012.
- Business value per user +1.26% in 14-day A/B test, subsidy cost rate essentially unchanged (~20.4%).
- P99 latency 21 ms at 500 QPS, scoring all 33 feasible joint treatments.

## Example application
- Discount allocation system for 2 service categories (e.g. ride-hailing and food delivery): each discount level is a treatment token, cross-attention estimates completion probability under the full discount vector, fusion gate adjusts OBS predictions with RCT data.

## Gotchas
- Business-specific calculations withheld for confidentiality — only relative changes reported.
- Evaluated only on M = 2 categories; extending to more than 7 categories requires re-evaluating treatment coverage and serving efficiency.
- The fusion gate is an additional MLP, adding model cost.