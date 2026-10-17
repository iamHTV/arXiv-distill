# Skill: q2d-web-retriever-evaluation
Source: 2609.08887v2
Type: evaluation-method

## When to use this skill
- Building or evaluating first-stage retrievers in production RAG systems.
- Need to evaluate on large corpus and agent-reformulated queries, not just human-written queries.
- Want to reduce evaluation cost via subcorpus sampling while preserving model rankings.

## When NOT to use this skill
- Evaluating on small corpora (fewer than millions of documents).
- Only human-written queries available, no agent-reformulated queries.
- Not evaluating first-stage retriever, only evaluating second-stage reranker.

## Input needed
- Large document corpus (e.g., ~190M web documents).
- Agent-reformulated queries based on real user queries.
- Three relevance-judgment sets: agent citations, production rankings, combined set.
- 13 retrievers to evaluate (lexical, dense, late-interaction).

## Steps to execute
1. Build Q2D-Web benchmark: sample queries from agent search calls, assemble and deduplicate corpus, construct three relevance-judgment sets.
2. Sample an evaluation subcorpus while retaining all labeled positives.
3. Score 13 retrievers (lexical, dense, late-interaction) on all three judgment sets.
4. Compare relative ordering of retrievers across topical domains, query languages, and query types.
5. To reduce evaluation cost, sample 1/3 of corpus using reciprocal rank fusion (RRF) over pooled retriever runs — preserves full-corpus model ranking.
6. Evaluate Recall@1000, Recall@100, and nDCG@10 on both full corpus and sampled corpus.

## Expected output
- Model ranking of 13 retrievers across three judgment sets.
- Confirmation that sampling 1/3 of corpus via RRF preserves full-corpus model ranking while raising Recall@1000 only by 4–7 points.

## Application example
- Building production RAG system: evaluate first-stage retriever on large corpus (~190M documents) with agent-reformulated queries, use RRF to sample 1/3 of corpus for fast evaluation while preserving model rankings.

## Gotchas
- Evaluation focuses on fixed-corpus; generalization to other corpora and live web search not studied.
- Relative ordering of retrievers largely insensitive to judgment set choice, but diverges across domains, languages, query types.
- pplx-embed-v1-4b wins all three judgment sets on Recall@1000; Nemotron-3-Embed-8B strongest on Recall@100 and nDCG@10 under Combined.
