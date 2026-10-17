# Skill: Attention-Handoff Tax — Đo curve + handoff tax, chọn single vs multi-agent
Source: 2610.06069v1 (Attention Tax, Handoff Tax)
Type: evaluation-method (architecture selection rule)

## Khi nào dùng skill này
- Quyết định có nên split task thành multi-agent chain (decomposition) hay chạy 1 agent; hoặc chọn chunk size (số steps/subagent); hoặc chọn parallel sampling vs thinking longer ở equal budget.
- Task có dạng chain of steps với context tích lũy (ledger, tool chains, document processing pipelines, multi-hop research).
- KHÔNG nên dùng: task đơn call không tích lũy context; task có verifiable answer trực tiếp (code, arithmetic đơn giản); chưa chạy được single agent làm baseline.

## Input cần có
- Task definition: step structure, tokens added per step k, task statement size c0.
- Model + serving config cố định (budget b/step, temperature).
- Khoảng ~100–200 instances + ~1,000 calls budget cho measurement.
- (Tùy chọn) summary schema cho handoff notes.

## Các bước thực hiện
1. Đo in-task curve: chạy single agent (1 growing conversation) trên N instances ở các context-load bins (ví dụ 2k/8k/32k/64k tokens, pad bằng well-formed digit-free prose); record per-step failure rate theo load. CHÚ Ý: định nghĩa failure trước — arithmetic vs format cho curve khác nhau (pilot: flat 5.5% vs steep 29.5% trên cùng 1,000 calls).
2. Đo handoff tax theo Definition 1: trên pool riêng, chạy mỗi chunk 2 lần — (a) continue from history, (b) start from summary note; lấy curve term Σ[g(c0+|H|+ki) − g(c0+s+ki)] cộng lại → h = G_M − G_H + curve term. Lặp ở 2–3 note lengths (tax phải nonincreasing in s).
3. Fit curve: linear regime (g = g0 + λc) hoặc knee-shaped (hinge fit). Nếu flat trong phạm vi đo → single agent dominates (Corollary 1) — dừng, không cần decompose.
4. Tính crossover depth (linear regime): L* = max{2, ⌊2(h+λs)/(λk)⌋+1}. Task depth < L* → single agent; > L* → decomposed.
5. Chọn chunk size: m* ≈ √(2h/(λk)) (linear, h tính cả overhead writer ∆o). Curve knee-shaped: agents own đủ steps nằm DƯỚI knee; square-root law chỉ áp dụng past knee.
6. Chọn summary length: interior optimum tại −h′(s*) = λ — đừng dùng fixed-ratio compaction mù.
7. Parallel vs sequential (nếu task cho phép N samples/step): đo marginal failure ε_b và pairwise correlation ρ giữa samples; tính F_max = ρε(1−ε)/(ρε(1−ε)+(½−ε)²); nếu F_max < ε∞(c) (thinking floor) → parallel sampling thắng for large N tại equal budget.
8. Validate: chạy prediction (exp(−G) per instance, product form) so với observed success ở 2–3 depths; predictions nên miss ≤ ~9pp (hướng single agent thường hơi trên prediction vì failures cluster trên hard instances).

## Output mong đợi
- Decision rule cụ thể: single agent đến depth X, decomposed với chunk size m past đó; predicted success rates cho cả 2 systems ở depths cần triển khai; handoff tax theo nats với CI.

## Ví dụ áp dụng
- Solopreneur doc-processing pipeline: đo curve thấy failure 3% (<8k tokens) → 60% (>32k); đo handoff tax 0.03 nats với 300-token notes; k = 400 tokens/step, λ = 8×10⁻⁶/token, s = 300 → L* = max{2, ⌊2(0.03+0.0024)/0.0032⌋+1} = 21. Documents cần >21 steps processing → decompose với m ≈ √(2·0.03/0.0032) ≈ 4–5 steps/agent; ngắn hơn → 1 agent.

## Gotchas
- Failure definition là 1 phần của curve — arithmetic failure có thể flat trong khi format failure (missing ANSWER line) steep: 47/51 format failures ở 64k vẫn có đúng number. Lặp instruction cạnh question để flatten.
- Fee steps (hoặc step nào phụ thuộc state carried in) đo state chứ không phải step — loại khỏi curve fitting, nhưng vẫn đếm context growth của chúng.
- Product form overstates single agent's loss khi failures cluster trên hard ledgers — observed single agent thường cao hơn prediction vài points; đừng surprise.
- Handoff tax bootstrap CI có thể bao gồm negative (đo được [−0.11, 0.16] nats) — theo Assumption 4, project negative về 0.
- Under knee-shaped curve, chunk size KHÔNG phải square root — agents own steps under knee trước.
- Crossover prediction test được ở winning side (depths > L*); bản thân crossover depth cần thêm measurement nếu task depth nằm gần L*.
- Vote floor phụ thuộc toàn bộ mixing law, không chỉ ρ — (ε_b, ρ) chỉ cho bound, không phải floor chính xác; common-shock floor ρε là 1 example.
- Temperature + budget cố định ảnh hưởng curve — giữ nguyên serving config giữa measurement và production.
- Handoff note content là design choice: balance + open holds + last-12-transactions trong paper; schema khác → tax khác.
- Million-step ambitions (L=10⁶) cần per-step vote failure và handoff tax đều ~10⁻⁶ → phải pass FULL STATE, không phải summary (Corollary 4).
