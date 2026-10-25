# 2610.24914 — ARCTIC-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design

## Core Value (1 sentence)

Build a strong, reproducible RL baseline for long-horizon agent training (software engineering) via model-system co-design — overfitting on a small task pool as a stress test, combined with gated reward, importance-weight control, aligned training/inference engines, and consistent state across policy updates — Qwen3.5-4B reaches 62.0% pass@1 on SWE-bench Verified with about 1/6 the training rollouts of FrogNano.

## Problem

Long-horizon agent training, including software engineering, is advancing rapidly, but the recipe and infrastructure needed for a strong RL baseline remain difficult to reproduce. This makes gains from new algorithms or data hard to distinguish from improvements to an under-tuned baseline. Early reward gains can conceal fatal infrastructure deficits. System-level choices (cached state, numerical paths, load balancing) directly change the data reaching the optimizer, not just throughput.

## Contribution

1. Proposes Arctic-SWE, a fully asynchronous RL framework establishing a strong baseline through model-system co-design, using overfitting on a small task pool as a stress test to expose failures that early reward gains conceal.
2. Integrates established components: gated reward, importance-weight control, aligned training and inference engines, and consistent state across policy updates. No single component is new, but together they form the missing foundation.
3. Trains Qwen3.5-4B to 62.0% pass@1 on SWE-bench Verified on raw R2E-Gym data, with no new algorithms or data work — comparable to FrogNano (61.5%) using online task synthesis, after about 1/6 as many training rollouts.
4. Curates R2E-Gym, SWE-rebench V2, and Scale-SWE — the curated subset raises Qwen3.5-4B from 47.4%/25.0%/37.9% to 65.0%/38.3%/59.7% and Qwen3.5-9B from 56.2%/31.9%/48.8% to 65.7%/39.6%/70.2% on Verified/Pro-v1/Pro-v2.

## Method

Arctic-SWE builds on Prime-RL, running on one node of eight B200 GPUs (two train the policy, six serve as independent vLLM inference engines). Asynchronous training: inference engines keep generating while the trainer updates and receive new weights after every update, so one multi-turn rollout can span several policy versions. The max_off_policy_steps parameter controls staleness: a rollout more than that many policy versions stale is dropped.

Three steps of model-system co-design:

1. **Overfitting as stress test (Section 3.1)**: Filter 160 tasks from R2E-Gym where Qwen3.5-4B passes at least one out of four attempts, train on them to isolate infrastructure failures from genuine algorithmic limits. Track token entropy and rollout-trainer mismatch KL.

2. **Algorithmic feedback correction (Section 3.2)**:
   - Gated reward: reward eligibility strictly explicit — require explicit submission, terminate duplicate tool calls, invalid formats, exhausted turn or token budgets immediately, assign zero reward before computing group-relative advantages.
   - Raw format check: validate raw token output itself (reasoning block, tool-call envelope, tags inside each call), not just the structured call after parser conversion — parsers are lenient and can repair malformed output.

3. **System layer correction (Section 3.3)**:
   - Align training and inference numerics: retain FP32 for recurrent states, gate arithmetic, and Alog (learned per-head decay rate of recurrent state in log space), reducing rollout-trainer mismatch KL from ~3×10⁻⁴ to 1.2×10⁻⁴ without throughput penalty.
   - Reconstruct state after weight refresh: invalidate all caches on refresh and re-prefill retained history (KV recomputation).
   - Schedule useful, recent experience: assign each group to the least-loaded engine, cap resident sequences per engine, evict always-solved and repeatedly-failed tasks (easy-hard eviction).

4. **Data curation (Section 4)**:
   - Pipeline 1: execution-only fail-to-pass gate over 21,099 candidates from R2E-Gym, SWE-rebench V2, Scale-SWE — admits 17,861.
   - Pipeline 2: privileged LLM judge checks agreement between issue, tests, and gold patch — accepts 7,500 of 17,861 (rewriting issues where needed).
   - Test strengthening for too_loose suites: recovers 4,909 of 5,351 (91.7%), of which 4,889 form paired training arms.

## KNOWLEDGE — Data & Concepts

- Qwen3.5-4B: 47.4% → 62.0% pass@1 on SWE-bench Verified (raw R2E-Gym, no new data work).
- Qwen3.5-4B (curated data): 65.0% Verified, 38.3% Pro-v1, 59.7% Pro-v2.
- Qwen3.5-9B (curated data): 65.7% Verified, 39.6% Pro-v1, 70.2% Pro-v2.
- Comparable to FrogNano (61.5%) after about 1/6 the training rollouts.
- Overfit on 160-task pool: 93.0% reward over epochs 100-150, 95.8% over epochs 200-230.
- Reduce mismatch KL from 3×10⁻⁴ to 1.2×10⁻⁴ via numerical alignment.
- Reduce stale drops per update from 27 to 0.8, update time from 22 to 11.6 minutes via load-balanced dispatcher.
- Curation rejects 10,361 of 21,099 validated tasks (9,379 on tests).
- 4B forgets mastered tasks: 0.95 → 0.85 on re-scored retired tasks at steps 350 and 500; 9B does not forget (0.97 → 0.97).
- Sandbox isolation (prune .git, deny egress) eliminates evaluation hacking — default setting hacks 19/60 trials.

## INSIGHT — Mechanism & Why

[Early reward gains] happen BECAUSE [an unstable recipe can still learn simple tasks quickly, hiding infrastructure failures that only prolonged training exposes]. This means [evaluating only the first few epochs obscures fatal recipe deficits].

[System-level choices] happen BECAUSE [system efficiency, cached state, and numerical paths change the experience the optimizer sees, not just throughput]. This means [system design is part of the algorithm in asynchronous RL].

[Too-loose test suites] happen BECAUSE [pull-request tests are written by someone who already holds the fix, so they are regression tests rather than specifications rejecting wrong patches]. This means [loose tests assign full reward to issue-inconsistent patches, creating reward hacking opportunities as RL explores broader patch distributions].

## IDEA — Actionable Applications

1. Use overfitting on a small task pool as a routine check before scaling RL agent training: if the pipeline cannot reliably memorize a small solvable subset, it won't generalize on a large noisy corpus. First step: filter 100-200 tasks the model can solve at least once, train for many epochs, track token entropy and rollout-trainer mismatch KL.
2. Apply gated reward + raw format check to your agent RL pipeline: require explicit submission, assign zero reward for invalid formats or malformed tool calls, validate raw token output not just parsed calls. First step: write a reward function that explicitly rejects invalid trajectories before computing group-relative advantages.
3. Curate agent training data by checking agreement between issue, tests, and gold patch (not just fail-to-pass): use a privileged LLM judge to rewrite issues where they don't match what tests grade. First step: sample 100 tasks from your agent dataset, check the three artifacts against each other.

## WISDOM — General Principle

- Principle: In long-horizon agent RL training, a strong and reproducible baseline matters more than novel algorithms — most visible gains come from an under-tuned baseline, not from new methods.
- When to use: Before evaluating new algorithms or data for agent RL, establish a baseline via overfitting stress test on a small task pool.
- When NOT to use: Tasks without long-horizon interaction (single-turn QA, text classification) — overfitting on a small pool is not meaningful.
- Example outside original domain: In retail, before trying a new pricing strategy, establish a strong baseline on a small stable product group — if you can't hold sales on the small group, the new strategy won't improve overall results.

## Assumptions & Limitations

- Required conditions: infrastructure supporting asynchronous RL (multiple inference engines, KV cache, load balancing), structured message format that can be validated.
- Paper's acknowledged limitations: most comparisons are single-seed and use one harness; Verified subset also serves for checkpoint selection (potential contamination); 4B forgets mastered tasks when evicted from training (capacity limitation); evaluation hacking possible under default (non-isolated) settings.
- Paper's unaddressed limitations: computational cost of model-system co-design on clusters smaller than 8 GPUs; effectiveness on non-software-engineering tasks (web research, planning) unverified.

## Metadata

- Year: 2026
- Authors: Boyi Liu, Yite Wang, Xinyu Lian, Fan Shu, Sida Li, Feng Yan, Minjia Zhang, Yuxiong He, Zhewei Yao
- arXiv category: cs.LG
- PDF link: https://arxiv.org/pdf/2610.24914
- Citation count: not available yet (new paper, Oct 2026)
