# [2609.14412v1] Question's Gambit: The First Move Matters in Agentic Deep Search

## Problem
- Deep research agents answer complex questions through iterative loops of searching, reading, and reasoning. Recent work on reasoning-intensive benchmarks such as BrowseComp-Plus shows that well-configured lexical retrieval can surface high-quality evidence, yet agents may still fail to connect documents carrying evidence to the gold documents. Prior work does not address the quality of the agent's first retrieval move — if early searches surface evidence for only some clues, the agent can be drawn toward an incomplete hypothesis and spend later turns following it.

## Contribution
- Question's Gambit — a first-move retrieval module that decomposes the question into a set of clues, reformulates them into complementary searches, consolidates the retrieved results, and reranks the candidate pool before the agent begins its iterative search-and-reasoning process. This produces an opening context designed to support both clue aggregation and final-answer verification.
- Also evaluated on MultiHop-RAG to test whether these benefits transfer beyond BrowseComp-Plus to a more conventional multi-hop question structure.

## Method (core summary)
- Problem formulation: Given a complex question q and a corpus D, the task is to produce an answer y that matches the reference answer y⋆. Such questions are inherently multi-clue: each question contains a latent set of heterogeneous information elements (partial descriptions, dates, locations, titles, affiliations) that jointly constrain the answer. Individual clues may be supported by different documents, leaving the required evidence distributed across the corpus.
- A deep search agent uses a large language model Sθ acting through its policy πθ, formulates its own textual queries x, and submits them to a retriever tool R, which returns a ranked list of documents. The agent operates in a ReAct-style loop.
- Question's Gambit proceeds in three stages:
  1. Question Decomposition: a decomposer extracts the clue set from the question, separating constraints that a whole-question query would otherwise blend together.
  2. Per-Clue Retrieval: each clue is issued to the retriever; the documents it returns serve as a feedback set for expanding that clue, so the retrieval query is grounded in corpus terminology rather than the expansion model's parametric knowledge. The clue, its expansion, and the question are concatenated into a single search string.
  3. Question-Conditioned Reranking: per-clue lists are merged into a deduplicated pool and reranked against the original question using a pointwise reranker. The top-k documents form the opening context O.
- The module runs once, entirely within the agent's first action, and returns an opening context O of size k that enters the trajectory as the first observation o1. Requires no retraining of the agent or retriever; leaves the subsequent search loop unchanged.

## Key Findings
- 7 authors from University of Toronto, Mila – Quebec AI Institute, University of Waterloo, UC Berkeley, McGill University, arXiv categories: cs.AI, cs.CL, cs.IR.
- BrowseComp-Plus: Question's Gambit improves answer accuracy over strong baselines, improving answer accuracy from 83.1% to 90.5% with gpt-5.5 over Pi-Serini (the strongest reported agentic baseline).
- DeepSeek-v4-pro: 71.4% → 76.9% (+5.5 pp); GPT-5.4-mini: 68.1% → 79.0% (+10.9 pp); GPT-5.5: 83.1% → 90.5% (+7.4 pp).
- Calibration error decreases: DeepSeek-v4-pro 7.0 → 3.99; GPT-5.4-mini 13.7 → 7.90; GPT-5.5 15.7 → 7.58. All three accuracy improvements are statistically significant.
- Benefits extend beyond initial retrieval: For GPT-5.5, surfaced gold recall increases from 94.4 to 98.1, previewed gold recall from 72.9 to 85.9, behavior gold recall from 56.1 to 75.9.
- MultiHop-RAG: Question's Gambit improves GPT-5.4-mini accuracy from 76.0% to 77.0% and GPT-5.5 accuracy from 81.0% to 81.5%.
- Tool-use analysis: Question's Gambit uses between 2.3 and 5.3 additional total calls while delivering accuracy gains of 5.5–10.9 percentage points. The increase is concentrated primarily in the initial first-move action and subsequent document reading, while agent-issued search calls remain comparable.

## Actionable Insights
1. The first retrieval move (first move) in deep search agents is an important design decision — the quality of the opening context matters more than the tools available inside the loop. Application: provide the agent with a prepared opening context containing evidence for the clues, rather than letting the agent search from the raw question alone.
2. Decompose the question into separate clues and retrieve each clue independently, then consolidate and rerank against the full question. Application: before the agent starts its search loop, split the question into separate constraints, retrieve each constraint, merge results and rerank against the complete question.

## Assumptions & Limitations
- Evaluation focuses on fixed-corpus deep research, using the full BrowseComp-Plus benchmark and a 200-question MultiHop-RAG control set; generalization to other corpora and live web search remains to be studied.
- Evaluates three agent models.

## Metadata
- Year: 2026, authors: Radin Hamidi Rad, Amin Bigdeli, Negar Arabzadeh, Sajad Ebrahimi, Charles L. A. Clarke, Benjamin C. M. Fung, Ebrahim Bagheri (University of Toronto, Mila – Quebec AI Institute, University of Waterloo, UC Berkeley, McGill University), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.14412v1
