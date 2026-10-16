# 2609.13548 — AutoTailor: Automatic, User-Aligned Capability Selection and Adaptation for Web Agents

## Problem
- Web agents use reusable tools (MCP APIs) to reduce cost/latency of low-level browser interaction, but automatically discovered tool collections are large (1,283 APIs), redundant, and poorly aligned with user demand. Open problem: build a capability space that stays compact while aligning with user needs — manual construction is costly, automated discovery has insufficient coverage.

## Contribution
- AutoTailor: a meta-agentic framework with two modules — Offline Selection (trajectories → parameterized Playwright programs → Quality Filter → Usage Likelihood Filter) and Online Dynamic Reselection (log usage → detect coverage gaps → add candidates → prune unused).
- Shows static filtering + dynamic adaptation improve accuracy, latency, and token cost simultaneously on 106 WebArena Postmill tasks.

## Method
- Offline: (1) Trajectory Crawling — collect diverse multi-step web trajectories; (2) API Construction — a code-gen LLM converts each trajectory into an async Playwright function, replacing scenario-specific values (user names, search terms) with semantic parameters while fixed labels/URLs stay literal → reusable task template; (3) Selection — QF: granularity filter (metadata-derived score, remove overly specific/low-level) + functional dedup (embed parameterized docstring, greedy centroid clustering at cosine ≥0.75, pairs >0.80 LLM-verified for functional equivalence, keep the more complete trajectory) 1,283→215; ULF: LLM assigns usage-likelihood 1–5, keeps 4–5, plus the highest-scoring API from any otherwise-uncovered semantic cluster if ≥3 (coverage preservation) 215→87.
- MCP synthesis: a dynamic MCP server registers programs as tools (function name = tool id, docstring = description, semantic params = input schema).
- Online DR (4 steps): Logged Runtime Usage (intent, tool-call sequence, outcome, cumulative usage) → Coverage-Gap Detection (uncovered = APIs fail the task OR the agent determines no suitable API; rolling window of 100 tasks, cosine-0.82 clustering of normalized intents) → Candidate Retrieval (LLM selects ≤5 candidate APIs from SQF per gap cluster) → Capability Pruning (invoked APIs protected; never-used eligible after 50 tasks; new APIs get a 50-task grace period; minimum active set of 10). Asymmetric: fast expansion, slow removal.
- Evaluation: WebArena Postmill, 106 tasks; tooling agent = Copilot with Claude Opus 4.8 connected to the AutoTailor MCP server; fallback agent = Playwright MCP; DR calibration: randomize the 106 tasks → simulated interaction sequence → frozen SDR = 33 APIs.

## Key Findings
- With ReAct fallback: SDR reaches 90.6% correctness (best), 72.45s latency (lowest), 98.46k tooling request tokens, 1.32m total request-token cost — vs ReAct alone (87.5%): +3.1pp correctness, −57.8% total request-token cost, −29.4% latency; vs Sinit: >24× reduction in tooling request tokens WHILE improving correctness.
- Static stages w/ ReAct: Sinit 88.0% (2.39m tokens), SQF 83.5% (403.30k tokens — order-of-magnitude reduction, latency 93.31→85.97s), SULF 87.3% (205.13k tokens, but ReAct LLM calls rise 4.25→5.33 and total cost 1.42m→1.52m — aggressive static filtering shifts unresolved tasks to the ReAct fallback).
- Without ReAct: Sinit 60.4%, SQF 59.9% (−0.5pp; latency 99.11→84.48s, tokens 2.78m→452.58k), SULF 50.2% (−9.7pp — ULF alone does not preserve coverage), SDR 60.1% (matches Sinit/SQF at 142.86k tokens = −94.9% request-token usage, latency 79.50s).

## Actionable Insights
- Don't keep every discovered tool: QF+ULF compresses 1,283→87 APIs (−93%) with near-unchanged correctness (60.4→59.9 without fallback) — redundancy in tool collections is a real cost, not insurance.
- Use fallback-aware filter ordering: ULF alone drops correctness −9.7pp (50.2%) because it removes "rarely used but essential" APIs — always keep the highest-scoring API per semantic cluster (score ≥3) to preserve coverage, and let a ReAct fallback compensate for the rest.
- Adapt the tool inventory online to actual usage: DR selects 33 APIs (from the 87 pool) matching the runtime distribution — 90.6% correctness at −57.8% token cost; the asymmetric policy (add fast on gaps, prune after 50-task inactivity) avoids churn.

## Assumptions & Limitations
- Evaluation uses templated WebArena tasks simulating repeated user interaction — not yet validated with real-world dynamic usage; calibration assumes task intents/frequencies remain approximately stable after calibration.
- DR calibration freeze: the evaluation measures the quality of the calibrated set and does not report per-step adaptation behavior (trigger counts, intermediate API sets).
- Per-user adaptation; shared capability profiles across user groups is future work.
- Thresholds are deployment-dependent (0.75/0.80/0.82 cosine, 100-task window, 50-task inactivity/grace, min 10 APIs) — calibrate per deployment.

## Metadata
- 2026 (2026-09-11), Xinyun Cao (University of Michigan), Adriana Szekeres, Fazle Elahi Faisal (Microsoft Research Redmond), cs.AI, preprint under review, https://arxiv.org/pdf/2609.13548
