# Skill: Windowed Interaction RL (WIRL) for Long-Horizon Agentic Tasks
Source: 2610.22344v1
Type: training-method / workflow

## When to use this skill
- You need to train/fine-tune an LLM agent for a long-horizon task where feedback arrives only after many decisions — MLE, data pipelines, content optimization, automated research.
- Trajectory-level rewards are too sparse or unstable; you need to learn from intermediate outcomes.
- Do NOT use: tasks with per-action feedback (use standard RL); tasks without verifiable execution feedback (no measurable execution success/score); without infrastructure for long-running experiments (paper: 12h × 20 vCPUs × 220 GB RAM × one H200 GPU per task).

## Inputs required
- Executable tasks with verifiable feedback: execution success/failure, scorable submissions, quality thresholds (paper uses Kaggle medal thresholds).
- An interaction harness: ReAct-style loop, tools (execute_code, update_answer, an analyze sub-agent), an experiment tree (solution nodes: code, logs, metadata), context compaction.
- Teacher trajectories for SFT (2 stages: general coding/tool-use + domain-specific), quality-filtered.
- Training infrastructure for async rollout collection + policy updates; log-probabilities of the rollout policy.

## Steps
1. **Build a task factory:** convert historical artifacts (Kaggle competitions, logs, cases) into executable tasks — public workspace + hidden test split + unified evaluator; a multi-agent pipeline (discovery → analyzer → generator) + validator checks (data integrity, submission format, evaluation behavior) + manual review.
2. **Hierarchical SFT Stage 1:** train on coding + tool-use trajectories from diverse agentic tasks → general tool-use and code revision capabilities.
3. **Hierarchical SFT Stage 2:** train on domain teacher trajectories (task initialization + sustained optimization + analysis sub-agent trajectories). Outcome-guided selection: for trajectories passing a quality threshold, identify the first best-performing submission; if post-peak degradation exceeds a threshold, retain the prefix up to the anchor; otherwise use the last submission. Loss applies only to newly generated reasoning/text/tool-call tokens; mask tool feedback and inherited history.
4. **WIRL windows:** while the agent runs, group consecutive model decisions between two successive experiment results into an execution window u_m, conditioned on the accumulated history.
5. **Window reward:** R_m = −1.0 (execution error caused by the model), −0.6 (no error but no scorable submission), −0.4 + T_m (below threshold), 1.0 + T_m (bronze/silver), 2.0 + T_m (gold); T_m ∈ {−0.2, 0, 0.2} per the trend vs the previous valid submission, 0 for the first submission. Use R_m as the shared optimization weight for ALL output tokens in the window (no group-relative normalization).
6. **Async collection:** asynchronously collect windows with trusted execution feedback into training batches — do not wait for the trajectory to finish.
7. **Policy correction:** for token t of model call j, compute q = exp(ℓ_old − ℓ_roll); weight the token by q if q ∈ [q_min, q_max], and exclude tokens outside the interval from the policy-gradient update (c = sg(q · 1[q_min ≤ q ≤ q_max])).
8. **Optimize:** loss = average over windows of (1/N_m) Σ c·L_PG + λ_KL·KL (vs a fixed SFT reference) − λ_H·entropy, where N_m = the number of valid output tokens in the window.

## Expected output
- An agent policy that learns long-horizon optimization: autonomously organizing experiments, revising from execution feedback, maintaining submission candidates.
- Each training stage adds gain (paper: 37.9% → 47.0% → 62.1% → 72.7% medal rate); WIRL beats GRPO (56.1%) and PPO-style (60.6%), both of which fell below the MLE-SFT baseline (62.1%).
- Capability generalizes: NatureBench Lite Surpass-SOTA 0% → 50%, scaffold optimization 23.3% → 43.7% held-out, algorithm-component reward 0.322 → 0.425.

## Example application
- A solopreneur fine-tunes an email-marketing optimization agent: build a task factory from past campaigns (A/B test results as verifiable feedback); SFT on their own trajectories (Stage 1 tool-use, Stage 2 marketing domain with outcome-guided trimming); WIRL windows group decisions between two campaign sends; reward −0.4/1.0/2.0 by conversion threshold + trend ±0.2; async collection while campaigns run overnight.

## Gotchas
- Wrong trajectory trimming: if you do NOT trim degraded tails, the model learns the post-peak decisions too (degradation); measure post-peak degradation and anchor at the first best submission.
- Reward hacking: the T_m trend bonus can encourage meaningless micro-improvements — verify the metric direction (increase/decrease) per task before setting T_m.
- Policy mismatch in async mode: do NOT skip policy correction — tokens outside [q_min, q_max] must be excluded, or off-policy data corrupts the update (in the paper, GRPO/PPO-style both fell below baseline).
- Window boundary: a window only ends when an experiment returns a result — if experiments are too long, windows get too large and credit assignment becomes sparse again; tune the execute_code frequency.
- Medal thresholds are task-specific: a domain without thresholds needs quality tiers defined before running.
- Cost: calls rose 1.00 → 9.39 for scaffold optimization — measure the accuracy-cost tradeoff separately.
- Contamination: exclude training tasks overlapping your benchmark before collecting trajectories.
