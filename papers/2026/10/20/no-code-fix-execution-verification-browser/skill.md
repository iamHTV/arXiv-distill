# Skill: No-Code Fix Execution Verification (rollback-based pipeline verify fix không cần code trong browser thật)
Source: 2610.11963v1
Type: evaluation-method / workflow

## Khi nào dùng skill này
- Support/triage workflow của bạn có nhiều "invalid" bug reports (user misconfiguration, outdated version, conflicting extension) cần no-code fix (hướng user change setting / update version / adjust workflow) và bạn muốn AUTO-VERIFY fix trước khi gửi cho user.
- Bạn build/triage LLM support agent và cần đo fix-generation capability KHÔNG dùng text similarity/LLM judge (BERTScore 0.831 median cho BOTH failing và working fixes — không phân biệt được).
- Bạn đánh giá computer-use/QA agent performance — cần executor calibrated vs human (executor shift 38.8% average, ranking τb 0.05–0.45).
- KHÔNG nên dùng: bug không re-establishable trong controlled environment (~82% candidates fail gates: platform-specific, live backend, entangled uncapturable state — accumulated profile, OS, third-party service, server-side change); app không có deterministic state readable qua debug protocol (không build được checker); nhỏ hơn 1 product (single-app study — generalization chưa kiểm chứng); budget không đủ cho multi-executor × 3-run matrix (≈3,000 episodes cho 322 fixes).

## Input cần có
- Candidate invalid bug reports với maintainer resolution trong thảo luận closed issue + gt fix phân loại version-type (update build) vs GUI-type (setting/extension action).
- Docker containers với pinned app builds (reported version + fixed version); scripted gate actions (apply + revert GT fix deterministically).
- ≥2 executor agents khác providers (1 proprietary computer-use + 1 open-weight CUA), shared action interface, ≤20 steps/episode, identical task prompt (bug report + fix text).
- Deterministic issue-specific checker per report: đọc browser/app state qua DevTools Protocol (preference value, rendered property) tied to stated actual result — executor claim KHÔNG bao giờ là verdict.
- Human calibration capacity: 2 raters double-blinded × 75-fix random sample (Cochran 95% ±10%).

## Các bước thực hiện
1. **Funnel + setup**: từ annotated reports → candidates subclass action-resolvable → Docker Linux containers; EXPECT ~17.6% qua 2 sanity gates (bug absent on GT-fixed state, present on rolled-back buggy state) → effective evaluation set; keep gates strict (scripted, KHÔNG agent-run → validity independent of executors).
2. **Generate candidate fixes**: 12 configuration template (Vanilla/No-Prior/RAG/Agentic-web-search × 6 backbones — hoặc subset phù hợp scale); 3 independent runs each; chronological filtering + exclude canonical issue page (chống data leakage).
3. **Execute**: fresh container per episode (buggy value pre-seeded); executor apply fix ≤20 steps; version-type: harness switches build WHEN executor opens update page (record resolution rate phụ thuộc executor perform update); 3 runs/fix/executor; log termination status (DONE/BLOCKED/budget-exhausted) riêng — KHÔNG dùng làm verdict.
4. **Check**: deterministic checker đọc state → bug still present? Resolved = checker confirms absent ≥1/3 runs; non-applicable = BLOCKED ≥2/3 runs; CŨNG tính majority vote (ordering stable) + per-run rates.
5. **Calibrate executors vs humans**: 75-fix sample, 2 raters double-blinded execute literally trên identical starting states; report agreement % + Wilson CI + Cohen's κ per executor + mismatch DIRECTION (false positives = overstate vs false negatives = understate); majority-vote variant (Δ ≤6.8%).
6. **Report**: per-executor + per-run + per-configuration rates, subclass breakdown (flag single-issue subclasses), ranking correlations τb, inter-executor agreement, aggregation rule used, executor + harness names (RQ2 = executor+harness comparison — sampling settings differ, record T/top-p); KHÔNG significance tests trên small sets — descriptive + issue-clustered bootstrap intervals.

## Output mong đợi
- Verified-fix workflow: resolution rate per executor (expect 15–50% spread, best-executor ~50%); applicability; resolution-among-applicable (~18–70%); executor accuracy vs human consensus 66–88% (κ 0.28–0.74); BERTScore control chứng minh similarity ≠ correctness (median 0.831 cả 2 classes); verdict only gửi user fixes checker-confirmed ≥1 run.

## Ví dụ áp dụng
- SaaS helpdesk: 20 candidate "invalid" reports (config errors, outdated-version) → funnel còn 6 re-establishable (Docker pinned builds); GT fixes applied+reverted scripted gates; 4 candidate LLM fixes/issue × 3 runs × 2 executors (Sonnet-class CUA + open-weight CUA); checker đọc app state qua debug protocol; resolution 30–65% tùy executor, shift ~35pp; human double-blind 15 fixes: Sonnet-class agreement 80% (κ 0.72), open CUA 65% với 13/20 mismatch = false positives → chỉ gửi fixes Sonnet-class checker-confirmed; Pipeline khoét ra 9/29 fixes BERTScore 0.83 nhưng NEVER work (108-fix all-fail analog) → tránh gửi garbage fixes cho user.

## Gotchas
- "Fix failed" có thể nghĩa "executor failed": executor shift 38.8% average — luôn ≥2 executors + human calibration trước khi kết luận config nào better.
- Agent DONE ≠ bug gone: 54.2% DONE episodes resolved, NHƯNG 15.0% budget-exhausted episodes ALSO resolved, 2.7% BLOCKED resolved; version-dependent issues: DONE-but-failed 121/324 OpenCUA episodes — never dùng agent completion signal.
- Checker leniency trap: expected value = browser default (không stored explicitly) → checker accepts absence → general settings reset counts as resolution (issues 25057/37372) — tighten checker cho default-valued states.
- Harness + sampling differences confound executor comparison (custom function-calling schema disadvantaged Muse Glimmer; greedy T=0 vs T=1.0 khác any-run benefit) — report ko interpretation RQ2 = executor+harness.
- Any-run aggregation inflates volatile executors (+38 fixes OpenCUA vs +12–24) — cross-executor comparison under any-run rule biased → majority vote ổn định hơn cho ranking.
- ~82% candidates không re-establishable (uncapturable state entanglement) — gates là measurement instrument, đừng hạ thấp gates để có set lớn hơn (verdict grounded verified states weighs more).
- Single-issue subclass (Wrong Version) + 9 issues total → descriptive only, no significance claims; consensus-only comparison (59/75) overstates accuracy (drops hardest-to-judge fixes) → report per-human agreement separately.
- High-temp executors benefit more from any-run rule — calibrate aggregation rule per executor temperature.

## Dry run test
- Test case giả (helpdesk 15 candidate reports, pinned builds sẵn): step 1 funnel → 4 issues qua gates (26.7%, tương đương 17.6% band); step 2 3 configs × 3 runs = 27 fixes; step 3 2 executors × 3 runs × 27 fixes = 162 episodes; step 4 checker: resolution 18%–44% (executor A) vs 41% (executor B), all-agree 47%; step 5 human sample 15 fixes: agreement 82% (κ 0.71, A) vs 68% (κ 0.30, B — 10/12 mismatch false positives); step 6 report A false-positive-prone, B understated → use A với verification + human spot-check. Output: workflow verify hoàn chỉnh, metrics + calibration → meaningful → [SKILL VALID].
