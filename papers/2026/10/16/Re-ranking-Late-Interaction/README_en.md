# [2609.38473v1] Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG Strategies for Scientific Question Answering

## Problem
RAG (Retrieval-Augmented Generation) is now the standard way to ground LLMs in external knowledge, yet the design space of retrieval pipelines is large and the trade-offs between variants are not well understood, especially on domain-specific corpora at realistic scale.

## Contribution
- Present a controlled comparison of six retrieval strategies for scientific question answering: (i) classic top-k dense retrieval, (ii) query rewriting, (iii) re-ranking, (iv) RRF (Reciprocal Rank Fusion), (v) agentic tool-call retrieval, (vi) ColBERTv2 late interaction.
- Use 463K arXiv papers, dataset of 19,484 questions.
- ColBERT achieves highest answer rates (99.9% on both query types).
- Late-interaction strategies retrieve gold paper in top 3 for 92.8–94.8% of queries — roughly double the best single-vector pipeline.

## Method (core summary)
Six retrieval strategies compared on the same 463K arXiv paper corpus and 19,484 scientific questions. Measure answer rate, Hit@3, mean paired delta versus Classic with 95% confidence intervals.

## Key Findings
- ColBERT achieves highest answer rates (99.9% on both query types).
- Tool Call lowest (98.3% problem, 96.9% method).
- ColBERT: +0.27 problem, +0.47 method; pooled +0.37 (95% CI [+0.36, +0.38]) versus Classic.
- Rephrased & Reranked: +0.13 problem, +0.23 method; pooled +0.18 (95% CI [+0.17, +0.19]).
- Fusion and Tool Call significantly worse than Classic.
- Late-interaction strategies retrieve gold paper in top 3 for 92.8–94.8% of queries — roughly double best single-vector pipeline (Rephrased & Reranked: 47.5% and 52.8%).
- Rewriting alone hurts retrieval on problem queries (Hit@3 39.7% vs. 46.3% for Classic) — rewriting without re-ranking can drift away.

## Actionable Insights
- Use ColBERTv2 late interaction for high-quality retrieval: answer rate 99.9%, top-3 gold paper 92.8–94.8%. Apply: solopreneur building a RAG system for professional document lookup should use ColBERTv2 instead of simple dense retrieval.
- Don't use query rewriting alone without re-ranking: it reduces Hit@3 from 46.3% to 39.7%. Apply: when writing a RAG pipeline, always combine re-ranking after query rewriting.

## Assumptions & Limitations
- Requires a document corpus and reference questions with ground truth; doesn't apply without ground truth.
- Paper admits: evaluated on arXiv scientific corpus, may differ on other domains.
- Limitation paper doesn't mention: not evaluated on real token/cost of each strategy, not tested on multiple languages.

## Metadata
- Year: 2026
- Authors: Bhagyesh Rathi, Eshan Chawla, William B. Andreopoulos (San Jose State University)
- arXiv category: cs.IR, cs.AI
- PDF link: https://arxiv.org/pdf/2609.38473
