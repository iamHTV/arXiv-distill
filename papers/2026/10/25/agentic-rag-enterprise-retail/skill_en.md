# Skill: Build retail-aware agentic RAG for multi-source enterprise data (RetailRAG)

Source: 2610.25096v1
Type: workflow

## When to use this skill

- You need to build enterprise data retrieval agents across heterogeneous data sources (SQL tables, text, APIs).
- Queries require bridging evidence across sources (multi-source chaining), not just retrieval from a single source.
- You want to reduce API call costs and improve accuracy for retail/enterprise data retrieval agents.

## When NOT to use this skill

- Data resides in a single source only and queries don't require bridging evidence across sources.
- You don't need to understand data schema before planning queries.
- You don't need local failure recovery when function calls fail.

## Required inputs

- Heterogeneous enterprise database (structured tables and unstructured text).
- Data schema: table names, column names, data types, categorical value constraints, entity alignment keys, derived analytical metrics.
- LLM backbone capable of function calling and multi-step planning.
- Retrieval tools: SQL engine for tables, retrieval engine for text.
- LLM API call environment with call counting capability.

## Steps to execute

1. Build data schema summary (auto-schema briefing): deterministically profile each column as numeric/categorical/free-text, have LLM organize into 4 sections (schema & metadata summary, categorical value constraints, entity alignment keys, derived analytical metrics).
2. Inject schema summary into the planner's prompt before planning begins.
3. Multi-step planning (source-routed plan chaining): adaptive router assesses query complexity, routes simple queries directly to a single tool call, reserves planning loop for multi-source queries. Planner produces full chain in a single pass specifying each step's source and search query, with later steps referencing earlier results as variables.
4. Execute each planned step on its declared tool, deterministically substituting prior values into the next step.
5. When a step fails mid-chain, repair only the failed step (diagnostic plan revision): diagnose — LLM detects failures from execution signals (empty results, zero aggregates) and assigns typed cause (schema mismatch, over-restrictive filter); revision — LLM rewrites only the failed step guided by diagnosed cause, keeping completed steps intact.
6. Evaluate: compute accuracy (Acc) and LLM-as-judge on multi-source queries across 3 diagnostic axes (reasoning depth, source diversity, evidence modality).

## Expected output

- A multi-source enterprise data retrieval agent with high accuracy on multi-hop cross-source queries.
- Reduced API calls compared to traditional agentic RAG baselines.
- Ability to recover from step-level failures without restarting the entire workflow.

## Example application

A Vietnamese solopreneur builds a sales support agent for online retail: retrieve from order table (SQL) and customer reviews (text) to answer "which product has the highest reviews last month and what's the total revenue from orders of that product". The agent uses auto-schema briefing to understand order table and review table structure, routes step 1 to review table (text) to find highest-rated product, step 2 to order table (SQL) to calculate total revenue, bridging evidence across both steps.

## Gotchas

- Multi-source chaining is the dominant bottleneck: most baselines drop sharply when queries require bridging across sources, not just per-step retrieval.
- Model scaling alone doesn't solve the problem; explicit cross-source orchestration is needed.
- Text retrieval is the dominant evidence modality bottleneck: text-only queries degrade more than SQL table queries.
- Cross-source bridging capability scales with model size, not model category.
- No explicit Limitations section in the paper (ends at Conclusion then References).
- No evaluation of storage/maintenance costs, no evaluation of stability when data changes over time.