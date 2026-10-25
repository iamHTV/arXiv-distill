# Skill: cua-recovery-error-recovery

Source: 2610.27645
Type: framework

## When to use this skill

- Building error recovery training data for computer-use agents in long-horizon workflows (desktop automation, GUI and CLI interaction).
- Want to evaluate whether an agent can detect and fix its own errors after an early error has affected the workflow.
- Have a deterministic desktop environment and can record interaction history (screenshots, GUI actions, CLI commands).

## When NOT to use this skill

- Single-step tasks (single-turn data entry, text retrieval) — no persistent state to corrupt, no recovery needed.
- Non-deterministic environments (automatic updates, random notifications) — cannot replay prefixes to identify root cause.

## Input needed

- Failed rollouts of an agent on desktop computer workflows (recorded screenshots, actions, CLI commands).
- Gold lineage for each task — the correct value at every step.
- A verifier to confirm whether the task has been completed.

## Steps to execute

1. Run multiple agents on long-horizon workflows (compose source tasks into long workflows with dependencies).
2. For each failed rollout, compare recorded execution with gold lineage to identify root-cause step tr, error type, and first step where error becomes evident.
3. Fix any unrelated mistakes before tr so the root cause is the only error in the prefix.
4. Create takeover states by replaying the rollout to depths d ∈ {0, 5, 10, 15, 20, 25} after the root cause.
5. Human annotators verify root cause, error type, error horizon, repaired prefix, and replayed state (for the test set).
6. For the training set: have the base model continue from each erroneous state with hints of increasing specificity (identify erroneous step → add conflicting evidence → add affected data); keep only verifier-accepted continuations; omit hints from training input.
7. Fine-tune the model on verified recovery trajectories (one epoch), with no hints in the training input.

## Expected output

- Test set: replayable erroneous states, human-verified, for measuring EAR (Error Awareness Rate), Rubric Score, Pass@3.
- Training set: verified recovery trajectories for fine-tuning a recovery agent.
- Fine-tuned agent recognizes errors better and completes more tasks.

## Example application

Desktop automation agent for ordering: agent picks the wrong product at step 3, error doesn't surface immediately, only appears at step 43 when the agent falsely reports completion but the cart is wrong. Use CUA-Recovery: create takeover state at step 3 (root cause), let a new agent take over and try to fix. Fine-tuning on verified recovery trajectories raises error recognition from 19.9% to 35.2% and improves task completion.

## Gotchas

- Clean-start performance doesn't predict error recovery — a strong clean-start agent may still fail to recognize inherited errors.
- Error awareness rarely leads to recovery (15.6% vs 12.2% verifier pass rate) — agents often identify a problem but leave the affected state unchanged.
- Environment must be deterministic to replay prefixes and identify root cause accurately.
- Human annotation cost for verifying erroneous states is high.
