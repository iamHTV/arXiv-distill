# Skill: Incremental Pooled LLM Evaluation (cost-effective retrieval model benchmarking)
Source: 2609.02745
Type: evaluation-method / workflow

## When to use this skill
- A production RAG system needs to compare/select retrieval models (embedding families, dense/sparse/hybrid) without gold qrels or with prohibitively expensive qrels
- New embedding models are released regularly (quarterly vendor updates) — you need a stable historical benchmark for governance
- You are expanding a benchmark (adding systems) and want to reuse previous judgments instead of re-running everything

Do NOT use: you need to resolve effectively tied systems (gap <0.001 nDCG — neither qrels nor pseudolabels can distinguish them); you need per-document certification (judge consistency is 93–96% exact); domain-specialist relevance criteria matter (TREC-COVID correlation is only 0.64–0.82 — the gap between a general LLM and specialist assessors).

## Input required
- A query set Q (production-representative: factual + multi-hop + real user queries; NO instruction-framed queries for retrieval evaluation)
- Candidate retrieval systems {S1..SN} (dense/sparse/hybrid configurations)
- A top-k retrieval depth (paper uses k=100)
- A pinned LLM judge version (GPT-4.1 gpt-4.1-2025-04-14 or equivalent), temperature 0.0
- A graded relevance prompt on a 3-point scale (0/1/2) with a brief CoT ("thought" ≤2 lines) + structured JSON output
- (Optional) gold qrels for calibration/validation on a subset

## Steps
1. Retrieve: each system Si × query q → top-k Ri(q).
2. Pool: P(q) = ∪ Ri(q) — the union of documents, no duplicates.
3. Judge: each unique (q,d) pair — single-turn prompt, no in-context examples, no system-level calibration; record the judge version + temperature in the metadata.
4. Evaluate: compute P@k, R@k, nDCG@k, MAP for each system using the shared judgments restricted to Ri(q). Note: pseudolabel nDCG is inflated +0.1–51% and recall deflated −17–39% (uniform across systems) → compare ORDINAL rankings, NOT absolute scores against human-scale metrics.
5. Incremental expansion: a new system S_{N+1} → retrieve + judge ONLY R_{N+1}(q)\P(q); reuse all previous judgments exactly; the new system is immediately comparable. Do NOT re-run previous judgments.
6. Bootstrap validation (B=10,000 resample queries, recompute the macro metric, re-rank): a pair (A,B) is "qrels-uncertain" if the swap probability >5% → effectively tied — do NOT decide the model on that pair.
7. Judge continuity: if the judge model is updated → selective re-judging of a 1,000-pair sample validates continuity (cross-judge binarized agreement 84–92%, system-level ρ=0.89–0.92).

## Expected output
- System rankings (P@k, R@k, nDCG@k, MAP) with Spearman/Kendall correlation vs gold (if available): expect nDCG@10 ρ=0.69–0.95 on general domains; 74% of pairwise disagreements fall within qrels bootstrap noise.
- Reuse rate 65–80% (production: 79.6%, a 4.9× cost reduction); incremental growth from 5 to 62 systems over 4 weeks ≈ $800 (GPT-4.1 pricing).
- Ranking stability: no meaningful-gap pair (Δ>0.001) reverses under pool growth; fragile pairs are the statistically indistinguishable ones.
- Example: a financial news QA system — the top-5 are all hybrid, selecting hybrid-emb3-large-256 (MAP 0.459 ≈ the 768-dim 0.461) for production because of latency + embedding cost.

## Example application
- An e-commerce search RAG: 3 initial systems (dense-emb3-large, dense-nomic-1.5, BM25) → pool ~50K judgments; two months later add hybrid-cohere-v4 → judge only ~15K new docs (65% reuse) → compare MAP/nDCG@10 against the 3 existing systems immediately; bootstrap shows the top-2 gap is 0.000014 → effectively tied → choose by latency/cost instead of score.

## Gotchas
- Do NOT use classical TREC pooling (unjudged = non-relevant): it penalises novel systems by 0.033–0.055 nDCG@10 (FiQA 8 swaps, TREC-COVID 10 swaps) — pooled LLM judging removed all 19 ranking errors.
- Do NOT compare absolute pseudolabel scores against human metrics: nDCG inflated +0.1–51%, recall deflated −17–39% — only ordinal rankings are trustworthy.
- Macro-averaged invariance is NOT guaranteed theoretically — fragile pairs (Δ<0.001) can reverse under pool growth (FiQA 53.8% of orderings, but the same pair differs by 0.000014) → always check the bootstrap swap probability before concluding.
- Do NOT use instruction-framed queries for retrieval evaluation (they degrade ALL systems by ΔMAP −0.039 by diluting the retrieval signal); do NOT use query expansion on well-formed queries (MAP 0.424 vs 0.459) — expansion is only a robustness mechanism for verbose formulations (−4.8pp → −1.1pp recall penalty).
- Pin the judge version + T=0 — mandatory; drift within a campaign is precluded by design; if the provider deprecates the pinned checkpoint, a re-judging strategy is needed.
- Higher dimensions improve dense (+0.029) but hybrid narrows the gap (+0.012) — BM25 fusion compensates for low dimensionality → 256-dim hybrid ≈ 1536-dim dense at lower cost.
- P@10 is less stable (sensitivity to a small number of judgments per query) — use nDCG@10/R@100/MAP as primary metrics.
- Domain matters: biomedical/specialist domains (TREC-COVID) show lower correlation (0.64–0.82) — the general-purpose LLM judge gaps against specialist assessors.
