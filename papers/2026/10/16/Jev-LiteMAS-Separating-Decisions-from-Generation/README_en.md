# [2610.21411v1] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

## Problem
Many multi-agent LLM systems use generative models for everything, including coordination operations that only need bounded decisions (selecting the next expert, pass/escalate). Using a large LLM for every decision wastes token between expert contributions.

## Contribution
- Introduce Jev-LiteMAS: combine a lightweight decision model (Jev) with generative execution and feedback.
- Solve planning gap: Jev dynamically selects experts from task and prior expert outputs, using accumulated context to ground subsequent execution without pre-generated trajectory.
- Solve review gap: Jev screens intermediate artifacts against task criteria; passing artifacts proceed directly, failing ones go to LLM review.

## Method (core summary)
Pipeline has two components: (1) Jev decision model takes task rubric, does local check (PASS/ESCALATE). PASS → artifact proceeds; ESCALATE → LLM review returns ACCEPT/REVISE + feedback, state updated. (2) Generative experts receive artifact via handoff and continue work within their responsibility. State is updated after each step.

## Key Findings
- Routing and review account for 31.7–43.5% of generative-LLM tokens across six measured MAS.
- vs LAS: Jev-LiteMAS reduces 12.7–54.6% generative-LLM tokens, accuracy within 1.34 percentage points, lower latency in 7/8 configurations.
- Jev screening detects 91.33–95.33% of corrupted artifacts; cascaded config uses 14.6–21.7% fewer tokens than LLM judging.
- Jev accounts for 2.92–6.85% of end-to-end latency and 1.56–2.14% of LLM model cost.

## Actionable Insights
- Don't use large LLM for every coordination decision: replace with lightweight decision model to route experts and filter artifacts; call LLM only when artifact needs revision. Apply: solopreneur running AI/content automation pipeline can cut inference cost by tens of percent.
- Keep semantic feedback when revising artifacts: removing it drops accuracy from 75.33% to 57.33% on IDRBench I3. Apply: when agent fixes code/text, it must explain why so the next agent knows how to adjust.

## Assumptions & Limitations
- Requires predefined pool of expert roles and legal actions; cannot create new experts for unseen tasks.
- Paper admits: when more artifacts need generative review, token/latency savings decrease.
- Limitation paper doesn't mention: not evaluated on sub-4B models, not tested on workflows longer than 8 steps.

## Metadata
- Year: 2026
- Authors: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li (Shanghai Jiao Tong University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.21411
