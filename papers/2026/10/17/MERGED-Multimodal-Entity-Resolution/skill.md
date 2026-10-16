# Skill: MERGED — Multi-Teacher Reasoning Distillation cho Entity Resolution
Source: 2609.01913
Type: framework / distillation-workflow

## Khi nào dùng skill này
- Task classification/relation evolving theo business definition (entity resolution, product matching, content moderation taxonomy) — cần adapt nhanh không relabel
- Cần compact model (7B) production-level accuracy tại cost/latency thấp (millions predictions/day)
- Có access large VLMs làm teacher nhưng không afford chạy chúng inference ở scale

Tình huống KHÔNG nên dùng: task có sẵn large human-labeled dataset quality cao (SFT human labels đủ); single-modal text-only task đơn giản (chưa validate text-only variant); cần faithfulness guarantee thật sự (paper chỉ đo consistency, không phải faithfulness).

## Input cần có
- 2 diverse teacher VLMs (>30B params, khác nhau — KHÔNG dùng 1 teacher)
- 1 meta-judge VLM (có thể là 1 trong teacher hoặc model khác)
- Student model compact (paper: Qwen2.5-7B-VL)
- Relation definition R dưới dạng prompt (ví dụ "exact match", "variant")
- Unlabeled pairs (text fields + images); human labels CHỈ cho evaluation
- SFT/DPO training infrastructure (token-level cross-entropy, DPO với β)

## Các bước thực hiện
1. Teacher generation: prompt K=2 teachers với same prompt (x, R); parse output thành (y, r, c) — label, reasoning trace, confidence [0,100]. Same prompt cho mọi teacher.
2. Route: agreement (y₁=y₂ + consistent evidence) → SFT set; disagreement (y₁≠y₂) → giữ lại 2 completions.
3. Meta-judge: với mỗi disagreement pair, judge chọn completion best follows R + grounded in observable evidence (criteria: favors specific matching/conflicting fields; penalizes vague/unsupported/contradicting rationale) → preference pair (chosen z⁺, rejected z⁻).
4. Stage 1 SFT: train student trên agreement set bằng token-level cross-entropy → πref.
5. Stage 2 DPO: continue từ πref, train trên preference pairs (β controls strength; KL giữ πθ trong ball quanh πref).
6. Scoring cho ranking metrics: p̂(y=1) = y·(½ + c/200) + (1−y)·(½ − c/200) — label + confidence kết hợp, không phải logit.
7. Adapt definition mới: regenerate teacher supervision under new R (chỉ ~10K samples), re-apply SFT+DPO TỪ existing checkpoint (warm-start) — KHÔNG from scratch.

## Output mong đợi
- 7B student: PR-AUC +13.79 over human-label SFT, +6.32 over 32B teacher zero-shot, cost $600/1M predictions (6× lower than teacher), <1s/sample; label-reasoning consistency +13.21 (92.82); adaptation với 10K samples: +6.97 over zero-shot.

## Ví dụ áp dụng
- E-commerce catalog 100K+ pairs, 8 languages: exact-match task MERGED = 90.96 PR-AUC. Definition đổi sang variant-match: warm-start từ exact checkpoint + 10K samples → 89.48 PR-AUC (vs zero-shot 82.51, from-scratch MERGED 85.53) — adapt trong days, không phải months.

## Gotchas
- KHÔNG dùng 1 teacher: single teacher có idiosyncratic interpretation + unstable trên ambiguous pairs → noisy supervision. Cần ≥2 diverse teachers.
- Disagreement là asset, không phải noise: bỏ disagreement pairs = mất preference data quý nhất; DPO stage đóng +4.15 PR-AUC.
- Meta-judge beats heuristic: high-confidence-correct 84.36, longer-reasoning-correct 86.17, meta-judge 90.96 — đừng chọn preference bằng confidence hay length.
- Consistency ≠ faithfulness: rationale supporting label không có nghĩa rationale đúng với evidence — cần human validation hoặc attribute-editing trước khi tin "reasoning".
- Warm-start confound: warm-start model đã thấy 10× data task gốc — so sánh fair cần evaluate original checkpoint trên task mới WITHOUT training (paper không report).
- SFT chiếm majority consistency gain (12.74/13.21); DPO mainly cải thiện discriminative reasoning, không phải consistency.
- Teacher cost là one-time (data generation); meta-judge also one-time — production inference chỉ chạy 7B student.
