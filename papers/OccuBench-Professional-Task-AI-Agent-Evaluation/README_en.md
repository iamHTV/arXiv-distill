# 2604.10866 OccuBench: Evaluating AI Agents on Real-World Professional Tasks

## Problem

AI agents are expected to perform professional work across hundreds of occupational domains, but existing benchmarks only evaluate in a few domains with public environments. No systematic cross-industry evaluation exists.

## Contribution

1. OccuBench — 100 professional scenarios, 10 industries, 65 domains. Language Environment Simulators (LESs) simulate domain-specific environments.
2. Multi-agent synthesis pipeline with guaranteed solvability, calibrated difficulty.
3. Two dimensions: task completion + environmental robustness under fault injection.

## Method (core summary)

100 scenarios across 10 industries. LESs simulate tool responses. Evaluate 15 frontier models. Fault injection: explicit, implicit, mixed.

## Key Findings

- No single model dominates all industries — distinct capability profiles
- GPT-5.2: 79.6% overall, leads Agriculture/Business/Industrial/Science
- Qwen 3.5 Plus: leads Healthcare (81%) and Commerce (81%)
- Gemini 3.1 Pro: 72.3%, leads Education (84%)
- Open-source competitive: Qwen 3.5 Plus (69.9%), DeepSeek V3.2 (69.6%)
- Implicit faults harder than explicit errors
- Higher reasoning effort: +27.5 points for GPT-5.2
- Strong agents ≠ strong simulators

## Actionable Insights

1. Choose model by domain specialty, not overall ranking.
2. Implicit faults biggest risk — add data validation layer.
3. Higher reasoning effort improves professional task performance significantly.

## Assumptions & Limitations

- LES simulation gap
- 100 scenarios limited
- Document-grounded tasks only
- Professional task definition varies

## Metadata

- Year: 2026
- Authors: Xiaomeng Hu, Yinger Zhang, Fei Huang, et al.
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2604.10866
- Citation count: N/A
- Classification: [applied]
- Skill: N/A — benchmark
