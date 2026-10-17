# Skill: synthetic-data-forgetting-mitigation
Source: 2609.10750v1
Type: framework

## When to use this skill
- Fine-tuning a retrieval model (e.g., Qwen3-Embedding-0.6B) on synthetic data for skill retrieval for LLM agents.
- Want to improve in-distribution retrieval without causing catastrophic forgetting on real and OOD data.
- Have limited real data and synthetic data available.

## When NOT to use this skill
- No synthetic data available for fine-tuning.
- Don't need to fine-tune the retrieval model (just use existing model as-is).
- Don't care about OOD performance (only care about in-distribution).

## Input needed
- Synthetic data for fine-tuning (e.g., Track A ~15K pairs or Track B ~14K pairs).
- Real data for evaluating OOD performance.
- Compact retrieval model such as Qwen3-Embedding-0.6B.
- Evaluation dataset with skills and queries.

## Steps to execute
1. Build synthetic data: Track A (~15K pairs) creates anchor-skill tasks with retrieval-derived positives and hard negatives; Track B (~14K pairs) combines real data, paraphrase generation, and multi-skill task synthesis.
2. Fine-tune the retrieval model (e.g., Qwen3-Embedding-0.6B) on synthetic data under varying fine-tuning regimes.
3. Apply forgetting mitigation approaches: embedding-anchor regularization, Learning without Forgetting (LwF), Elastic Weight Consolidation (EWC), and L2-initialization.
4. Evaluate on synthetic data (in-distribution) and real/OOD data (out-of-distribution).
5. Compare performance before and after applying forgetting mitigation approaches.

## Expected output
- Retrieval model with good performance on synthetic data (in-distribution) without causing catastrophic forgetting on real and OOD data.
- Forgetting mitigation approaches improve synthetic in-distribution retrieval by 13.98% for 0.6B Qwen retriever and reranker.

## Application example
- Build a skill retrieval system for LLM agents: fine-tune Qwen3-Embedding-0.6B on synthetic skill data, apply forgetting mitigation approach (e.g., LwF or EWC) to maintain performance on real and OOD data.

## Gotchas
- Synthetic-data fine-tuning improves in-distribution retrieval but causes catastrophic forgetting on real and OOD data.
- In the most aggressive fine-tuning configuration, OOD recall drops from 0.850 to 0.650.
- Forgetting mitigation approaches not only retain OOD performance but also improve synthetic in-distribution retrieval.
