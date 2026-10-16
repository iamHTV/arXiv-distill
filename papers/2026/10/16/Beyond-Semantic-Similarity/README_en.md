# [2610.05750v1] Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks

## Problem
Modern information systems, including many agentic workflows, use dense retrieval to explore large amounts of unstructured data. However, dense retrieval relies on surface-level semantic similarity, which is insufficient for increasingly complex search applications.

## Contribution
- Investigate agentic retrieval that combines the reasoning capabilities of LLMs with the efficient corpus exploration of retrievers in a ReAct agentic loop.
- Show agentic retrieval is more effective than standard retrieval: improving nDCG@10 by 8.7 points using the same embedding model.
- Agentic retrieval is highly generalizable: the same pipeline achieves competitive results on both ViDoRe v3 and BRIGHT leaderboards, while specialized retrieval methods struggle on out-of-domain tasks.

## Method (core summary)
Agentic retrieval combines LLM reasoning ability with retriever corpus exploration in a ReAct agentic loop. The agent uses reasoning to decide what to query, which section to inspect, and when to stop, instead of relying only on semantic similarity once.

## Key Findings
- Agentic retrieval improves nDCG@10 by 8.7 points vs standard retrieval, using the same embedding model.
- Highly generalizable: same pipeline achieves competitive results on ViDoRe v3 and BRIGHT leaderboards, while specialized retrieval methods struggle on out-of-domain tasks.
- Cost: agentic retrieval averages 107.4 seconds vs 0.67 seconds for standard retrieval.
- Consumes 764.1K input tokens and 5.8K output tokens per query.

## Actionable Insights
- Only use agentic retrieval for complex search tasks where standard retrieval is insufficient: cost is high (107s, 764K tokens) so only enable when needed. Apply: solopreneur building a content search system should use standard retrieval for simple queries, enable agentic retrieval only for complex multi-step reasoning queries.
- Agentic retrieval generalizes well across domains (ViDoRe, BRIGHT), so one pipeline can serve multiple query types. Apply: build a single agentic retrieval system instead of multiple specialized retrieval methods per domain.

## Assumptions & Limitations
- Requires an existing retriever system and an LLM with reasoning capability; doesn't apply with simple dense retrieval only.
- Paper admits: high cost (107s, 764K tokens/query) limits large-scale deployment.
- Limitation paper doesn't mention: not evaluated on languages other than English, not tested on very large document collections (millions of documents).

## Metadata
- Year: 2026
- Authors: Reza Esfandiarpoor, Radek Osmulski, Yauhen Babakhin, Gabriel de Souza P. Moreira, Oliver Holworthy, Jie He, Ronay Ak, Jiarui Cai, Ryan Chesler, Bo Liu, Even Oldridge (NVIDIA, University of Edinburgh)
- arXiv category: cs.AI, cs.IR
- PDF link: https://arxiv.org/pdf/2610.05750
- Code: https://github.com/NVIDIA/NeMo-Retriever/tree/main/retrieval-bench
