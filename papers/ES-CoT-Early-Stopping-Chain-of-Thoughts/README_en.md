# [2509.14004] Early Stopping Chain-of-thoughts in Large Language Models

## Problem
Reasoning LLMs generate long chain-of-thoughts (CoT) to solve complicated problems, but lengthy CoT incurs high inference costs. Previous methods on inference-stage efficient reasoning either require white-box models or are not reliable through direct prompting.

## Contribution
1. **ES-CoT**: Inference-time method shortens CoT generation by detecting answer convergence and stopping early with almost no performance loss.
2. **Linguistic markers**: When observing markers like "wait" in reasoning → prompt LLM to output current step answer. Track run length of consecutive identical step answers.
3. **Results**: Reduces inference tokens by 41% on average, maintains accuracy.

## Method (core summary)
ES-CoT: (1) During CoT generation, detect linguistic markers ("wait", "but", "however"); (2) At markers, prompt LLM to output current final answer (step answer); (3) Track run length of consecutive identical step answers; (4) When run length exceeds threshold → answer converged → stop early. Empirical + theoretical: step answers steadily converge, large run-length jumps mark convergence.

## Key Findings
- Token reduction: 41% average across 6 datasets, 3 LLMs
- Olympiad + Qwen3: 10,652 → 4,624 tokens (-56.59%)
- Accuracy maintained comparable to standard CoT
- Works across QwQ 32B, Qwen3 8B, DeepSeek-R1-Distill-Llama 8B
- Composable with self-consistency prompting

## Actionable Insights
1. **Early stopping for CoT reasoning**: When deploying reasoning LLMs, implement ES-CoT to reduce inference costs. Example: when AI assistant reasons through complex problem, detect convergence and stop early — 41% token savings.

2. **Linguistic markers are convergence signals**: "Wait", "but", "however" in CoT signal answer refinement. Use these as checkpoints. Example: when monitoring AI reasoning, trigger step answer extraction at linguistic markers.

3. **Run length = convergence measure**: Consecutive identical step answers = converged. Track run length. Example: if 10 consecutive step answers identical → stop, no need to continue reasoning.

## Assumptions & Limitations
**Conditions for method to work:**
- LLM generates linguistic markers in CoT
- Step answers converge to final answer
- Minimum run-length threshold tuned

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- Not all reasoning tasks have clear convergence
- Linguistic markers may not appear in all domains
- Threshold sensitivity
- May miss late-stage corrections

## Metadata
- Year: 2025
- Authors: Minjia Mao, Bowen Yin, Yu Zhu, Xiao Fang
- Category: cs.CL
- PDF: https://arxiv.org/pdf/2509.14004
- Citation count: [EXTRACTION FAILED]
