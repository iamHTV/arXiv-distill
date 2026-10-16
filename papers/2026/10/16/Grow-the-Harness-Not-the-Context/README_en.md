# [2609.26760v2] Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents

## Problem
LLM agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context, wasting tokens and inference cost.

## Contribution
- Study whether task feedback can turn recurring control decisions into reusable specialist agents instead of letting LLM re-process repeatedly.
- Growing Harness: replace inference with code, turn feedback into reusable control structure, cutting 76–92% LLM calls and 74–99% inference cost.
- Evaluated on BrowseComp-Plus and WebArena-Verified; success stays at 44.7–45.3% across model scales, while Tool-Calling drops to 6.7% with a 4B model.

## Method (core summary)
Growing Harness learns the harness agent from failure-guided feedback, turning control into reusable code instead of letting LLM re-process repeatedly. Includes function-level guidance, gate validation, and trace-local edits. Each optimization step improves the harness based on feedback from prior runs.

## Key Findings
- Reduce 76.0–91.8% LLM calls and 74.4–98.6% online cost vs Tool-Calling across six settings.
- WebArena-Verified: success stays at 44.7–45.3% across three deployment models, while Tool-Calling drops from 30.0% (gpt-oss-120b) to 6.7% (Qwen3.5-4B).
- BrowseComp-Plus: +17.3 pp, -90% cost; WebArena-Verified: +38.6 pp, -99% cost; +32.0 pp, -91% cost; +15.3 pp, -96% cost depending on configuration.
- Replacing inference with code: 76–92% fewer LLM calls at 74–99% lower cost.
- Removing function-level guidance halves final success from 36% to 18%.

## Actionable Insights
- Instead of letting LLM re-think everything in every task, build a reusable harness (control code) from feedback of previous runs. Apply: solopreneur running agents that process related tasks (web browsing, data extraction) should save control decisions as reusable code, only call LLM when truly needed.
- Use few-shot or function-level guidance to maintain accuracy while reducing LLM calls. Apply: when building an agent pipeline, add function-level guidance and gate validation so the agent doesn't over-think.

## Assumptions & Limitations
- Requires related tasks so feedback can accumulate; doesn't apply to fully independent tasks.
- Paper admits: WebArena-Verified success only 44.7–45.3%, still low for production-grade deployment.
- Limitation paper doesn't mention: not evaluated on tasks beyond web browsing, not tested on multi-agent collaboration.

## Metadata
- Year: 2026
- Authors: Laizhen Li, Jiarui Li, Juanjuan Zhao, Kejiang Ye, Ye Li, Cheng-zhong Xu, Xitong Gao
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.26760
