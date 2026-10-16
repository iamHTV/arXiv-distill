# Skill: rag-scientific-code-understanding
Source: 2609.12190v1
Type: framework

## When to use this skill
- Building an internal code lookup/understanding system for a business or individual.
- Want to use small local models instead of large cloud-hosted models (data privacy, cost reduction).
- Have a codebase to search and understand (e.g. scientific code, business code).

## When NOT to use
- No codebase to search from.
- Need an all-round code agent (edit files, run tests, verify output) rather than just lookup.

## Required input
- Codebase to understand and search (e.g. C++, Python code).
- Embedding system and vector store to store code context.
- A small LLM that can run locally.

## Steps
1. Build a codebase-specialized vector store: parse code, construct structural graph, generate LLM entity explanations, and embed (offline ingestion stage).
2. When user asks, retrieve relevant context from vector store and let small model answer (online answering stage).
3. Use a small model (e.g. 9B) for the answering stage, not a large cloud-hosted model.
4. Evaluate answers with a larger model as an independent judge.

## Expected output
- Small model (9B) achieves 0.795 average score on 100-question benchmark, outperforming larger models.
- System runs locally, ensures data privacy, and is free (no cloud API fees).

## Example application
Solopreneur has internal data analysis tool code: build a codebase-specialized vector store for this code, use a small model (9B) running locally to answer code questions (e.g. "what does this function do", "why error here"). Helps keep code private and reduce cost vs using Claude Code or Codex on cloud.

## Gotchas
- System is based solely on semantic explanation of codebase, not an all-round code agent (doesn't edit files, run tests, or iteratively verify its own output).
- Need to build a specialized vector store for each codebase, can't share across different codebases.
- Need a larger model as judge to evaluate answers, which can add evaluation cost.
