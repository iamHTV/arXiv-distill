# [2610.25954v1] CXBENCH: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows

## Core Value (1 sentence)
CXBENCH evaluates outcome and process compliance separately for LLM agents in regulated customer-service workflows: 69.29% of executions pass outcome but only 13.81% pass both, with 55.48% being false-passes (outcome correct but process-violating).

## Problem
Existing tool-agent benchmarks largely score final business states, accepting trajectories that reach correct outcomes through non-compliant processes. In regulated domains (banking, telecom, insurance, healthcare, utilities, government benefits), agents must also provide disclosures, obtain consent, and follow required procedures — not just achieve the right business result.

## Contribution
1. Propose CXBENCH, a benchmark evaluating outcome and process compliance separately across 120 tasks in 6 regulated domains.
2. Rule cards link cited regulatory obligations to observable trace evidence; a hybrid grader combines deterministic checks for ordering and authority with an LLM judge for semantic requirements.
3. Define false-pass: an outcome-pass run that fails process checks — exposing failures hidden by outcome-only scoring.
4. Shared execution with submission controls: default mediated-submit mode where the runtime submits drafts only after customer confirmation; direct-submit mode for studying submission authority effects.

## Method
CXBENCH evaluates each episode on two axes: outcome (whether the business result was achieved) and process (whether the recorded interaction satisfied applicable requirements). Each task combines a customer request, a tool-based environment, and explicit process requirements. The agent interacts with a customer simulator (gpt-5.4-mini) via conversation and uses domain-specific tools through a shared runtime, which records the trace. After execution, an outcome checker evaluates the final business state; a hybrid process grader combines deterministic checks (event ordering, tool permissions, confirmation-submission agreement) with an LLM judge (gpt-5.6-sol) for semantic requirements against a task-specific checklist. Both components must pass for process verdict to pass. Overall success requires both verdicts. False-pass = outcome pass ∧ process fail. Default runtime mode: agent prepares a draft, runtime submits only after customer confirms matching fields under the task's confirmation contract; direct-submit mode exposes submission tools to the agent and disables runtime-mediated submission.

## KNOWLEDGE — Data & Concepts
- 120 tasks across 6 regulated domains: banking, telecommunications, insurance, healthcare, utilities, government benefits (20 tasks per domain)
- 7 models evaluated, 840 records total
- Customer simulator: gpt-5.4-mini; Judge: gpt-5.6-sol
- 53 rule cards (53 obligations extracted from regulatory materials via Legal Information Institute, deduplicated to 53 cards)
- 69.29% (582/840) of executions pass outcome check
- 13.81% (116/840) of executions pass both outcome and process checks
- 466 false-passes = 55.48% of all evaluations, 80.07% of outcome passes
- Domain variation: banking 94.29% outcome-pass but 5.71% both-pass; government benefits 84.29%/4.29%; healthcare 13.57%/2.14%
- False-pass breakdown: 329 rejected only by LLM judge, 38 only by hard rules, 99 by both; 35 of 53 hard rules fail at least once; insurance ordering rule fails in 47 false-pass records
- Submission control: mediated-submit both-pass 20.83%, direct-submit 0.83%, direct-submit (checks excluded) 18.33%; false-pass rises from 43.33% to 66.67%
- Judge configuration: gpt-6-astra changes pooled both-pass from 13.89% to 14.72%, preserves all strict pairwise orderings (Kendall's τb = 0.9661); hybrid verdicts agree 92.22%
- Judge accuracy on development traces: 88.33%; process pass precision 69.70%, recall 85.19%, F1 76.67%; process failure precision 95.40%, recall 89.25%
- Per-model results (Table 3): glm-5.1 (outcome 77.50%, both-pass 21.67%, false-pass 55.83%); gpt-5.4 (64.17%, 20.83%, 43.33%); gpt-5.4-mini (61.67%, 15.00%, 46.67%); qwen3.6-plus (70.83%, 15.00%, 55.83%); deepseek-v4-flash (77.50%, 13.33%, 64.17%); qwen3.5-plus (70.83%, 8.33%, 62.50%); gpt-4o-mini (62.50%, 2.50%, 60.00%)
- deepseek-v4-flash and glm-5.1 tie on outcome rate (77.50%) but reach 13.33% and 21.67% both-pass respectively; gpt-5.4 has lower outcome rate (64.17%) but higher both-pass rate (20.83%) than deepseek-v4-flash

## INSIGHT — Mechanism & Why
[Outcome-only scoring overlooks process violations] BECAUSE [agents can achieve correct final states through non-compliant processes, such as missing required disclosures or consent; checking only the final state cannot detect violations during the interaction]. This means [agent reliability is overestimated if only outcomes are scored].
[Hybrid grader detects complementary failures] BECAUSE [deterministic checks evaluate ordering and authority while LLM judge evaluates semantic requirements; 329/466 false-passes are rejected only by LLM judge, 38 only by hard rules, 99 by both]. This means [both types of checks are necessary — neither is sufficient alone].
[Submission control has large effect on both-pass] BECAUSE [when agents submit directly (direct-submit), both-pass drops from 20.83% to 0.83%, false-pass rises from 43.33% to 66.67%; excluding submission-mechanism checks rescores both-pass at 18.33%]. This means [submission authority is a real interventional variable, not just a scoring artifact].
[Model ordering changes when process compliance is included] BECAUSE [models with high outcome can have low process (deepseek-v4-flash outcome 77.50% but both-pass only 13.33%), while gpt-5.4 has lower outcome (64.17%) but higher both-pass (20.83%)]. This means [outcome-only scoring can mis-rank models].

## IDEA — Actionable Applications
1. Apply [hybrid grader (deterministic + LLM judge)] to [evaluating process compliance of enterprise agents]: first step is to build rule cards linking regulatory obligations to trace evidence, then combine deterministic checks for ordering/authority with LLM judge for semantic requirements.
2. Apply [false-pass metric] to [detecting failures hidden by correct outcomes]: first step is to track executions that pass outcome but fail process checks, treating them as potential compliance risks.
3. Apply [runtime mediated-submit] to [controlling submission authority for business actions]: first step is to configure runtime to submit drafts only after customer confirms matching fields, not allowing agents to submit directly.

## WISDOM — General Principles
1. Principle: Correct outcome does not imply correct process — an agent can achieve the business goal while violating regulated procedures. Apply when: evaluating agents in regulated environments (finance, healthcare, insurance). Do not apply when: tasks have no explicit process requirements.
2. Principle: Process compliance evaluation requires combining deterministic checks (ordering, authority) and semantic evaluation (LLM judge) — neither is sufficient alone. Apply when: building agent compliance evaluation systems. Do not apply when: only need simple final-state checking.

## Assumptions & Limitations
- Conditions that must hold: domain-specific tool environment available, customer simulator available, process requirements encoded as rule cards.
- Limitations acknowledged by paper: evaluation does not by itself establish legal compliance of real-world deployment; judge development involved 5 senior software engineering experts (one drafted, three reviewed, one annotated 120 gpt-5.4-mini traces); these are calibration traces, not an independent held-out validation set.
- Limitations paper does NOT mention: no evaluation on tasks outside regulated customer service; no direct comparison with other benchmarks beyond Table 1; no real inference cost of hybrid grader measured.

## Metadata
- Year: 2026
- Authors: Boxi Yu, Yuzhong Zhang, Zhenfeng Su, Linfu Xi, Yinghan Yao, Shitao Chen, Yang Cao, Liting Lin, Lionel Briand, Emir Muñoz (Lero/University of Limerick, CUHK-Shenzhen, Peking, Xi'an Jiaotong, South China Univ of Technology, Genesys Cloud)
- arXiv Category: cs.AI
- PDF Link: https://arxiv.org/pdf/2610.25954
- arXiv ID: 2610.25954v1
- Label: [applied]
- Citation count: [not found]