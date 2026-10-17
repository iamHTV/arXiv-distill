# [2609.26760v2] Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents

## Problem
- Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. Prior work does not address whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning.

## Contribution
- Grow the Harness — a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fixed model and tool interfaces but encodes no task-solving controller.
- Function-level execution traces localize each failure to a bounded code surface; an optimizer repairs a window of failures jointly, and a success-first held-out gate rolls back repair sequences that harm prior capability.
- Accepted edits accumulate in one shared harness, allowing its control structure to emerge from task feedback.
- Across BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters, Growing Harness achieves the highest mean success in five of six benchmark-model settings and trails the best mean by 0.7 pp. in the sixth.
- Relative to a Tool-Calling agent, it reduces LLM calls by 76.0–91.8% and deployed-agent inference cost by 74.4–98.6%.
- On WebArena-Verified, its success remains 44.7–45.3% across model scales, whereas Tool-Calling falls to 6.7% with the 4B model.

## Method (core summary)
- Strategy-free scaffold that exposes fixed model and tool interfaces but encodes no task-solving controller.
- Function-level execution traces localize each failure to a bounded code surface.
- Optimizer repairs a window of failures jointly.
- Success-first held-out gate rolls back repair sequences that harm prior capability.
- Accepted edits accumulate in one shared harness.
- Evaluated on BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters.

## Key Findings
- 10 authors from SII, Chinese Academy of Sciences, UCAS, Shenzhen University of Advanced Technology, University of Macau, arXiv category: cs.AI.
- Across four benchmarks and two backbones, Growing Harness achieves the highest mean success in five of six benchmark-model settings and trails the best mean by 0.7 pp. in the sixth.
- Relative to Tool-Calling agent, it reduces LLM calls by 76.0–91.8% and deployed-agent inference cost by 74.4–98.6%.
- On WebArena-Verified, its success remains 44.7–45.3% across model scales, whereas Tool-Calling falls to 6.7% with the 4B model.

## Actionable Insights
1. Turn agent feedback into reusable executable code instead of having the LLM re-derive control decisions each task. Application: convert feedback into reusable control code, reducing LLM calls by 76.0–91.8% and inference cost by 74.4–98.6%.
2. Turn agent feedback into reusable executable code instead of having the LLM re-derive control decisions each task. Application: convert feedback into reusable control code, reducing LLM calls by 76.0–91.8% and inference cost by 74.4–98.6%.

## Assumptions & Limitations
- Evaluated on BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters.
- No detailed information about training time and computational cost.

## Metadata
- Year: 2026, authors: Laizhen Li, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang (SII, Chinese Academy of Sciences), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.26760v2
