# Skill: agentic-retrieval-react-loop
Source: 2610.05750v1
Type: workflow

## When to use this skill
- Search system needs to handle complex queries requiring multi-step reasoning.
- Standard retrieval (dense retrieval based on semantic similarity) is not accurate enough for your application.
- Can tolerate higher cost (time, tokens) for better accuracy.

## When NOT to use
- Simple search, only basic semantic similarity needed.
- Cannot tolerate 107s and 764K tokens per query cost.

## Required input
- An existing retriever system (dense retrieval).
- An LLM with reasoning capability.
- Unstructured data corpus to search.

## Steps
1. Build a ReAct agentic loop: LLM reasons about what query to make, retriever searches, LLM checks results, decides whether to continue or stop.
2. Repeat this loop until the agent has enough information to answer.
3. Only enable agentic retrieval for complex queries; use standard retrieval for simple queries (to save cost).
4. Evaluate on nDCG@10 and related metrics to confirm effectiveness.

## Expected output
- Improve nDCG@10 by about 8.7 points vs standard retrieval.
- Generalizes well across domains (ViDoRe, BRIGHT).
- Cost: ~107 seconds and 764K input tokens + 5.8K output tokens per complex query.

## Example application
Solopreneur building a legal document search system: simple queries ("2026 tax code") use standard retrieval; complex queries ("compare tax rules between 2025 and 2026 for small businesses") use agentic retrieval with ReAct loop for LLM multi-step reasoning across multiple sources.

## Gotchas
- Very high cost: 107.4s vs 0.67s for standard retrieval; 764.1K input tokens per query.
- Only use for truly complex queries, not every query.
- Need an LLM with good reasoning capability for agentic retrieval to work well.
