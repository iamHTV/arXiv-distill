# Skill: questions-gambit-first-move-retrieval
Source: 2609.14412v1
Type: framework

## When to use this skill
- Building deep search agents that answer complex questions through iterative loops of searching, reading, and reasoning.
- Need to improve the first retrieval move — the opening context the agent receives before starting its search loop.
- Have a fixed document corpus and a retriever tool available.

## When NOT to use this skill
- Questions that are not multi-clue (don't have multiple different constraints requiring evidence from different documents).
- No retriever tool available or cannot build an opening context.
- Live web search rather than fixed-corpus search.

## Input needed
- Complex question with multiple different constraints (multi-clue).
- Document corpus to retrieve from.
- Retriever tool returning a ranked list of documents.
- Large language model to decompose the question into clues and act as the agent.

## Steps to execute
1. Decompose the question into a set of clues (information fragments/constraints) — each clue is one constraint the answer must satisfy.
2. Retrieve each clue independently: issue each clue to the retriever, keep the returned documents as a feedback set.
3. Expand each clue: use an expansion model to rewrite the clue based on the feedback set, then concatenate clue, expansion, and question into a single search string.
4. Merge per-clue lists into a deduplicated pool.
5. Rerank the pool against the original question using a pointwise reranker — each document is scored on how well it serves the question as a whole.
6. Take the top-k documents as the opening context O.
7. Insert the opening context into the agent trajectory as the first observation o1, then let the agent continue its search-and-reasoning loop normally.

## Expected output
- Answer accuracy improves: GPT-5.5 from 83.1% to 90.5% (+7.4 pp), GPT-5.4-mini from 68.1% to 79.0% (+10.9 pp), DeepSeek-v4-pro from 71.4% to 76.9% (+5.5 pp).
- Calibration error decreases: GPT-5.5 from 15.7 to 7.58.
- Gold recall improves at every stage: surfaced from 94.4 to 98.1, previewed from 72.9 to 85.9, behavior from 56.1 to 75.9 (with GPT-5.5).

## Application example
- Deep research agent answering "Who is Aman's wife?" with multiple constraints (immigrated 1890-1899, worked as farmer in Washington, major life event at hotel wedding 1940-1944, name appeared on historic Montana list before 2023): split question into separate clues, retrieve each clue, merge and rerank against the full question, provide opening context to agent before starting search loop.

## Gotchas
- Evaluation focuses on fixed-corpus deep research; generalization to live web search not studied.
- Module runs once entirely within the agent's first action — no retraining of agent or retriever required.
- Tool calls increase by 2.3–5.3 total calls but concentrated primarily in initial first-move action and subsequent document reading; agent-issued search calls remain comparable.
