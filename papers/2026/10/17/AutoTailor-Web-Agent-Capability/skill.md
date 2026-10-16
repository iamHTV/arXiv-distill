# Skill: AutoTailor Capability Inventory (quản lý tool set web agent)
Source: 2609.13548
Type: framework / capability-management-workflow

## Khi nào dùng skill này
- Web/browser agent có tool collection discovered tự động — lớn, redundant, misaligned user demand
- Cần nén tool set (hàng nghìn APIs) mà không mất coverage, đồng thời reduce token cost + latency
- Task distribution thay đổi theo thời gian — tool inventory cần adapt online

Tình huống KHÔNG nên dùng: tool set nhỏ hand-crafted (<50 tools) ổn định; không có trajectory corpus hoặc runtime usage logs; không có ReAct/Playwright fallback để bù uncovered tasks.

## Input cần có
- Corpus web trajectories (task description + context + ordered browser actions)
- Code-gen LLM (chuyển trajectory → async Playwright function)
- Embedding model (docstring embedding cho clustering) + LLM verifier (functional equivalence) + LLM scorer (usage-likelihood 1–5)
- Dynamic MCP server (register/reload tools runtime)
- Runtime logs: user intent, tool-call sequence, task outcome, cumulative API usage
- Fallback agent (ReAct + Playwright MCP) cho uncovered tasks

## Các bước thực hiện
1. API Construction: prompt code-gen LLM convert mỗi trajectory thành async function; thay scenario-specific values (names, search terms, titles) bằng semantic parameters; giữ fixed labels, built-in options, URLs literal. Đảm bảo name/signature/docstring mô tả task, arguments, steps, return value.
2. Quality Filter (QF): (a) granularity filter — metadata-derived granularity score, bỏ overly specific/low-level/fine-grained, giữ user-facing operations ở target abstraction; (b) dedup — embed parameterized docstring, greedy centroid clustering cosine ≥0.75, pairs >0.80 → LLM verifier so sánh task descriptions, action sequences, executable code; giữ trajectory complete hơn, tie-break fewer steps rồi earlier corpus order.
3. Usage Likelihood Filter (ULF): LLM score usage-likelihood 1–5 conditioned trên target website + parameterized description; giữ score 4–5; THÊM highest-score API mỗi uncovered semantic cluster nếu score ≥3 (preserve coverage — đừng bỏ cả category).
4. MCP synthesis: register programs thành MCP tools (function name = tool id, docstring = description, semantic params = input schema).
5. Online Dynamic Reselection: log mỗi task (intent, tool-call sequence, outcome, usage); mark uncovered khi APIs fail HOẶC agent xác định no suitable API; normalize intents (parameterize task-specific values), embed + cluster (cosine ≥0.82), rolling window 100 tasks; trigger reselection periodically hoặc sau N uncovered tasks.
6. Candidate addition: LLM chọn ≤5 inactive APIs từ candidate pool (SQF) mỗi gap cluster; reload MCP tools. Clusters without candidate → reconsider sau khi có thêm runtime evidence.
7. Pruning: invoked APIs protected; never-used eligible sau 50-task inactivity; new APIs grace 50 tasks; min active set 10. Asymmetric: add nhanh, prune chậm.

## Output mong đợi
- Compact MCP capability set: 1,283 → 215 (QF) → 87 (ULF) → 33 (DR); với ReAct fallback: correctness 90.6% (+3.1pp vs ReAct alone 87.5%), total request-token cost −57.8%, latency −29.4%; không fallback: 60.1% correctness match full set với −94.9% request tokens.

## Ví dụ áp dụng
- E-commerce browser agent: crawl 1,283 trajectory-derived APIs (search, add-to-cart, checkout, refund...). QF bỏ overly-specific "search red size-42 running shoes under $50" → 215; ULF giữ high-demand (checkout, search) + 1 API mỗi cluster → 87; sau 100-task window, gap cluster "wishlist sharing" phát hiện → thêm 3 candidates, prune 57 never-used → 33 APIs. Correctness 90.6%, token cost −57.8%.

## Gotchas
- QF làm correctness −4.5pp (88.0→83.5) — granularity filter bỏ capabilities useful cho subset tasks; ULF phục hồi 87.3% nhưng đẩy unresolved tasks sang fallback (ReAct calls 4.25→5.33, total cost 1.42m→1.52m) — aggressive static filtering KHÔNG tự động reduce end-to-end cost.
- ULF alone không preserve coverage: −9.7pp (59.9→50.2) không có fallback — "ít dùng" ≠ "không essential"; phải giữ best API mỗi semantic cluster.
- DR calibration freeze: set được freeze sau calibration — evaluation không đo intermediate adaptation; với real usage cần re-run calibration khi distribution shift.
- Thresholds deployment-dependent: cosine 0.75/0.80/0.82, window 100, inactivity/grace 50, min 10 — calibrate per deployment, đừng copy cứng.
- Candidate pool phải là SQF (quality-filtered), không phải Sinit —否则 thêm lại redundant APIs.
- Pruning cần sustained evidence: single-task non-use không prune (50-task inactivity) — tránh removing seasonal capabilities.
- Coverage-gap detection phụ thuộc agent tự báo "no suitable API" — fallback agent phải honest về inability, không phải silently fail.
