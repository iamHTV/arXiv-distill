# Skill: Incremental Pooled LLM Evaluation (benchmark retrieval models tiết kiệm cost)
Source: 2609.02745
Type: evaluation-method / workflow

## Khi nào dùng skill này
- Production RAG cần so sánh/chọn retrieval model (embedding families, dense/sparse/hybrid) mà KHÔNG có gold qrels hoặc qrels quá expensive
- Embedding models mới released thường xuyên (quarterly vendor updates) — cần stable historical benchmark cho governance
- Đang mở rộng benchmark (thêm systems) — muốn reuse previous judgments thay vì re-run toàn bộ

Tình huống KHÔNG nên dùng: cần resolve effectively tied systems (gap <0.001 nDCG — neither qrels nor pseudolabels distinguish được); cần per-document certification (judge consistency 93–96% exact); domain specialist relevance criteria quan trọng (TREC-COVID correlation chỉ 0.64–0.82 — gap general LLM vs specialist assessors).

## Input cần có
- Query set Q (production-representative: factual + multi-hop + real user queries; KHÔNG instruction-framed queries cho retrieval evaluation)
- Candidate retrieval systems {S1..SN} (dense/sparse/hybrid configurations)
- Top-k retrieval depth (paper dùng k=100)
- LLM judge pinned version (GPT-4.1 gpt-4.1-2025-04-14 hoặc tương đương), temperature 0.0
- Graded relevance prompt 3-point scale (0/1/2) với brief CoT ("thought" ≤2 lines) + structured JSON output
- (Tuỳ chọn) gold qrels cho calibration/validation subset

## Các bước thực hiện
1. Retrieve: mỗi system Si × query q → top-k Ri(q).
2. Pool: P(q) = ∪ Ri(q) — union of documents, KHÔNG duplicate.
3. Judge: mỗi unique (q,d) pair — single-turn prompt, no in-context examples, no system-level calibration; record judge version + temperature trong metadata.
4. Evaluate: compute P@k, R@k, nDCG@k, MAP cho mỗi system dùng shared judgments restricted to Ri(q). Lưu ý: pseudolabel nDCG inflated +0.1–51%, recall deflated −17–39% (uniform across systems) → so sánh ORDINAL rankings, KHÔNG so sánh absolute scores với human-scale metrics.
5. Incremental expansion: system S_{N+1} mới → retrieve + judge CHỈ R_{N+1}(q)\P(q); reuse mọi previous judgments exactly; new system immediately comparable. KHÔNG re-run previous judgments.
6. Bootstrap validate (B=10,000 resample queries, recompute macro metric, re-rank): pair (A,B) "qrels-uncertain" nếu swap probability >5% → effectively tied, KHÔNG quyết định model trên cặp đó.
7. Judge continuity: nếu update judge model → selective re-judging 1,000-sample validates continuity (cross-judge binarized agreement 84–92%, system-level ρ=0.89–0.92).

## Output mong đợ
- System rankings (P@k, R@k, nDCG@k, MAP) với Spearman/Kendall correlation vs gold (nếu có): expect nDCG@10 ρ=0.69–0.95 trên domains general; 74% pairwise disagreements within qrels bootstrap noise.
- Reuse rate 65–80% (production: 79.6%, 4.9× cost reduction); incremental growth 5→62 systems trong 4 weeks ≈ $800 (GPT-4.1 pricing).
- Ranking stability: no meaningful-gap pair (Δ>0.001) reverses under pool growth; fragile pairs = statistically indistinguishable pairs.
- Ví dụ: financial news QA — top-5 all hybrid, chọn hybrid-emb3-large-256 (MAP 0.459 ≈ 768's 0.461) cho production vì latency + embedding cost.

## Ví dụ áp dụ
- E-commerce search RAG: 3 systems ban đầu (dense-emb3-large, dense-nomic-1.5, BM25) → pool ~50K judgments; 2 tháng sau thêm hybrid-cohere-v4 → judge chỉ ~15K new docs (65% reuse) → so sánh ngay MAP/nDCG@10 với 3 systems cũ; bootstrap cho thấy top-2 gap 0.000014 → effectively tied → chọn theo latency/cost thay vì score.

## Gotchas
- KHÔNG dùng classical TREC pooling (unjudged = non-relevant): penalises novel systems 0.033–0.055 nDCG@10 (FiQA 8 swaps, TREC-COVID 10 swaps) — pooled LLM judging removed all 19 ranking errors.
- KHÔNG so sánh absolute pseudolabel scores với human metrics: nDCG inflated +0.1–51%, recall deflated −17–39% — chỉ ordinal rankings đáng tin.
- Macro-averaged invariance KHÔNG guaranteed theoretically — fragile pairs (Δ<0.001) có thể reverse under pool growth (FiQA 53.8% orderings, but same pair differ 0.000014) → luôn check bootstrap swap probability trước khi kết luận.
- KHÔNG dùng instruction-framed queries cho retrieval evaluation (degrade ALL systems ΔMAP −0.039 by diluting retrieval signal); KHÔNG dùng query expansion cho well-formed queries (MAP 0.424 vs 0.459) — expansion chỉ robustness mechanism cho verbose formulations (−4.8pp → −1.1pp recall penalty).
- Judge pin version + T=0 mandatory — drift within campaign precluded by design; nếu provider deprecates pinned checkpoint → re-judge strategy.
- Higher dimensions improve dense (+0.029) nhưng hybrid narrowing gap (+0.012) — BM25 fusion compensates low dimensionality → 256-dim hybrid ≈ 1536-dim dense với cost thấp hơn.
- P@10 less stable (sensitivity to small number of judgments per query) — dùng nDCG@10/R@100/MAP làm primary metrics.
- Domain matters: biomedical/specialist domains (TREC-COVID) correlation thấp hơn (0.64–0.82) — general-purpose LLM judge gap vs specialist assessors.
