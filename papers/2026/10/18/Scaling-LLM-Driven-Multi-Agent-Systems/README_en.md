# [2607.27942v1] Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis

## Problem
LLM-based multi-agent systems (MAS) have the potential to solve complex tasks through coordinated ensembles of specialized agents, but the architectural design space remains largely non-systematized. There is no consensus on how to build robust, generalizable MAS, and scaling agent systems inevitably introduces new failure modes: communication overload, inter-agent inconsistency, loss of efficiency, and loss of system-wide task alignment. Prior studies examine single scaling dimensions (agent count, debate rounds) and report bounded, architecture-dependent benefits, without systematically characterizing how accuracy, cost, and reliability jointly evolve under principled architectural scaling.

## Contribution
- Four design principles for scalable MAS architectures: simplicity (P1), elastic feedback (P2), sequential workflows with optional loops (P3), and summary-based communication (P4).
- A reference architecture operationalizing these principles via a shared group chat of agent summaries and topology design rules.
- Evaluation of four configurations of increasing complexity (from 1 agent to 7 agents) on the terminal-bench benchmark (80+ system engineering tasks) using two LLMs of differing capability (GPT-5-mini, GPT-5-nano).

## Method
The reference architecture has two core components: (1) Group chat of summaries — each agent, upon completing its sub-task, posts a natural-language summary to a shared channel; subsequent agents receive the full accumulated chat history as context. (2) Directed workflow with optional loops — topology is a directed graph Gw=(A,E,s,T) with constraints: each non-terminal agent has at least one successor, each non-start agent is reachable, each agent has at most three successors. Each agent decides when done and which successor to activate via a [<next_agent>] tag in its final summary. Four configurations evaluated: Singleton (baseline), MAS-S (3 agents, 1 loop), MAS-M (5 agents, 3 loops), MAS-L (7 agents, 5 loops).

## Key Findings
- On terminal-bench, GPT-5-mini with MAS-M achieves accuracy 0.348 vs Singleton 0.296 (+15.2% relative), but MAS-L drops to 0.315 (−9.7% vs MAS-M).
- Completion token cost scales approximately linearly with architectural complexity: baseline → +1× → +1.4× → +3.2× (GPT-5-mini).
- Consistency (share of solved tasks solved in all runs) is below 50% across all configurations: 42%, 46%, 36%, 46% (GPT-5-mini).
- With GPT-5-nano (weaker model), accuracy is nearly flat (0.097 → 0.090 → 0.105 → 0.105) — architectural complexity cannot compensate for an insufficient base model.

## Actionable Insights
1. Architectural sophistication is not always better — when the base LLM is insufficiently capable, adding agents only burns tokens and propagates errors. Apply: before building multi-agent, test the base model on a single task; only expand if the model meets an acceptable threshold.
2. Performance peaks at intermediate complexity (MAS-M: 5 agents, 3 loops), not the most complex configuration. Apply: start with the simplest architecture, expand incrementally based on actual need, monitor the cost–accuracy trade-off at each step.
3. Consistency is the central bottleneck — downstream agents accept and reinforce the framing established by upstream agents. Apply: design quality-assurance (QA) agents with adversarial orientations, encouraged to probe, challenge, and proactively invoke feedback loops.

## Assumptions & Limitations
- Evaluated on terminal-bench (system engineering tasks in a terminal environment); results may not transfer directly to other domains (content, marketing, business).
- Only two models tested (GPT-5-mini, GPT-5-nano); does not generalize to all LLMs.
- Consistency measured over 3 runs; a small number of runs may not capture full stochastic variation.
- The paper does not specify training cost and detailed wall-clock time.

## Metadata
- Year: 2026, Authors: Linus Sander, Fengjunjie Pan, Vahid Zolfaghari, Andre Schamschurko, Nenad Petrovic, Alois Knoll (Technical University of Munich), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2607.27942v1