# 2601.10589 Safety Self-Play (SSP): Be Your Own Red Teamer

## Problem

Current safety alignment depends on static external red teaming — fixed defense prompts, pre-collected adversarial datasets. Leads to rigid defense that overfits known patterns and fails on novel threats. Reactive, not proactive.

## Contribution

1. SSP — single LLM as both Attacker and Defender in unified RL loop. Self-play creates evolving attack strategies.
2. Reflective Experience Replay with UCB sampling — focus on failure cases.
3. SSP outperforms static methods, achieves lowest refusal rate (best safety-usability balance).

## Method (core summary)

Unified RL loop: LLM alternates Attacker/Defender roles. Attacker rewarded for successful jailbreaks, Defender for correct refusals. Experience replay with UCB prioritizes failures. Defender learns from accumulated failures. Attacker evolves via self-play dynamics.

## Key Findings

- Lowest ASR on HarmBench
- Lowest refusal rate on OR-Bench — best safety-usability balance
- Diversity emerges from self-play without explicit diversity reward
- Ablation: UCB + replay essential
- Autonomous evolution — no manual dataset curation

## Actionable Insights

1. Use self-play for safety alignment — model auto-discovers vulnerabilities.
2. Reflective Experience Replay — focus training on failure cases.
3. Safety-usability balance achievable — don't over-block legitimate queries.

## Assumptions & Limitations

- Single LLM playing both roles — model-dependent
- Convergence may be slow for strong attackers
- English benchmarks primarily
- RL training cost
- Attacker bounded by model's own knowledge

## Metadata

- Year: 2026
- Authors: Hao Wang, Yanting Wang, Hao Li, Rui Li, Lei Sha
- Category: cs.AI, cs.CL
- PDF: https://arxiv.org/pdf/2601.10589
- Citation count: N/A
- Classification: [applied]
- Skill: safety-self-play-alignment
