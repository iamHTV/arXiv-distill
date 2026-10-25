# Skill: arctic-swe-rl-baseline

Source: 2610.24914
Type: framework

## When to use this skill

- Before evaluating new algorithms or data for long-horizon agent RL training, establish a strong and reproducible baseline.
- Want to use overfitting on a small task pool as a routine check to expose infrastructure failures that early rewards conceal.
- Have infrastructure supporting asynchronous RL (multiple inference engines, KV cache, load balancing).

## When NOT to use this skill

- Tasks without long-horizon interaction (single-turn QA, text classification).
- Clusters smaller than 8 GPUs (model-system co-design cost unverified).

## Input needed

- Small task pool (100-200) that the model can solve at least once out of four attempts.
- Asynchronous RL infrastructure: at least 2 training GPUs, multiple vLLM inference engines.
- Structured message format (reasoning block, tool-call envelope, tags).

## Steps to execute

1. Filter a small task pool: select tasks the model solves at least once out of four attempts.
2. Train on the small pool for many epochs, tracking token entropy and rollout-trainer mismatch KL — if the pipeline cannot reliably memorize the small subset, the recipe is not stable.
3. Apply gated reward: require explicit submission, assign zero reward for invalid formats, malformed tool calls, exhausted turn or token budgets.
4. Apply raw format check: validate raw token output itself (reasoning block, tool-call envelope, tags inside each call), not just the structured call after parser conversion.
5. Align training and inference numerics: retain FP32 for recurrent states, gate arithmetic, and Alog (per-head decay rate in log space).
6. Invalidate all caches on weight refresh and re-prefill retained history.
7. Assign each group to the least-loaded engine, cap resident sequences per engine, evict mastered and repeatedly-failed tasks.
8. Curate training data: Pipeline 1 (execution-only fail-to-pass gate) then Pipeline 2 (privileged LLM judge checking agreement between issue, tests, gold patch).

## Expected output

- Stable RL baseline that can overfit the small task pool to >90% reward.
- Reward does not collapse after many epochs.
- A baseline for comparing new algorithms and data.

## Example application

Train a code-writing agent on 160 SWE tasks: filter 160 tasks Qwen3.5-4B solves at least 1/4 of the time, run overfitting for many epochs. If reward collapses after epoch 11 (as with initial Prime-RL), apply gated reward and raw format check → reward stabilizes at 74.5%+, reaching 62.0% on SWE-bench Verified.

## Gotchas

- Early rewards conceal infrastructure failures — evaluating only the first few epochs is not enough.
- Asynchronicity means inference engine speed and trainer speed shape training dynamics, not just throughput.
- 4B may forget mastered tasks when they are evicted from training (capacity limitation).
- Sandbox isolation (prune .git, deny egress) is needed to prevent evaluation hacking.
