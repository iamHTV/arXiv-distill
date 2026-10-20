# Skill: KG Semantic Mediation Layer — auto-build KG from schema + prompt mediation for enterprise data assistants
Source: 2610.23304v1
Type: framework / workflow

## When to use this skill
- Building an enterprise data assistant (LLM) for business users who do NOT know SQL; user prompts are short, goal-oriented, and never reference the schema.
- Multi-table database with complex joins; schema-similarity retrieval alone produces hallucinated joins.
- You want to replace hand-curated few-shot examples per table (brittle, labor-intensive) with an automatic, low-maintenance mechanism.
- Do NOT use: single-table schemas (no joins — mediation is redundant); SQL-fluent users who always reference the schema; databases whose metadata lacks PK-FK AND lacks reliable name/type heuristics (joins_on edges cannot be built); organizations that forbid sending schema data to external embedding APIs.

## Inputs needed
- Database schema metadata (information schema: tables, columns, PK-FK constraints; fallback name-matching + type-compatible heuristics) + column descriptions/metadata.
- Embedding model + vector store (paper: OpenAI text-embedding-3-large + ChromaDB 1.3.4; a self-hosted equivalent works).
- A prompt-refinement LLM (GPT-4.1 / Claude Sonnet 4 class) + an LLM-as-Judge for the completeness gate (Pydantic structured output, 3 few-shot examples).
- 2 human analysts for the 2-round audit (TP/FP/FN) — or a sampled audit at small scale.
- Sample real user interaction logs (ideally >=100) for evaluation.

## Steps
1. **Auto-build KG** (NetworkX-class): nodes = tables + columns (from the information schema); edges = has_column (table->columns) + joins_on (PK-FK first, fallback name-matching + type-compatible); deliberately add NO domain constructs (metrics, filters) in the first cycle — isolate structural knowledge. Paper scale: 273 nodes / 540 edges.
2. **Vector-store nodes**: embed each node (identifier + type + name + description) into a ChromaDB-class store for semantic matching of user phrasing to canonical KG nodes (entry points).
3. **Mediation pipeline per query**: (a) segment the prompt into intent units; (b) similarity_search per segment -> entry nodes, retrieve table->all columns + column->parent table; (c) traverse the KG for direct + indirect join paths -> a subgraph (target ~54 nodes / 99 edges — "just-right" context); (d) LLM refinement: mediated prompt preserving the original intent + explicit table/column/join specs.
4. **Completeness gate**: LLM-as-Judge binary COMPLETED/NOT COMPLETED (3 few-shot examples, structured output); NOT COMPLETED -> block or clarify instead of executing wrong.
5. **Human audit**: 2 analysts, 2 iterations (analyst 1 reviews -> analyst 2 reviews those results -> compare/discuss/resolve) -> Precision/Recall/F1 on mediated prompts (TP = correct database info, FN = missing, FP = wrong).
6. **Monitor + governance**: F1 >= target (paper: KG F1 89-90%); completeness >= no-mediation baseline; annotator agreement >=95%; KG versioning + change management as the schema evolves; end-to-end spot-check (TP prompts must execute without extra discovery).

## Expected output
- Mediated prompts with correct tables/columns/joins for imperfect user prompts: Precision ~87-91%, Recall ~88-94%, F1 ~89-90% (2 LLMs), completeness >= baseline (93.04% vs 91.14% on GPT-4.1), mediation latency ~2.7s/query (vs 1.1s schema-only), annotator agreement 95.57-98.73%. User intent preserved despite injected database content.

## Example application
- An analytics assistant for a solopreneur (DB with 15 tables: orders/customers/products): user asks "revenue from returning customers in Q3 by product category" -> mediation segments -> retrieves customers (returning = repeat buyers), orders, products nodes -> join path customers->orders->order_items->products -> mediated prompt with explicit joins -> assistant returns the correct category breakdown. Schema-only: picks the right tables but joins customers.created_at incorrectly -> wrong customer grouping (hallucinated join -> silently wrong result).

## Gotchas
- Schema-only mediation hallucinates joins on complex schemas — WRONG JOINS, ONCE ENCODED, make downstream planning + execution reliably fail: never ship schema-only for multi-join enterprise databases.
- Auto-built KG lacks domain constructs (metrics, filters) — mediation may produce minimal changes when knowledge is missing (the completeness metric does NOT catch these cases -> sampled human audit needed).
- "Just-right" subgraph beats flooding: injecting the full schema overwhelms the LLM and increases false assumptions.
- Polysemous domain terms (e.g., "fiscal unity" income-tax vs VAT) need KG-level disambiguation cues — schema similarity cannot distinguish them.
- Latency trade: KG 2.7s vs schema 1.1s — acceptable for the precision gain; the paper does not report mediation inference COST per query — measure it yourself.
- OpenAI embeddings send schema text externally: enterprise data-lake privacy may require self-hosted embeddings for sensitive data.
- Single-enterprise validation (158 interactions / 29 users): test on your own corpus before trusting the numbers.

## Dry run test
- Hypothetical case (commerce DB, 15 tables, ~90 columns, 12 FK joins; 20 real short user prompts): step 1 build KG ~15 table nodes + ~90 column nodes + ~40 edges in ~2 minutes; step 2 embed nodes; step 3 mediate the 20 prompts: 17/20 mediated prompts have sufficient context -> LLM judge COMPLETED on 18; human audit: TP-only 15, FN 2 (missing join path), FP 1 (wrong column) -> Precision 15/(15+1)=93.75%, Recall 15/17=88.24%, F1 90.9%; completeness 95% >= baseline 90%; a demo 3-table join is correct where schema-only hallucinated a join -> wrong result. Output: mediated prompts + measured metrics -> meaningful -> [SKILL VALID].
