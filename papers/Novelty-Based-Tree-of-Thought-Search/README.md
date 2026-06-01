# 2605.06040 Novelty-based Tree-of-Thought Search for LLM Reasoning

## Problem

Tree of Thoughts (ToT) và chain-of-thought cải thiện LLM reasoning nhưng vẫn brittle (dễ gãy), chưa đạt human-level, và suffer high time/token costs (chi phí thời gian/token cao). Branching factor (hệ số phân nhánh) của tree search dẫn đến compute costs lớn. Cần cách prune (cắt tỉa) search tree mà không giảm performance.

## Contribution

1. Transfer concept of novelty từ width-based planning sang language domains — define measurable novelty (tính mới có thể đo lường) cho LLM reasoning: uniqueness của new thought so với previously seen thoughts trong search tree.
2. Novelty estimation bằng LLM prompting — leverage embedded general knowledge từ pre-training để estimate novelty score.
3. Novelty-based pruning — prune branches với low novelty, reduce overall tree size → reduce token cost while maintaining performance.

## Method (tóm tắt cốt lõi)

Extend Tree of Thoughts với novelty concept: (1) Standard ToT: generate successor thoughts via LLM prompting; (2) Novelty estimation: for each new thought, prompt LLM to compare with previously seen thoughts, estimate novelty score (how unique is this thought?); (3) Pruning: thoughts với novelty below threshold → prune branch, don't explore further; (4) Width-based search insight: many reasoning problems have low inherent width (<3), meaning most branches are redundant → aggressive pruning possible; (5) Trade-off: additional novelty prompts per state vs. reduced overall tree size → net token savings.

## Key Findings

- Novelty pruning reduces token cost up to 20× for same performance (Blocksworld DFS)
- Many LLM reasoning problems have low inherent width (width <3) → high pruneable state volume
- Game of 24: LLM struggle with complex planning (3/50 normal, 23/50 thinking mode)
- Explicitly separating steps (ESA) degraded performance
- Average 229K tokens (normal), 330K tokens (thinking) per task without pruning
- In poorly configured settings, performance degraded significantly — tuning required
- Novelty concept transfers from classical planning to language reasoning domains

## Actionable Insights

1. Khi dùng Tree of Thoughts, thêm novelty-based pruning để giảm 10-20× token cost. Ví dụ: math reasoning task với ToT — mỗi thought có novelty score, prune branches mà novelty thấp (redundant approaches), focus compute vào unique solution paths.
2. Width-based insight: nhiều reasoning problems có inherent width <3 — nghĩa là chỉ cần explore 2-3 truly different approaches, không cần exhaustive branching. Ví dụ: code debugging — chỉ 2-3 distinct failure modes, prune redundant explorations.
3. Novelty estimation cost-effective: 1 additional LLM call per thought để estimate novelty, nhưng saves many downstream calls bằng pruning non-novel branches. ROI positive khi tree depth >3.

## Assumptions & Limitations

- Giả sử: LLM can accurately estimate novelty — may not always be reliable
- Limitation: Tuning required — novelty threshold và pruning aggressiveness are domain-specific
- Limitation: Additional prompt overhead per state — only saves when tree is large enough
- Limitation: Tested on limited benchmarks (Blocksworld, Game of 24)
- Limitation (tự thấy): Novelty estimation quality depends on LLM capability — weaker models may give poor novelty scores, leading to over-pruning

## Metadata

- Năm: 2026
- Tác giả: Leon Hamm, Zlatan Ajanovic
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.06040
- Citation count: N/A
- Nhãn: [applied]
- Skill: novelty-pruning-tree-of-thought
