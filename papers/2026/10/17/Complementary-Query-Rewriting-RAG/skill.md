# Skill: Complementary Rewrite Router (query rewriting cost-aware cho RAG mạnh)
Source: 2609.05637
Type: deployment-workflow / evaluation-method

## Khi nào dùng skill này
- RAG pipeline đã có dense retrieval + cross-encoder reranking + MMR — muốn thêm query rewriting mà không phí LLM call mỗi query
- Corpus lớn (enterprise, 100K+ docs) nơi ~60% queries không có relevant doc trong top-10 baseline
- Cần biết TRƯỚC khi combining: corpus này fusion-friendly (low overlap) hay fusion-hostile (high overlap)

Tình huống KHÔNG nên dùng: retriever chưa rerank (kết quả paper không áp dụng — rewriting trông tốt hơn trên weak baseline nhưng đó là artifact); corpus multi-relevant cao overlap (AmbigNQ-style) — combining sẽ HẠI; latency budget không cho phép 2nd retrieval pass.

## Input cần có
- Fixed pipeline: dense retriever (paper: bge-base-en-v1.5), cross-encoder reranker (bge-reranker-base), MMR (λ=0.85)
- LLM cho rewrite/generation (paper: GPT-4.1 temp 0.7)
- Helper expansion strategy: Query2Doc (peak accuracy), HyDE (gần bằng), hoặc S4 Comparative (cheapest, +2.98 Enterprise)
- 1 tập queries representative để calibrate threshold τ

## Các bước thực hiện
1. Chạy baseline S1 (original query, không LLM) → lấy top-1 reranker score mỗi query. Tính mean score của hit vs miss (paper Enterprise: hit 0.711±0.047, miss 0.612±0.085). Đặt τ = midpoint (paper: 0.65), KHÔNG tune trên eval metric.
2. (Audit overlap) Tính pairwise Jaccard@10 giữa các method trên sample queries: <0.5 → combining lợi (enterprise regime); >0.55 → combining có thể hại, bỏ bước 4.
3. Deploy router: query nào có S1 top-1 score < τ → chạy thêm helper (Query2Doc mặc định; S4 nếu cần cheap) và merge 2 result lists bằng score-based mixing (max similarity, global top-K). Query ≥ τ → trả S1 alone.
4. (Optional, low-overlap corpus) Ensemble post-hoc: merge top-20 pools của S1 + S3 + S4 + HyDE (+Query2Doc) — enterprise gain +12.5 đến +13.8pp HIT@10; KHÔNG áp dụng trên high-overlap corpus.
5. Monitor: % queries expanded (expected 1–40% tùy corpus difficulty), win/tie/loss trên triggered queries (target >10% wins, <1% losses), answer F1 trên sample.
6. Tune τ theo cost budget: τ thấp → expand nhiều (τ=0.55: +2.20, 23.1%); τ cao → expand ít (τ=0.70: +6.17, 51.7%); τ≥0.75 = always-merge (lãng phí).

## Output mong đợi
- ~Nửa full-merge gain (paper: +4.33 HIT@10 Enterprise) tại ~40% rewriting cost; answer F1 +1.92 (p<0.01); auto-disable trên fusion-hostile corpus (7.2% expanded, giữ baseline); <0.1% queries bị degrade.

## Ví dụ áp dụng
- EnterpriseRAG-Bench (512K docs, 470 queries): baseline S1 HIT@10 39.22. Router τ=0.65: 39% queries trigger Query2Doc → HIT@10 43.55 (+4.33), trong khi always-merge đạt 47.94 nhưng tốn 2.6× LLM calls. Trên AmbigNQ router chỉ fire 7.2% và giữ 93.76 (vs always-merge 93.42 — LỖI −0.25).

## Gotchas
- Đo hit/miss score distribution TRƯỚC khi đặt τ — nếu top-1 score không phân biệt hit/miss (weak separation như AmbigNQ), router vô dụng.
- KHÔNG combine trên high-overlap corpus: Jaccard@10 0.55–0.99 (S2–S4 pairs ~0.99) → max-score merge đẩy high-scoring non-relevant docs crowd out relevant set, −2.49pp (p<0.001).
- S2 (Neighbor) high-variance + highest runtime — giá trị nằm ở ensemble diversity, không phải solo reliability; prefer S4 khi cần cheap member.
- Solo performance KHÔNG predict ensemble value: S3/S4 modest solo nhưng thêm vào S1+HyDE+Q2D vẫn lift 50.00→51.70.
- Budget-matched control nhắc nhở: nếu gain của bạn ≈ 40% từ deeper reranking (TopK-100) thì ~60% còn lại mới là complementarity thật — đừng quy toàn bộ gain cho rewriting.
- Web-QA datasets cũ (HotpotQA 2018, AmbigNQ 2020) có memorization confound; enterprise synthetic post-cutoff mới là bằng chứng clean.
- Router là heuristic simulation — production cần A/B test latency + cost under load trước khi kết luận.
