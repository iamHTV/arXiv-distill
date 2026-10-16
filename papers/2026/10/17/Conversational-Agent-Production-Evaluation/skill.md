# Skill: Commissioned Agent Evaluation (đánh giá behavior-specific production agent)
Source: 2609.32092
Type: evaluation-method / workflow

## Khi nào dùng skill này
- Production LLM agent (conversational shopping assistant, support agent) cần improve một behavior cụ thể
- Aggregate metrics (relevance, intent understanding, satisfaction) cho thấy quality kém nhưng không chỉ ra behavior nào cần sửa
- Log KHÔNG replay được (mỗi modification đổi các turn sau) và system varies run-to-run (LLM stochasticity + data đổi daily)

Tình huống KHÔNG nên dùng: behavior chưa reproduce được locally (investigation phải dừng — không optimize against behavior không study được); user thật không thể simulated đủ close để reproduce behaviors; cần measure business outcomes (phải A/B test, không phải offline framework này).

## Input cần có
- Production logs: customer messages + request context (page, shopping context) + products/items shown + pseudonymized customer identifiers
- Local instance của production assistant (đầy đủ components: guards, router, agents, retrieval, curation)
- LLM judge + LLM compiler (generate assertions) + customer simulator (grounded user simulation)
- Mô tả ngắn behavior cần investigate (từ report hoặc automated quality assessment)

## Các bước thực hiện
1. Commission: xác định behavior; harness tạo (a) targeted assertions (pass/fail conditions, nhiều strictness levels: any / first / ≥75% / all) vào versioned assertion library, (b) fixed cohort scenarios từ production pool (sampling: random / embedding-based farthest-point-nearest-neighbor-stratified-hybrid / intent-based). Human review assertions trước freeze. Freeze: cohort + assertions + evidence fields + decision thresholds + roles (target/guardrail/diagnostic).
2. Reproduce: chạy unchanged local assistant trên cohort; behavior reproduce khi targeted assertions fail trên đủ cohort; failure rate local ≈ reported rate. Nếu fail → dừng investigation.
3. Baseline: ≥3 runs of unchanged system → stored baseline (behavior + run-to-run variation).
4. Hypothesize: Improvement Orchestrator đọc assertion profile + traces → diverse hypotheses (prefer diverse over variations of same local change; propose along COMPLETE interaction path, không chỉ component nơi failure visible). Mỗi hypothesis = isolated modification trên clean local version. Autonomy budget cap số versions.
5. Compare: modified version chạy cùng số runs trên cùng scenarios; paired difference per scenario (modified mean − baseline mean); 2,000 percentile bootstrap resamples (fixed seed); verdict: signal+ (interval entirely >0), signal- (<0), noise (chứa 0, half-width ≤ threshold 0.05 trên 0–1 scale / 0.25 trên 1–5), borderline (chứa 0, half-width > threshold). Borderline → extend 5 runs.
6. Advance: target signal+ + no guardrail signal- → evaluation thứ 2 cùng điều kiện → cả hai pass → human review → possible online A/B test. Dừng tại first reproducible improvement (tránh optimize cho frozen cohort).
7. Post-investigation: reflection review investigation + cách conduct; nếu evaluation là nguyên nhân → propose harness revision (scenario selection, simulation, interpretation) → human approval → version mới, apply future investigations only, KHÔNG alter recorded decisions.

## Output mong đợi
- Verdict per hypothesis với paired bootstrap interval + assertion profile (vị trí failure: any/first/≥75%/all); modification pass cả 2 evaluations → human review + A/B test candidate; harness revision list (human-gated).
- Ví dụ: carousel category failure — profile cho first product 0.833 vs all 0.640 → effect ở prominent positions → fix curation prompt (strict rule) → first product +0.060, all +0.007.

## Ví dụ áp dụng
- Shopping assistant trả products ngoài category: commission 4 assertions (any/first/≥75%/all category match), cohort 51 production conversations, baseline 3 runs; hypothesis "curation prompt preference không đủ" → strict rule prompt → 3 runs → paired bootstrap: first product +0.060 signal-ish, profile confirms prominent-position mechanism → deploy. Gender case: h1 (tool description) borderline +0.067 [−0.022,+0.178] → reject; h2 (context binding default trong system prompt agent khác) +0.267 [+0.067,+0.511] signal+ + reproduce 3 runs + guardrail pass → confirm offline.

## Gotchas
- KHÔNG pool all sessions: pooling đếm scenario difficulty thành uncertainty → mất small improvement nhất quán. Scenario là unit of analysis; repeated sessions KHÔNG phải independent observations.
- Guardrail higher score KHÔNG phải lý do accept (task completion 4.27→4.96 trong gender case — only target signal+ matters; guardrail chỉ cần no signal-).
- Judge phải được audit như software: evidence sufficiency (assertion thiếu evidence), config propagation (temperature=0 configured but not passed to model), statistics (between-scenario vs across-run variance). Plausible-looking output vẫn sai được.
- Cohort KHÔNG phải random sample — failure rate mô tả cohort, KHÔNG estimate production frequency; đừng report như production rate.
- Multiplicity: hypothesis count không fixed in advance (50 nulls @ 0.05 → P(≥1 false signal+) > 0.9); classical corrections (Bonferroni) không fit (cùng modification accepted early, rejected late) — dùng anytime-valid e-values (Ville's inequality) nếu loop dài; small cohorts (9 scenarios) → bootstrap under-covers, borderline triggers more runs not acceptance.
- Cost scales với hypotheses: 3-turn session ≈ 4k (simulator) + 13k (task-completion) + 6k/assertion tokens; 300-session × 4-assertion investigation ≈ 10M tokens.
- Frozen evaluation outdated: record assistant build + judge models; rerun baseline khi either changes.
- Simulator không replay log — first message unchanged, subsequent turns GENERATED conditioned trên recorded messages (style examples, không script); validate simulator bằng cách reproduce reported failures + đọc plausibility.
- Stops at first reproducible improvement BY DESIGN — muốn explore thêm cần new evidence hoặc fresh cohort (không loop trên frozen cohort).
