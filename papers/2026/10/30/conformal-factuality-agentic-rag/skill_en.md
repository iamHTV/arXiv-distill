# Skill: conformal-filtering-agentic-rag (conformal filtering for agentic RAG)

Source: 2610.34872v1
Type: framework / workflow

## When to use this skill

- RAG agent systems needing per-claim factuality guarantees.
- Need to report reliability and answer availability side by side, not just a single number.
- Ability to decompose responses into atomic claims and score relevance against retrieved documents.

Do NOT use this skill when:
- Every question must be answered regardless of evidence support.
- No calibration set is available to set the conformal threshold.

## Input needed

- Separate calibration and test sets (60 questions, 100 seeded 30/30 calibration–test partitions).
- Atomic claim decomposer.
- Retrieval-based relevance scorer.
- Similarity cutoff θ = 0.3, top-k = 10, max 3 retrieval operations and 3 policy decisions.
- Five conformal targets (80, 85, 90, 92.5, 95%) to select the production threshold.

## Steps to execute

1. After the RAG agent generates an answer, decompose it into atomic claims.
2. Score each claim's relevance against retrieved documents using Ragent(c; x) = max(0, max d∈Dπ(x) sret(d) sim(c, d)).
3. Set the conformal threshold λα from the calibration set using split-conformal order statistics: λα = V(kα) with kα = ⌈(n + 1)(1 − α)⌉.
4. Keep only claims with relevance ≥ λα: Fλ(C(x)) = {c ∈ C(x) : eR(c) ≥ λ}.
5. Generate the final answer from retained claims; if no claims are retained, the answer is empty (vacuously fully supported by convention).
6. Report both the full-support rate FS(λ) and non-empty response coverage NE(λ).

## Expected output

- Full-support rate 89–95% at the 95% target.
- Non-empty response coverage 17–60% at the 95% target (depends on model/dataset).
- Claim retention 10–43%, supported-claim fraction 90–98%.
- Clear reliability–informativeness trade-off.

## Example application

RAG agent answering general knowledge questions (TriviaQA): the agent performs adaptive evidence acquisition (up to 3 retrievals), then generates an answer. Apply the skill: decompose the answer into claims, score relevance against retrieved documents, keep only claims exceeding the 95% conformal threshold. Result: the answer contains only evidence-supported claims, full-support rate 95%, but only 60% of answers are non-empty (the rest are filtered empty). Report both metrics so users see the trade-off.

## Gotchas

- Higher conformal targets improve reliability but reduce answer availability; do not use a uniform threshold across all datasets.
- An empty claim set is vacuously fully supported by convention — report non-empty coverage alongside to avoid misinterpretation.
- Conformal filtering is post-generation and does not control when the agent stops retrieving.
- Small sample size (60 questions per dataset) may limit generalizability.
- Evaluated on only two models (GPT-6 Luna, Llama 3.1 8B) and three QA benchmarks.
