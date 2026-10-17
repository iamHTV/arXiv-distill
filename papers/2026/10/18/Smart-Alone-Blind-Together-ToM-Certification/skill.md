# Skill: Blind-Spot Gate — Chứng nhận deployment ToM module (không deploy)
Source: 2610.19051v1 (Smart Alone, Blind Together)
Type: evaluation-method (deployment certification)

## Khi nào dùng skill này
- Multi-agent system có coordinator act on inferred beliefs về teammates (LLM đọc convention/state của agent khác rồi hành động), và wrong action có cost thực.
- Cần decide deploy/không deploy 1 ToM module TRƯỚC khi chạy production, đặc biệt khi games/episodes của module ít (direct A/B measurement chưa đủ data).
- KHÔNG nên dùng khi: module chỉ output advisory không hành động (accuracy đủ); không simulate được coordinator với injected beliefs; module tạo nhiều coherent errors cùng lúc (error load > 4 — dùng direct measurement).

## Input cần có
- Simulator của coordinator nhận injected beliefs (chạy episode với belief sai đã biết).
- Cost model: harm h (scaling consequence của wrong action, ví dụ wasted round → eject worker; lives trong game).
- Module cần certify: error statistics q_u (error rate trên mỗi belief u) và joint errors Δ_uv = Pr[both wrong] − q_u q_v.
- Ngưỡng safety floor (chấp nhận bao nhiêu deferral).

## Các bước thực hiện
1. Đo single-error costs: chạy paired single-injection replays (ThresholdProbe) — với mỗi belief u, inject 1 wrong belief, đo c_u (cost của belief u alone wrong). Cũng dự đoán được break-even threshold a*(h) = |ℓ(h)|/(1+|ℓ(h)|) trong 0.03–0.05.
2. Đo pairwise interactions I_uv: chạy pair-injection replays (inject 2 wrong beliefs u,v cùng lúc), I_uv = interaction term. Đọc dấu từ task structure trước: unit lost khi BẤT KỲ belief sai (series) → supermodular (damage overlaps); unit lost chỉ khi TẤT CẢ sai (parallel/redundancy) → submodular (damage compounds).
3. Thu thập error statistics của module: q_u trên mỗi belief, và measured dependence Δ_uv từ module's outputs thực tế (clone/public/mixed team).
4. Tính gate: B̂ = b0 + Σ_u q_u c_u + Σ_{u<v} (q_u q_v + λ Δ_uv) I_uv với λ=1. Act iff B̂ > 0; nếu B̂ ≤ 0 → defer về passive belief-free policy.
5. Check error load: mean wrong beliefs/episode > 4 → gate (order-2) không còn reliable; hand to direct measurement (A/B test trên estimation half, approve chỉ khi one-sided 95% lower bound > 0).
6. Validate: so sánh gate decision với direct measurement trên held-out episodes; theo dõi false approvals (approve harmful) — target 0 significant FA; deferrals là price phải trả.
7. Đối với redundant teams (nhiều observers): tính n_eff = ln Pr[all wrong]/ln E p_t — nếu n_eff gần 1 (errors shared blind spots), redundancy từ copies là ảo; diversify models hoặc defer trên unread targets.

## Output mong đợi
- Go/no-go decision per deployment cell với measured regret ~0.02 (vs accuracy rule 0.056, 3.2 false approvals); 0 significant false approvals trên 20 splits; recover beneficial deployments accuracy reject (7 classifiers: regret 0.004 vs 0.479) và catch harmful deployments accuracy approve (Bayesian module: FA* 17/20 splits cho accuracy, 1 cho gate).
- Break-even threshold a*(h) per harm level để biết accuracy cần đạt bao nhiêu mới justify acting.

## Ví dụ áp dụng
- Solopreneur chạy 3-agent content moderation: agent A đọc intent user, agent B action dựa trên đọc đó. Bước 1: inject wrong intent vào 100 episodes, đo cost 1 wrong moderation (false ban = user churn, c_u). Bước 2: các moderation decision là parallel (only all wrong → harm) hay series (any wrong → harm)? Bước 3: đo q_u, Δ_uv từ logs. Bước 4: B̂ ≤ 0 → defer về rule-based passive policy cho đến khi module tốt hơn. Expected: gate tránh được các deployment mà accuracy (0.8) vẫn approve nhưng shared errors compound harm.

## Gotchas
- Accuracy threshold calibrated trên independent errors fail theo hướng dự đoán: too strict khi damage overlaps (reject beneficial), too lenient khi damage compounds (approve harmful) — luôn xác định series/parallel structure trước.
- Copies của 1 model KHÔNG phải n independent observers: 3 Opus 5.5 copies worth 1.11 independent (all-wrong 9% vs 0.15%); dùng mixed models (4 Claude models joint misread 7.5% vs 9.0% Opus clones) hoặc accept deferral.
- Gate là second-order: modules với nhiều coherent errors cùng lúc (Haiku task assignment, ~8 errors/episode trong coherent blocks) bị gate defer sai — check error load, nếu > 4 thì direct measurement.
- Shared default answers (ví dụ convention "A" listed first) làm joint failure cao trên unhinted targets — relabel/rotate defaults hoặc force diverse sampling.
- Gate cần simulator; nếu không inject beliefs được, fallback là safety test (A/B + 95% bound) — tốn episodes của module.
- Max reasoning effort không cứu redundancy: Opus 5.5 13× tokens, accuracy không đổi (0.869), n_eff 1.10 vs 1.11 — đừng confuse compute với independence.
