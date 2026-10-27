# Skill: ACTS — Lập lịch topology giao tiếp role-aware cho team agent
Source: 2610.25851
Type: framework (multi-agent communication scheduling)

## Khi nào dùng skill này
- Bạn có team 3+ agent LLM (writer/editor/reviewer/researcher...) mà đang dùng full-mesh debate hoặc broadcast chaîne cố định → token cost cao, accuracy không tương xứng.
- Bạn muốn thiết kế "ai nói với ai, khi nào" theo role + state thay vì trò chuyện all-to-all mỗi round.
- Bạn đo lường cost-per-task của team agent và cần tối accuracy-per-token, không raw accuracy.

## Khi KHÔNG nên dùng
- Task single-agent đã đủ (IG≈0 — information gain null): team agent vô nghĩa, chỉ tốn token (HLE evidence: ACTS ≈ single-agent).
- Workflow không có measurable task reward (creative subjective, không ground truth) — scheduler cần labeled reward để train/validate.
- Team chỉ 2 agent hoặc N rất lớn (>10) — paper chỉ validate N=3; N lớn cần test lại.

## Input cần có
- N agents, mỗi agent 1 role ρ_i (job description rõ ràng: critic, researcher, writer...).
- Task class + measurable reward (accuracy / pass rate) để evaluate; sample 30–50 task để measure IG (Δaccuracy single vs team).
- Backbone LLM (frozen); budget token cap B per workflow; production API access.
- (Path A RL) infra MARL: replay buffer, GNN/GRU modules, target network — cần engineering effort.

## Các bước thực hiện
1. **Measure IG trước (gate)**: chạy single-agent vs full-team trên sample; ΔACC < 2/n (n = sample size) → task IG≈0 → DÙNG SINGLE AGENT, dừng. ΔACC lớn → team xứng đáng, tiếp.
2. **Định nghĩa 6 communication modes**: off (agent tắt, skip LLM call), solo (làm một mình), broadcast (gửi tất cả), attn-broadcast (gửi subset relevance cao), receive (nhận tất cả), attn-receive (pull subset relevance cao). Task mỗi agent mỗi round: chọn mode + partners.
3. **Build role embedding + relevance scores**: encode mỗi role thành vector (dùng backbone LLM embed role description); mỗi round tính directed relevance α_ij giữa agent i→j từ hidden state + role embedding (directional: α_ij ≠ α_ji). Threshold ᾱ = mean over eligible candidates → attn-* modes retain edges α > ᾱ. Eligible set loại agent đã chọn off/solo (Eq. 1).
4. **Path A (full ACTS, cần MARL)**: train scheduler CTDE — local Q network per agent (GRU state + GNN aggregate theo topology + relational attention), centralized topological mixer Q_tot = b_t + Σ_h w_h·Σ_i λ_{i,h}Q_i với weights từ global state + in/out neighborhood; objective w_task·R_task − w_tok·min(Σtoken/B, 1); replay buffer + TD target greedy; backbone frozen.
5. **Path B (heuristic zero-RL — cho solopreneur)**: skip training; dùng rule instantiation: (a) partner selection = attn threshold on α_ij computed từ role-affinity matrix (role pairs thường complement: critic↔writer, researcher↔writer high affinity; same-role pairs low); (b) mode policy from IG regime: high-IG task → broadcast/attn-broadcast cho phép; low-IG → attn-receive pull-based + off/solo allowed; (c) token penalty = hard cap B, abort round khi vượt; (d) early termination khi majority agents off/solo 2 consecutive rounds.
6. **Credit assignment theo topology**: khi đánh giá agent (manual hoặc automated), weight contribution by directed in/out neighborhood — agent i's credit ∝ Σ edges (i,j) sử dụng message i, KHÔNG count participation. (Evidence: topology mixer là component mạnh nhất — bỏ nó −3,18pp accuracy +24% token.)
7. **Early termination + monitoring**: track per-round token + action distribution; off share > ~20% → team đang correctly hạn chế communication; broadcast share cao trên low-IG task → cấu hình sai, re-run với threshold thấp hơn... đúng hơn: attn-receive để pull.
- **Evaluate Pareto**: plot accuracy vs token của single / static / adaptive / scheduled team; team chỉ được giữ nếu nằm trên Pareto frontier (≥ accuracy của static ở ≤ token của nó). Report token-per-solved-task và accuracy-per-token, không raw accuracy.

## Output mong đợi
- Communication schedule per round (edges + modes), token usage ≤ budget B, accuracy ≥ static baseline trên high-IG task, và near-single-agent cost trên low-IG task; table Pareto accuracy-vs-token xác nhận team xứng đáng.

## Ví dụ áp dụng
- Solopreneur content pipeline 3 agent (Researcher / Writer / Editor) trên task "viết blog so sánh 5 sản phẩm" (high-IG: multi-entity evidence): Researcher broadcast finding cho Writer; Editor attn-receive pulls chỉ section liên quan từ Writer + Researcher (không receive full); round 2 Researcher off (done), Writer solo polish, Editor attn-receive. Token ~12k vs full-mesh 3-round ~21k (−43%), accuracy giữ (Editor vẫn nhận đủ evidence). Trên task "định dạng lại 1 đoạn text" (low-IG): skip team → single Writer, tiết kiệm ~100% token team.

## Gotchas
- **IG gate bắt buộc**: deploying team trên IG≈0 task = waste (ACTS itself học về mức single-agent trên HLE) — luôn measure ΔACC single-vs-team BEFORE build scheduler.
- **Directional scores**: α_ij ≠ α_ji — "Writer gửi cho Editor" khác "Editor gửi cho Writer"; đừng dùng symmetric cosine similarity cho partner selection.
- **Fixed partners worst variant**: ablation (b) fixed partner routing = accuracy 72,50% + token 8,10k vs ACTS 75,01% + 5,97k — KHÔNG hardcode role-pair graph; role affinity chỉ là init heuristic ở Path B, phải recompute theo state mỗi round.
- **Token penalty clamp**: objective clamp B (min(Σ/B,1)) nghĩa penalty saturates — set B realistic (budget thật), kẻ cả scheduler "hợp tác" over-squeeze → quality drop.
- **Training cost excluded**: 5,97k token là INFERENCE only; Path A training (MARL + replay LLM calls) tốn tương đương nhiều round — chỉ đáng khi team chạy hàng nghìn task (amortize).
- **Aggregation node**: paper dùng final answer-aggregation node riêng (không trong 3 agents) — đội của bạn cần 1 aggregator cuối, không để agent tự kết luận riêng lẻ.
- **N=3 only**: kết quả chưa validate cho N>3; scaling cạnh Θ(N²) all-to-all vẫn là risk — cap N hoặc sparse coupling khi mở rộng.
- **Path B heuristic chưa được paper validate** — nó là instantiation rule của pattern ACTS, phải đo Pareto của bạn trước khi tin (Path A mới là paper result).
