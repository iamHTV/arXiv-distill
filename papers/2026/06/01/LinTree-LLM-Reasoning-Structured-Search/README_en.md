# [2605.31492v1] LinTree: Improving LLM Reasoning with Explicitly Structured Search Histories

## Problem
LLMs solve reasoning problems by generating intermediate traces that explore and revise partial solutions. From a search perspective, traces are linearized search trees. But when the model backtracks or switches branches, the trace does NOT explicitly identify which search state is being revisited. Prior work has not tested whether raw search history alone is sufficient to outperform heuristic search.

## Contribution
1. **Compares trace-conditioned vs local-state heuristic**: Across 3 reasoning environments (Blocks World, Navigation, Sokoban), raw search history alone does NOT reliably outperform heuristic search.
2. **LinTree — parent pointers**: Adds simple parent pointers to explicitly represent tree structure → improves both task performance and search efficiency.
3. **Key insight**: Search history becomes most useful when tree structure is made explicit — implicit traces are not enough.

## Method (core summary)
LLM reasoning traces = linearized search trees: model extends partial solution, abandons when it fails, backtracks to try alternatives. Compares: (1) Implicit reasoning — model conditions on flat trace (no structure); (2) BFS (RL) — best-first search with LLM heuristic, only observes local state; (3) LinTree — adds parent pointers to trace, explicitly labels parent-child relationships in search tree. Parent pointers are simple: each step records "parent: step_N" to identify which search state is being expanded.

## Key Findings
- Implicit reasoning model: LOWER success rates than BFS (RL), only modest improvements in search expansions
- GRPO improves implicit policy over SFT, but still doesn't establish advantage over local-state heuristic
- LinTree (parent pointers): improves BOTH solve rate and search efficiency vs implicit reasoning
- Key: tree structure must be explicit — flat serialization loses structure
- Tested on 3 controlled environments: Blocks World, Navigation, Sokoban

## Actionable Insights
1. **Structured traces > flat traces**: When designing reasoning prompts for LLMs, add explicit structure markers. Don't just "Step 1, Step 2, Step 3" — add parent references: "Step 3 (from Step 1): trying alternative". Example: when debugging code, structured trace "Line 45 ← Line 30 ← Line 10 (root cause)" better than flat log "Line 10, Line 30, Line 45".

2. **Parent pointers are minimal change with big impact**: Just adding 1 field "parent: step_N" to each reasoning step → improves performance. Example: when building AI reasoning system, each step in chain-of-thought adds reference to step it branched from. Simple but helps model track search state.

3. **Search history alone is not enough**: Raw flat history = model doesn't exploit it. Must make tree structure explicit. Example: when training AI to explore solution space, don't just log sequential steps — log branching structure: "tried A → failed → backtracked to root → tried B → succeeded".

## Assumptions & Limitations
**Conditions for method to work:**
- Task must have tree-structured search space
- Model must be capable enough to utilize structured traces
- Parent pointers must correctly identify search states

**Limitations the paper acknowledges:**
- Tested on 3 controlled environments — generalizability unclear
- Parent pointers are minimal structure — more complex representations possible
- GRPO alone doesn't establish advantage

**Limitations the paper does NOT mention:**
- Only tests small-scale reasoning tasks — no real-world complex reasoning
- Parent pointers add overhead to trace length
- No comparison with other structured representations (graphs, DAGs)
- No cost of generating structured traces addressed
- 3 environments specific — coding, math, others may differ

## Metadata
- Year: 2026
- Authors: Liwei Kang, Yee Whye Teh, Wee Sun Lee
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.31492v1
- Citation count: [EXTRACTION FAILED]
