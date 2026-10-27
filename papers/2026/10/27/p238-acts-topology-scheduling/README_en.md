# [2610.25851] ACTS: Role-Aware Communication Topology Scheduling for Efficient LLM Multi-Agent Collaboration

## Problem
- Prior topology-scheduling methods fall into three weak families: (1) STATIC topologies (LLM-Debate, AutoGen, MetaGPT, ChatDev, LangGraph) broadcast every round regardless of usefulness → exponential token overhead; (2) TASK-ADAPTIVE topologies (G-Designer, TopoDIM, MaAS) fix the complete graph before execution — directed links remain fixed during interaction and cannot adapt to evolving local states; (3) MARL-based scheduling (Agent Q-Mix) does not condition partner selection on agent roles or evolving states, and its QMIX mixer does not encode realized directed incoming/outgoing neighborhoods → topology-unaware credit assignment. Gap: no prior method jointly learns (a) round-wise communication modes, (b) role-aware directed partner selection, and (c) topology-conditioned team-value evaluation.

## Contribution
- ACTS (Adaptive Communication Topology Scheduling) under CTDE (Centralized Training with Decentralized Execution): a dual-attention design.
- Role-conditioned Relational Attention: selects variable-cardinality directed partner sets from role embeddings and evolving local states (directional: α_ij ≠ α_ji in general).
- Topological Attention Mixer: embeds the realized directed topology into team value decomposition — utility weights conditioned on the global state and on incoming/outgoing neighborhoods → topology-aware TD (temporal-difference) credit assignment; preserves IGM (Individual-Global-Max) consistency under a fixed pre-decision context → valid decentralized greedy execution.

## Method (core)
- Directed graph G_t = (I, E_t); G_1 initialized as the complete directed graph without self-loops. Six communication modes: off, solo, broadcast, attn-broadcast, receive, attn-receive; choosing off/solo removes an agent from the communication-eligible set (Eq. 1); attn-broadcast/retention rule keeps edge i→j when α_ij exceeds the mean threshold ᾱ_out over eligible candidates (symmetric ᾱ_in for attn-receive) (Eq. 6); edge (i,j) exists iff j∈S_i or i∈R_j (Eq. 7).
- Recurrent state: h_t^i = GRU(GNN(o_t^i, e_ρ(ρ_i), G_t), h_{t−1}^i) — role embedding e_ρ fused into observations (Eq. 3).
- Relational attention (Eq. 4–5): α_ij = softmax_{j≠i}(W_Q h_i)ᵀ(W_K h_j)/√d_rel (directional); feature refinement ξ_i = h_i + Σ_j α_ij W_V h_j; mode choice a_i = argmax_a Q(ξ_i, a).
- Topological mixer (Eq. 9–11): aggregate in/out neighborhoods m_{i,r}; topology key z_i = Φ(h_i ∥ e_ρ(ρ_i) ∥ m_{i,in} ∥ m_{i,out}) (used only by the centralized mixer); global state s_t is the query; nonnegative per-head weights w_{i,h} = |[f_w(s_t)]_h| and offset b_t = V_b(s_t); Q_tot = b_t + Σ_h w_h·(Σ_i λ_{i,h} Q_i^top); ∂Q_tot/∂Q_i = Σ_h w_h λ_{i,h} ≥ 0 → monotonic mixing, IGM inclusion (equality when logits finite and Σw > 0) (Eq. 12).
- Objective (Eq. 2): max_π E[w_task·R_task(τ) − w_tok·min(Σc_tok/B, 1)] — token penalty clamped at scale B. TD target y_t = r_t + γQ⁻_tot(α*_{t+1}) with greedy targets from the target network; TD loss Eq. 13–14; backbone LLMs FROZEN; discrete topology transitions excluded from gradients; replay buffer (D) centralized training.

## Key Findings
- 9 benchmarks across 4 domains: code generation (LiveCodeBench v6, HumanEval), multiple-choice reasoning (MMLU-Pro, first 250 of Humanity's Last Exam), multi-hop QA (HotpotQA), competition math (AIME 2025/2026, HMMT 2025, Beyond-AIME). Frozen backbones GPT-OSS-120B and DeepSeek-V4-Flash; each task = 3 role-conditioned agents + a final answer-aggregation node; results averaged over 3 random seeds.
- ACTS achieves the highest macro-average accuracy on both backbones: 75.01% (GPT-OSS-120B) and 69.43% (DeepSeek-V4-Flash) — exceeding Agent Q-Mix by 3.18 and 6.19 points — and best or tied-best on every benchmark.
- Token usage: 5.97k / 4.03k per sample (×10³ tokens) → 15.42% / 13.84% reduction vs Agent Q-Mix (~7.06k / ~4.68k implied); Pareto-optimal in all four panels (2 backbones × 2 IG regimes).
- Single-agent prompting is cheaper but costs ~27 points of accuracy on HotpotQA (GPT-OSS-120B); on HLE (IG ≈ 0) ACTS matches single-agent performance — it learns when communication is NOT warranted.
- Information gain (IG) analysis: uplift below the sampling-noise threshold x = 2/n yields null IG — HLE always null; HMMT null with DeepSeek-V4-Flash (limited capacity); HotpotQA and contest math show positive IG (complementary cross-entity evidence, divergent solution paths).
- Ablations (Table 2): topological mixer → QMIX: 71.83% / 7.41k tokens (GPT-OSS-120B) and 63.24% / 4.96k — strongest degradation; learned routing → fixed partners: 72.50% / 8.10k and 66.10% / 6.20k — largest overhead; removing role embeddings (keeping role-specific prompts): 73.40% / 6.80k and 67.10% / 4.60k. Full ACTS: 75.01% / 5.97k and 69.43% / 4.03k.
- Learned action distribution (DeepSeek-V4-Flash): high-IG HotpotQA — off 4.2%, broadcast 22.7%; near-zero-IG HLE — off rises to 21.3%, broadcast drops to 12.1%, attn-broadcast 6.4%, attn-receive dominates at 28.3% (pull-based retrieval).

## Actionable Insights
- Don't broadcast by default: fixed partner routing is the worst ablated variant (72.50% accuracy, 8.10k tokens vs ACTS 75.01% / 5.97k). Example: in a writer/editor/fact-checker team, route critique only to the agent whose role matches the section's weakness instead of full-mesh debate.
- Learn when NOT to communicate: off/solo modes plus early termination once a majority of agents deactivate (off share rises 4.2%→21.3% on zero-IG tasks). Example: before deploying a multi-agent team, measure single-vs-team Δaccuracy on a sample of your own tasks — if Δ < 2/n noise threshold, skip the team entirely (near-equal accuracy, far fewer tokens).
- Pull beats push on low-signal tasks: attn-receive dominates (28.3%) on HLE — agents ASK for information rather than broadcasting it. Example: a research/summarization agent queries peers on demand instead of pushing full context to everyone.
- Credit agents by directed neighborhood (in/out), not participation: the topology-aware mixer is the strongest component (removing it costs 3.18 pp accuracy and +24% tokens). Example: when manually reviewing an agent team, weight each agent by what its messages actually changed downstream, not by how much it spoke.
- Token budget as a first-class objective: the clamped token penalty (min(Σ/B, 1)) yields accuracy UP and tokens DOWN 13.8–15.4%. Example: set a hard per-workflow token cap and optimize accuracy-per-token rather than raw accuracy.

## Assumptions & Limitations
- Conditions: scheduler trained per benchmark/task distribution (cross-task generalization unproven); fixed team size N=3 + 1 aggregation node; only 2 backbones tested; training cost (MARL + LLM calls during training) is NOT included in the reported 5.97k (per-sample inference tokens only).
- Paper states no dedicated limitations section (conclusion claims only benefits). [MY OWN] IG framework assumes agents contribute complementary evidence — homogeneous-knowledge tasks yield null IG where the team is pointless; the scheduler needs a labeled task reward (accuracy) → unfit for subjective workflows without ground truth (creative/content judgment); code availability not stated (project website only).

## Metadata
- 2026, Haibin Li & Wenya Yu (equal contribution), Xuefeng Jiang, Jia Li, Xiao Han, Shuai Su, Wei Wei (Beihang University, Nanyang Technological University, University of Chinese Academy of Sciences), cs.MA, https://arxiv.org/abs/2610.25851, project: https://acts-mas.github.io/ACTS/, citation count: [NOT FOUND]
