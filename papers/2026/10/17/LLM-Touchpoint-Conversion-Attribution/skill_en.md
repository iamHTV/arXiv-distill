# Skill: LOTUS Pairwise Touchpoint Selection (semantic attribution for CVR)
Source: 2608.28649
Type: prompt-pattern / evaluation-method

## When to use this skill
- You need to identify meaningful touchpoints in a full user behavior path for conversion attribution, CVR training, or ad credit allocation
- Heuristic rules (taxonomy/CF) miss semantically-related touchpoints (complementary products, shared scenarios/IPs)
- You need high-quality labels for an auxiliary conversion prediction task without fine-tuning

Do NOT use: only in-shop attribution is needed (the Base heuristic suffices); the model is <100B params (lags flagship models badly — implicit F1 0.42–0.45 vs 0.51–0.56); you need online A/B evidence (the paper reports offline GAUC only).

## Input required
- User profile + conversion event (item, shop, category metadata)
- Candidate touchpoint (or full behavior log for the listwise fallback) with product metadata: image, title, shop, category
- A flagship-class LLM (≥100B params or proprietary) with thinking mode

## Steps
1. Define label criteria in the prompt: Explicit = shop/brand matching, leaf-category matching, CF-based similar-category matching; Implicit = (a) functional complementarity (camera + memory card), (b) scenario/audience alignment (shared anime IPs). Three classes: Irrelevant / Explicit / Implicit.
2. Pairwise judging: for EACH candidate touchpoint, send (user profile + 1 candidate + conversion) → the model returns a 3-way label. DON'T send the whole list at once (listwise over-filters, lower recall; pairwise-listwise gap 6–12pp with small models).
3. Aggregate: per-conversion precision/recall/F1 per class, macro-average across conversions; Overall F1 = (F1_Exp + F1_Imp)/2. Expected ceiling: explicit ~0.90, implicit ~0.54 — implicit is always ~0.4 F1 harder.
4. (Optional) Feed labels into the CVR model: selected touchpoints (Explicit + Implicit) as positive samples for an auxiliary indirect conversion prediction task; expected offline GAUC +0.35pp over the in-shop baseline, +0.15pp over heuristic cross-shop (CABB).
5. (Optional) Thinking mode: enable thinking for listwise (+0.0196 avg gain); pairwise gain is small (+0.0082) — prioritize the pairwise protocol first.

## Expected output
- Per-touchpoint 3-way labels + relation types (taxonomy/CF/complementarity/scenario) → enriched conversion path for attribution, CVR auxiliary task, ad credit allocation.
- Example: user buys a camera → touchpoints: camera bag (explicit leaf-category), memory card (implicit functional complementarity), anime poster (implicit scenario alignment) — heuristics see only the camera bag.

## Example application
- E-commerce CVR: 1,000 conversions, 3-day lookback, ~70 touchpoints per conversion → pairwise-judge each touchpoint with GPT-5.5/GLM-5.1 → labels → auxiliary task → GAUC +0.35pp. With 0.1pp GAUC ≈ substantial revenue growth, +0.35pp is material.

## Gotchas
- Implicit recall is the bottleneck: listwise recall is very low (over-filtering); pairwise recall 0.55–0.62 explicit, 0.44–0.56 implicit. Measure recall separately, don't look only at F1.
- Small models (<100B) lag seriously on implicit (Qwen3.5-27B implicit F1 0.4491 vs GPT-5.5 0.5567) — use flagship models in production.
- Thinking mode does NOT rescue small models much (Qwen3.5-27B +0.0231 implicit listwise — still low).
- Random-guessing F1 ≈ 0.1491 (implicit prevalence) — the baseline to sanity-check model output.
- LLM labels are NOT perfect (implicit F1 ceiling 0.54) — the auxiliary task benefits from volume, not absolute precision; but don't use them as sole ground truth for high-stakes attribution decisions.
- Heuristic baselines must NOT be shown to annotators (contamination risk) — keep this when building your own evaluation set.
