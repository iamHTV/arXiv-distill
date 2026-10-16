# Skill: Execution-Grounded Query Refinement (detect-and-route loop for structured-query agents)
Source: 2609.12746
Type: framework / agent-workflow

## When to use this skill
- An agent generates executable queries (Text-to-Cypher/SPARQL/SQL) against a live database — well-formed-but-wrong queries execute silently and return misleading data
- You need to recover failed queries WITHOUT increasing the call budget for successful queries
- You are considering building a feedback-synthesis module (LLM-synthesised hints) — this paper shows that module is worth only ~1 point of exact match

Do NOT use: high-entropy output spaces (open-ended generation — sampling diversity helps); no executor/validator available (no hard failure signal to detect).

## Input required
- A live database connection + schema (for EXPLAIN pre-validation + LIMIT 1 execution)
- The question + a parsed schema (deterministic parser; LLM extraction only as fallback)
- A correction budget of N=2 validation cycles and M=1 relaxation pass
- A fixed relaxation hint set H_relax (six hints: case-insensitive regex, substring rather than equality, canonical datetime() formatting, dropping over-restrictive labels, simplifying RETURN)

## Steps
1. Schema Parsing (0 LLM calls): deterministically parse the raw schema → normalised nodes/properties/relationships (8 formats; LLM-extraction fallback only when the parser fails).
2. Generation (1 LLM call): a candidate query from the parsed schema + question.
3. Validation (0–2 calls): EXPLAIN against the live schema; execute with LIMIT 1. If both pass → RETURN IMMEDIATELY (total 1 call, the same as single-pass). On failure → parse the query (1 call) + a deterministic schema check (do the labels/relationship types/properties exist?); on violations → synthesise grounded hints H_val (1 call).
4. Correction (1 call): rewrite the query from the hints + schema Σ + correction history Γ (prompt instruction: do NOT repeat any prior attempt). Route back to step 3; loop until valid or N=2.
5. Execution (0 calls): run the validated query. Non-empty → return. Empty → inject H_relax (a constant, 0 calls) + one correction pass (M=1), then return the result (empty or not).
6. Do NOT build parallel sampling (Best-of-3 degrades quality 10.8–11.4% in low-entropy spaces); do NOT invest in feedback-synthesis sophistication — a raw database error string is equivalent within ±0.075 set-F1 (TOST p=0.002).

## Expected output
- Recovery of 91.7% of single-pass failures (pooled 93.8%), hit retrieval +11.8%.
- Cost: a successful query = 1 call; a failed query adds up to 3 calls per cycle; mean 1.1–2.5 calls per query depending on backbone.
- Per-metric caveats: order-sensitive GLEU over-reports against set equivalence (65.9% of pairs) and under-reports against semantics (33.9% of partial-BLEU queries are fully correct); the LLM judge is optimistic by ~9 points against blind human labels.
- Example: `WHERE org.name CONTAINS "new energy technologies"` (returns ∅) → inject H_relax → `WHERE org.name =~ '(?i).*new energy technologies.*'`.

## Example application
- A Graph RAG agent over a Neo4j knowledge graph: single-pass generation fails on 1,917/14,826 model–query pairs (13%) → the detect-and-route loop recovers 91.7% with the raw Neo4j error string (NO hint-synthesis module needed), at 3.14–4.19 mean pipeline stages per query but only 1.1–2.5 LLM calls (Schema Parsing + Execution + short-circuit Validation = 0 calls).

## Gotchas
- Empty-reference trap: 12.0% of queries have an empty reference result — the GLEU convention awards 1.0 to a non-empty output → a query that should return nothing scores perfectly; report strict set-theoretic metrics beside GLEU.
- The relaxation pass can INDUCE exactly that failure (returning something when nothing is correct) — monitor the empty-result rate post-relaxation.
- Schema-only validation (WITHOUT execution) triggers unnecessary rewrites when baseline quality is high — schema-only LAST-CQ slightly decreases GLEU on the 2 strongest models; execution evidence is necessary.
- Naive retry (raw error string) WINS on 1 of 6 models (DeepSeek 20.2% vs 17.9%) — schema-grounded hints are NOT always better; measure before adopting.
- Best-of-3 at T=0.7 makes the hit rate FALL (87.6%→85.2%) — temperature moves mass OFF the correct forms in low-entropy output spaces.
- Judge κ=0.63 inter-model ≠ human agreement (human–judge κ=0.48 three-way, 0.59 valid/invalid) — LLM–LLM agreement overstates validity by ~9 points.
- BLEU≥0.999 as an EM proxy understates order-invariant accuracy (naive 19.9%→22.6% under direct set equality); 2.9% of set-identical results score <1.0 purely from row ordering.
- The comparison set is conditioned on our own failures: a counterfactual retry measures relative correction quality under a shared detector, not end-to-end system quality.
- M=1 as a single-shot latch — larger M was never measured; do NOT extrapolate the recovery rate to multi-cycle relaxation.
