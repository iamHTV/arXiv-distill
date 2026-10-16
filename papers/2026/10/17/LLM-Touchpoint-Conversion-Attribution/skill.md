# Skill: LOTUS Pairwise Touchpoint Selection (semantic attribution cho CVR)
Source: 2608.28649
Type: prompt-pattern / evaluation-method

## Khi nào dùng skill này
- Cần identify meaningful touchpoints trong full user behavior path cho conversion attribution, CVR training, ad credit allocation
- Heuristic rules (taxonomy/CF) bỏ sót semantically-related touchpoints (complementary products, shared scenario/IP)
- Cần labels chất lượng cao cho auxiliary conversion prediction task mà không fine-tune

Tình huống KHÔNG nên dùng: chỉ cần in-shop attribution (Base heuristic đủ); model <100B params (lag xa flagship — implicit F1 0.42–0.45 vs 0.51–0.56); cần online A/B evidence (paper chỉ offline GAUC).

## Input cần có
- User profile + conversion event (item, shop, category metadata)
- Candidate touchpoint (hoặc full behavior log cho listwise fallback) với product metadata: image, title, shop, category
- LLM flagship-class (≥100B params hoặc proprietary) với thinking mode

## Các bước thực hiện
1. Định nghĩa label criteria trong prompt: Explicit = shop/brand matching, leaf-category matching, CF-based similar-category matching; Implicit = (a) functional complementarity (camera + memory card), (b) scenario/audience alignment (shared anime IPs). 3 lớp: Irrelevant / Explicit / Implicit.
2. Pairwise judging: cho MỖI candidate touchpoint, gửi (user profile + 1 candidate + conversion) → model trả 3-way label. KHÔNG gửi cả list cùng lúc (listwise over-filter, recall thấp; gap pairwise-listwise 6–12pp với small models).
3. Aggregate: per-conversion precision/recall/F1 per class, macro-average across conversions; Overall F1 = (F1_Exp + F1_Imp)/2. Expected ceiling: explicit ~0.90, implicit ~0.54 — implicit luôn khó hơn ~0.4 F1.
4. (Optional) Feed labels xuống CVR model: selected touchpoints (Explicit + Implicit) làm positive samples cho auxiliary indirect conversion prediction task; expected offline GAUC +0.35pp over in-shop baseline, +0.15pp over heuristic cross-shop (CABB).
5. (Optional) Thinking mode: bật thinking cho listwise (+0.0196 avg gain); pairwise gain nhỏ (+0.0082) — prioritize pairwise protocol trước.

## Output mong đợi
- Per-touchpoint 3-way labels + relation types (taxonomy/CF/complementarity/scenario) → enriched conversion path cho attribution, CVR auxiliary task, ad credit allocation.
- Ví dụ: user mua camera → touchpoints: camera bag (explicit leaf-category), memory card (implicit functional complementarity), anime poster (implicit scenario alignment) — heuristic chỉ thấy camera bag.

## Ví dụ áp dụng
- E-commerce CVR: 1,000 conversions, 3-day lookback, ~70 touchpoints/conversion → pairwise judge mỗi touchpoint với GPT-5.5/GLM-5.1 → labels → auxiliary task → GAUC +0.35pp. Với 0.1pp GAUC ≈ substantial revenue growth, +0.35pp là material.

## Gotchas
- Implicit recall là bottleneck: listwise recall rất thấp (over-filter); pairwise recall 0.55–0.62 explicit, 0.44–0.56 implicit. Đo recall riêng, đừng只看 F1.
- Small models (<100B) lag nghiêm trọng trên implicit (Qwen3.5-27B implicit F1 0.4491 vs GPT-5.5 0.5567) — dùng flagship cho production.
- Thinking mode KHÔNG rescue small models nhiều (Qwen3.5-27B +0.0231 implicit listwise — vẫn thấp).
- Random-guessing F1 ≈ 0.1491 (implicit prevalence) — baseline để sanity-check model output.
- Labels từ LLM KHÔNG perfect (implicit F1 ceiling 0.54) — auxiliary task hưởng lợi từ volume, không yêu cầu precision tuyệt đối; nhưng đừng dùng làm sole ground truth cho high-stakes attribution decisions.
- Heuristic baselines KHÔNG được show cho annotators (contamination risk) — giữ nguyên khi build evaluation set riêng.
