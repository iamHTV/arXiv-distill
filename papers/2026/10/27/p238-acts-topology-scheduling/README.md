# [2610.25851] ACTS: Role-Aware Communication Topology Scheduling cho LLM Multi-Agent

## Problem
- Prior work có 3 họ đều yếu: (1) static topology (LLM-Debate, AutoGen, MetaGPT, LangGraph...) broadcast mọi round dù communication có ích hay không → token overhead exponential; (2) task-adaptive topology (G-Designer, TopoDIM...) xác định đồ thị TRƯỚC khi execute → link cố định, không theo evolving execution state; (3) MARL-based (Agent Q-Mix) partner selection KHÔNG condition on agent role hay evolving local state, mixer QMIX không encode directed incoming/outgoing neighborhood → credit assignment không topology-aware. Gap: chưa ai jointly learn (a) round-wise communication mode, (b) directed partner selection role-aware, (c) topology-conditioned team value evaluation.

## Contribution
- ACTS (Adaptive Communication Topology Scheduling) under CTDE (Centralized Training Decentralized Execution — huấn luyện tập trung, execute phi tập trung): dual-attention design.
- Role-conditioned Relational Attention: chọn variable-cardinality directed partner sets từ role embedding + evolving local states (α_ij ≠ α_ji — directional).
- Topological Attention Mixer: embed realized directed topology vào team value decomposition, utility weights condition on global state + in/out neighborhoods → topology-aware TD credit assignment, bảo toàn IGM (Individual-Global-Max) consistency → decentralized greedy execution valid.

## Method (tóm tắt cốt lõi)
- Đồ thị directed G_t=(I,E_t), G_1 = complete graph no self-loops. 6 communication modes: off, solo, broadcast, attn-broadcast, receive, attn-receive; agent chọn a_off/a_solo → rời eligible set (Eq. 1); attn-broadcast/receive retain edge khi α score > mean eligible threshold ᾱ_out/ᾱ_in (Eq. 6); edge (i,j) tồn tại iff j∈S_i ∨ i∈R_j (Eq. 7).
- Recurrent: h_t^i = GRU(GNN(o_t^i, e_ρ(ρ_i), G_t), h_{t−1}^i) (Eq. 3) — role embedding e_ρ gắn vào observation.
- Relational attention (Eq. 4–5): α_ij = softmax(W_Q h_i)ᵀ(W_K h_j)/√d_rel directional; ξ_i = h_i + Σα_ij W_V h_j; a_i = argmax Q(ξ_i, a).
- Topological mixer (Eq. 9–11): aggregate in/out neighborhoods m_{i,r}; topology key z_i = Φ(h_i ∥ e_ρ ∥ m_in ∥ m_out), global state s_t là query → head weights w_{i,h}=|[f_w(s_t)]_h| (nonnegative) + offset b_t; Q_tot = b_t + Σ_h w_h·(Σ_i λ_{i,h} Q_i); ∂Q_tot/∂Q_i = Σ_h w_h λ_{i,h} ≥ 0 → monotonic, IGM (Eq. 12).
- Objective (Eq. 2): max E[w_task·R_task(τ) − w_tok·min(Σc_tok/B, 1)] — token penalty clamp ở scale B. TD loss Eq. 13–14; backbone LLM FROZEN; topology transition excluded khỏi gradient; replay buffer; target greedy từ Q⁻ network.

## Key Findings
- 9 benchmarks 4 domains: code (LiveCodeBench v6, HumanEval), multiple-choice reasoning (MMLU-Pro + HLE first 250), multi-hop QA (HotpotQA), competition math (AIME 2025/2026, HMMT 2025, Beyond-AIME). 2 frozen backbones GPT-OSS-120B + DeepSeek-V4-Flash; 3 role agents + answer-aggregation node; 3 seeds.
- ACTS avg accuracy cao nhất cả 2 backbone: 75,01% (GPT-OSS-120B) và 69,43% (DeepSeek-V4-Flash) — vượt Agent Q-Mix +3,18 / +6,19 point; best hoặc tied-best mọi benchmark.
- Token: 5,97k / 4,03k per-sample (GPT-OSS-120B / DeepSeek-V4-Flash) → giảm 15,42% / 13,84% vs Agent Q-Mix (~7,06k / ~4,68k); Pareto-optimal cả 4 panel (2 backbone × 2 task IG regimes).
- Single-agent prompting rẻ hơn nhưng −27 point accuracy trên HotpotQA (GPT-OSS-120B); trên HLE (IG≈0) ACTS ≈ single-agent → biết khi nào KHÔNG communicate.
- IG (information gain — độ tăng thông tin) threshold x=2/n: HLE null IG; HMMT null IG với DeepSeek-V4-Flash (limited capacity); HotpotQA + contest math positive IG.
- Ablation (Table 2 clean): mixer→QMIX: 71,83%/7,41k (GPT-OSS-120B), 63,24%/4,96k — degradation mạnh nhất; routing→fixed partners: 72,50%/8,10k, 66,10%/6,20k (overhead lớn nhất); bỏ role embedding (giữ role prompts): 73,40%/6,80k, 67,10%/4,60k. Full ACTS 75,01%/5,97k, 69,43%/4,03k.
- Action distribution (DeepSeek-V4-Flash): high-IG HotpotQA off 4,2% broadcast 22,7%; near-zero-IG HLE off 21,3%, broadcast 12,1%, attn-broadcast 6,4%, attn-receive dominant 28,3% (pull-based retrieval).

## Actionable Insights
- Đừng broadcast mặc định trong team agent: fixed partner routing tệ nhất (72,50% + 8,10k tokens vs ACTS 75,01% + 5,97k). Ví dụ: team viết-bài (writer/editor/fact-checker) chỉ route critique đến agent role phù hợp với section yếu, không debate full-mesh.
- Học khi nào KHÔNG communicate: mode off/solo + early termination khi majority inactive (off 4,2%→21,3% trên task IG≈0). Ví dụ: trước khi deploy multi-agent, test Δaccuracy single vs team trên sample task của bạn — nếu Δ < 2/n noise threshold → skip team, tiết kiệm token ở accuracy gần như nhau (đẳng cấp HLE).
- Pull beats push trên task signal thấp: attn-receive dominant (28,3%) trên HLE — agent HỎI info thay vì broadcast. Ví dụ: agent research tóm tắt chỉ query agent khác on-demand, không push full context cho tất cả.
- Credit agent theo neighborhood directed (in/out), không theo participation: mixer topology-aware là component mạnh nhất (bỏ → −3,18pp accuracy + 24% token). Ví dụ: review team thủ công, weight agent bằng "message của nó thay đổi gì downstream" chứ không phải "nó đã nói nhiều".
- Token budget là objective hạng 1: penalty token clamp B (min(Σ/B,1)) → accuracy UP token DOWN 13,8–15,4%. Ví dụ: đặt hard token cap/workflow, optimize accuracy-per-token, không raw accuracy.

## Assumptions & Limitations
- Điều kiện: scheduler trained riêng per benchmark/task distribution (generalization cross-task chưa chứng minh); team size cố định N=3 + 1 aggregation node; chỉ 2 backbones (120B + V4-Flash); backbone LLM frozen nên scheduler overhead (GNN+GRU+attention) không đổi — nhưng training cost (MARL, replay buffer, LLM calls during train) KHÔNG nằm trong 5,97k token (chỉ per-sample inference).
- Paper KHÔNG có dedicated limitations section; kết luận chỉ claim benefit. [MY OWN]: IG framework giả định agents đóng góp complementary evidence — task đồng nhất (agents cùng knowledge) → null IG, team vô nghĩa; scheduler cần labeled task reward (accuracy) → không apply được workflow không có ground truth rõ ràng (creative/content subjective); code availability không stated (chỉ project website).

## Metadata
- 2026, Haibin Li, Wenya Yu (equal contribution), Xuefeng Jiang, Jia Li, Xiao Han, Shuai Su, Wei Wei (Beihang University, Nanyang Technological University, University of Chinese Academy of Sciences), cs.MA, https://arxiv.org/abs/2610.25851, project: https://acts-mas.github.io/ACTS/, citation count: [NOT FOUND]
