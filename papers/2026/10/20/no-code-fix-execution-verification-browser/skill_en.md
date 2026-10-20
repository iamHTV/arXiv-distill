# Skill: No-Code Fix Execution Verification (rollback-based pipeline verifying code-free fixes in a real browser)
Source: 2610.11963v1
Type: evaluation-method / workflow

## When to use this skill
- Your support/triage workflow has many "invalid" bug reports (user misconfiguration, outdated version, conflicting extension) that need no-code fixes (direct the user to change a setting, update a version, or adjust workflow), and you want to AUTO-VERIFY fixes before sending them to users.
- You build/triage an LLM support agent and need to measure fix-generation capability WITHOUT text similarity / LLM judges (BERTScore median 0.831 for BOTH failing and working fixes — it cannot separate them).
- You evaluate computer-use / QA agent performance and need executors calibrated against humans (executor shift 38.8% average; ranking tau-b 0.05-0.45).
- Do NOT use: bugs not re-establishable in a controlled environment (~82% of candidates fail the gates: platform-specific, live backend, uncapturable-state entanglement — accumulated profile, OS, third-party service, server-side change); apps without deterministic state readable via a debug protocol (no checker can be built); single-product studies where generalization is unverified; budgets insufficient for a multi-executor x 3-run matrix (~3,000 episodes for 322 fixes).

## Inputs needed
- Candidate invalid bug reports with the maintainer resolution in the closed-issue discussion + the ground-truth fix classified version-type (update build) vs GUI-type (setting/extension action).
- Docker containers with pinned app builds (reported version + fixed version); scripted gate actions (apply + revert the GT fix deterministically).
- >=2 executor agents from different providers (1 proprietary computer-use + 1 open-weight CUA), shared action interface, <=20 steps/episode, identical task prompt (bug report + fix text).
- A deterministic issue-specific checker per report: reads browser/app state via DevTools Protocol (preference value, rendered property) tied to the stated actual result — the executor's claim is NEVER the verdict.
- Human calibration capacity: 2 double-blinded raters x a 75-fix random sample (Cochran 95% ±10%).

## Steps
1. **Funnel + setup**: annotated reports -> action-resolvable-subclass candidates -> Linux Docker containers; EXPECT ~17.6% to pass the two sanity gates (bug absent on GT-fixed state, present on rolled-back buggy state) -> effective evaluation set; keep the gates strict (scripted, NOT agent-run — validity independent of the executors).
2. **Generate candidate fixes**: a 12-configuration template (Vanilla/No-Prior/RAG/Agentic-web-search x 6 backbones — or a subset matching your scale); 3 independent runs each; chronological filtering + canonical issue page exclusion (against data leakage).
3. **Execute**: fresh container per episode (buggy value pre-seeded); executor applies the fix in <=20 steps; version-type issues: the harness switches the build WHEN the executor opens the update page (record that resolution depends on the executor performing the update); 3 runs per fix per executor; log termination status (DONE/BLOCKED/budget-exhausted) separately — never used as the verdict.
4. **Check**: the deterministic checker reads state -> is the bug still present? Resolved = checker confirms absence in >=1 of 3 runs; non-applicable = BLOCKED in >=2 of 3 runs; ALSO compute majority vote (ordering stable) + per-run rates.
5. **Calibrate executors vs humans**: a 75-fix sample, 2 double-blinded raters execute literally on identical starting states; report agreement % + Wilson CI + Cohen's kappa per executor + mismatch DIRECTION (false positives = overstatement vs false negatives = understatement); majority-vote variant (delta <=6.8%).
6. **Report**: per-executor + per-run + per-configuration rates, subclass breakdown (flag single-issue subclasses), ranking correlations tau-b, inter-executor agreement, the aggregation rule used, executor + harness names (RQ2 = executor+harness comparison — sampling settings differ; record T/top-p); NO significance tests on small sets — descriptive + issue-clustered bootstrap intervals.

## Expected output
- A verified-fix workflow: resolution rate per executor (expect a 15-50% spread, best executor ~50%); applicability; resolution-among-applicable (~18-70%); executor accuracy vs human consensus 66-88% (kappa 0.28-0.74); a BERTScore control showing similarity != correctness (median 0.831 in both classes); only checker-confirmed fixes (>=1 run) are sent to users.

## Example application
- SaaS helpdesk: 20 candidate "invalid" reports (config errors, outdated versions) -> funnel leaves 4 re-establishable (Docker pinned builds); GT fixes applied + reverted by scripted gates; 4 candidate LLM fixes per issue x 3 runs x 2 executors (Sonnet-class CUA + open-weight CUA); the checker reads app state via a debug protocol; resolution 30-65% depending on executor, ~35pp shift; a 15-fix double-blind human check: Sonnet-class agreement 82% (kappa 0.71), open CUA 65% with 10/12 mismatches being false positives -> send only fixes that the Sonnet-class executor checker-confirmed; the pipeline weeds out 9/29 BERTScore-0.83 fixes that NEVER work (all-fail-set analog) — avoiding garbage fixes reaching users.

## Gotchas
- "Fix failed" can mean "executor failed": the executor shift averages 38.8% — always use >=2 executors + human calibration before concluding which configuration is better.
- Agent DONE does not mean bug gone: 54.2% of DONE episodes resolved, BUT 15.0% of budget-exhausted episodes ALSO resolved and 2.7% of BLOCKED ones did; on version-dependent issues, DONE-but-failed = 121/324 OpenCUA episodes — never use the agent's completion signal.
- Checker leniency trap: when the expected value is the browser default (not stored explicitly), the checker accepts absence -> a general settings reset counts as resolution (issues 25057/37372) — tighten checkers for default-valued states.
- Harness + sampling differences confound executor comparison (the custom function-calling schema disadvantaged Muse Glimmer; greedy T=0 vs T=1.0 differ in any-run benefit) — report and interpret RQ2 as executor+harness.
- Any-run aggregation inflates volatile executors (+38 fixes for OpenCUA vs +12-24) — cross-executor comparisons under the any-run rule are biased; majority vote is more stable for rankings.
- ~82% of candidates are not re-establishable (uncapturable-state entanglement) — the gates are a measurement instrument; do not loosen the gates to get a bigger set (verdicts grounded in verified states carry more weight).
- Single-issue subclass (Wrong Version) + 9 issues total -> descriptive only, no significance claims; consensus-only comparison (59/75) overstates accuracy (drops the hardest-to-judge fixes) -> report per-human agreement separately.
- High-temperature executors benefit more from the any-run rule — calibrate the aggregation rule per executor temperature.

## Dry run test
- Hypothetical case (helpdesk with 15 candidate reports, pinned builds ready): step 1 funnel -> 4 issues pass the gates (26.7%, near the 17.6% band); step 2 3 configs x 3 runs = 27 fixes; step 3 2 executors x 3 runs x 27 fixes = 162 episodes; step 4 checker: resolution 18%-44% (executor A) vs 41% (executor B), all-three agreement 47%; step 5 human sample of 15 fixes: agreement 82% (kappa 0.71, A) vs 68% (kappa 0.30, B — 10/12 mismatches false positives); step 6 report A false-positive-prone, B understating -> use A with verification + human spot-check. Output: a complete verification workflow with metrics + calibration -> meaningful -> [SKILL VALID].
