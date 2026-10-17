# Skill: Structured Paper Representation for Agents (SPRA)

Source: 2610.21424v1
Type: framework

## When to use this skill
- You are building AI research systems or literature agents and need structured paper representation for querying, traversal, and reuse.
- You want to reduce token cost when feeding papers to LLM agents compared to full-paper input.
- You need to connect research findings to methods, conditions, and cross-paper comparisons.

## When NOT to use this skill
- You only need to store raw text of papers, not query research structure.
- You don't have enough paper data to build a structured corpus.

## Input required
- Research papers parsed into section-aware Markdown with source markers.
- JSON schema defining research roles (Problem, Contribution, Component, ExperimentSetup, Measure, Finding) and typed relations between them.
- Programmatic API access for agents to query research objects.

## Steps to execute
1. Parse source papers into section-aware Markdown with source markers.
2. Extract research units into six roles: Problem, Contribution, Component, ExperimentSetup, Measure, Finding.
3. Build internal relations (part_of, co_contribution, compares_to, evaluates, about, supports, motivates, resolves) between units.
4. Build citation relations (builds_on, uses_component, compares_with) connecting to prior work.
5. Attach source locators to each unit and relation for verification.
6. Export data via a structured API (Paper Schema API) for agent querying.

## Expected output
- A collection of structured papers with research objects and typed relations.
- Agents can query, traverse, and reuse paper-level research objects.
- Reduced token cost compared to feeding full papers to LLM.
- Verifiable provenance for every research object.

## Example application
You build an AI research assistant agent. Instead of having the agent read full papers (costing many tokens), you extract papers into structured objects: Problem (what current approaches don't solve), Contribution (what the paper solves), Finding (benchmark results). The agent queries these objects via Schema-RAG, connecting Finding from paper A to ExperimentSetup from paper B to compare methods. Reduces 95.3% tokens compared to feeding full papers.

## Gotchas
- Overall score in idea generation tasks is slightly lower than Full Compact (0.067/5), trading quality for token efficiency.
- Need enough paper data of good quality to build a structured corpus.
- Research unit extraction requires a good extraction model or pipeline to ensure accuracy.