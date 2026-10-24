# Skill: Build structured knowledge base for scientific papers (SPRA)

Source: 2610.21424v2
Type: workflow

## When to use this skill

- You need to build a knowledge query system from research papers or technical documents, where AI agents need fast lookup and source verification.
- You have a large collection of papers (hundreds of thousands to millions) and want to represent content as structured objects rather than raw text.
- You want to reduce token costs when agents retrieve information from multiple papers simultaneously.

## When NOT to use this skill

- Tasks require understanding full article context (e.g., Top-5 synthesis needs full text).
- You don't need source verification and only need quick summaries.
- You don't have documents parseable into section-aware Markdown.

## Required inputs

- Source articles parsed into section-aware Markdown with source markers.
- A strong LLM for structure extraction (5 core LLM calls: unit census, relation planning, Problem/Method/Evidence filling, two citation passes).
- Section-aware parsing tool (e.g., MinerU).
- Access to Sciverse platform or local Paper Schema API installation.
- JSON storage and relation querying environment.

## Steps to execute

1. Parse source articles into section-aware Markdown with source markers.
2. Run shared unit census to identify research objects.
3. Plan relations between objects across 6 roles: Problem, Contribution, Component, ExperimentSetup, Measure, Finding.
4. Fill content by role: Problem (problem/gap), Contribution (contribution), Component (component), ExperimentSetup (experiment setup), Measure (measure), Finding (finding).
5. Run two citation passes to join roles and verbatim signals to bibliographic metadata by citation key.
6. Check schema validity: verify types, endpoints, provenance, and census coverage.
7. Store objects and relations as structured JSON, keeping external citations in a separate layer.
8. Build query interface (API) so agents can look up, traverse relations, and expand citations.

## Expected output

- A set of structured research objects (SPRA instances) with typed relations and source bindings.
- A Paper Schema API interface for agents to look up, traverse, and reuse paper content.
- Token cost reduction vs passage retrieval and Full Compact.

## Example application

A Vietnamese company wants to build a research assistant for its R&D team: collect 10,000 AI papers on NLP, parse into section-aware Markdown, extract the 6 roles and relations between them, store in a knowledge base. The AI agent can answer "which method is most used for text classification in the last 3 years" by traversing compares_to and evaluates relations instead of reading all 10,000 papers.

## Gotchas

- Full Compact is not always optimal for all tasks: on Top-5 synthesis, compact structure trails full text on grounding and qualification. Evaluate per task needs.
- Compact structure must be assessed against each task's information needs — full text is not always better.
- Cannot isolate contribution of individual role or predicate labels from overall evaluation.
- Hosted service (Sciverse) behavior may change under updates; results characterize recorded service invocations.
- Automated extraction may omit or misstate qualifications, affecting how research claims are understood.