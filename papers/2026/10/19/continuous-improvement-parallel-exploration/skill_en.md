# Skill: Withheld-Leaderboard Reward Loop (WLRL)
Source: 2608.04341v1
Type: framework / workflow

## When to use this skill
- You have an optimization problem with a large solution space (prompt tuning, query rewriting, retrieval pipeline, data pipeline) and a measurable automated metric (accuracy, precision, coverage...).
- You want an agent to self-improve continuously with no human in the loop, or you want N agents exploring in parallel to escape a single paradigm.
- Do NOT use: tasks with no automated evaluation or ambiguous success criteria; no held-out test set to withhold as reward; no control over the sandbox (agents could read each other's code or leak test labels).

## Inputs required
- Dataset split into train/test; test labels MUST be organizer-only; agents see only train labels for self-evaluation.
- Leaderboard API: accepts submissions, scores against withheld ground truth, returns scores + ranking, logs to a persistent JSON ledger; shows scores + approach descriptions but NOT code.
- Qualification gate: a metric threshold on EVERY category independently (paper: ≥95% P@1 per category); qualified submissions ranked by average coverage.
- Sandbox: per-agent working directory + read-only shared resources; automated pre-run leak check.
- Resource lock (for shared GPU/CPU): two-level lock + CLAIM/RELEASE protocol + watchdog terminating unauthorized processes.
- A moderator agent scoped to logistics only: time warnings, leaderboard updates, queue management; NO technical advice.
- LLM agent + required tool environment (embedding models, index, string libraries...); fixed time budget (paper: 5 hours), no submission cap.

## Steps
1. **Setup:** split train/test, lock test labels organizer-only; install LeaderboardAPI + JSON ledger; configure sandbox isolation + leak check + resource lock; write the task briefing (task, data format, submission protocol, resource rules, time budget, baseline reference).
2. **Launch:** run N agents (paper used 1 and 5) with the same briefing; the only human command is "Run the competition with N agents for T hours." The moderator manages time automatically (warns at 30/5 minutes, forcibly terminates at the deadline).
3. **Agent loop (automatic):** analyze data/errors → survey candidate methods → hypothesize → implement → self-evaluate on train → submit test predictions → observe leaderboard → revise. Agents write periodic liveness heartbeats + fixed-cadence progress posts; they do NOT stop after a submission — they keep analyzing, revising, resubmitting until the budget ends.
4. **Reward feedback:** each submission returns per-category scores + qualification flag + ranking + approach descriptions of all submissions (the shared reward channel). Agents use this signal to revise; they never use each other's code.
5. **Review:** the organizer confirms final standings; analyze the qualified-submissions count, method diversity (embedding / string / TF-IDF families), and coverage on the hardest category.

## Expected output
- A leaderboard of qualified submissions ranked by average coverage; best qualified coverage well above baseline (paper: 33.3% → 47.8–57.4% single agent, 62.8–69.4% with 5 agents).
- With N≥5: agents diverge to qualitatively different methods within minutes; the winning method usually arrives LATE after a plateau — do not stop early.
- Single agent: deep iteration within the seeded paradigm (high P@1) but narrow; parallel: broader, slightly lower per-agent precision, high GPU contention.

## Example application
- A Vietnamese solopreneur optimizing a SKU-extraction pipeline for a marketplace shop: split 1,000 listings into train/test, build a LeaderboardAPI scoring P@1 per category, run 5 Claude agents for 5 hours with the briefing + BGE-M3 baseline. Expectation: agents discover string-matching/TF-IDF fusion on their own, which a single agent never tries; qualified coverage roughly doubles.

## Gotchas
- A single agent falls into a structural trap: it iterates BGE-M3 variants forever, never tries the simple lexical/string baseline, and in one run wrongly concluded a category was "unsolvable" and stopped early — always run N≥5 or seed opposing method families.
- Agent count is NOT a causal variable: it co-varies with compute, GPU contention, and leaderboard visibility — report descriptive ranges, never claim "5 agents beat 1 agent" as a scaling law.
- Artifact reuse: agents TRIED to reuse each other's code/indexes (observed) → block it structurally (per-agent directory + read-only shared), don't just discourage it.
- GPU crashes: naive concurrent use crashed the node in early runs → mandatory two-level lock + watchdog.
- Moderator drift: the moderator tends to drift into technical guidance → scope it logistics-only as an explicit design requirement.
- No code audit: infrastructure prevents cross-agent damage but does NOT safety-review agent-written code → run in a disposable sandbox.
- Set the qualification gate on the worst category, not the average — the baseline had 97.3% average P@1 yet FAILED because one category was below 95%.
