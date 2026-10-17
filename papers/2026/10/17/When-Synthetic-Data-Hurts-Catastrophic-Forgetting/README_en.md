# [2609.10750v1] When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents

## Problem
- LLM agents increasingly rely on external skills retrieved at runtime, making skill selection from large repositories a critical challenge. Prior work does not address whether synthetic-data fine-tuning degrades a model's ability to retrieve skills for real-world or out-of-distribution (OOD) tasks.

## Contribution
- Production skill router over 34,396 skills and a large-scale study of skill retrieval using limited real supervision and synthetic data.
- Two synthetic training tracks: Track A (~15K pairs) creates anchor-skill tasks with retrieval-derived positives and hard negatives; Track B (~14K pairs) combines real data, paraphrase generation, and multi-skill task synthesis.
- Evaluates several forgetting mitigation fine-tuning approaches: embedding-anchor regularization, Learning without Forgetting (LwF), Elastic Weight Consolidation (EWC), and L2-initialization.

## Method (core summary)
- Repository of 34,396 skills.
- Tasks from SkillsBench and Terminal-Bench 2, ~1K trials across 109 tasks using hybrid retrieval pipelines in Harbor environment.
- Two synthetic training tracks: Track A (~15K pairs) with retrieval-derived positives and hard negatives; Track B (~14K pairs) combining real data, paraphrase generation, and multi-skill task synthesis.
- Evaluates compact retrieval models such as Qwen3-Embedding-0.6B under varying fine-tuning regimes.

## Key Findings
- 5 authors from Manulife, arXiv category: cs.IR.
- Synthetic supervision improves in-distribution retrieval but causes catastrophic forgetting on real and OOD data.
- In the most aggressive fine-tuning configuration, OOD recall drops from 0.850 to 0.650.
- Forgetting mitigation approaches (embedding-anchor regularization, LwF, EWC, L2-initialization) retain OOD performance AND improve synthetic in-distribution retrieval by 13.98% for 0.6B Qwen retriever and reranker.

## Actionable Insights
1. Synthetic-data fine-tuning improves in-distribution retrieval but causes catastrophic forgetting on real and OOD data. Application: when fine-tuning a retrieval model on synthetic data, use forgetting mitigation approaches like LwF, EWC, L2-initialization.
2. Forgetting mitigation approaches (embedding-anchor regularization, LwF, EWC, L2-initialization) not only retain OOD performance but also improve synthetic in-distribution retrieval by 13.98% for 0.6B Qwen retriever and reranker. Application: always apply forgetting mitigation techniques when fine-tuning on synthetic data.

## Assumptions & Limitations
- Statistical power limited: Val-set 1 (n=21) and Val-set 3 (n=10) are small; single-task variations can shift RECALL@10 by ~5%.
- Evaluated on 34,396-skill repository.
- Focused on Qwen3-Embedding-0.6B model.

## Metadata
- Year: 2026, authors: Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund (Manulife), arXiv category: cs.IR, PDF link: https://arxiv.org/pdf/2609.10750v1
