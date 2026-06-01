# Skill: HAGE Weighted Graph Memory
Source: 2605.09942
Type: framework

## When to use this skill

- When building agent memory systems needing multi-session persistence where flat vector search is insufficient — agent needs to reason over relationships between memories
- When memory retrieval needs to adapt to query intent — same memory store but different queries traverse different relational paths
- When having downstream task feedback to optimize retrieval quality

- Do NOT use when: memory store small (<1K items); queries all same type; no RL training infrastructure

## Input needed

- Memory items with timestamps
- Relation types (temporal, causal, entity, topic)
- Queries with ground-truth answers for RL training
- Backbone LLM

## Steps

1. **Construct Memory Graph** — Nodes = memory items. Edges = relation-specific connections. Initial weights = heuristic.
2. **Query Intent Classification** — LLM classifies query into relational intent categories.
3. **Query-Conditioned Traversal** — Routing network modulates edge embeddings. Score = semantic_similarity + query_conditioned_edge_score.
4. **RL Edge Optimization** — Use downstream reward to update edges and routing. Joint optimization with Adam.
5. **Retrieve and Generate** — Select top-K nodes, generate answer.

## Expected output

- Improved long-horizon reasoning vs flat vector search
- Query-adaptive retrieval
- Better accuracy-efficiency trade-off than full-context

## Example application

Scenario: Personal AI assistant with 5K memories over 6 months. Build graph with temporal, entity, topic edges. Query "What about Project Alpha last month?" → temporal+entity routing → retrieve 5 relevant conversations from 5K.

## Gotchas

- Graph construction critical: poor edges → poor retrieval
- RL needs reward signal
- Scalability concern for 100K+ nodes
- Cold start: new items need bootstrap edge strategy
