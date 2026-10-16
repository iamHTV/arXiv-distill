# Skill: AutoTailor Capability Inventory (web-agent tool-set management)
Source: 2609.13548
Type: framework / capability-management-workflow

## When to use this skill
- A web/browser agent has an auto-discovered tool collection that is large, redundant, and misaligned with user demand
- You need to compress a tool set (thousands of APIs) without losing coverage while reducing token cost and latency
- The task distribution changes over time — the tool inventory needs online adaptation

Do NOT use: a small hand-crafted, stable tool set (<50 tools); no trajectory corpus or runtime usage logs; no ReAct/Playwright fallback to cover uncovered tasks.

## Input required
- A corpus of web trajectories (task description + context + ordered browser actions)
- A code-gen LLM (trajectory → async Playwright function)
- An embedding model (docstring embedding for clustering) + LLM verifier (functional equivalence) + LLM scorer (usage-likelihood 1–5)
- A dynamic MCP server (register/reload tools at runtime)
- Runtime logs: user intent, tool-call sequence, task outcome, cumulative API usage
- A fallback agent (ReAct + Playwright MCP) for uncovered tasks

## Steps
1. API Construction: prompt the code-gen LLM to convert each trajectory into an async function; replace scenario-specific values (names, search terms, titles) with semantic parameters; keep fixed labels, built-in options, URLs literal. Ensure name/signature/docstring describe the task, arguments, steps, and return value.
2. Quality Filter (QF): (a) granularity filter — metadata-derived granularity score, remove overly specific/low-level/fine-grained, keep user-facing operations at the target abstraction; (b) dedup — embed parameterized docstrings, greedy centroid clustering at cosine ≥0.75, pairs >0.80 → LLM verifier compares task descriptions, action sequences, executable code; keep the more complete trajectory, tie-break by fewer steps then earlier corpus order.
3. Usage Likelihood Filter (ULF): LLM scores usage-likelihood 1–5 conditioned on the target website + parameterized description; keep scores 4–5; ALSO keep the highest-scoring API from any otherwise-uncovered semantic cluster if score ≥3 (coverage preservation — don't drop entire categories).
4. MCP synthesis: register programs as MCP tools (function name = tool id, docstring = description, semantic params = input schema).
5. Online Dynamic Reselection: log every task (intent, tool-call sequence, outcome, usage); mark uncovered when APIs fail OR the agent determines no suitable API; normalize intents (parameterize task-specific values), embed + cluster (cosine ≥0.82), rolling window of 100 tasks; trigger reselection periodically or after N uncovered tasks.
6. Candidate addition: LLM selects ≤5 inactive APIs from the candidate pool (SQF) per gap cluster; reload MCP tools. Clusters without a candidate → reconsider after more runtime evidence.
7. Pruning: invoked APIs protected; never-used eligible after 50-task inactivity; new APIs get a 50-task grace period; minimum active set of 10. Asymmetric: add fast, prune slow.

## Expected output
- A compact MCP capability set: 1,283 → 215 (QF) → 87 (ULF) → 33 (DR); with ReAct fallback: correctness 90.6% (+3.1pp over ReAct alone at 87.5%), total request-token cost −57.8%, latency −29.4%; without fallback: 60.1% correctness matching the full set at −94.9% request tokens.

## Example application
- An e-commerce browser agent: crawl 1,283 trajectory-derived APIs (search, add-to-cart, checkout, refund...). QF removes overly-specific "search red size-42 running shoes under $50" → 215; ULF keeps high-demand (checkout, search) + 1 API per cluster → 87; after a 100-task window, a "wishlist sharing" gap cluster is detected → 3 candidates added, 57 never-used pruned → 33 APIs. Correctness 90.6%, token cost −57.8%.

## Gotchas
- QF drops correctness −4.5pp (88.0→83.5) — the granularity filter removes capabilities useful for a subset of tasks; ULF recovers 87.3% but shifts unresolved tasks to the fallback (ReAct calls 4.25→5.33, total cost 1.42m→1.52m) — aggressive static filtering does NOT automatically reduce end-to-end cost.
- ULF alone does not preserve coverage: −9.7pp (59.9→50.2) without fallback — "rarely used" ≠ "not essential"; always keep the best API per semantic cluster.
- DR calibration freeze: the set is frozen after calibration — the evaluation doesn't measure intermediate adaptation; with real usage, re-run calibration when the distribution shifts.
- Thresholds are deployment-dependent: cosine 0.75/0.80/0.82, window 100, inactivity/grace 50, min 10 — calibrate per deployment; don't copy blindly.
- The candidate pool must be SQF (quality-filtered), not Sinit — otherwise you re-add redundant APIs.
- Pruning needs sustained evidence: single-task non-use doesn't prune (50-task inactivity) — avoids removing seasonal capabilities.
- Coverage-gap detection depends on the agent self-reporting "no suitable API" — the fallback agent must be honest about inability, not silently fail.
