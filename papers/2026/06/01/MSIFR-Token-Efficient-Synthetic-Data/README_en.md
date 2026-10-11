# [2605.14062] Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Generation via Multi-Stage In-Flight Rejection

## Problem
Synthetic data generation with LLMs is widely used in post-training pipelines. But existing approaches generate full outputs before applying quality filters — leading to substantial token waste on samples ultimately discarded. Need to detect and terminate low-quality generation trajectories at intermediate checkpoints.

## Contribution
1. **MSIFR (Multi-Stage In-Flight Rejection)**: Lightweight, training-free framework that detects and terminates low-quality generation at intermediate checkpoints.
2. **Fast rule-based validators**: Checks arithmetic inconsistencies, hallucination patterns, formatting violations.
3. **Formal sequential decision process**: Proves any non-trivial discard policy reduces expected token consumption.

## Method (core summary)
MSIFR: decomposes generation process into sequential stages. At each stage, applies fast rule-based validators: arithmetic check, hallucination detection, format validation. If fail → terminate early, don't complete generation. Formalized as sequential decision process. Martingale property: early rejection doesn't bias expected utility of retained samples.

## Key Findings
- Token reduction: 11%-77% standalone, up to 78.2% with early-exit methods
- Llama-3.1-8B: strongest efficiency profile — lowest tokens on 4/7 benchmarks
- Accuracy: meets or exceeds traditional baseline in majority of pairs
- 5× throughput improvement with LYNX combination
- No additional training or architectural changes needed

## Actionable Insights
1. **Early rejection = massive savings**: Don't generate full output before filtering. Reject at intermediate checkpoints. Example: when generating synthetic training data, validate at 50% completion — if fail, terminate, save 50% tokens.

2. **Rule-based validators are fast**: Arithmetic, hallucination, format checks — lightweight, no model needed. Example: when generating math solutions, check arithmetic consistency at each step — if wrong, terminate early.

3. **50% cutoff optimal**: Mid-solution cutoff consistently optimal across benchmarks. Example: when designing synthetic data pipeline, set checkpoint at 50% completion for validation.

## Assumptions & Limitations
**Conditions for method to work:**
- Rule-based validators defined per domain
- Sequential generation process
- Intermediate checkpoints available

**Limitations the paper acknowledges:**
- Task-specific validators by design
- 50% cutoff may need retuning for different domains
- Experiments on 7-8B models only

**Limitations the paper does NOT mention:**
- Validator design effort per domain
- False rejection rate (rejecting good samples)
- Very long-form content may need different approach

## Metadata
- Year: 2026
- Authors: Anjir Ahmed Chowdhury, Syed Zawad, Feng Yan
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.14062
- Citation count: [EXTRACTION FAILED]
