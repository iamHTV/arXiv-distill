# Skill: HAGE Weighted Graph Memory
Source: 2605.09942
Type: framework

## Khi nào dùng skill này

- Khi build agent memory system cần multi-session persistence (bộ nhớ đa phiên) mà flat vector search insufficient — agent cần reason over relationships giữa memories, không chỉ similarity
- Khi memory retrieval cần adapt to query intent — cùng 1 memory store nhưng different queries cần traverse different relational paths
- Khi có downstream task feedback (answer correctness) để optimize memory retrieval quality

- KHÔNG dùng khi: memory store nhỏ (<1K items, vector search đủ); queries đều same type (không cần relation-aware routing); không có RL training infrastructure

## Input cần có

- Memory items (conversations, events, facts) với timestamps
- Relation types between items (temporal, causal, entity-based, topic-based)
- Queries với ground-truth answers for RL training
- Backbone LLM for query intent classification và response generation

## Các bước thực hiện

1. **Construct Memory Graph** — Nodes = memory items. Edges = relation-specific connections (temporal: happened before/after; causal: caused; entity: shares entity; topic: same topic). Initial edge weights = heuristic (e.g., temporal proximity, entity overlap). Store as directed multi-relational graph.

2. **Query Intent Classification** — LLM classifies query into relational intent categories: temporal (when did X happen?), causal (why did X cause Y?), entity (what about person Z?), topical (what's related to topic W?). Output: intent vector.

3. **Query-Conditioned Traversal** — Routing network modulates edge embeddings based on intent vector. Compute traversal score = α × semantic_similarity(query, node) + β × query_conditioned_edge_score. Traverse graph starting from entry nodes, accumulate top-K nodes by score.

4. **RL Edge Optimization** — (a) Use downstream task reward (answer correctness) to update edge weights and routing network; (b) Positive reward → reinforce traversal paths that led to correct answer; (c) Negative reward → suppress noisy paths; (d) Joint optimization with Adam optimizer.

5. **Retrieve and Generate** — Select top-K nodes by traversal score, concatenate with query, generate answer. Monitor accuracy-efficiency trade-off: higher K → better accuracy but more context tokens.

## Output mong đợi

- Improved long-horizon reasoning accuracy vs flat vector search
- Query-adaptive retrieval (different queries traverse different paths)
- Accuracy-efficiency trade-off better than full-context approach

## Ví dụ áp dụng

Scenario: Personal AI assistant with 6 months of conversation history (5K memories). (1) Build memory graph: temporal edges between consecutive days, entity edges (mention same person), topic edges (same project); (2) User asks "What did we discuss about Project Alpha last month?" → intent = temporal + entity + topic → traverse temporal edges to last month + entity edges to "Project Alpha" → retrieve 5 relevant conversations; (3) RL training: user marks answer helpful → reinforce those traversal paths; (4) Result: accurate retrieval from 5K memories using only relevant subset.

## Gotchas

- Graph construction is critical: poor initial edges → poor retrieval. Need domain-specific relation types.
- RL training needs reward signal: if no downstream task with clear correctness, use human feedback or LLM-as-judge.
- Scalability: graph traversal cost grows with graph size. For 100K+ nodes, need efficient graph indexing.
- Cold start: new memory items have no edges initially — need bootstrap strategy (e.g., auto-generate edges based on content similarity).
