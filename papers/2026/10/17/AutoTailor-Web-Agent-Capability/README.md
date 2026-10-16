# 2609.13548 — AutoTailor: Automatic, User-Aligned Capability Selection and Adaptation for Web Agents

## Problem
- Web agent dùng reusable tools (MCP API) giảm cost/latency của low-level browser interaction, nhưng automatically discovered tool collections lớn (1,283 APIs), redundant, poorly aligned với user demand. Open problem: xây capability space vừa compact vừa align nhu cầu user — manual construction costly, automated discovery coverage不足.

## Contribution
- AutoTailor: meta-agentic framework 2 module — Offline Selection (trajectory → parameterized Playwright programs → Quality Filter → Usage Likelihood Filter) và Online Dynamic Reselection (log usage → detect coverage gaps → add candidates → prune unused).
- Chứng minh static filtering + dynamic adaptation cải thiện đồng thời accuracy, latency, token cost trên 106 WebArena Postmill tasks.

## Method
- Offline: (1) Trajectory Crawling — collect diverse multi-step web trajectories; (2) API Construction — code-gen LLM convert mỗi trajectory thành async Playwright function, scenario-specific values (user names, search terms) → semantic parameters, fixed labels/URLs giữ literal → reusable task template; (3) Selection — QF: granularity filter (metadata-derived score, bỏ overly specific/low-level) + functional dedup (embed parameterized docstring, greedy centroid clustering cosine ≥0.75, pairs >0.80 LLM-verified functional equivalence, giữ trajectory complete hơn) 1,283→215; ULF: LLM score usage-likelihood 1–5, giữ 4–5, thêm highest-score API mỗi uncovered semantic cluster nếu ≥3 (preserve coverage) 215→87.
- MCP synthesis: dynamic MCP server register programs as tools (function name = tool id, docstring = description, semantic params = input schema).
- Online DR (4 steps): Logged Runtime Usage (intent, tool-call sequence, outcome, cumulative usage) → Coverage-Gap Detection (uncovered = APIs fail task HOẶC agent xác định no suitable API; rolling window 100 tasks, cosine 0.82 clustering normalized intents) → Candidate Retrieval (LLM chọn ≤5 candidate APIs từ SQF mỗi gap cluster) → Capability Pruning (invoked APIs protected; never-used eligible sau 50 tasks; new APIs grace 50 tasks; min active set 10). Asymmetric: expansion nhanh, removal chậm.
- Evaluation: WebArena Postmill 106 tasks; tooling agent = Copilot với Claude Opus 4.8 kết nối AutoTailor MCP server; fallback agent = Playwright MCP; DR calibration: randomize 106 tasks → simulated interaction sequence → frozen SDR = 33 APIs.

## Key Findings
- Với ReAct fallback: SDR 90.6% correctness (best), latency 72.45s (lowest), 98.46k tooling request tokens, total request-token cost 1.32m — vs ReAct alone 87.5%: +3.1pp correctness, −57.8% total request-token cost, −29.4% latency; vs Sinit: >24× reduction tooling request tokens VỚI correctness cải thiện.
- Static stages w/ ReAct: Sinit 88.0% (2.39m tokens), SQF 83.5% (403.30k tokens, −order of magnitude, latency 93.31→85.97s), SULF 87.3% (205.13k tokens, nhưng ReAct LLM calls 4.25→5.33 và total cost 1.42m→1.52m — aggressive static filtering đẩy unresolved tasks sang ReAct fallback).
- Không ReAct: Sinit 60.4%, SQF 59.9% (−0.5pp, latency 99.11→84.48s, tokens 2.78m→452.58k), SULF 50.2% (−9.7pp — ULF alone không preserve coverage), SDR 60.1% (match Sinit/SQF tại 142.86k tokens = −94.9% request-token usage, latency 79.50s).

## Actionable Insights
- Đừng giữ toàn bộ discovered tools: QF+ULF nén 1,283→87 APIs (−93%) với near-unchanged correctness (60.4→59.9 without fallback) — redundancy trong tool collections là real cost, không phải insurance.
- Dùng fallback-aware filter ordering: ULF một mình làm correctness −9.7pp (50.2%) vì bỏ "ít dùng nhưng essential" APIs — luôn giữ highest-score API mỗi semantic cluster (score ≥3) để preserve coverage, và dùng ReAct fallback bù đắp phần còn lại.
- Adapt tool inventory online theo actual usage: DR chọn 33 APIs (từ pool 87) match runtime distribution — 90.6% correctness với −57.8% token cost; asymmetric policy (add nhanh khi gap, prune sau 50-task inactivity) tránh churn.

## Assumptions & Limitations
- Evaluation dùng templated WebArena tasks mô phỏng repeated user interaction — chưa validate với real-world dynamic usage; calibration giả định task intents/frequencies approx stable sau calibration.
- DR calibration freeze: evaluation đo quality của calibrated set, không report per-step adaptation behavior (trigger counts, intermediate API sets).
- Per-user adaptation; shared capability profiles across user groups là future work.
- Thresholds deployment-dependent (0.75/0.80/0.82 cosine, 100-task window, 50-task inactivity/grace, min 10 APIs) — cần calibrate per deployment.

## Metadata
- 2026 (2026-09-11), Xinyun Cao (University of Michigan), Adriana Szekeres, Fazle Elahi Faisal (Microsoft Research Redmond), cs.AI, preprint under review, https://arxiv.org/pdf/2609.13548
