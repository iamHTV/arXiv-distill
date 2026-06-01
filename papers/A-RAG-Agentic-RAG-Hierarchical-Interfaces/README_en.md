# [2602.03442] A-RAG: Scaling Agentic RAG via Hierarchical Retrieval Interfaces

## Problem
Frontier language models have strong reasoning and long-horizon tool-use capabilities. But existing RAG systems fail to leverage these capabilities. Two old paradigms: (1) single-shot retrieval + concatenate; (2) predefined workflow. Neither paradigm allows the model to participate in retrieval decisions — preventing efficient scaling with model improvements.

## Contribution
1. **A-RAG framework**: Agentic RAG that exposes hierarchical retrieval interfaces directly to the model.
2. **3 retrieval tools**: Keyword search, semantic search, chunk read — agent adaptively searches across multiple granularities.
3. **Outperforms existing approaches**: Comparable or lower retrieved tokens on multi-hop QA benchmarks.

## Method (core summary)
A-RAG: exposes 3 retrieval tools directly to LLM agent: (1) Keyword search — find by keywords; (2) Semantic search — find by meaning; (3) Chunk read — read paragraph details. Agent decides when to use which tool, adaptively searches across granularities. Model-driven retrieval instead of algorithm-driven.

## Key Findings
- Outperforms Graph-RAG and Workflow RAG on diverse benchmarks
- Comparable or lower retrieved tokens
- Scales with model size and test-time compute
- Multi-hop QA: HotpotQA, 2WikiMultiHopQA, MuSiQue, GraphRAG-Bench

## Actionable Insights
1. **Agent-friendly interfaces > complex algorithms**: When building RAG systems, design interfaces for agents instead of complex retrieval algorithms. Example: expose keyword search, semantic search, chunk read as tools — let agent decide.

2. **Hierarchical retrieval**: Multiple granularities (keyword → semantic → chunk) for better coverage. Example: when building knowledge base search, provide keyword search for quick lookup, semantic search for concept matching, chunk read for detailed info.

3. **Model-driven retrieval scales**: Agent-driven retrieval scales with model improvements. Invest in model quality. Example: when upgrading LLM, retrieval automatically improves — no algorithm redesign needed.

## Assumptions & Limitations
**Conditions for method to work:**
- LLM with strong tool-use capabilities
- Corpus indexed for keyword and semantic search
- Multi-hop QA tasks tested

**Limitations the paper acknowledges:**
- No exhaustive tool design comparison
- Not validated on larger models (GPT-5, Gemini-3)
- Multi-hop QA only — other tasks untested

**Limitations the paper does NOT mention:**
- Computational cost of agent-driven retrieval
- Latency compared to single-shot retrieval
- Tool selection accuracy
- Scalability to very large corpora

## Metadata
- Year: 2026
- Authors: Mingxuan Du, Benfeng Xu, Chiwei Zhu, et al.
- Category: cs.CL
- PDF: https://arxiv.org/pdf/2602.03442
- Citation count: [EXTRACTION FAILED]
