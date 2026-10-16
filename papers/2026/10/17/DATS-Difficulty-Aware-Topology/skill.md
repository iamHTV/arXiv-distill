# Skill: Dats — Difficulty-Aware Topology Router (chọn multi-agent topology per problem)
Source: 2609.13890
Type: framework / routing-workflow

## Khi nào dùng skill này
- Multi-agent system với ≥3 pipeline templates (single call, chain, mesh, hierarchical) và budget giới hạn
- Cần so sánh/s deployed cost-aware routers một cách công bằng (budget-matched protocol)
- Collaboration benefit varies with problem difficulty — easy problems không cần multi-agent, hard problems mới đáng trả 5–10× tokens

Tình huống KHÔNG nên dùng: chỉ có 1 topology; mọi problem đều cùng difficulty; latency/Worst-case cost là constraint chính (protocol chỉ equalise expected monetary spend).

## Input cần có
- Problem statements + cached outcomes (pass/fail) cho MỌI topology trong catalogue trên một benchmark representative (paper: 614 problems × 5 topologies × 4 backbones = 12,280 executions, ~$1,807)
- Cost table c_t (tokens/USD per problem per topology — measured once, reuse; stable within 3% across backbones)
- Budget B dưới dạng fraction of always-hierarchical (most expensive fixed topology) cost
- 39-feature extractor: lexical (5), structural (4), complexity (3), difficulty rating (1), TF-IDF SVD (16), algorithmic one-hot (10 categories, keyword vote)

## Các bước thực hiện
1. Cache outcomes: chạy full grid (mỗi problem × mỗi topology), ghi pass/fail + token counts. KHÔNG retrain agents — predictor không nhận gradient.
2. Extract 39 features per problem (feature extraction <1ms/problem, linear in statement length).
3. Train topology-graph GNN: shared trunk 39→d (affine+ReLU); node init h^0_t = ReLU(W_0[z ∥ e_t] + b_0) với e_t = (agent count, edge count, diameter, mean degree); message passing 2 rounds với tied W_self, W_nbr (mean over neighbors); per-node sigmoid readout. Loss = mean BCE over 5 heads (targets là per-topology outcomes, KHÔNG phải single label). Adam lr 1e-3, early stopping, <30s CPU. 13.7K params.
4. Calibrate λ bằng bisection trên 3-fold split của training fold: B target fraction of always-hierarchical cost, tolerance 0.5% hoặc 60 iterations (paper: λ ≈ 0.052–0.065; 21.4 steps trung bình). KHÔNG tune λ cho accuracy — λ là budget parameter.
5. Inference: predict ŝ_t(x) cho 5 topologies → τ*(x) = argmax_t [ŝ_t(x) − λĉ_t] với ĉ_t = c_t/max c → execute CHỈ topology được chọn. Tại λ=0.06, upgrade Single→HRM phải buy ≥5.4 points predicted success.
6. Verify realised spend out of fold (tolerance 0.4pp) và báo USD/problem + % of reference budget bên cạnh accuracy. Compare accuracies only within matched group; fixed topologies/oracle report separately như frontier locators.

## Output mong đợ
- Per-problem topology assignment + predicted success probabilities (ECE ~0.027, Brier ~0.172, mild under-confidence ở 0.4–0.7 band).
- Budget-matched accuracy: paper 77.69% pass@1 tại 40% always-hierarchical cost ($0.377/problem), +4.07 over always-HRM, +6.03 over direct classification, +9.12 over Random.
- Routing distribution: ~49% Single, ~13% HRM, 38% Chain/mid (suite-dependent: 80% HumanEval+ → Single; 47% APPS-Competition → HRM).
- Ví dụ: coding agent 5 templates, budget 40% HRM → Dats solves 477/614 vs 452 always-HRM, tiết kiệm 60% spend.

## Ví dụ áp dụ
- Deploy coding agent trên 2 benchmark levels (easy: HumanEval+-like; hard: competition-like): cache 5 topologies × 100 problems each, train Dats, bisection λ to 40% budget → easy problems 80% single call, hard graph/DP problems 49% HRM. Đổi budget sang 60%: chỉ cần bisection lại λ (KHÔNG retrain) — factorisation predict-then-optimize cho phép recalibrate cost penalty là single scalar.

## Gotchas
- KHÔNG dùng direct five-way classification thay cho predict-then-optimize (−6.03 points): label "topology that solved it" ambiguous khi nhiều topologies succeed (38% problems), undefined khi none succeed.
- KHÔNG dùng flat multi-label head (5 independent sigmoids) thay cho topology-graph GNN (−1.66 points): topologies form connectivity order — solvability inherits the order almost monotonically; graph head biết structure đó với FEWER parameters (13.7K).
- KHÔNG compare routers với shared λ ("fair" comparison) — λ multiplies each method's own score scale → realised spend spreads 21.6pp và rankings reverse (RandomForest first ở shared λ, Dats first khi calibrated, gap 3.42 points). Luôn calibrate + báo realised spend.
- KHÔNG fine-tune pretrained encoders (CodeBERT/GraphCodeBERT) cho representation — 125M params fine-tuned mua +0.49 points KHÔNG significant (p>0.35, seed SD 0.71). 39 hand-crafted features đủ.
- Transfer across backbones KHÔNG significant (p=0.318): routing policy transfers nhưng probability calibration shifts → recalibrate trên few hundred cached problems khi đổi backbone.
- LiveCodeBench-style contest problems: stylistically uniform statements đánh bại surface features (oracle gap 20 points) — cần features mạnh hơn cho contest regime.
- Protocol equalise expected spend, KHÔNG equalise latency/worst-case/variance — method meet budget bằng occasionally expensive topology là khác với method never does.
- Difficulty × category interaction là nơi signal sống: linear probe −3.75 points vì không express "hard graph problems need HRM while hard implementation problems do not".
