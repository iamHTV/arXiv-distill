# Skill: HTN-Orchestrate — Hai lớp Planner/Orchestrator cho multi-agent research
Source: 2610.22195v1 (HTN-Orchestrate)
Type: framework (multi-agent orchestration)

## Khi nào dùng skill này
- Multi-agent task cần cả structured decomposition (dependencies giữa subtasks) lẫn adaptive execution (findings reshape plan).
- Research/web-investigation pipeline: task có subtasks phụ thuộc kết quả lẫn nhau ("phân tích X" cần output của "tìm X").
- KHÔNG nên dùng: task đơn giản 1-2 bước (ReAct đủ); task không có dependency giữa subtasks (Agent Team đơn giản hơn); cần decomposition sâu >2 levels (paper cap depth 2 — chưa test).

## Input cần có
- Task q + worker roles (research, verification) + tools (web search, retrieval, scholarly search, Python, file reading).
- Budgets: max depth (2), max children/node (4), max concurrent workers/leaf (3), max orchestration rounds/epoch (12), rebuild limit (1).
- Backbone model cho Planner/Orchestrator (high reasoning effort) + workers (low reasoning effort).

## Các bước thực hiện
1. Khởi tạo task network T = (V, Eh, Ed) với root = q, evidence summary M = ∅, epoch e = 0.
2. PlanOrExecute mỗi ready planning leaf (pending, tất cả prerequisites completed): xem goal, task description, ancestors, summaries of prerequisite results → hoặc mark direct execution, hoặc expand thành children + sibling dependency edges. Validate coverage của parent + acyclicity; revise nếu fail. DEPENDENT subtasks: chỉ decompose SAU KHI prerequisite results trả về (result-informed planning).
3. Dispatch ready executable leaves đến Orchestrators song song (wave). Mỗi Orchestrator: nhận context C_v (task, leaf objective, ancestors, prerequisite summaries); loop dispatch/wait/finish — dispatch select roles + task-specific instructions dựa trên evidence hiện tại (initial investigation → focused search hoặc verification khi report reveal gap/disputed claim); progressive collection (follow-up while assignments active); finish → SynthesizeLeaf (summary, resolved/unresolved outcome, evidence references).
4. PropagateResults: record leaf results; recursively synthesize mỗi parent whose children ALL returned (AND semantics — non-leaf chỉ synthesize sau khi TẤT CẢ children complete).
5. Check root: resolved → return synthesized result. Không → settle/stop ongoing work, CollectEvidence extract supported findings từ completed VÀ partial reports thành M; e+1; nếu e ≥ rebuild limit hoặc budgets exhausted → synthesize evidence đến giờ + report unresolved requirements (KHÔNG treat stopping như success).
6. Rebuild: InitializeRoot(q, M) — new network rooted tại original task, condition trên evidence summary M (planning context, KHÔNG auto-mark subtask completed); quay bước 2.
7. Termination hygiene: output luôn phản ánh sufficiency of evidence; unresolved requirements được report rõ.

## Output mong đợm
- Final answer + evidence references; internal stats: tree depth/leaves, executed leaf instances, worker invocations, orchestrator rounds, rebuild rate. Expected gains (paper, BrowseComp): +2.45pp vs Agent Team, +15.80pp vs ReAct; faster trên 67.9% shared successes (median ratio 0.699); concurrency 2.47 vs 1.70.

## Ví dụ áp dụng
- Solopreneur research task "phân tích pricing strategy của competitor X": Planner tạo "thu thập pricing pages" → sau khi result trả, decompose "so sánh tiers" condition trên actual prices tìm được (không phải guess trước); leaf orchestrator dispatch researcher + verifier; nếu root unresolved sau wave (ví dụ pricing page không load được), CollectEvidence giữ candidate pages + rejected URLs, rebuild với "tìm pricing qua review sites". Expected: đúng target, 4 leaves thay vì 5.

## Gotchas
- Đừng decompose dependent subtasks upfront — ablation: −1.5pp accuracy, +4.79 phút median, nhiều invocations hơn. Decompose SAU KHI prerequisite results có.
- AND semantics nghiêm ngặt: parent synthesize chỉ sau khi TẤT CẢ children complete — 1 leaf stuck kéo cả parent; dùng orchestrator rounds/time budgets để bound.
- Rebuild KHÔNG phải restart: evidence carryover (M) là planning context, không auto-complete — nếu không giữ partial findings, rebuild mất hết progress (case Q501: đúng "Serial Killer" vs sai "Silent Night").
- Outcome = sufficiency of evidence, không phải "verifier invoked" hay "workers stopped" — don't game the outcome field.
- Budgets bắt buộc: depth 2, ≤4 children, ≤3 workers, ≤12 rounds, 1 rebuild — không có chúng network growth unbounded.
- Workers low reasoning effort, orchestration agents high — tiết kiệm cost; đừng đảo ngược.
- Decomposition phải validate coverage + acyclicity — LLM generate children có thể miss parent aspect hoặc tạo dependency cycle.
- Chỉ test 1 backbone (DeepSeek-V4.1-Flash) — validate trên model của bạn trước khi production.
