# [2610.20776v1] INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems

## Problem
LLM-based agents increasingly execute long-horizon, end-to-end workflows involving shell commands, code modification, dependency installation, and interaction with remote services. This growing autonomy expands their exposure to indirect prompt injection (IPI), where adversarial instructions embedded in external content are interpreted as legitimate task directives. Existing evaluations, however, often...

## Contribution
- Introduce INFUSE: a unified surface benchmark for indirect prompt injection in agentic systems.
- Evaluate on 40 tasks with 56 attacks, defining up to 40 × 56 = 2,240 (task, attack) configurations per model.
- Across the benchmark, mean attack success reaches 19.6% under LLM-based evaluation (ASR-L) and 15.4% under heuristic verification (ASR-H).
- Per-model ASR-L ranges from 3.2% to 41.9%.
- Instructional hardening reduces mean attack success from 58.2% to 14.3%, revealing substantial but model-dependent security–utility trade-offs.
- 41,824 attack trajectories, explicit refusal is rare (RR ≤ 1.0% for every model).
- Highest-ASR tasks: T17 Tech Writing 51.6%, T13 File Org. 49.9%, T9 Security 49.1%, T3 Dep. Setup 47.9%.

## Method (core summary)
INFUSE is a unified benchmark for indirect prompt injection in agentic systems. Evaluate on 40 tasks with 56 attacks, each (task, attack) configuration run on each model. Measure ASR-L (attack success rate by LLM evaluation) and ASR-H (by heuristic evaluation). Compare different models and defense methods.

## Key Findings
- Mean attack success: 19.6% (LLM-based), 15.4% (heuristic).
- Per-model ASR-L: 3.2% to 41.9%.
- GPT-5: 26.3% ASR-L, Claude-Sonnet-4.6: 3.2% ASR-L, Gemini-3.1-Flash-Lite-Preview: 41.9% ASR-L.
- Instructional hardening reduces mean attack success from 58.2% to 14.3% (43.9 points reduction).
- Meta-SecAlign reduces ASR-L by 55% at 8B and 74% at 70B.
- Refusal remains rare (at most 1.0% for every model).
- Transfer: 9.3–35.7% of previously successful attacks transfer (102 of 456 cells pooled, 22.4%).

## Actionable Insights
- Don't trust agent LLM to be safe against indirect prompt injection: mean attack success 19.6% shows systems are vulnerable. Apply: solopreneur using LLM agents should add defense mechanisms like instructional hardening, input sanitization, output validation.
- Instructional hardening is an effective defense: reduces attack success from 58.2% to 14.3%. Apply: when building LLM agents, add instructional hardening (security instructions) so agents don't follow adversarial instructions embedded in external content.
- Evaluate agent robustness before production deployment. Apply: when building LLM agents, test against indirect prompt injection attacks to find vulnerabilities and fix them before shipping.

## Assumptions & Limitations
- Requires an LLM agent and real query data; doesn't apply if only a single model.
- Paper admits: evaluated on specific agent systems; may differ on other systems.
- Limitation paper doesn't mention: not evaluated on many domains beyond tasks used, not tested on real cost of defense mechanisms.

## Metadata
- Year: 2026
- Authors: Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas, Sreepriya Damuluru, Taylor T. Johnson, Kevin Leach (Vanderbilt University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.20776
