# 2605.09942 HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution

## Problem

Memory retrieval in agentic LLM systems is often treated as a static lookup problem — relying on flat vector search or fixed binary relational graphs. Fixed structures cannot capture varying strength, confidence, and query-dependent relevance of relationships between events. As agents accumulate experience across sessions, context-only interaction leads to diluted, misplaced, or forgotten information.

## Contribution

1. HAGE — weighted multi-relational memory framework reconceptualizing retrieval as sequential, query-conditioned traversal over unified relational memory graph.
2. Relation-specific graph views — each edge has a trainable relation feature vector encoding multiple relational signals. Query-conditioned routing network dynamically modulates edge embeddings.
3. RL-based training jointly optimizing routing behavior and edge representations using downstream task rewards.

## Method (core summary)

(1) Memory graph: directed multi-relational graph with nodes = memory items, edges = relation-specific connections with trainable feature vectors; (2) Query-conditioned retrieval: LLM classifier identifies relational intent → routing network modulates edge embeddings; (3) Traversal scores = semantic similarity + query-conditioned edge representations; (4) RL training: optimize router + edge modules with downstream rewards; (5) Top-K retrieval until context budget exhausted.

## Key Findings

- Best/second-best on most LoCoMo categories: Multi-Hop, Temporal, Open-Domain, Single-Hop, Adversarial
- Baselines: Full Context, A-MEM, MemoryOS, Nemori, MAGMA, MemSkill
- Improves long-horizon reasoning accuracy
- Favorable accuracy-efficiency trade-off
- Query-conditioned traversal outperforms static graph traversal

## Actionable Insights

1. Don't use flat vector search — organize memory as multi-relational graph with learnable edges. Example: customer support agent — edges between "complaint" and "product defect" nodes weighted higher for troubleshooting queries.
2. Query-conditioned routing — analyze intent before traversing. Example: "what happened last week?" → temporal edges; "why did X cause Y?" → causal edges.
3. RL edge optimization — update weights with downstream task rewards.

## Assumptions & Limitations

- Assumption: relation types identifiable from query — noisy queries may misroute
- Limitation: Only LoCoMo and HotpotQA tested
- Limitation: RL training adds overhead
- Limitation: Graph construction not addressed
- Limitation (observed): Scalability to 100K+ nodes not analyzed

## Metadata

- Year: 2026
- Authors: Dongming Jiang, Yi Li, Guanpeng Li, Qiannan Li, Bingzhe Li
- Category: cs.AI, cs.CL
- PDF: https://arxiv.org/pdf/2605.09942
- Citation count: N/A
- Classification: [applied]
- Skill: hage-weighted-graph-memory
