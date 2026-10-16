# Skill: MERGED — Multi-Teacher Reasoning Distillation for Entity Resolution
Source: 2609.01913
Type: framework / distillation-workflow

## When to use this skill
- A classification/relation task whose definitions evolve with business needs (entity resolution, product matching, content moderation taxonomy) — you need fast adaptation without relabeling
- You need a compact model (7B) at production-level accuracy with low cost/latency (millions of predictions/day)
- You have access to large VLMs as teachers but cannot afford to run them at inference scale

Do NOT use: a large high-quality human-labeled dataset already exists (SFT on human labels suffices); a simple single-modal text-only task (no text-only variant validated); you need a real faithfulness guarantee (the paper measures consistency, not faithfulness).

## Input required
- 2 diverse teacher VLMs (>30B params, DIFFERENT from each other — never a single teacher)
- 1 meta-judge VLM (can be one of the teachers or a separate model)
- A compact student model (paper: Qwen2.5-7B-VL)
- The relation definition R as a prompt (e.g., "exact match", "variant")
- Unlabeled pairs (text fields + images); human labels ONLY for evaluation
- SFT/DPO training infrastructure (token-level cross-entropy, DPO with β)

## Steps
1. Teacher generation: prompt K=2 teachers with the same prompt (x, R); parse output into (y, r, c) — label, reasoning trace, confidence [0,100]. Same prompt for every teacher.
2. Route: agreement (y₁=y₂ + consistent evidence) → SFT set; disagreement (y₁≠y₂) → keep both completions.
3. Meta-judge: for each disagreement pair, the judge picks the completion that best follows R and is most grounded in observable evidence (criteria: favors specific matching/conflicting fields; penalizes vague, unsupported, or input-contradicting rationales) → preference pair (chosen z⁺, rejected z⁻).
4. Stage 1 SFT: train the student on the agreement set with token-level cross-entropy → πref.
5. Stage 2 DPO: continue from πref, train on preference pairs (β controls strength; KL keeps πθ within a ball around πref).
6. Scoring for ranking metrics: p̂(y=1) = y·(½ + c/200) + (1−y)·(½ − c/200) — combine label and confidence, never logits.
7. Adapt to a new definition: regenerate teacher supervision under the new R (~10K samples), re-apply SFT+DPO FROM the existing checkpoint (warm-start) — NOT from scratch.

## Expected output
- A 7B student: PR-AUC +13.79 over human-label SFT, +6.32 over the 32B teacher zero-shot, cost $600/1M predictions (6× lower than the teacher), <1s/sample; label-reasoning consistency +13.21 (92.82); adaptation with 10K samples: +6.97 over zero-shot.

## Example application
- E-commerce catalog, 100K+ pairs, 8 languages: MERGED on the exact-match task = 90.96 PR-AUC. Definition changes to variant-matching: warm-start from the exact checkpoint + 10K samples → 89.48 PR-AUC (vs zero-shot 82.51, from-scratch MERGED 85.53) — adapt in days, not months.

## Gotchas
- Never use a single teacher: one teacher has idiosyncratic interpretation and is unstable on ambiguous pairs → noisy supervision. Use ≥2 diverse teachers.
- Disagreement is an asset, not noise: dropping disagreement pairs loses the most valuable preference data; the DPO stage contributes +4.15 PR-AUC.
- Meta-judge beats heuristics: high-confidence-correct 84.36, longer-reasoning-correct 86.17, meta-judge 90.96 — don't select preferences by confidence or length.
- Consistency ≠ faithfulness: a rationale supporting the label doesn't mean the rationale matches the evidence — add human validation or attribute-editing before trusting "reasoning".
- Warm-start confound: warm-started models have seen 10× the original task's data — a fair comparison needs the original checkpoint evaluated on the new task WITHOUT training (the paper doesn't report this).
- SFT accounts for the majority of the consistency gain (12.74 of 13.21); DPO mainly improves discriminative reasoning, not consistency.
- Teacher cost is one-time (data generation); the meta-judge is also one-time — production inference runs only the 7B student.
