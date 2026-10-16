# [2610.11578v1] Chronos Enables Code Agents to Reason over Software Evolution

## Problem
Historical pull requests record the design decisions, compatibility constraints, and implementation patterns behind a codebase's current state. Experience relevant to a new task can span related changes whose descriptions emphasize different concerns. Current code agents often cannot access and use this history effectively.

## Contribution
- Introduce Chronos: a test-time framework that makes this connected history available to LLM agents.
- Chronos raises the mean resolution rate from 69.2% to 72.9% (+3.7pp) and reaching 79.8% with MiniMax M2.5.
- With the same backbone, Chronos raises resolution rates from 48.3% to 51.7% on SWE-Bench Pro and from 41.0% to 43.5% on FEA-Bench Lite.
- Two single-agent variants reach 78.4% and 77.8%, compared with 76.4% for the base agent.
- Fraction of tasks receiving useful experience: 68% → 89% (compared with flat semantic retrieval).
- Graph-grounded retrieval: useful-card fractions 12.4% (Embedding) → 28.7% (Chronos); Hit from 68% → 89%.

## Method (core summary)
Chronos is a test-time framework that makes pull request history available to LLM agents. The system uses pull request history to provide relevant experience for new tasks, helping agents make better decisions about bug fixes, feature implementation, and code refactoring.

## Key Findings
- Chronos raises mean resolution rate from 69.2% to 72.9% (+3.7pp) and reaching 79.8% with MiniMax M2.5.
- With same backbone: SWE-Bench Pro 48.3% → 51.7%, FEA-Bench Lite 41.0% → 43.5%.
- Two single-agent variants: 78.4% and 77.8%, vs base agent 76.4%.
- Fraction of tasks receiving useful experience: 68% → 89% (vs flat semantic retrieval).
- Graph-grounded retrieval: useful-card fractions 12.4% → 28.7%; Hit from 68% → 89%.
- Full workflow: 79.8% resolution rate with graph-grounded retrieval, 79.0% with flat semantic search (+0.8pp).

## Actionable Insights
- Use pull request history to provide relevant experience for code agents, instead of only relying on model's internal knowledge. Apply: solopreneur building code development agents should integrate pull request history so agents understand why code was written that way.
- Use graph-grounded retrieval instead of flat semantic retrieval to improve quality of retrieved experience. Apply: when building code development agents, build a knowledge graph from pull request history so agents can retrieve experience more accurately.

## Assumptions & Limitations
- Requires pull request history and real codebase data; doesn't apply without pull request history.
- Paper admits: evaluated on SWE-Bench Pro and FEA-Bench Lite; may differ on other tasks.
- Limitation paper doesn't mention: not evaluated on many domains beyond software development, not tested on real system cost.

## Metadata
- Year: 2026
- Authors: Xin Yin, Yiang Zhang, Zhiyuan Peng, Chao Ni, Zhe Cui, Xiaohua Xin (Zhejiang University, Shanghai Jiao Tong University, Hithink Research, National Industrial Information Security Development Research Center)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.11578
