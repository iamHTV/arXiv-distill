# 2610.32305 — DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks

## Core Value (1 sentence)

DMAIC-Bench is a benchmark for evaluating agent "self-restraint": the capacity to stop or redirect when intermediate evidence shows prerequisites are unmet — not just judging output quality. Across 13 frontier models, execution-level routing accuracy averages 92% on GO decisions but only 19% on NO-GO decisions, and blinded expert review finds 47% of reached NO-GO decisions have reports acting on invalid evidence.

## Problem

Existing agent benchmarks primarily measure task completion or final artifact quality, without testing whether agents use intermediate evidence to decide whether to continue, redirect, or stop at each stage of multi-stage analytical tasks. Self-reflection — an agent critiquing its own output — does not demonstrate that evidence changed the next action. This capability is called "self-restraint" and has not been evaluated in any agent benchmark.

## Contribution

1. **DMAIC-Bench**: A benchmark for evaluating self-restraint with 97 seeded multi-stage tasks across 15 industrial cases in 4 sectors, built on Lean Six Sigma's explicit statistical prerequisites (Define–Measure–Analyze–Improve–Control cycle).
2. **Paired counterfactual variants**: Require opposite actions at the same workflow position, distinguishing warranted restraint from indiscriminate stopping.
3. **Execution trace scoring and independent expert review**: Any forbidden downstream computation after a failed diagnostic counts as a route error, even if the report withholds its result.
4. **Life sciences extension**: 16 RNA-seq and GWAS tasks show the framework can evaluate evidence-dependent decisions beyond industrial workflows.

## Method

DMAIC-Bench builds each case as a guarded decision graph with graded decision forks. At each fork, the agent must use diagnostic evidence to decide whether to proceed (GO), divert, gather remedial data, or stop (NO-GO).

**Evaluation:**
- 13 frontier models from 6 providers, each completing 3 independent attempts per task.
- Each complete episode traverses 300 evaluated decisions: 52 NO-GO and 248 GO choices.
- 40 matched forks pair all 52 NO-GO instances with 146 topologically identical GO counterparts, isolating the role of seeded data while keeping workflow positions fixed.
- Scoring via a private scorer reading execution traces; final claims evaluated through blinded expert review.
- Metrics: pass@k (fraction of tasks succeeding in at least one of k attempts) and pass_k (fraction succeeding across all k attempts).
- No proprietary agent scaffolding or custom prompt adapters, to preserve evaluation neutrality across vendors.

## KNOWLEDGE — Data & Concepts

- 97 seeded multi-stage tasks, 15 industrial cases, 4 sectors; 8 cases adapted from real black-belt improvement project closure reports.
- 13 models from 6 providers.
- Execution-level routing accuracy averages 92% on matched GO decisions (confidence interval 86–97).
- Accuracy on NO-GO decisions only 19% (confidence interval 8–30); a 73-point gap (interval 59–87).
- 174 instances: agents ran forbidden computation after logging a failed diagnostic.
- Blinded expert audit of 11 agents: 47% of reached NO-GO decisions have reports acting on invalid evidence (interval 31%–61%).
- Only 0–7 cases for some models correctly identify all failed prerequisites.
- 12/13 models remain below 50% NO-GO accuracy even with explicit stopping permission.
- Life sciences extension: 16 RNA-seq and GWAS tasks show the framework transfers.

## INSIGHT — Mechanism & Why

[The 73-point gap between GO and NO-GO] occurs BECAUSE [agents are good at continuing when evidence supports it, but poor at stopping when evidence opposes it — self-reflection only judges output without demonstrating that evidence changed the next action]. This means [evaluating agents only by final outcomes hides flaws in trajectory management].

[Reports acting on invalid evidence at 47% of reached NO-GO decisions] occurs BECAUSE [agents often make correct diagnoses but still perform analyses that those results disallow, or omit the failed result from reports]. This means [correct diagnosis is not sufficient — agents must govern their trajectory based on computed evidence].

[Explicit stopping permission helps some models but does not consistently restore correct decisions at both GO and NO-GO forks] occurs BECAUSE [the core issue is not permission to stop, but the agent's ability to identify failed prerequisites and act on them]. This means [intervention is needed in the evidence-based decision mechanism, not just permission to stop].

## IDEA — Actionable Applications

1. Build checkpoints in multi-agent analytical pipelines: before the agent performs expensive analysis, require the agent to confirm prerequisites from previous step results. First step: add a "gate" step between data processing stages where the agent must log prerequisite OK/FAILED before continuing.

2. Use counterfactual task design to test agents: create paired similar tasks where seeded data leads to opposite diagnoses, requiring opposite actions at the same workflow position. First step: in internal agent evaluation, create mirror task pairs with opposite diagnoses and measure whether the agent changes its action.

3. Apply blinded expert review to agent reports: experts unaware of automatic evaluation results review agent reports to check whether the agent acted on invalid evidence. First step: select failed agent reports, send to blinded experts for evidence violation review.

## WISDOM — General Principle

- Principle: In multi-stage analytical agent systems, the capacity to stop or redirect based on evidence is as important as the capacity to continue — an agent can make correct diagnoses yet still perform forbidden actions if it cannot restrain itself.
- When to use: Multi-stage agent processes where each stage depends on previous stage results (e.g., business data analysis, scientific research, quality control).
- When NOT to use: Single-stage tasks with no prerequisites to check before acting.
- Example outside original domain: In bank loan approval, before approving a loan, the system must confirm all prerequisites (income, credit history, collateral) are met — an agent may identify risk but must be restrained from approving if conditions are not met.

## Assumptions & Limitations

- Conditions that must hold: tasks with seeded data having clear statistical prerequisites; sandbox environment that can control data access.
- Paper's acknowledged limitations: this is a preprint (not peer-reviewed); the automatic scorer is private (not fully public); 13 frontier models may not represent all open-source agents.
- Limitations paper does NOT state: effectiveness on tasks without clear statistical prerequisites; cost of blinded expert review at scale; generalizability across agent frameworks beyond Harbor 0.22.0.

## Metadata

- Year: 2026
- Authors: Shan Peng, Shuaiqi Cheng, Miao Peng, Chenyi Zi, Jia Li
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.32305
- Citation count: not yet (new paper, Oct 2026)