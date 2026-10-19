# Skill: when-debate-helps
Source: 2610.04686v1
Type: framework

## When to use this skill
- You have a multi-agent reasoning system and want to know whether debate beats majority voting.
- Need to disentangle proposal supply from readout to diagnose why debate fails.
- Have resources to run multiple debate rounds and a verifier/LLM judge to assign verification evidence.

## When NOT to use this skill
- Assuming debate is always better than majority voting (debate can damage vote-correct cases).
- Tasks without comparable final answer values (open-ended, no auto-grading).

## Required inputs
- A small agent society (K=4) debating reasoning tasks (math, science, multi-discipline).
- Majority vote as the first readout step.
- A verifier or LLM judge to assign verification evidence to each candidate proposal.
- A neural-thicket pool: small weight perturbations around a pretrained base model (θm = θ0 + σmϵ(sm)).
- Coverage objectives (labeled or label-free) to select complementary agents.

## Steps
1. Identify a reasoning task with comparable final answer values (AMC12, MATH500, GPQA, MMLU-Redux...).
2. Build the neural-thicket pool: sample small weight perturbations around pretrained weights; each is a nearby specialist agent.
3. Select a small society of K agents via coverage selection: AC-Greedy (labeled: pick agents correct on construction set) or SC-Greedy (label-free: answer-cluster support) — not just top individual accuracy.
4. Run debate with K agents over T rounds; each agent proposes a rationale + normalized answer each round; majority vote as initial readout.
5. Compute recoverable headroom: fraction of cases where the society contains the correct answer but majority vote misses it.
6. Apply LVD (verification-aware readout): verifier/LLM judge assigns answer-specific verification evidence to each candidate proposal before final generation; pseudo-count vector Wη,t allocates verification mass to the correct answer.
7. Decompose the gain: G = H·R + Pr(P=0,V=0)·I − Pr(V=1)·L (recovered headroom + new-correctness − harm to vote-correct).
8. Evaluate robustness across multiple random seeds (matched stochastic evaluations).

## Expected output
- Debate beats majority voting when there is recoverable headroom AND verification-aware readout; you know whether debate fails due to proposal supply or readout.

## Example application
- A math-solving multi-agent system: instead of majority vote only, run debate with 4 agents over 5 rounds, then use an LLM judge to verify each candidate proposal before the final answer; select the agent society via coverage (not the 4 highest-accuracy agents).

## Gotchas
- Do not assume debate is always better than voting — debate can damage vote-correct cases or discard useful alternatives.
- Do not ignore proposal supply: if no correct proposal is surfaced, even the best readout cannot recover it.
- Do not select the agent society by individual accuracy alone; need complementary proposal coverage.
- Intervene early: interaction adds gains in early rounds; proposal coverage can collapse in later rounds.

## Self-check
- Can someone who has not read the original paper follow these 8 steps? [YES] — each step is a concrete action.
- Which step is most vague? Step 6 (LVD with pseudo-count vector) needs a concrete verifier/LLM judge implementation.
- Is the Input section sufficient? [YES] — agent group, majority vote, verifier, neural-thicket pool, coverage objectives are all covered.

## Dry run (hypothetical scenario)
- Scenario: A company's 4-agent math-solving system wants to know if debate helps.
- Run the skill: (1) Identify math tasks with standard answers; (2) build neural-thicket pool from base model; (3) select 4 agents via SC-Greedy (label-free); (4) run debate over 5 rounds, majority vote each round; (5) compute recoverable headroom; (6) apply LVD: LLM judge verifies each candidate proposal before final answer; (7) decompose the gain; (8) evaluate across 5 seeds; if debate beats voting and headroom is high, deploy.

## Verdict: [SKILL VALID]
