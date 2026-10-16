# Skill: Query-Free LLM Relevance Judge Pipeline
Source: 2610.14550
Type: evaluation-method (offline relevance metric cho retrieval/ads không có query)

## Khi nào dùng skill này
- Đánh giá offline hệ thống retrieval/recommendation/ads mà không có explicit query (chỉ có engagement history)
- Cần metric correlate với online KPI (CTR/CVR) trước khi chạy A/B test tốn kém
- LLM judge quá đắt để gọi trên mọi event–candidate pair ở production volume
- KHÔNG nên dùng: search retrieval (có query — dùng metric chuẩn), hoặc catalog nhỏ không cần scale

## Input cần có
- Engagement history H_u = {(product, event_type)} per user (view, add-to-cart, purchase...)
- Multimodal product embedding (có sẵn) + candidate set từ retrieval
- Calibration split có human label (đủ để bootstrap)
- Teacher LLM (Gemini-2.5-Pro class) + verifier LLM thứ hai + human auditor

## Các bước thực hiện
1. Nén history: gán SID (Semantic ID) cho mỗi product bằng RQ-kmeans (L=3 stage, codebook 512); nhóm theo (SID prefix, event type); chọn đại diện = product gần nhất; weight w_g = log(1+|g|)·β(e_g) với β(purchase)=3, add-to-cart=2, khác=1.
2. Agentic guideline discovery: seed prompt taxonomy 5 tầng (Exact/Similar/Substitute/Complementary/Irrelevant) KHÔNG có định nghĩa → teacher label calibration split → cluster cặp lỗi theo confusion + rationale → reasoner propose ≤3 sub-rule → chấp nhận iff paired-bootstrap 95% CI trên Δaccuracy loại trừ 0 và không per-class F1 regression >0.5pp; chạy nhiều trial, chỉ giữ rule lặp lại.
3. Human business-alignment pass: audit 3 tiêu chí (business-critical mismatch: demographic, regulated category, advertiser exclusion; editorial standard; reproducibility trên 200 cặp business-stratified); rule bị veto → trả Phase A kèm note.
4. Distillation: build corpus 4 stage (stratified seed sampling; multi-source candidates: retrieval logs + conversion signals + advertiser groups; hard-case mining N=10/seed bằng multimodal embedding filter; teacher label + rationale). Teacher + verifier GPT-5-class chạy song song; đồng thuận confidence cao → chấp nhận, disagreement → human.
5. Fine-tune student (Gemini-2.5-Flash class): LoRA rank 16, lr multiplier 2, 5 epochs; multi-label classification + attribute-level rationale. Deploy student làm judge J.
6. Compute metric: MicroRel/MacroRel under threshold-k aggregation, k≈7 (peak [5,7]); validate Pearson vs online CTR/CVR/CP trước khi dùng làm gate.

## Output mong đợi
- Offline relevance metric correlate với conversion P/R, directionally aligned CTR/CVR delta; judge latency ~750ms p50, ~18 QPS (~9× teacher); LLM calls giảm ~30× nhờ SID compression.

## Ví dụ áp dụng
- App content recommendation: nén 30-day interaction history thành intent set, judge mỗi candidate content theo intent tiers, dùng MicroRel làm gate trước khi A/B test feed algorithm mới.

## Gotchas
- Prompt-only student giữ p95 dài như teacher (8,807ms) — phải fine-tune, không chỉ prompt, để nén latency.
- Rule demographic quá hiếm trong calibration set → agentic loop deprioritize — human pass là load-bearing, đừng bỏ.
- Recency truncation (last 1-day) trông ổn trên online metric (±0.03–0.06) nhưng halves intent fidelity (Spearman 0.53) — đừng dùng metric online để chọn cách nén.
- k quá thấp (k=1) quy 1 weak intent match = broad coverage; k quá cao (>8) candidate pass-rate <5%.
