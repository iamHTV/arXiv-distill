# 2609.05637 — Better Together: Complementary Query Rewriting Under a Strong RAG Baseline (EMNLP 2026)

## Problem
- Niềm tin phổ biến (LangChain MultiQueryRetriever): rewrite query thành nhiều variants cải thiện coverage. Nhưng hầu hết prior comparison rewrite trên retriever YẾU (bi-encoder trần, không reranking) → rewrite nào cũng trông tốt. Câu hỏi chưa trả lời: rewrite còn giúp khi search đã mạnh chưa?

## Contribution
- So sánh có kiểm soát, statistically rigorous: 6 methods dưới 1 pipeline cố định mạnh, 3 datasets, 3 seeds, paired-bootstrap significance.
- Kết quả complementarity: rewriting giúp bằng combination không phải replacement, validated bằng budget-matched controls; negative result có mechanism (tại sao combining fail trên AmbigNQ); confidence-gated router cost-aware.

## Method
- Pipeline cố định: bge-base-en-v1.5 dense retrieval, bge-reranker-base cross-encoder reranking, MMR diversification (λ=0.85), sentence chunking (512/50), score-based mixing (max similarity across variants, global top-K), GPT-4.1 (temp 0.7) cho mọi LLM generation. Multi-query variants quality-filtered (cosine tới original trong [0.4, 0.9]).
- 6 methods 3 families: S1 Parent (original query, không LLM call); S2 Neighbor (sibling questions — expensive, highest variance, most variations); S3 Synonym (reword, thesaurus-able); S4 Comparative (comparison question — cheapest trong S2–S4, 1 variant); HyDE (hypothetical answer passage); Query2Doc (pseudo-document appended).
- Datasets: HotpotQA (5,000 train examples), AmbigNQ (2,002 dev), EnterpriseRAG-Bench (511,958 synthetic docs, 470 answerable questions, Onyx, MIT license, kịch bản công ty "Redwood Inference"; ~60% queries không có relevant doc trong baseline top-10). Metrics: Recall@10, NDCG@10, MRR@10, HIT@10; significance paired bootstrap 2,000 iterations.

## Key Findings
- Solo: rewriting competitive at best, gains modest (0.2–3.7pp HIT@10). Best solo shifts theo dataset: S3 trên Enterprise (42.91, p=0.008 vs S1 39.22), S2 trên HotpotQA HIT@10 (97.65), Query2Doc trên HotpotQA Recall/NDCG; AmbigNQ multi-query methods +8pp NDCG@10, +10pp MRR@10 (p<0.001). S2 high-variance + highest runtime; S4 +2.4pp Enterprise (p=0.042), cheapest.
- Complementarity: rescue rate — Query2Doc cứu 14.8% S1 misses trên Enterprise, S3/S2 cứu 57.0%/56.7% trên AmbigNQ, HyDE/Query2Doc tới 62.1% trên HotpotQA. Oracle headroom: +1.72 HotpotQA, +2.72 AmbigNQ, +12.83 Enterprise (Jaccard@10 pairwise 0.14–0.45 trên Enterprise vs 0.55–0.99 trên AmbigNQ).
- Ensemble (seed-42, post-hoc): HotpotQA five-way 99.40 (oracle 99.37 — saturated); Enterprise four-way S1+S3+S4+HyDE 51.70 (+12.5 over S1, +8.3 over best solo Q2D 43.40, p<0.001), five-way 52.98 (+13.8, cách oracle 55.74 ~2.8pp). AmbigNQ: MỌI combination đều hại — five-way 92.96 vs best solo S3 95.45 (−2.49pp, p<0.001); reciprocal-rank fusion cũng fail.
- Budget-matched controls: TopK-100 reranking pool (5×) và multi-pass HNSW (4 index seeds) chỉ đạt ~44.3 HIT@10 (+5pp) = 40–41% của ensemble gain → ~60% là complementarity thật.
- Router (gate = S1 top-1 reranker score < τ=0.65 → chạy thêm Query2Doc và merge): Enterprise +4.33/+8.72 gain (~nửa) tại 39.0% queries expanded (2.6× fewer LLM calls); τ=0.70 → +6.17 tại 51.7%; AmbigNQ gần abstain (7.2%) giữ baseline (93.76 vs 93.67) — tự tránh loss; HotpotQA +0.52 tại 1.2%. Calibration transfer ≤2.55pp, held-out ≤0.11pp. Helper-agnostic: Q2D +4.33, HyDE +4.18, S4 +2.98.
- Router safety: 183/470 triggered, 11.3% wins, ~88% ties, ≤0.2% losses; 1,410 query-seed pairs chỉ 1 query degraded (0.07%).
- Answer quality (200-query Enterprise sample, GPT-4.1 reader): always-merge F1 +2.46 (p=0.003), router +1.92 (p=0.008) tại ~40% cost; gain localizes ở 75 triggered queries (+4.79 F1, p<0.01).
- Robustness: E5-base-v2 retriever pattern holds (S1 42.98, Q2D 44.26); Llama-3.3-70B generation = GPT-4.1 (95.47 both trên AmbigNQ S3).

## Actionable Insights
- Đừng hỏi "rewrite nào thắng" — hỏi "method nào fail trên query khác nhau". Thêm S3/S4 (modest solo) vào S1+HyDE+Q2D vẫn lift Enterprise 50.00→51.70/52.98 — solo performance KHÔNG predict ensemble value.
- Deploy router trước khi deploy always-merge: gate bằng S1 top-1 reranker score (threshold ~0.65, midpoint hit/miss distributions), helper mặc định Query2Doc (hoặc S4 khi cần cheap) — bắt ~nửa gain với ~40% cost, tự tắt trên corpus fusion-hostile.
- Check Jaccard@10 pairwise trước khi combining: overlap cao (0.55–0.99, nhiều relevant docs/query như AmbigNQ) → combining HẠI (−2.4pp); overlap thấp (0.14–0.45, enterprise) → combining lợi +12.8pp headroom.

## Assumptions & Limitations
- Ensembles post-hoc trên independently run strategies (không jointly executed system); router là heuristic simulation — cần production A/B test trước deploy.
- Answer-quality study: 1 reader model (GPT-4.1), 200 queries, SQuAD-style F1 chỉ partial capture long-form quality.
- Enterprise results từ 1 synthetic benchmark (EnterpriseRAG-Bench) — generalization chưa test.
- Memorization confound trên web QA (HotpotQA 2018, AmbigNQ 2020 có thể nằm trong pretraining GPT-4.1); EnterpriseRAG-Bench release May 2026 post-date mọi cutoff nên gains ở đó không phải memorization.
- Multi-variation strategies có real latency/cost (S2 cao nhất).

## Metadata
- EMNLP 2026 accepted, 2026 (v2 2026-09-09), Sara Shanian, Xiaoqin Yi, Pavlo Ruban, Kurt MacDonald (ServiceNow), cs.CL, https://arxiv.org/pdf/2609.05637
