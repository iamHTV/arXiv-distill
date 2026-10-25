# Daily arXiv distill summary — 2026-10-26

Today the system scanned arXiv, filtered by topic, and distilled 3 papers on AI/LLM/agents suitable for Vietnamese solopreneurs. Each paper is summarized by three questions: **What it does** / **What you learn** / **How to apply it**. All figures come directly from the source papers.

### [1] Neuro-Inspired Inhibitory Message Passing for Accurate and Token-Efficient Multi-Agent Reasoning (2610.24718v1)

**What it does:** Builds a training-free message router for multi-agent groups — forwards only the original evidence sentence each receiver does not yet have, removing duplicates and sender reasoning/answers.

**What you learn:** Limiting redundant information sent to each agent makes the group 39-77 percentage points more accurate and cuts 10-46% of tokens (text processing units) per run, stable even with up to 64 agents. On HiddenBench, Qwen3-8B keeps 80-86% accuracy from 4 to 64 agents, versus standard communication (23% at N=4, dropping to 8% at N=64).

**How to apply it:** When running a multi-agent group for business decisions, set up a router that sends only new information each member does not know yet, instead of pushing the whole discussion — keeps group chats/meetings concise and avoids early majority bias.

### [2] ARCTIC-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design (2610.24914v1)

**What it does:** Builds a reinforcement learning foundation for software-engineering agents, combining system design and modeling — overfitting on a small task set as a stress test, gated reward, aligning training and inference engines.

**What you learn:** Qwen3.5-4B achieves 62.0% pass@1 (first-try pass rate) on SWE-bench Verified (coding-agent benchmark), equivalent to FrogNano (61.5%) with only about 1/6 of the training runs. A strong baseline (foundation) matters more than a new algorithm.

**How to apply it:** Before deploying a new agent, establish a strong baseline on a small, stable task set — if you cannot hold results on the small set, the new method will not improve overall.

### [3] CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents (2610.27645v1)

**What it does:** Builds an evaluation benchmark and training data for error recovery of computer-using agents (CUA) in long-horizon workflows, from real errors caused by the agent itself (not manually injected errors).

**What you learn:** Clean-start success does not predict error recovery — Kimi-K3 solves 66.9% of tasks from scratch but recognizes only 7.8-18.5% of its own errors. Fine-tuning on verified recovery trajectories raises error awareness rate (EAR) from 19.9% to 35.2%.

**How to apply it:** In automated retail or customer support, before accepting an order, check early decisions (product selection, quantity), not just the final state — an early error can ruin the whole order and only surface at delivery.

## WHAT YOU CAN APPLY

1. Set up a router that sends only new information each member does not know (message routing) — keeps agent groups/meetings concise and avoids early majority bias.
2. Build a strong baseline on a small task set before deploying a new agent — avoid wasting effort on unstable methods.
3. Check early decisions in automated workflows (orders, quantities), not just final state — catch errors early before they cause harm.
4. Use real error-recovery data (not duplicated success data) to fine-tune your agent — helps it recognize and fix its own errors.
5. Evaluate agents by error-recovery ability, not just clean-start success — a strong agent can still fail from an undetected early error.

---
Summary of 3 papers distilled today. Details per paper in `papers/2026/10/26/`.
