# 2605.06040 Novelty-based Tree-of-Thought Search for LLM Reasoning

## Problem

Tree of Thoughts (ToT) and CoT improve LLM reasoning but remain brittle, not human-level, and suffer high time/token costs. Branching factor leads to large compute costs. Need pruning without performance loss.

## Contribution

1. Transfer novelty concept from width-based planning to language domains — measurable novelty for LLM reasoning.
2. Novelty estimation via LLM prompting using pre-training knowledge.
3. Novelty-based pruning — prune low-novelty branches, reduce tree size → 10-20× token savings.

## Method (core summary)

Extend ToT: (1) Generate successor thoughts; (2) Estimate novelty per thought via LLM comparison with previous thoughts; (3) Prune below threshold; (4) Many reasoning problems have width <3 → aggressive pruning possible; (5) Additional novelty prompt vs. reduced tree → net savings.

## Key Findings

- Up to 20× token cost reduction for same performance (Blocksworld DFS)
- Many reasoning problems have inherent width <3
- Game of 24: 3/50 normal, 23/50 thinking mode
- 229K tokens/task normal, 330K thinking without pruning
- Tuning required — poorly configured settings degrade performance

## Actionable Insights

1. Add novelty pruning to ToT → 10-20× token savings. Example: math reasoning — prune redundant approaches, focus on unique paths.
2. Width <3 insight: only explore 2-3 truly different approaches. Example: debugging — 2-3 failure modes, prune redundant explorations.
3. 1 novelty prompt per thought saves many downstream calls. ROI positive at depth >3.

## Assumptions & Limitations

- Assumption: LLM accurately estimates novelty
- Limitation: Tuning required per domain
- Limitation: Additional prompt overhead
- Limitation: Limited benchmarks tested
- Limitation (observed): Novelty quality depends on LLM capability

## Metadata

- Year: 2026
- Authors: Leon Hamm, Zlatan Ajanovic
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.06040
- Citation count: N/A
- Classification: [applied]
- Skill: novelty-pruning-tree-of-thought
