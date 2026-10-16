# [2609.12190v1] Retrieval-Augmented Generation for Scientific Code Understanding

## Problem
Large language models have become central to modern coding assistants, but state-of-the-art systems such as Claude Code or Codex rely on very large, cloud-hosted models with significant computational cost and data-privacy implications.

## Contribution
- Investigate whether a useful, fully local coding agent can be built around small open-source models by shifting the computational burden away from inference.
- Develop a RAG system for scientific code understanding that strictly separates an expensive offline ingestion stage from a lightweight online answering stage.
- Evaluate on a 100-question benchmark spanning eleven categories over the IPPL scientific codebase written in C++, with answers scored by an independent frontier model as the judge.
- Across seven answering models, model family and retrieval quality matter more than parameter count — a 9B model achieves the highest average score (0.795).

## Method (core summary)
The RAG system for scientific code understanding strictly separates an expensive offline ingestion stage (parsing, structural graph construction, LLM-generated entity explanations, and embedding) from a lightweight online answering stage. The online stage uses a pre-built, codebase-specialized vector store to answer questions with small local models.

## Key Findings
- Across seven answering models, model family and retrieval quality matter more than parameter count.
- 9B model achieves highest average score (0.795), outperforming larger models within the same pipeline and same models embedded in Claude Code retrieval architecture.
- Offline-prepared retrieval context condenses code understanding into explanations and structural metadata that small models can use without extensive reasoning.

## Actionable Insights
- Don't need large cloud-hosted models for coding assistants: small models (9B) can achieve higher scores with good retrieval context. Apply: solopreneur building internal coding assistant should use small local models with pre-built RAG vector store, ensuring data privacy and reducing cost.
- Separate expensive ingestion stage from lightweight online answering: build vector store once, then answer quickly and cheaply. Apply: when building internal code lookup system, build codebase-specialized vector store once, then let small models answer.

## Assumptions & Limitations
- Requires a codebase and data to build vector store; doesn't apply without a codebase.
- Paper admits: system is based solely on semantic explanation of codebase, not an all-round code agent (doesn't edit files, run tests, or iteratively verify its own output).
- Limitation paper doesn't mention: not evaluated on many codebases beyond IPPL, not tested on real ingestion stage cost.

## Metadata
- Year: 2026
- Authors: Aaron Nobile, Andreas Adelmann, Mohsen Sadr (ETH Zürich, Paul Scherrer Institute, MIT)
- arXiv category: cs.AI, cs.SE
- PDF link: https://arxiv.org/pdf/2609.12190
