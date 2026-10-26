# [2609.18283] Where Should Agents Live? — agentic-eCAL: Energy-Memory Characterization cho Agentic AI Edge-Cloud

## Problem
- Prior work (eCAL gốc, single-model metrics) evaluate isolated single-model inference hoặc overlook multi-agent execution graph entirely → operator KHÔNG có model foundational để biết: distributed agent communication có tốn meaningful energy không, và agent team nên reside ở tier nào (edge/cloud). 3 property làm energy accounting khác single inference: (a) model off-the-shelf → embodied (pre-training) energy shared; (b) unit of work là workflow không phải inference — transcript tích lũy → token volume super-linear theo steps; (c) heterogeneous components (tool Etool, vector retrieval Eret, 7-layer OSI transmission Etx).

## Contribution
- agentic-eCAL: generalize eCAL (energy cost of AI lifecycle) sang directed multi-agent workflow — per-bit metric [J/b]: (E_W + γe(E_emb+E_emb,ret))/B_useful; reduction về eCAL inference đơn khi K=1, co-located, no tool/retrieval.
- Two-rate closed-form single-call energy model: E_call ≈ c_pre·p_in + c_dec(b)·p_out — prefill compute-bound (batch-independent), decode memory-bandwidth-bound (amortize weights trên batch b, KV-cache floor c_0).
- Empirical validation NVML-metered A100/H100 vLLM: 270 configs/model (Qwen2.5-7B, Llama-3.1-8B), 2–30 agents, batch 2–256; R²=0.996, MAPE ~10–12%.

## Method (tóm tắt cốt lõi)
- Workflow energy: E_W = (1+γ_v)[ΣE_call + ΣE_tool + ΣE_ret + E_tx] (γ_v = virtualization/orchestration overhead ~10%); memory feasibility per site: βN_params + γΣc_a ≤ M_u (β=2 bytes/param, γ = KV bytes/token).
- c_dec(b) = a_dec/b + c_0; fitted Qwen2.5-7B a_dec=3.2 c_0=0.02 J/token, Llama-3.1-8B 3.3/0.06; c_pre ≈ 0.02–0.03 J/token (η_pre 0.74–0.85). Crossover: call prefill-dominated khi p_in/p_out > c_dec(b)/c_pre → production batch crossing → workflow energy scales K^a, 1≤a≤2 (small batch decode-bound a→1; large batch prefill-bound a→2).
- History-carrying loop: p_in^(k) ≈ p_sys + s·k → Σp_in quadratic sK²/2, Σp_out linear sK; APC (automatic prefix caching) co-located giảm về O(K), distributed microservices re-prefill full transcript.
- Retrieval E_ret = βN_emb·p_q·p_emb/(η_emb·Π_emb) + α_idx·d_emb·log(M_vec); context 2K→10K tokens raises energy/token ~3× (70B).
- OSI 7-layer E_tx: protocol overhead 100–200%, HARQ retransmission 5G cell-edge R≈1.5–2.0; bearers: 5G RAN ε≈10⁻⁶, metro/fixed 10⁻⁷, optical 10⁻⁸ J/b.
- 8 orchestration topologies (Star, Persona-Star, Proposer-Critic, Tournament, Tree, Chain, Cascading-Chain, Diamond): summed prefill = N·p_0 + E·τ — chỉ edge count E matter, shape không; 6 architecture E≈N−1, Diamond E≈1.5N, Cascading-Chain E≈5N.
- Hand-off protocol (K=3, 4-agent workflow): transcript 0.33 Mbit/session vs increment 0.051 (6.5× less) vs summary 0.079 vs KV-cache migration 18.9 Gbit (cache 131 kB/token vs token 17 bits) → dynamic range 3.7×10⁵ (protocol) vs 4.8× (architecture) vs ~10³ (bearer). Parity intensity ε* text >3×10⁻³ J/b (ko bearer deployed nào reach); KV migration ε* = 5.1×10⁻⁸ J/b by K=6 → cache effectively non-transportable.

## Key Findings
- Inter-agent text transport <0.25% workflow energy (E_tx/E_prefill ≈ 1/496 cho 2,700-token hand-off qua 5G); 1,290 tokens crossing boundaries cost 8.9 mJ metro → 0.52 J loaded edge cell = 0.003–0.186% E_W at b=64. Dominant cost of distribution = additional inference + context processing induced by communication, KHÔNG phải truyền text.
- History carry K=6: +32.8% energy Qwen2.5-7B (89 J vs 67 J), +21.7% Llama-3.1-8B (185 vs 152 J); Llama ~2× Qwen energy (c_0 0.06 vs 0.02; γ 131 vs 56 kB/token).
- Batching: −38.1% energy at N=2 (130 vs 210 J) nhưng chỉ −15.4% at N=30 (4,400 vs 5,200 J) — batch amortization không overcome quadratic prefill explosion của dense team; exponent a: Qwen 1.10→1.42, Llama 1.02→1.17 (b 2→256).
- Placement governed by MEMORY: ≥64GB host all 4 weight classes (incl 4-bit 70B); concurrent N=10 sessions 1–2 (8GB Orin) → 59 (A100); within 8–16GB class varies 16× — GPT-OSS-20B (γ=48 kB/token) 112 sessions, Qwen2.5-7B (56) 87, OLMo-2-7B (512) 7 → binding constraint = KV width γ, không phải weights.
- 4-agent RAG case (planner→retriever→analyst→writer, Llama-3 8B): 4,990 prompt vs 1,020 generated tokens (ratio 4.9), transcript 56% writer prompt; retriever least efficient 0.034 J/bit vs 0.0116–0.0123 (2.8×) at b=64; workflow 0.0162 J/bit vs calls 0.0146.
- ETSI ZSM infra-repair benchmark (k3s edge, 24 incidents, 60 min/50 turns, ≥3 runs): Qwen3.5-9B energy 257.0–1029.2 kJ/run (4.0×), score 50.0–64.6%; Single 61.7%, chỉ P+R+W+V beat (64.6%) tốn 2.9× energy; kJ/success Single 17.4 vs multi 29.0–79.2. Qwen2.5-7B: Single 9.2%, multi-agent 0.4–4.6% WORSE dù ≤2611.1 kJ/run; kJ/success 49.7 vs 320.0–5222.3 (lên đến 23.9× energy, 4.0× với 9B). PS+V: score 45.8→59.7%, cost 51.5→68.4 kJ; PS cost 31.2→79.2 kJ mà score ~constant 1→5 proposers.
- Amortization: embodied Llama-3 8B 0.91 GWh (1.3M H100-hours) dominate đến G≈1.2×10¹⁰ invocations (20–60× BLOOMz parity 2–6×10⁸); Llama-3 70B parity tại 0.66× invocations của 8B (pre-training energy chỉ +4.9× 8B→70B).

## Actionable Insights
- Placement quyết bởi VRAM fit (weights + KV cache per session), KHÔNG bandwidth: text hand-off <0.25% energy → đừng optimize network location; optimize memory density. Ví dụ: chọn host agent team theo γ (KV kB/token) × concurrent sessions budget — GPT-OSS-20B host được 112 sessions vs OLMo-2-7B 7 trên cùng GPU.
- Bound context growth trong multi-step pipeline: transcript carry quadratic K², K=6 tốn +32.8%; hand-off increment (0.051 Mbit) hoặc summary (0.079) thay full transcript (0.33 Mbit, 30× growth K=1→6). Ví dụ: agent chain mỗi bước chỉ gửi diff + 200-token summary thay vì full history.
- Keep teams small + sparse coupling: all-to-all Θ(N²) prefill; N=30 batching chỉ saves 15.4%; independent agents collapse linear. Ví dụ: thay 30-agent debate (32–158× single call), dùng sequential chain E≈N−1 edges — cost như nhau mà energy thấp hơn bậc.
- Multi-agent KHÔNG tự better: benchmark kJ/solved task trước khi adopt — single agent beat most multi topologies trên Infra-Bench (Single 61.7% vs best-multi 64.6% nhưng 2.9× energy; 7B single BETTER 9.2% vs 0.4–4.6%). Ví dụ: trước khi mua multi-agent orchestration, đo cost/solved-task của 1 agent ReAct baseline.
- RAG retrieval là cost center ẩn: retriever 2.8× cost/bit vs neighbors (prefill 2,000 tokens để emit 120); context +10K tokens ~3× energy/token (70B). Ví dụ: giới hạn retrieved chunks, reuse prefix cache (TTFT −4×, tuned RAG −60%).

## Assumptions & Limitations
- Phải calibrate coefficients trên GPU thực (NVML metering); datasheet BHBM cho c_dec lower bound (serving stack ~70% peak bandwidth) → magnitude error ~1/3, form đúng.
- Paper thừa nhận: prefill giả sử full prefix (conservative upper bound — APC/RadixAttention cắt TTFT 4×); MoE phải dùng N_act (active routed params) không phải N_params; calibration A100 PagedAttention fragmentation — FP8/FP4 architecture mới sẽ shift roofline; embodied G hard tracking cho redistributed open-weight models.
- [MY OWN] Benchmark task domain hẹp (kubernetes infra repair 24 incidents) — generalization sang content/marketing workflow chưa đo; token estimates từ stipulation (Fig. 4 token budgets stipulated, không measured); embedding/tool energy analytical không metered directly.

## Metadata
- 2026, Jožef Stefan Institute (Carolina Fortuna, Vid Hanžel, Tim Strnad, Blaž Bertalanič), submitted IEEE JSAC Special Issue Agentic AI, cs.AI, https://arxiv.org/abs/2609.18283, code: https://github.com/sensorlab/a-eCAL (upon acceptance), citation count: [NOT FOUND]
