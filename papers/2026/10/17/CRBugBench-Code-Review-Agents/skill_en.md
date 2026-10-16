# Skill: Bug-grounded Review Agent Evaluation (CRBugBench method)
Source: 2610.13668
Type: evaluation-method (benchmark construction + evaluation for code review agents)

## When to use this skill
- Evaluating whether a code review agent actually catches bugs (instead of lexically matching human comments)
- Building a custom benchmark for your own repos (OSS or proprietary) to measure review quality over model evolution
- Do NOT use: evaluating style/subjective review aspects (conciseness, tone) — this method only measures bug-finding

## Inputs required
- Repo history: PR discussion threads + bug-fix PRs (to mine ground-truth bugs)
- Sandbox environment for the agent (repo at the introducing commit, restricted internet)
- An LLM judge panel + a rubric matching findings ↔ ground-truth bugs

## Steps
1. Mine bugs from history via two sources: (a) human review threads with bug-related comments that were addressed before merge (catch-before-merge); (b) bug-fix PRs traced back to the introducing PR (catch-after-merge / escaped).
2. Create review tasks: give the agent a sandboxed repo at the introducing commit + diff; the agent explores/experiments then writes review.md, self-ranking findings by severity.
3. An LLM judge panel compares each finding in review.md against the ground-truth bug, labels match/no-match; compute recall@5.
4. Segment analysis: split OSS vs proprietary, PR size/heterogeneity, bug severity/type, local vs non-local reasoning — use logistic regression to learn where the agent is weak.
5. Tune the harness in cost-effectiveness order: exploration-nudging prompts first (+5.8% @ 1.10× cost), then multi-agents (+4.7% @ 5.55×) or high reasoning effort (36%→57% @ 23.22×).
6. Dispatch models by PR characteristics: small homogeneous PRs → cheap models (gpt-5.6-luna class); large heterogeneous PRs → opus-class + human review.

## Expected output
- recall@5 on your own task set; how many % of human-verified bugs the agent catches; a model-dispatch + harness-tuning roadmap along the cost-performance Pareto front.

## Example application
- A team wants a review agent for a monorepo: mine 200 bugs from 6 months of history, run the agent, measure recall@5 = 65%; find a 20% drop on PRs >500 lines → rule: large PRs always get human review.

## Gotchas
- Human comments are NOT good ground truth (nitpicking, social dynamics) — use bugs verified by fixes, not comments.
- Agents rarely execute code (9.7% of turns) — bugs needing runtime evidence are easily missed; supply a repository knowledge base for proprietary repos.
- Agents trust misleading PR descriptions — do not let the description anchor the review; inspect the actual code.
- recall@5 overstates if production only checks the top comment — calibrate against top-1/top-3.
- A harness that helps one model may be useless for the next (fast model evolution) — re-evaluate periodically.
