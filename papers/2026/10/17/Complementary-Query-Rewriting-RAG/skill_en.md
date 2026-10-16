# Skill: Complementary Rewrite Router (cost-aware query rewriting for strong RAG)
Source: 2609.05637
Type: deployment-workflow / evaluation-method

## When to use this skill
- Your RAG pipeline already has dense retrieval + cross-encoder reranking + MMR, and you want to add query rewriting without wasting an LLM call on every query
- A large corpus (enterprise, 100K+ docs) where ~60% of queries have no relevant document in the baseline top-10
- You need to know BEFORE combining whether the corpus is fusion-friendly (low overlap) or fusion-hostile (high overlap)

Do NOT use: no reranker in the loop (the paper's results don't transfer — rewriting looks better on weak baselines but that's an artifact); high-overlap multi-relevant corpora (AmbigNQ-style) where combining HURTS; latency budget that can't afford a second retrieval pass.

## Input required
- Fixed pipeline: dense retriever (paper: bge-base-en-v1.5), cross-encoder reranker (bge-reranker-base), MMR (λ=0.85)
- An LLM for rewriting/generation (paper: GPT-4.1, temp 0.7)
- A helper expansion strategy: Query2Doc (peak accuracy), HyDE (nearly as good), or S4 Comparative (cheapest, +2.98 on Enterprise)
- A representative query set to calibrate threshold τ

## Steps
1. Run baseline S1 (original query, no LLM) and collect the top-1 reranker score per query. Compute mean score of hits vs misses (paper, Enterprise: hit 0.711±0.047, miss 0.612±0.085). Set τ = midpoint (paper: 0.65), tuned NOT against the evaluation metric.
2. (Overlap audit) Compute pairwise Jaccard@10 between methods on a sample of queries: <0.5 → combining pays (enterprise regime); >0.55 → combining may hurt, skip step 4.
3. Deploy the router: for queries with S1 top-1 score < τ, also run the helper (Query2Doc by default; S4 if expansion calls must be cheap) and merge the two result lists with score-based mixing (max similarity, global top-K). Queries ≥ τ return S1 alone.
4. (Optional, low-overlap corpora) Post-hoc ensemble: merge the top-20 pools of S1 + S3 + S4 + HyDE (+ Query2Doc) — enterprise gain +12.5 to +13.8pp HIT@10; do NOT apply on high-overlap corpora.
5. Monitor: % of queries expanded (expected 1–40% depending on corpus difficulty), win/tie/loss on triggered queries (target >10% wins, <1% losses), and answer F1 on a sample.
6. Tune τ to the cost budget: lower τ → more expansion (τ=0.55: +2.20, 23.1% expanded); higher τ → less (τ=0.70: +6.17, 51.7%); τ≥0.75 degenerates to always-merge (wasteful).

## Expected output
- About half of the full-merge gain (paper: +4.33 HIT@10 on Enterprise) at ~40% of the rewriting cost; answer F1 +1.92 (p<0.01); auto-disable on fusion-hostile corpora (7.2% expanded, baseline held); <0.1% of queries degraded.

## Example application
- EnterpriseRAG-Bench (512K docs, 470 queries): baseline S1 HIT@10 = 39.22. Router at τ=0.65: 39% of queries trigger Query2Doc → HIT@10 43.55 (+4.33), while always-merge reaches 47.94 at 2.6× the LLM calls. On AmbigNQ the router fires on only 7.2% and holds 93.76 (vs always-merge 93.42 — a LOSS of −0.25).

## Gotchas
- Measure the hit/miss score distribution BEFORE setting τ — if the top-1 score doesn't separate hits from misses (weak separation like AmbigNQ), the router is useless.
- Do NOT combine on high-overlap corpora: Jaccard@10 0.55–0.99 (S2–S4 pairs ≈0.99) makes max-score merging crowd out the small relevant set with high-scoring non-relevant docs: −2.49pp (p<0.001).
- S2 (Neighbor) is high-variance with the highest runtime — its value is ensemble diversity, not solo reliability; prefer S4 when you need a cheap member.
- Solo performance does NOT predict ensemble value: S3/S4 are modest solo but still lift S1+HyDE+Q2D from 50.00 to 51.70.
- The budget-matched control reminds you: if ~40% of your gain also comes from deeper reranking (TopK-100), only the remaining ~60% is genuine complementarity — don't attribute the whole gain to rewriting.
- Old web-QA datasets (HotpotQA 2018, AmbigNQ 2020) carry a memorization confound; post-cutoff synthetic enterprise data is the clean evidence.
- The router is a simulated heuristic — production needs an A/B test of latency and cost under load before concluding.
