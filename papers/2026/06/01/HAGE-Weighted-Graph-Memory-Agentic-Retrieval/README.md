# 2605.09942 HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution

## Problem

Memory retrieval trong agentic LLM systems thường được treat như static lookup problem — dựa vào flat vector search hoặc fixed binary relational graphs (đồ thị quan hệ nhị phân cố định). Fixed graph structures không capture được varying strength (độ mạnh thay đổi), confidence (độ tin cậy), và query-dependent relevance (liên quan tùy truy vấn) của relationships giữa events. Khi agents accumulate experience qua nhiều sessions, context-only interaction bị diluted (pha loãng), misplaced (sai vị trí), hoặc forgotten (quên).

## Contribution

1. Propose HAGE — weighted multi-relational memory framework (khung bộ nhớ đa quan hệ có trọng số) reconceptualize retrieval thành sequential, query-conditioned traversal (duyệt theo chuỗi, điều kiện hóa theo truy vấn) trên unified relational memory graph.
2. Relation-specific graph views — mỗi edge có trainable relation feature vector encoding multiple relational signals. Query-conditioned routing network dynamically modulates edge embeddings.
3. RL-based training framework jointly optimizes routing behavior và edge representations using downstream task rewards.

## Method (tóm tắt cốt lõi)

(1) Memory graph: directed multi-relational graph G_t với nodes = memory items, edges = relation-specific connections với trainable feature vectors; (2) Query-conditioned retrieval: LLM-based classifier identifies relational intent từ query → routing network modulates corresponding dimensions của edge embedding; (3) Traversal scores = learned combination of semantic similarity + query-conditioned edge representations → prioritize high-utility paths, suppress noisy connections; (4) RL training: optimize router + edge modules jointly using downstream task rewards (answer correctness); (5) Top-K retrieval: select nodes by traversal score until context budget exhausted.

## Key Findings

- Evaluated trên LoCoMo (ultra-long conversations, 9K tokens avg) và HotpotQA (multi-hop QA)
- HAGE achieves best/second-best trên most LoCoMo categories: Multi-Hop, Temporal, Open-Domain, Single-Hop, Adversarial
- Comparison baselines: Full Context, A-MEM, MemoryOS, Nemori, MAGMA, MemSkill
- HAGE improves long-horizon reasoning accuracy vs state-of-the-art agentic memory systems
- Favorable accuracy-efficiency trade-off — better accuracy without excessive compute
- Query-conditioned traversal outperforms static graph traversal
- RL-based edge learning contributes to performance improvement

## Actionable Insights

1. Khi build agent memory system, KHÔNG dùng flat vector search — thay vào đó organize memory thành multi-relational graph với learnable edge weights. Ví dụ: customer support agent — edges giữa "customer complaint" nodes và "product defect" nodes có higher weight khi query liên quan đến troubleshooting.
2. Query-conditioned routing cho memory retrieval — phân tích intent của query trước khi traverse graph. Ví dụ: agent có 10K memories, query "what happened last week?" → route to temporal edges; query "why did X cause Y?" → route to causal edges.
3. RL training cho memory edges — optimize edge weights bằng downstream task rewards. Ví dụ: chatbot trả lời customer questions → reward = answer correctness → RL updates edge weights để improve retrieval cho similar future queries.

## Assumptions & Limitations

- Giả sử: relation types có thể identified từ query — noisy queries có thể misroute
- Limitation: Benchmark coverage — chỉ LoCoMo và HotpotQA, chưa test trên diverse agent tasks
- Limitation: Training cost — RL-based optimization adds overhead so với static approaches
- Limitation: Graph construction — how to initially create edges? Paper assumes pre-existing relational structure.
- Limitation (tự thấy): Scalability concern — graph grows with memory, traversal cost may increase. Paper doesn't analyze scalability to 100K+ memory nodes.

## Metadata

- Năm: 2026
- Tác giả: Dongming Jiang, Yi Li, Guanpeng Li, Qiannan Li, Bingzhe Li
- Category: cs.AI, cs.CL
- Link PDF: https://arxiv.org/pdf/2605.09942
- Citation count: N/A
- Nhãn: [applied]
- Skill: hage-weighted-graph-memory
