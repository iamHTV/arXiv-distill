# 2609.01913 — MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation (NeurIPS 2026 Workshop VLM4RWD)

## Problem
- Product entity resolution: relation definitions (exact, variant, substitute, trending, customer interest) evolve with business needs — each change defines a new task. Fine-tuning is SOTA but needs human annotation: slow (weeks), costly, noisy (fatigue/subjective bias), and carries no reasoning. Large VLMs zero-shot adapt immediately and supply reasoning, but cost/latency cannot meet millions-of-predictions-per-day scale, and they hallucinate rationales that don't support their predictions.

## Contribution
- MERGED: a distillation framework that transfers not just labels but structured reasoning from large teacher VLMs into a compact 7B student — no human annotation for training (human labels used only for evaluation).
- Routing rule: teacher agreement → SFT; teacher disagreement → meta-judge-curated DPO preference pairs.
- Adaptation: re-applying MERGED from an existing checkpoint with 10K samples adapts to a new definition in days, not months.

## Method
- Teacher generation: K=2 diverse large VLMs (>30B params), same prompt; each teacher emits (label y, reasoning r, confidence c ∈ [0,100]).
- Agreement (y₁=y₂, consistent evidence) → high-confidence set for SFT (token-level cross-entropy). Two-teacher consensus increases precision and reduces label noise.
- Disagreement (y₁≠y₂) → two competing completions → a meta-judge VLM selects the completion that best follows the relation definition R and is most grounded in observable evidence (favors specific matching/conflicting fields; penalizes vague, unsupported, or input-contradicting rationales) → preference pair (chosen/rejected) for DPO (β controls preference strength; KL ball around πref).
- Score for PR-AUC: p̂(y=1|x,R) = y·(½ + c/200) + (1−y)·(½ − c/200).
- Dataset: internal e-commerce retailer, 100K+ human-audited product-listing pairs, 8 languages (EN/FR/ES/DE/IT/TR/PT/JA), 18 countries; test set ~6,000 pairs, pair-disjoint, balanced classes; multimodal (images + long heterogeneous text fields).

## Key Findings
- Exact-match: MERGED (Qwen2.5-7B-VL student) reaches 90.96% PR-AUC / 86.25% accuracy / $600 per 1M predictions / <1s per sample — vs Qwen2.5-32B-VL zero-shot 84.64 PR-AUC at $3,600 per 1M (6× cost): +6.32 PR-AUC at 6× lower cost; vs the same backbone SFT on human labels (77.17): +13.79.
- Gain decomposition: human-label SFT 77.17 → model labels +3.50 (80.67) → +reasoning +6.14 (86.81) → +DPO +4.15 (90.96). The majority of the 13.79 gain comes from reasoning distillation and the preference signal, not the label source.
- Reward-model ablation: high-confidence-correct 84.36, longer-reasoning-correct 86.17, meta-judge 90.96 — heuristics are far behind LLM judgment.
- Label-reasoning consistency (LLM-as-judge, 0–100): 7B zero-shot 79.61, 32B zero-shot 81.91, 7B SFT 92.35, MERGED 92.82 (+13.21 total; SFT accounts for 12.74, DPO adds only 0.47).
- Adaptation (variant task, 10K samples = 1/10 of exact-task data): zero-shot 82.51; from-scratch SFT 83.18 (+0.67); from-scratch MERGED 85.53 (+3.02); exact-MERGED checkpoint + SFT 87.27; MERGED-adapt (SFT+DPO warm-start) 89.48 (+6.97 over zero-shot, beating from-scratch training).

## Actionable Insights
- When a relation definition changes: don't relabel — regenerate teacher supervision under the new definition and re-run SFT+DPO from the existing checkpoint; 10K samples suffice (+6.97 over zero-shot, beats from-scratch +3.02).
- Distill reasoning along with labels: model labels alone +3.50, adding reasoning +6.14, adding DPO +4.15 — label-only distillation leaves the majority of the value behind.
- Treat disagreement as an asset: ambiguous pairs aren't noise — they are the most valuable preference pairs for DPO; a meta-judge with grounded-evidence criteria beats heuristics (90.96 vs 84.36/86.17).

## Assumptions & Limitations
- Label-reasoning consistency ≠ faithfulness (a necessary but weaker condition) — not validated with humans or attribute-editing.
- Warm-start confound: warm-started models have seen 10× more exact-task data; the exact checkpoint evaluated on the variant task WITHOUT further training is not reported.
- Dataset is proprietary and not released (only prompts in Appendix A); only one transfer direction tested (exact→variant), Qwen-family baselines only; K=2 teachers (ensemble size unexplored); the meta-judge is a one-time dependency during data generation; no calibration/confidence-interval/per-language breakdown; no text-only ablation.

## Metadata
- NeurIPS 2026 Workshop VLM4RWD, 2026 (v2 2026-10-07), You-Lin Chen, Kyoungjun Park (UT Austin, intern at Amazon), Abhishek Prasad, Ram Tripathi, Prithviraj Sen, Bin Xu, Pedro Herrero-Vidal (Amazon), cs.IR, https://arxiv.org/pdf/2609.01913
