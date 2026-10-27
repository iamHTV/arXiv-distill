# [2610.35082] CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems

## Problem
- Current Agent Skill (reusable capability package for agents) security checks examine each package in isolation: static/semantic scanning, manifest-based runtime controls. Prior work has not solved composition risk because the unit of analysis is the single package — while a Skill's output is reused downstream by other Skills without carrying the restrictions and authorization tied to its original purpose. Motivating case: three individually benign Skills (read CI status, prepare reproduction materials, run validation workflow) combine to make the agent execute code from a submitted package without authorization.

## Contribution
- Defines Conflict of Skills (CoS): policy violations arising from artifact or decision reuse across Skills that each pass individual checks, via four mechanisms: security-context attenuation, semantic interface bridging, semantic authority promotion, target/action binding drift.
- CoSA: an attack framework that adds locally-admitted Skills (passing the single-package scanner), capped at 5% of the pool, via capability supplementation (supplying missing business operations) or relationship reshaping (altering artifact exchange, decision reuse, target/action bindings) — without modifying existing Skills or runtime permissions.
- CoSA-Bench: 288 business tasks across 4 domains (recruiting, finance, IT, business) and 3 risk categories: data leakage (DL), unauthorized state modification (UA), unsafe execution (UE).
- CoSA-Guard: a pre-action hook checking information flow and authorization.

## Method (core summary)
- Task τ=(u, e0, Γ); each Skill operation gets one of six roles: READ, TRANSFORM, ASSESS, EXTERNALIZE, MUTATE, EXECUTE.
- Artifact dependency Arth and decision dependency Dech require evidence of reuse in the trajectory (execution trace) — temporal order alone is insufficient.
- CoS witness (eq. 1): ∃ constraint c, chain w: c(Ω)=0, Depc(w,h)=1, |S(w)|≥2, all Skills in w pass Π. Risk increment (eq. 2): ∆D = E[R(V_D∪I_D) − R(V_D)].
- Pipeline: discovery (operation-level contract analysis) → LLM proposes candidates guided by the 4 mechanisms → contract-consistency filtering + local admission Π → deterministic budgeted maximum coverage selection → paired runs V_D vs V_D∪I_D with autonomous Skill selection; an LLM judge counts a violation only when a concrete effect occurs.

## Key Findings
- Policy violations: 35.02% (1513/4320) → 58.45% (2525/4320), +23.43 percentage points (pp) with only ≤5% added Skills.
- OpenClaw 31.94→54.24 (+22.29pp), OpenHands 40.07→66.11 (+26.04pp), OpenCode 33.06→55.00 (+21.94pp); increases in 159/180 model–harness–domain–risk groups.
- 5 models: Qwen3.6, MiniMax-M3, DeepSeek-V4, GPT-5.6, GLM-5.1; 3 harnesses: OpenClaw, OpenHands, OpenCode. GPT-5.6 most robust (+8.33pp) yet still 29.86–34.03% violations after augmentation.
- Data leakage shows the largest increase in every harness: +25.00/+31.04/+25.21pp; UA +18.13–25.83pp, UE +20.00–23.75pp.
- Retrieval is a weak proxy: ITR (injected-Skill trigger rate) correlates weakly with ∆ASR (r=0.058); GPT-5.6 and MiniMax-M3 have near-identical ITR (83.45% vs 83.33%) but very different ∆ASR (10.88 vs 29.51pp).
- OpenClaw ablations: random benign injection 26.39% (−5.55pp), random candidate selection 43.40% (+11.46pp), full CoSA 54.24% — ~10.8pp above random at the same budget.
- CoSA-Guard (OpenClaw recruiting, 5 models): ASR (attack success rate) 65.28% (235/360) → 6.67% (24/360), −58.61pp; Risk Coverage 82.73% (115/139); PCTC (Policy Compliant Task Completion) 66.67%→65.00%; FBR (False Block Rate) 3.33%.
- Cisco AI Defense scanner: severe-alert counts unchanged after augmentation — static alerts do not distinguish realized risk.

## Actionable Insights
1. Audit composition, not individual Skills: before adding a new Skill/plugin to an agent, run paired tests on 10–20 identical tasks with and without the new Skill, counting policy-violating side effects. Example: adding an "invoice drafting" Skill to a support agent → run the same 20 tickets in both configurations and compare unauthorized DB writes/emails sent.
2. Install a pre-action gate: before any write/send/execute action, hook that checks the payload's provenance (where the data came from) and authorization bound to the specific action+target. Example: in an automation workflow, the "send email to customer" node must verify the content carries an approval flag from the ticket system.
3. Measure risk change directly: do not use retrieval rate (how often a Skill is invoked) as a safety gauge. Example: a plugin safety report should state the violation delta between the two configurations, not the plugin's invocation frequency.

## Assumptions & Limitations
- Conditions: added Skills pass the single-skill scanner, budget ≤5% of pool, domain relevance, sandbox with controlled services.
- Paper-stated: limited domains/models/harnesses/risk categories; bounded budget; fixed model/tools/permissions; long-horizon dependencies not covered.
- Not stated but observed: each task runs once per condition → no variance estimate; random baselines use a single realization; no separate ablation of capability supplementation vs relationship reshaping; the Guard uses GPT-5 to judge ambiguous evidence → depends on a second LLM; only the ClawHub ecosystem (OpenClaw) was tested.

## Metadata
- Year: 2026 (Oct 26, 2026). Authors: Yujia Zheng (USTB/ZODA), Tianhao Li (OWASP), Shangzhi Xu, Yuekai Huang, Ziyou Jiang, Zhaoyang Li, Yuyao Ge, Junran Peng, Mingyang Li (ISCAS). Categories: cs.CL, cs.AI, cs.CR. Link: https://arxiv.org/abs/2610.35082. Citation count: [NOT FOUND — paper 2 days old].
