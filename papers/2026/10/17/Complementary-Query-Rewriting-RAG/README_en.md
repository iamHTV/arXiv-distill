# 2609.05637 — Better Together: Complementary Query Rewriting Under a Strong RAG Baseline (EMNLP 2026)

## Problem
- Popular belief (LangChain MultiQueryRetriever): rewriting the user's question into several variants improves coverage. But most prior comparisons rewrite on top of a WEAK retriever (a bare bi-encoder, no reranking), which makes almost any rewrite look good. Unanswered question: does rewriting still help once search is already strong?

## Contribution
- A controlled, statistically rigorous comparison: six methods under one fixed strong pipeline, three datasets, three seeds, paired-bootstrap significance tests.
- The complementarity result: rewriting helps by combination, not replacement, validated against budget-matched controls; a negative result with its mechanism (why combining fails on AmbigNQ); and a cost-aware confidence-gated router.

## Method
- Fixed pipeline: bge-base-en-v1.5 dense retrieval, bge-reranker-base cross-encoder reranking, MMR diversification (λ=0.85), sentence chunking (512/50), score-based mixing (keep each document's max similarity across variants, take global top-K), GPT-4.1 (temp 0.7) for all LLM generation. Multi-query variants are quality-filtered (cosine to the original in [0.4, 0.9]).
- Six methods in three families: S1 Parent (original query, no LLM call); S2 Neighbor (sibling questions — expensive, highest variance, most variations); S3 Synonym (reword — thesaurus-approximable); S4 Comparative (comparison question — cheapest of S2–S4, one variant); HyDE (hypothetical answer passage); Query2Doc (pseudo-document appended to query).
- Datasets: HotpotQA (first 5,000 train examples, file order), AmbigNQ (full 2,002-query dev set), EnterpriseRAG-Bench (511,958 synthetic documents, 470 answerable questions; Onyx, MIT license; "Redwood Inference" simulated company; ~60% of queries have no relevant document in the baseline's top-10). Metrics: Recall@10, NDCG@10, MRR@10, HIT@10; significance via paired bootstrap (2,000 iterations).

## Key Findings
- Solo: rewriting is competitive at best; gains are modest (typically 0.2–3.7pp HIT@10). The best solo method shifts by dataset: S3 on Enterprise (42.91, p=0.008 vs S1's 39.22), S2 on HotpotQA HIT@10 (97.65), Query2Doc on HotpotQA Recall/NDCG; on AmbigNQ multi-query methods beat the baseline by +8pp NDCG@10 and +10pp MRR@10 (p<0.001). S2 is high-variance with the highest runtime; S4 adds +2.4pp on Enterprise (p=0.042) and is the cheapest rewriting strategy.
- Complementarity: rescue rates — Query2Doc rescues 14.8% of S1's misses on Enterprise; S3 and S2 rescue 57.0%/56.7% on AmbigNQ; HyDE/Query2Doc rescue up to 62.1% on HotpotQA. Oracle-union headroom over the best solo: +1.72 (HotpotQA), +2.72 (AmbigNQ), +12.83 (Enterprise); Enterprise pairwise Jaccard@10 is 0.14–0.45 (diverse) vs 0.55–0.99 on AmbigNQ (overlapping).
- Ensembles (post-hoc seed-42): HotpotQA five-way 99.40 (oracle 99.37 — saturated); Enterprise four-way S1+S3+S4+HyDE 51.70 (+12.5 over S1, +8.3 over best solo Query2Doc 43.40, p<0.001) and five-way 52.98 (+13.8, within ~2.8 points of the 55.74 oracle). AmbigNQ: EVERY combination underperforms the best solo (five-way 92.96 vs S3's 95.45, −2.49pp, p<0.001); reciprocal-rank fusion fails too.
- Budget-matched controls: S1 with a TopK-100 reranking pool (5× default) and S1 with multi-pass HNSW (4 index seeds) converge to ~44.3 HIT@10 (+5pp) — only 40–41% of the four-way ensemble's +12.5pp gain, so ~60% is genuine complementarity.
- Router (gate: run Query2Doc and merge only when S1's top-1 reranker score < τ=0.65): Enterprise captures +4.33 of the +8.72 full-merge gain (~half) while expanding only 39.0% of queries (2.6× fewer LLM calls); τ=0.70 reaches +6.17 at 51.7% expanded. AmbigNQ: nearly abstains (7.2% expanded) and holds baseline (93.76 vs 93.67), automatically avoiding the loss that always-merging incurs. HotpotQA: +0.52 at 1.2% expansion. Calibration transfers across datasets (≤2.55pp) and generalizes to held-out queries (≤0.11pp). Helper-agnostic: Query2Doc +4.33, HyDE +4.18, S4 +2.98.
- Router safety: on Enterprise 183/470 queries trigger; 11.3% wins, ~88% ties, ≤0.2% losses; across 1,410 query-seed pairs only 1 query is actively degraded (0.07%).
- Answer quality (200-query Enterprise sample, GPT-4.1 reader): always-merge improves F1 +2.46 (p=0.003), the router +1.92 (p=0.008) at ~40% of the expansion cost; the gain localizes to the 75 router-triggered queries (+4.79 F1, p<0.01).
- Robustness: replacing the retriever with E5-base-v2 keeps the pattern (S1 42.98, Query2Doc 44.26); replacing GPT-4.1 with Llama-3.3-70B for generation gives identical AmbigNQ S3 results (95.47 both).

## Actionable Insights
- Stop asking "which rewrite wins"; ask "which methods fail on different questions." Adding modest solo performers (S3, S4) to S1+HyDE+Query2Doc still lifts Enterprise from 50.00 to 51.70/52.98 — solo performance does NOT predict ensemble value.
- Deploy the router before ever deploying always-merge: gate on S1's top-1 reranker score (threshold ≈0.65, the midpoint of hit/miss score distributions), default helper Query2Doc (or S4 when expansion calls must be cheap) — capture ~half the gain at ~40% of the cost, with auto-disable on fusion-hostile corpora.
- Check pairwise Jaccard@10 before combining: high overlap (0.55–0.99, multi-relevant queries like AmbigNQ) makes combining HARMFUL (−2.4pp); low overlap (0.14–0.45, enterprise-style) offers +12.8pp headroom.

## Assumptions & Limitations
- Ensembles are post-hoc analyses over independently run strategies, not a jointly executed system; the router is a cost-aware heuristic evaluated in simulation — production A/B testing is required before deployment.
- The answer-quality study uses one reader model (GPT-4.1), 200 queries from one benchmark, and SQuAD-style F1 only partially captures long-form answer quality.
- Enterprise results come from a single synthetic benchmark (EnterpriseRAG-Bench); generalization to other enterprise corpora is untested.
- Memorization confound on web QA (HotpotQA 2018 and AmbigNQ 2020 plausibly appear in GPT-4.1's pretraining); EnterpriseRAG-Bench was released May 2026, post-dating all retriever/reranker/LLM cutoffs, so its gains cannot be memorization.
- Multi-variation strategies carry real latency and cost (S2 highest).

## Metadata
- EMNLP 2026 accepted, 2026 (v2 2026-09-09), Sara Shanian, Xiaoqin Yi, Pavlo Ruban, Kurt MacDonald (ServiceNow), cs.CL, https://arxiv.org/pdf/2609.05637
