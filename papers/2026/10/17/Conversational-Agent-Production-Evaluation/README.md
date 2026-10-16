# 2609.32092 — On Evaluating and Improving Conversational Agents in Production

## Problem
- Offline evaluation production conversational agent gặp 3 obstacles: (i) logged conversation KHÔNG replay được against modified system — response khác làm mọi turn sau invalid; (ii) unchanged system tự varies run-to-run (LLM stochastic + products/prices/personalization signals đổi daily); (iii) aggregate quality scores (relevance, intent understanding) combine distinct behaviors — biết quality đổi nhưng không biết behavior nào gây ra, không sửa được.

## Contribution
- Framework 4 phần: Evaluation Harness (commission targeted evaluation: targeted assertions + fixed cohort customer scenarios), grounded user simulation (simulator viết customer turns mới conditioned trên recorded messages/context, KHÔNG replay log), Improvement Orchestrator (assertion results → hypotheses → isolated modifications → paired percentile bootstrap comparison), human-gated self-revising harness (revision sau investigation, human approval, chỉ apply future, không alter past decisions).
- Áp dụng production: Zalando Production Assistant, 20+ European markets, hàng triệu conversations/tháng.

## Method
- System under test: 2 guards (in-house malicious-intent classifier pre-processing + general content moderation during generation) → LLM router → verticals (fashion agent in-house: product search, beauty/kids, size/fit, cart, small talk — chạy speculative song song router; customer care service: language detection, case classification, RAG help-center, order/return/shipment queries; gift card deep link; sensitive-data refusal). Search action: query generation (1–3 queries + structured filters) → retrieve/rank/personalize → merge (dedup vs shown products) → LLM curation (carousel ≤8 items; shortfall filled từ pre-curation ranking KHÔNG check). State: message history + structured search state + consent-gated customer memory (sizes, brands, materials, past interactions). Web-search sub-agents cho out-of-catalog questions (moderated).
- Cohort: pool production conversations từ defined period (reconstruct cần customer messages + request context + products shown); sampling: random / embedding-based (farthest-point, nearest-neighbor, stratified, hybrid) / intent-based (10 intents, ~40 subtopics). Pseudonymized. Cohort KHÔNG phải random sample — failure rate mô tả cohort, không estimate production.
- Assertions: LLM compiler → versioned assertion library; human review trước freeze; profile đánh giá same requirement ở nhiều strictness levels (any / first / ≥75% / all products). Evidence fields fixed trước khi evaluate modified versions.
- Simulation: conversation-grounded (first recorded message unchanged; subsequent messages làm example cách customer giao tiếp, KHÔNG script; turn limit bounded) hoặc goal-based (goal description + context + turn limit). Simulator scorer: goal pursuit, task adherence, interaction efficiency, stopping behavior.
- Paired decision rule: ≥3 runs/version; paired difference per scenario (modified mean − baseline mean); 2,000 percentile bootstrap resamples fixed seed; interval entirely >0 → signal+, entirely <0 → signal-, chứa 0 → noise (half-width ≤ threshold 0.05 on 0–1 scale, 0.25 on 1–5) hoặc borderline. Scenario = unit of analysis. Roles frozen: target / guardrail / diagnostic. Advancement: target signal+ + no guardrail signal- + second evaluation same conditions → human review → possible online A/B test.
- Improvement Orchestrator: diverse hypotheses (prefer diverse over local variations), autonomy budget cap, isolated modification on clean local version, sequential evaluation; borderline → extend to 5 runs; stops at first reproducible improvement (tránh optimize for frozen cohort).

## Key Findings
- Investigation 1 (category): carousels chứa products ngoài requested category; 51 production conversations, 50 scored, 3 runs/version. Baseline: any 0.913±0.012, first 0.833±0.023, ≥75% 0.733±0.076, all 0.640±0.040 (~1 carousel trong 3 có out-of-category product). Fix: curation prompt preference → strict rule (prompt instruction, không code filter). Modified: 0.947/0.893/0.747/0.647 (∆ +0.033/+0.060/+0.013/+0.007) — profile cho thấy effect ở prominent positions, không phải whole result set. Deployed.
- Investigation 2 (gender): gender-silent requests từ men's context trả women's products; 10 goal-based scenarios (9 men's + 1 women's guardrail), 5 runs/version. h1 (tool description tại suspected component): first product 0.733→0.800, +0.067 [−0.022, +0.178] borderline. h2 (shopping context thành binding default trong system prompt của different agent): 0.733→1.000, +0.267 [+0.067, +0.511] signal+; task completion 4.27→4.96 (+0.22, signal+ — nhưng higher guardrail không tự là lý do accept). h2 reproduce thêm 3 runs; guardrail pass mọi run. Confirmed offline.
- Judge audits tìm 3 defects: (a) assertion thiếu evidence nó cần (relevant result info chưa được add vào judge evidence); (b) judge temperature đặt 0 nhưng client KHÔNG pass setting tới model — configured but not applied; (c) separate benchmark report dùng between-scenario differences thay vì across-run variation. Cả 3 output plausible-looking; (a) và (b) có thể đã đổi decision.
- E-value post hoc check (Waudby-Smith–Ramas betting): h2 betting interval lower end 0.00–0.01 vs bootstrap 0.067 → h2 sẽ borderline tại 9 scenarios; doubling lên 18 scenarios → lower end 0.08 = signal+.
- Cost: 3-turn session ≈ 4,000 tokens simulated customer + 13,000 task-completion score + 6,000/assertion; category investigation (300 sessions, 4 assertions) ≈ 10M tokens. Judging dominates (input tokens).
- Production traffic (4 months 2026): ~50% product searches, style advice/outfit 2nd, product details 3rd, ~10% orders. Attributes: category > color > brand > gender > size > material.

## Actionable Insights
- Đánh giá behavior-specific, không aggregate: commissioned assertions ở nhiều strictness levels (any/first/≥75%/all) cho profile chỉ ra failure nằm ở carousel positions nào → hypothesis đúng (category fix ở curation prompt, không phải retrieval).
- So sánh paired per-scenario, KHÔNG pool all sessions: pooling đếm scenario difficulty variation thành uncertainty → mất small improvement nhất quán mọi scenario. Dùng ≥3 runs + percentile bootstrap intervals trên scenario-level differences.
- Audit judge như software: kiểm tra (1) judge có đủ evidence cho mỗi assertion không, (2) config thực sự được pass tới model không (temperature=0 configured but not applied), (3) statistics dùng đúng variance source không. Output plausible-looking vẫn có thể sai.

## Assumptions & Limitations
- Offline results only — offline improvement không establish customer satisfaction/business outcomes; cần controlled A/B tests.
- Simulator validated bằng cách reproduce reported failures + đọc simulated conversations; CHƯA đo mức simulator match real customer behavior across wide range of intents/scenarios.
- Paired bootstrap treat judge + production environment fixed; judge models differed across investigations; recorded scores predate temperature fix.
- No formal multiplicity correction — hypothesis count không fixed in advance (50 nulls at 0.05 → P(≥1 false signal+) > 0.9); safeguards (fix roles, second evaluation, cap hypotheses) lower but don't bound risk; classical corrections (Bonferroni) không fit — đề xuất anytime-valid inference với e-values (Ville's inequality).
- Gender case: 9 paired scenarios limited power; percentile bootstrap under-covers ở size này.
- Cohort failure rate không estimate production frequency (cohort selected to show failure).

## Metadata
- 2026 (2026-09-25), Kasra Hosseini, Wen-Sen Cheng, Marco-Andrea Buchmann, Emir Mulabegovic, Weiwei Cheng (Zalando SE Berlin / Zalando Switzerland), cs.MA, https://arxiv.org/pdf/2609.32092
