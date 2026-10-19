# Skill: embedding-surgery
Source: 2609.05110v1
Type: framework

## When to use this skill
- A dense retrieval system (search, recommendation, RAG) needs to correct specific ranking errors per query without retraining or re-indexing.
- Feedback signals are available (editorial, user interactions, LLM pseudo-labels) to identify more relevant vs. less relevant documents.
- Want to apply localized, minimal updates to document embeddings at query time.

## When NOT to use this skill
- Assuming document embeddings never need to change (feedback and search intent are perfectly stable).
- Using LLM pseudo-labels as the sole feedback source without quality checks (LLM labels have systematic weaknesses).

## Required inputs
- A dense retrieval system with indexed document embeddings (FAISS, HNSW, IVF, etc.).
- Feedback signals: editorial judgments, user interactions (clicks), or LLM pseudo-labels (BGE, Qwen rerankers).
- A convex optimization solver (CVXPY or equivalent) on a single CPU core.
- Computational budget per query (surgery is performed independently per query).

## Steps
1. Retrieve top-k documents for the query via the existing dense retrieval system (e.g., k=20).
2. Receive feedback signals for the query: identify preference pairs (dr, dn) where dr should be ranked above dn (from editorial, simulated user interactions, or LLM reranker).
3. Formulate the convex optimization problem: minimize Σ∥Δdi∥2^2 over top-k documents subject to ⟨q, dr + Δdr⟩ ≥ ⟨q, dn + Δdn⟩ + ε for all (dr, dn) ∈ R.
4. Choose the surgery variant: symmetric (default, both adjust — most effective), demotion (only less relevant modified), promotion (only more relevant modified).
5. Solve the quadratic program (CVXPY) to obtain the updates Δdi.
6. Apply updates immediately to the index (in-place overwriting): d'i = di + Δdi; only modify embeddings of documents involved in constraints; all other embeddings remain unchanged.
7. Re-rank with the corrected embeddings and return results for the query.
8. (Optional) Combine with CoRocchio (query adaptation) for additional gains.

## Expected output
- Consistent nDCG@10 accuracy improvements, up to +60.64% relative (TAS-B on DL-Hard under editorial feedback); localized updates preserving the global embedding space structure; safe application on ANN indexes (IVF, HNSW) without costly re-indexing.

## Example application
- Enterprise internal document search: when a user indicates that result #3 is more relevant than result #1 for the query "checkout procedure", apply embedding surgery to boost embedding of result #3 and/or demote result #1, then re-rank results for the same query going forward.

## Gotchas
- Do not use LLM pseudo-labels as the sole feedback source without quality checks (LLM labels have systematic weaknesses and cannot fully replace human relevance assessments).
- Near-random click behavior yields limited gains and can marginally degrade original retrieval effectiveness (Robust '04).
- Do not forget to preserve the global embedding space structure — updates must be minimal (minimize ∥Δdi∥2^2).
- Do not retrain or re-index after each feedback — that is the key advantage of embedding surgery.

## Self-check
- Can someone who has not read the original paper follow these 8 steps? [YES] — each step is a concrete action.
- Which step is most vague? Step 3 (formulating the convex optimization problem with ranking constraints) needs a concrete CVXPY implementation.
- Is the Input section sufficient? [YES] — dense retrieval system, feedback signals, convex solver, computational budget are all covered.

## Dry run (hypothetical scenario)
- Scenario: Enterprise internal document search; a user indicates result #3 is more relevant than result #1 for the query "checkout procedure".
- Run the skill: (1) Retrieve top-20 documents for the query; (2) identify preference pair (result #3, result #1) from feedback; (3) formulate convex optimization problem with ranking constraint result #3 above result #1; (4) choose symmetric variant; (5) solve via CVXPY to get Δembedding; (6) apply in-place overwriting to the index; (7) re-rank with corrected embeddings and return results.

## Verdict: [SKILL VALID]
