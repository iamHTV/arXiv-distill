# [2610.04686v1] When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning

## Core value (1 sentence)
Multi-agent debate beats majority voting only when both conditions hold: proposal supply surfaces a correct answer (creating recoverable headroom) AND the readout identifies that answer when voting misses it, via Latent Verification Debate (LVD) — answer-specific verification evidence before final generation.

## Problem
Prior work failed to disentangle why multi-agent debate often loses to simple majority voting or self-consistency: is it because correct proposals are never surfaced, or because the readout fails to identify correct proposals when voting misses them?

## Contribution
- Introduces the supply-readout framework: debate requires (1) proposal supply to surface at least one correct answer, and (2) readout to select correct proposals rather than merely counting how many agents repeat each proposal.
- Formalizes recoverable headroom: cases where the initial proposal stage contains the correct answer but majority vote selects a wrong answer; exact decomposition separating recovered headroom, newly-correct cases, and damage to vote-correct cases.
- Develops Latent Verification Debate (LVD): a verification-aware readout model where candidate proposals receive answer-specific verification evidence before final generation; controlled fixed-proposal interventions estimate the latent effect in equivalent peer-support units.
- Builds agent societies from neural-thicket agents using labeled (AC-Greedy) and label-free (SC-Greedy) coverage objectives to select agents with complementary proposal behavior.

## Method
Supply-readout framework. Round t=0 is independent proposal; rounds t≥1 are debate updates. Each agent produces a rationale and a normalized answer. Majority vote picks the most frequent answer. The proposal-hit diagnostic asks whether the correct answer was surfaced (not an available readout). Recoverable headroom H(S) = Pr(P=1, V=0): the fraction of cases where the society contains the correct answer but majority vote misses it. Exact gain decomposition: Gη(S) = E[Dη − V] = H(S)·Rη(S) + Pr(P=0,V=0)·Iη(S) − Pr(V=1)·Lη(S), where R = recovery rate of vote-missed surfaced answers, I = new-correctness emerging after the initial proposal stage, L = harm to vote-correct cases. LVD augments proposal-count readout with an effective verified pseudo-count vector Wη,t: pLVD,η(y=k|x,Ft,W) ∝ κq0θ(k|x) + C(k)t + W(k)η,t. Debate creates non-null drift toward correctness only when verified pseudo-counts allocate more mass to the correct answer than the proposal-only posterior already does. Society construction: neural-thicket agents (small weight perturbations θm = θ0 + σmϵ(sm) around a pretrained base model); select a small society of K agents with complementary proposal coverage via AC-Greedy (labeled: ψAC = 1{agent's answer = correct answer}) or SC-Greedy (label-free: answer-cluster support score). Evaluation: Qwen3-4B-Instruct and OLMo-3-7B-Instruct, K=4 agents, T=5 rounds, unified compute budget (vote20 for voting rows, R3 majority state from matched four-agent traces for debate rows).

## KNOWLEDGE — Data & figures
- Multi-agent debate often loses to simple majority voting/self-consistency; symmetric truth-agnostic interaction creates no positive expected drift toward correctness (martingale null).
- Recoverable headroom: initial proposal stage has correct answer but majority vote misses it.
- LVD: verification-aware readout creating non-null drift only when verification evidence favors the correct answer beyond proposal-count posterior.
- Table 1 (Qwen3-4B): SC@20 91.20, Vanilla Debate 92.69, SC-Greedy Debate 92.29; Neural Thicket Vote 90.93, Top-4 Debate 92.15, AC-Greedy Debate 92.29.
- Table 1 (OLMo3-7B): SC@20 87.01, Vanilla Debate 86.33, SC-Greedy Debate 84.03; Neural Thicket Vote 86.87, Top-4 Debate 85.93, AC-Greedy Debate 85.25.
- Stochastic robustness (5 seeds): SC-Greedy +1.14 pts, AC-Greedy +1.46 pts on Qwen3-4B; +0.96, +2.01 pts on OLMo3-7B vs Vanilla Debate.
- Table 2 (AMC12 → MMLU-Redux transfer): Qwen3-4B SC-Greedy Final 76.33 vs Init Vote 72.33 (+4.00 lift); OLMo SC-Greedy Final 59.67 vs Init Vote 55.33.
- Controlled fixed-proposal probes: correct support improves accuracy from 0.325 to 0.655 at d=3 (averaged across 4 backbone-dataset combos); original correct peer responses have positive margin effects in all 4 combos; median effects ~2 controlled messages on GPQA and >3 on MMLU-Redux; answer-stripped T−F gap positive in all combos.
- Dynamics: R0 accuracy 76.09% → R2 78.34% → R3 78.52% (immediate finalizer cannot explain R2–R3 plateau; interaction adds gains).
- Code: github.com/Wang-ML-Lab/when-debate-helps
- arXiv category: cs.AI

## INSIGHT — Mechanism & why
[Debate often loses to majority vote] BECAUSE [either correct proposals are never surfaced (no headroom), or the readout fails to identify correct answers when voting misses them; having only one of the two is insufficient]. This means [debate needs both sufficient proposal supply and a verification-aware readout to beat voting].
[Recoverable headroom creates an opportunity for readout] BECAUSE [when the correct answer is surfaced but majority vote misses it, readout can recover it by assigning more verification evidence to the correct proposal]. This means [debate helps when there is recoverable headroom AND readout can convert headroom into final accuracy].
[Coverage-selected agent societies produce more complementary correct proposals] BECAUSE [selecting agents with complementary proposal coverage instead of ranking by individual accuracy produces more distinct correct answers with less duplication]. This means [complementary diversity beats redundant excellence].

## IDEA — What to apply
Apply LVD to an enterprise multi-agent system: step 1 is to use majority vote as the first step, then use a verifier/LLM judge to assign verification evidence to each candidate proposal before generating the final answer.
Use neural thicket + coverage selection to build complementary agent societies: step 1 is to sample small weight perturbations from a base model, then select agents with complementary proposal coverage rather than picking the highest-scoring agents.

## WISDOM — General principle
Principle: Debate helps when proposal supply surfaces a correct answer (creating recoverable headroom) AND readout can identify that answer when voting misses it; neither alone suffices. Debate is not universally better than voting — it can damage vote-correct cases or discard useful alternatives; its value depends on proposal headroom, the backbone's ability to evaluate competing evidence, and inference cost.

## Assumptions & Limitations
- Conditions for validity: reasoning tasks with comparable final answer values, small agent society (K=4), multiple debate rounds (T=5).
- Limitations acknowledged by the paper: debate is not always better than voting; headroom conversion is task- and backbone-dependent; inference cost is a practical factor; results on two backbones (Qwen3-4B, OLMo3-7B) don't guarantee all larger models.
- Limitations the paper does NOT mention: operational cost of running multiple debate rounds at scale; stability across more random seeds than 5; latency impact of running verifier/LLM judge per candidate proposal.

## Metadata
- Year: 2026
- Authors: Zihao Zhao, Tunyu Zhang, Haizhou Shi, Yusong Zhao, Xinxi Zhang, Hao Wang (University of Illinois Urbana-Champaign, Rutgers University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.04686v1
- arXiv ID: 2610.04686v1
- Label: [applied]
- Skill: when-debate-helps | Test: [SKILL VALID]
