# 2610.27645 — CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents

## Core Value (1 sentence)

Build an evaluation and training benchmark for error recovery in long-horizon computer-use agents (CUA), built from real policy-induced failures rather than injected errors — current agents rarely recover completely (EAR ≤ 44.0%, Pass@3 ≤ 25.5%), and fine-tuning on the verified training set raises EAR from 19.9% to 35.2%.

## Problem

As computer-use agents (CUA) move to long-horizon workflows spanning multiple applications, undetected errors can silently corrupt persistent state and cause cascading failures in subsequent actions. Existing benchmarks focus primarily on end-to-end task performance, providing limited insight into whether agents can detect and recover from errors during execution. The few benchmarks that evaluate recovery rely largely on manually injected errors, which may not reflect the types or horizons of failures induced by real agent policies — this mismatch limits both realistic evaluation and systematic progress.

## Contribution

1. Proposes CUA-Recovery, an evaluation and training benchmark for error recovery in long-horizon computer-use tasks, built from real policy-induced failures.
2. Builds ReRail, a framework for synthesizing long-horizon tasks and trajectories in a persistent desktop environment — ReRail composes MyPCBench tasks into new long-horizon workflows with executable ground truth, collects verifier-confirmed failures from multiple policies, and turns them into verified recovery trajectories.
3. CUA-Recovery comprises a human-verified test suite of 2,250 erroneous states over 100 tasks and a training suite of 8.6K verified recovery trajectories over 377 tasks.
4. Evaluation shows agents struggle both to recognize inherited errors and to complete tasks: across six agents and six takeover depths, Error Awareness Rate (EAR) reaches at most 44.0% and Pass@3 at most 25.5%. After fine-tuning Qwen3.5-35B-A3B on the training suite, its average EAR rises from 19.9% to 35.2% on held-out recovery states, and its Rubric Score goes from 5.0% to 16.1%.

## Method

Environment and tasks: A computer-use task is modeled as a Partially Observable Markov Decision Process (POMDP) (S, A, O, T, Ω). A state si is the full persistent state of the machine after step i: application databases, files, and user interface. An action a is an operation issued by the agent, including GUI operations (click, drag, scroll, typing, key combination) and CLI commands. At step i the agent observes a screenshot oi (revealing only part of the state), and its action updates the state as si = T(si-1, ai).

Building the benchmark with ReRail (4 main steps):

1. **Building tasks with dependencies**: Start from MyPCBench tasks. ReRail creates an executable intermediate representation recording application operations, data they read and write, and checks on their outputs. Running this graph on a fresh environment snapshot gives expected intermediate values and final state. To form longer workflows, connect two tasks when the output of the first can serve as input to the second — creating a dependency along which a mistake can spread. The resulting pool contains 477 workflows, with medians of three source tasks and 22 graph nodes per workflow.

2. **Checking the generated tasks**: Execute each workflow to obtain reference intermediate values and final state, then freeze verifiers to this gold lineage. Perturb intermediate values and rerun the workflow; a mutation is caught if a downstream verifier fails or final outputs/stored data differ from the gold lineage. Retain workflows catching at least half of executed mutations.

3. **Constructing erroneous states and evaluation suite**: Split composed workflows into training and test tasks. Run six agents (GPT 5.5, Claude Opus 4.8, Kimi-K3, Qwen3.5-35B-A3B, EvoCUA-32B, OpenCUA-72B) on the workflows. For each failed rollout, ReRail compares recorded execution with gold lineage to identify root-cause step tr, error type, and first step where error becomes evident. Experts fix any unrelated mistakes before tr so the root cause is the only error in the prefix. ReRail creates takeover states by replaying the rollout to depths d ∈ {0, 5, 10, 15, 20, 25} after the root cause. Human annotators verify root cause, error type, error horizon, repaired prefix, and replayed state for the test suite.

4. **Generating the training suite**: For each erroneous state in the training split, the base model Qwen3.5-35B-A3B attempts to complete the task with guidance about the earlier error. Recovery generation begins with a hint identifying the erroneous step, then adds conflicting evidence and affected data if earlier attempts fail. The first continuation accepted by the final verifier becomes the training target; a teacher model is used when the base model produces no verified continuation. Hints are omitted from the training input, matching the unaware takeover setting used for evaluation.

## KNOWLEDGE — Data & Concepts

- Across six agents and six takeover depths: EAR at most 44.0%, Pass@3 at most 25.5%.
- GPT 5.5 reaches max 25.5% Pass@3 at d = 20; Claude Opus 4.8 max 7.7%; no open-source agent exceeds 6.4%.
- Test suite: 2,250 human-verified erroneous states over 100 tasks, from 619 failed rollouts of six agents.
- Training suite: 8,640 verified recovery trajectories over 377 tasks; 67.5% span multiple applications, average 60 steps.
- Error types: Planning and perception = 57.3% of root causes; termination = 23.5%; execution = 19.1%. Comparison: AgentNet 84.3% and GUI-Reflection 71.2% attributed to execution errors.
- Error horizon: median 17 steps; 78.1% of errors surface at least 3 steps later; 60.0% first appear at the final step.
- Kimi-K3 solves 66.9% of MyPCBench tasks from clean start but recognizes only 7.8–18.5% of inherited errors in its own failures.
- Fine-tuning Qwen3.5-35B-A3B on training suite: EAR 19.9% → 35.2%, Rubric Score 5.0% → 16.1%.
- Gains +15.3 points on MyPCBench (9.2% → 24.5% Pass@3) and +10.8 points on Odysseys (24.1% → 34.9% Pass@3).
- ReRail-35B-A3B reaches 16.6% Pass@3 on Kimi-K3's failure states at d = 0 vs 11.6% for Kimi-K3; and 12.7% on EvoCUA-32B's states vs 6.4%.
- Ablation: successful-trajectory control raises EAR 19.9% → 23.6%, recovery trajectories raise to 35.2%; clean-start Pass@3 on MyPCBench reaches 13.8% vs 24.5% — improvement comes from learning to recover, not just more in-domain data.

## INSIGHT — Mechanism & Why

[Clean-start performance doesn't predict error awareness] happens BECAUSE [an agent can solve a task well from scratch but fail to recognize inherited errors — Kimi-K3 solves 66.9% of MyPCBench from scratch but recognizes only 7.8–18.5% of its own errors]. This means [clean-start success doesn't imply reliable recovery; evaluating only the final outcome doesn't distinguish whether an agent detected and fixed its own errors along the way].

[Most errors are decision errors, not execution errors] happens BECAUSE [planning and perception account for 57.3% of root causes, while execution errors account for only 19.1% — examples: choosing records from the wrong year, reading a quantity incorrectly, creating events in the wrong calendar app]. This means [recovery requires the agent to revisit earlier decisions and the data they produced, not just fix a wrong click].

[Long error horizon] happens BECAUSE [persistent-state component errors have effects that remain active and influence subsequent operations; errors are rarely visible when they happen, surfacing many steps later]. This means [median delay is 17 steps, 78.1% surface at least 3 steps later, 60.0% only at the final step — recovery requires revisiting earlier work].

[Error awareness rarely leads to recovery] happens BECAUSE [agents often identify a problem but leave the affected state unchanged or fail to repair all its consequences — verifier pass rate is 15.6% for aware runs vs 12.2% for unaware runs]. This means [awareness is necessary but not sufficient for recovery].

## IDEA — Actionable Applications

1. Build error recovery training data for computer-use agents: collect real policy-induced failures (not injected errors), have the agent continue from erroneous states with hints of increasing specificity, keep only verifier-confirmed recoveries, fine-tune without hints. First step: log failed rollouts of a desktop-computer agent, identify root cause by comparing with gold lineage.
2. Apply to desktop automation agents: after an agent errs, pause at the root-cause step, have a new agent take over with the history and try to fix the error without being told an error occurred. First step: create takeover states at different depths (0, 5, 10, 15, 20, 25 steps after root cause) and evaluate whether the agent notices the error (EAR) and completes the task (Rubric Score, Pass@3).
3. Use verified recovery trajectories as fine-tuning data instead of perfect trajectories — gains are much larger than successful trajectories matched on tokens. First step: fine-tune for one epoch on 8.6K verified recovery trajectories, omitting hints from training input.

## WISDOM — General Principle

- Principle: In long-horizon agent systems, error detection and recovery matter as much as task execution — a strong clean-start agent can still fail catastrophically due to one early undetected error.
- When to use: Desktop computer agent workflows that maintain persistent state across many steps and multiple applications.
- When NOT to use: Single-step tasks (single-turn data entry, text retrieval) — no persistent state to corrupt, no recovery needed.
- Example outside original domain: In retail operations, before accepting an order from an automated system, check early decisions (product selection, quantity) not just the final state — an early error can corrupt the entire order and only surface at delivery time.

## Assumptions & Limitations

- Required conditions: deterministic desktop environment after disabling reproducibility-breaking factors (automatic updates, notification daemons); context window limited (K = 20 most recent screenshots in evaluation).
- Paper's acknowledged limitations: this is a preprint (not peer-reviewed); human-verified test set limited to 100 tasks; single-epoch fine-tuning; environment assumed deterministic.
- Paper's unaddressed limitations: effectiveness on non-desktop-computer tasks (web, mobile) unverified; cost of human-annotating 2,250 erroneous states at scale; generalization across agent scaffolds beyond the six evaluated.

## Metadata

- Year: 2026
- Authors: Xu Hu, Haoming Li, Yuxiang Wang, Jinxin Yang, Kangshuo Li, Licheng Wang, Dingyi Kang, Jiayu Song, Tianhao Wang, Zhanhua Hu, Xu Yang, Qiannan Li, Bingzhe Li, Feng Chen
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.27645
- Citation count: not available yet (new paper, Oct 2026)
