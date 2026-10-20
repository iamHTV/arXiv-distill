# Skill: Asymmetric Dynamic Routing (ADR) — query-adaptive RAG with three asymmetric traversal operators
Source: 2609.29282v2
Type: framework / workflow

## When to use this skill
- A RAG pipeline over a structured corpus (existing or buildable KG/hypergraph) currently uses ONE traversal config for all queries — wasting tokens on simple queries and lacking context on complex ones.
- You need to cut RAG latency/tokens WITHOUT losing quality (candidate: -45% latency, -49% prompt tokens AND +1.86 quality points).
- The corpus has regions with different knowledge density (sparse vs dense) where the best mode differs per domain.
- Do NOT use: corpora without a buildable KG/hypergraph (flat chunks only — use Adaptive-RAG / naive-RAG routing instead); nearly uniform query distributions (all simple or all complex — routing gain ~0); zero-overhead latency budgets (the classifier is one lightweight call but still a call); very small corpora (<100 docs).

## Inputs needed
- Dual-hypergraph knowledge base (DHI-style): factual hypergraph HK (entities, pairwise edges |e|=2, higher-order factual hyperedges |e|>=3, each carrying an atomic direct insight iota(e)) + insight mapping pi (hyperedge -> insight vertex) + deep insight hypergraph HD (insight vertices; insight edges epsilon with synthesized narrative insights I(epsilon)).
- Embedding model for entities + insight edges (paper: text-embedding-3-small) + generation LLM (paper: GPT-4o-mini, T=0).
- Query-complexity classifier (lightweight structured classifier) returning {Simple, Moderate, Complex} + confidence; threshold gamma (default 0.75).
- Evaluation judge (LLM-as-a-Judge over 5 dims: Comprehensiveness/Diversity/Empowerment/Logicality/Readability, 0-100) + per-mode token/latency logging.

## Steps
1. **Build the dual hypergraph offline** (before deployment): extract entities + pairwise factual relations + higher-order factual hyperedges (joint relations among >=3 entities); attach iota(e) to each higher-order edge; map pi -> insight vertices; group insight vertices into insight edges epsilon with narrative I(epsilon). One-time upfront indexing cost.
2. **Classify the query**: classifier -> y in {1,2,3} + confidence c. If c < gamma (0.75) -> conservative fallback y=2 (Moderate). Calibrate gamma: fallback rate >~68% means gamma too high (lower it); ambiguous queries misrouting (Logicality drop) means gamma too low (raise it; reference: 0.50 -> Logicality -1.14).
3. **Route asymmetrically**:
   - Simple -> Operator 1: Vas = top-k_e entities maximizing sum cos(e_v, q); Esub = edges intersecting Vas != empty; STOP (zero-hop-like: no neighborhood expansion, no cross-layer traversal).
   - Moderate -> Operator 2: Useed = pi(higher-order edges in Esub); Eup = insight edges intersecting Useed != empty (single adjacency expansion in HD); context = facts Esub + narratives Eup.
   - Complex -> Operator 3: E* = top-k_d insight edges maximizing sum cos(e_epsilon, q); Eground = pi^-1(E*) subset EK; context = narratives E* + facts Eground.
4. **Generate**: format the joint context -> generation LLM at T=0.
5. **Monitor + calibrate**: log per query (mode, tokens, latency, judge scores); if Complex queries in sparse domains retrieve insufficient facts, add a dense-vector fallback branch; benchmark the three frozen modes (Simple/Moderate/Complex-only) to verify the dynamic gain (+1.39 to +2.11 points expected).

## Expected output
- Per-query adaptive retrieval: average latency ~238ms + prompt tokens ~1,929 (vs 435ms + 3,760 under Complex-only) = -45.3% latency, -48.7% tokens, quality 83.91 vs 82.05 (+1.86); beats the best static mode on every domain (+0.94 to +2.11); complex causal queries stay coherent with 41.2% fewer tokens than always-deep retrieval.

## Example application
- Knowledge base of product docs + blog (solopreneur content site): "how long is the refund window?" -> Simple -> anchor {refund policy, window} -> 2 facts, small context; "how do returns interact with loyalty-point accrual?" -> Moderate -> facts + insight edges; "why did churn spike after the pricing change?" -> Complex -> top-down insight edges (pricing -> usage drop -> churn) pi^-1-grounded to source docs -> causal chain + facts, ~41% fewer tokens than always-complex retrieval.

## Gotchas
- Sparse-domain Complex queries: insight grounding may lack supporting facts (weak graph connectivity) -> you MUST have a dense-vector fallback branch (the paper admits this but does not evaluate it quantitatively).
- Wrong gamma: 0.50 misroutes ambiguous queries (Logicality -1.14); >=0.85 sends 68.4% to Moderate fallback + 58ms wasted latency. Measure fallback rate + Logicality whenever gamma changes.
- Excess depth hurts quality on dense corpora (Moderate-only beats Complex-only by +1.39-1.51): never default to "deeper = better".
- Upfront indexing cost: HK+HD built offline — trade construction time against online savings; not worth it for tiny corpora.
- The classifier is independent of graph structure: it sees query text, not graph state -> re-calibrate on domain shift.
- Quality metrics are judge perception only: add separate exact-match/F1 checks for domains where factual correctness is critical.
- Complex-only naive path pulls 3,850 tangential tokens (irrelevant EGFR in the pathology example) — without routing, context dilution + hallucinated associations increase.

## Dry run test
- Hypothetical case (KB of 200 commerce docs): step 1 build KG (1,800 entities, 2,600 edges, 140 insight vertices) once offline; step 2 classifier over 15 test queries -> 5 Simple / 6 Moderate / 4 Complex, gamma=0.75 sends 1 query to Moderate fallback; step 3 route: Simple queries average 980 tokens (vs 3,760 Complex-only), the churn-pricing Complex query yields a grounded causal chain at 2,210 tokens + facts; step 4 T=0 generation; step 5 monitor: average latency 240ms, tokens 1,950, judge 84.1, vs Complex-only frozen baseline 82.3. Output: adaptive routing works, metrics measured, gain +1.8 points / -48% tokens -> meaningful -> [SKILL VALID].
