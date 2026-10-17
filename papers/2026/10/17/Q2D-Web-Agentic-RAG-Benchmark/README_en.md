# [2609.08887v2] Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems

## Problem
- Evaluating first-stage retrievers in large-scale production RAG requires a benchmark that pairs a large-scale corpus with a large set of agent-reformulated search queries based on real user queries and their conversation threads, and that labels many relevant documents per query. No existing public benchmark evaluates this setting: large-scale collections typically provide only a small number of evaluation queries, whereas benchmarks with many queries generally contain only millions of documents. Moreover, most benchmarks assess human-written queries, while the first-stage retrievers in agentic RAG pipelines serve machine-written reformulations whose distribution differs from human search behavior.

## Contribution
- Q2D-Web (Query2Doc-Web) — a large-scale agentic retrieval benchmark consisting of a ~190M-document web corpus and ~70k agentic search queries in ten languages, reformulated from real-world user queries in production systems.
- Q2D-Web provides three sets of fixed relevance judgments: agent citations, production rankings, and a combined set that unions both signals and adds LLM-based judgments of unlabeled pooled documents to reduce false negatives.
- Benchmarks 13 retrievers including lexical, dense, and late-interaction models and finds that their relative ordering is largely insensitive to the choice of judgment set, while diverging substantially across topical domains, query languages, and query types.
- To enable fast evaluation, also studies subcorpus sampling as an approximation to full-corpus evaluations. Retaining a third of the corpus, selected by reciprocal rank fusion (RRF) over pooled retriever runs, preserves the full-corpus model ranking under the combined judgments while raising absolute Recall@1000 only by 4–7 points.

## Method (core summary)
- Q2D-Web construction pipeline: sample queries from agent search calls, assemble and deduplicate the corpus, construct three relevance-judgment sets, and sample an evaluation subcorpus while retaining all labeled positives.
- Three relevance-judgment sets: agent citations, production rankings, and a combined set that unions both signals and adds LLM-based judgments of unlabeled pooled documents.
- 13 retrievers benchmarked: lexical, dense, and late-interaction models.
- Subcorpus sampling: retaining a third of the corpus, selected by RRF over pooled retriever runs, preserves the full-corpus model ranking under combined judgments.

## Key Findings
- 7 authors from Perplexity AI, arXiv category: cs.IR.
- ~190M documents, ~70k queries, 10 languages.
- Relative ordering of retrievers largely insensitive to judgment set choice, but diverges substantially across topical domains, query languages, and query types.
- Retaining 1/3 of corpus via RRF preserves full-corpus model ranking while raising Recall@1000 by 4–7 points.
- pplx-embed-v1-4b wins all three judgment sets (Citation, Web Ranking, and Comb.) on Recall@1000.
- Nemotron-3-Embed-8B strongest on Recall@100 and nDCG@10 under Combined.
- Late-interaction models trail dense encoders of same size on Recall@1000 by 3–5 points but gap narrows to at most 1 point on nDCG@10.
- Qwen3-Embedding family: Recall@1000 improves monotonically with model size (0.6B→4B→8B: 58.68→62.78→65.32 on Comb.).

## Actionable Insights
1. Evaluate first-stage retrievers in RAG using a benchmark with a large corpus and agent-reformulated queries, not just human-written queries. Application: when building production RAG systems, evaluate the first-stage retriever on a large corpus (~190M documents) with agent-generated queries, not just hand-written queries.
2. Subcorpus sampling via reciprocal rank fusion (RRF) can preserve full-corpus model ranking while using only 1/3 of the corpus. Application: when evaluating retrievers on large corpora, use RRF to sample 1/3 of the corpus to reduce evaluation cost while preserving model rankings.

## Assumptions & Limitations
- Evaluation focuses on fixed-corpus; generalization to other corpora and live web search needs further study.
- Evaluates 13 retrievers (lexical, dense, late-interaction).

## Metadata
- Year: 2026, authors: Maximilian Schall, Sedigheh Eslami, Markus Krimmel, Antoine Chaffin, Louis Milliken, Bo Wang, Denis Bykov (Perplexity AI), arXiv category: cs.IR, PDF link: https://arxiv.org/pdf/2609.08887v2
