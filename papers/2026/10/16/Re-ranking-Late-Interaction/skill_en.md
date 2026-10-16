# Skill: rag-retrieval-strategy-comparison
Source: 2609.38473v1
Type: framework

## When to use this skill
- Building a RAG system for looking up professional/technical documents.
- Want to choose the right retrieval strategy (top-k, re-ranking, ColBERT, agentic tool-call).
- Have a document corpus and reference questions for evaluation.

## When NOT to use
- No document corpus to search from.
- Only need simple search, no need to compare multiple strategies.

## Required input
- Document corpus (e.g. 463K arXiv papers or business documents).
- Reference questions with standard answers (gold papers).
- Retrieval strategies already implemented (top-k, rewriting, re-ranking, ColBERT, etc.).

## Steps
1. Implement six retrieval strategies: classic top-k dense, query rewriting, re-ranking, RRF, agentic tool-call, ColBERTv2 late interaction.
2. Run all on the same corpus and question dataset.
3. Measure answer rate, Hit@3, mean paired delta vs Classic baseline with 95% CI.
4. Choose the strategy with highest answer rate and Hit@3 (ColBERTv2 is usually best).
5. Don't use query rewriting alone without re-ranking.

## Expected output
- ColBERTv2: answer rate 99.9%, top-3 gold paper 92.8–94.8%.
- Rephrased & Reranked: pooled +0.18 delta vs Classic.
- Tool Call: lowest (96.9–98.3% answer rate).

## Example application
Solopreneur building a legal document lookup system: implement ColBERTv2 late interaction for retrieval, combine with re-ranking after query rewriting. Evaluate on legal text corpus and reference questions, choose the strategy with highest answer rate.

## Gotchas
- Rewriting alone reduces retrieval quality (Hit@3 39.7% vs 46.3% Classic) — always combine with re-ranking.
- Tool Call agentic model has the lowest answer rate — don't use as primary strategy.
- Need corpus and reference questions to evaluate strategy correctly.
