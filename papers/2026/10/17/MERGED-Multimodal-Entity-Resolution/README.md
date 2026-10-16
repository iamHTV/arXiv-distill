# 2609.01913 — MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation (NeurIPS 2026 Workshop VLM4RWD)

## Problem
- Product entity resolution: relation definitions (exact, variant, substitute, trending, customer interest) evolve theo business needs — mỗi change = task mới. Fine-tuning SOTA nhưng cần human annotation: chậm (weeks), costly, noisy (fatigue/subjective bias), không có reasoning. Large VLM zero-shot adapt ngay + có reasoning, nhưng cost/latency không đáp ứng millions-of-predictions-per-day, và hallucinate rationale không support prediction.

## Contribution
- MERGED: distillation framework transfer CẢ label lẫn structured reasoning từ large teacher VLMs vào compact 7B student — KHÔNG cần human annotation cho training (human labels chỉ dùng evaluation).
- Routing rule: agreement → SFT, disagreement → meta-judge-curated DPO preference pairs.
- Adaptation: re-apply MERGED từ existing checkpoint với 10K samples cho definition mới (days, không phải months).

## Method
- Teacher generation: K=2 diverse large VLMs (>30B params), same prompt, mỗi teacher emit (label y, reasoning r, confidence c ∈ [0,100]).
- Agreement (y₁=y₂, consistent evidence) → high-confidence set cho SFT (token-level cross-entropy). Consensus tăng precision, giảm label noise.
- Disagreement (y₁≠y₂) → 2 competing completions → meta-judge VLM chọn completion best follows R + grounded in observable evidence (favors specific matching/conflicting fields, penalizes vague/unsupported) → preference pair (chosen/rejected) cho DPO (β controls preference strength, KL ball quanh πref).
- Score cho PR-AUC: p̂(y=1|x,R) = y·(½ + c/200) + (1−y)·(½ − c/200).
- Dataset: internal e-commerce, 100K+ human-audited pairs, 8 languages (EN/FR/ES/DE/IT/TR/PT/JA), 18 countries; test ~6,000 pairs, pair-disjoint, balanced classes; multimodal (images + long heterogeneous text).

## Key Findings
- Exact-match: MERGED (Qwen2.5-7B-VL) 90.96% PR-AUC / 86.25% accuracy / $600 per 1M predictions / <1s per sample — vs Qwen2.5-32B-VL zero-shot 84.64 PR-AUC / $3,600 (6× cost) → +6.32 PR-AUC tại 6× lower cost; vs cùng backbone SFT human labels 77.17 → +13.79.
- Decomposition gain: human-label SFT 77.17 → model labels +3.50 (80.67) → +reasoning +6.14 (86.81) → +DPO +4.15 (90.96). Majority gain đến từ reasoning distillation + preference signal, không phải label source.
- Reward model ablation: High-confidence-correct 84.36, Longer-reasoning-correct 86.17, Meta-judge 90.96 — heuristic preference thua xa.
- Label-reasoning consistency (LLM-as-judge 0–100): 7B zero-shot 79.61, 32B zero-shot 81.91, 7B SFT 92.35, MERGED 92.82 (+13.21; SFT chiếm 12.74, DPO chỉ +0.47).
- Adaptation (variant task, 10K samples = 1/10 exact data): zero-shot 82.51; from-scratch SFT 83.18 (+0.67); from-scratch MERGED 85.53 (+3.02); exact-MERGED checkpoint + SFT 87.27; MERGED-adapt (SFT+DPO warm-start) 89.48 (+6.97 over zero-shot, beats from-scratch).

## Actionable Insights
- Khi definition thay đổi: đừng relabel — regenerate teacher supervision under new definition và re-run SFT+DPO từ checkpoint cũ; 10K samples đủ (+6.97 over zero-shot, beats from-scratch +3.02).
- Distill reasoning cùng label: model labels alone +3.50, thêm reasoning +6.14, thêm DPO +4.15 — label-only distillation bỏ lại majority value.
- Dùng disagreement làm asset: ambiguous pairs không phải noise — chúng là preference pairs quý nhất cho DPO; meta-judge (grounded-evidence criteria) beats heuristic (confidence/length) 90.96 vs 84.36/86.17.

## Assumptions & Limitations
- Label-reasoning consistency ≠ faithfulness (necessary but weaker condition) — chưa validate bằng human hay attribute-editing.
- Warm-start advantage confound: warm-start models đã thấy 10× exact-task data; exact checkpoint evaluated on variant WITHOUT training không được report.
- Dataset proprietary, không release (chỉ public prompts Appendix A); chỉ 1 transfer direction (exact→variant), Qwen-family baselines; K=2 teachers (ensemble size unexplored); meta-judge là one-time dependency khi generate data; no calibration/CI/per-language breakdown; no text-only ablation.

## Metadata
- NeurIPS 2026 Workshop VLM4RWD, 2026 (v2 2026-10-07), You-Lin Chen, Kyoungjun Park (UT Austin, intern Amazon), Abhishek Prasad, Ram Tripathi, Prithviraj Sen, Bin Xu, Pedro Herrero-Vidal (Amazon), cs.IR, https://arxiv.org/pdf/2609.01913
