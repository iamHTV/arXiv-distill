# Skill: Receiver-Relative Protocol Selector (Gain − Tax Communication Control)
Source: 2610.03769v1
Type: evaluation-method / workflow

## Khi nào dùng skill này
- Multi-agent workflow (workflow đa tác tử) có sender với context rộng + executor với local view hạn chế, và bạn cần chọn protocol truyền thông (skip / compress / raw / escalate / refresh) từng bước một.
- Cần tối ưu accuracy–cost frontier (biên độ chính xác–chi phí): tránh gửi message tốn kém khi receiver đã đủ context, hoặc gửi raw context khi compression đủ dùng.
- Tình huống KHÔNG nên dùng: single-agent (không có sender/receiver asymmetry); task không đo được artifact/action targets (không có hit_joint); không đủ budget để chạy paired RO/SF/MA calibration (mỗi step cần 3 protocol runs).

## Input cần có
- Task có acceptable artifact/action targets đo được (G_t = {(Z^art, Z^act)}) — labels KHÔNG expose cho sender/receiver/selector.
- Receiver fixed (model + prompt + parser + context window + tool interface), sender (model), message budget B (tokens).
- Paired RO/SF/MA calibration records (receiver-only / raw-context / bounded-message) chia theo instance_id, giữ receiver interface + action set cố định.
- Ước lượng: gain surrogate Â (clipped leading-token log-probability difference), action-level offset τ̂ (protocol burden + gain effects), local-sufficiency rate (từ held-out RO records), cost weights η_c, η_r (tune trên held-out split; paper dùng η_c = 10⁻⁴ trên raw token counts, η_r = 0 cho static one-step).

## Các bước thực hiện
1. **Calibrate offline:** chạy paired RO/SF/MA trên calibration set (paper: instance-disjoint, 5–40% records → accuracy 0.7368–0.7458). Trích action-level offset τ̂ cho mỗi protocol action; local-sufficiency rate cho early-skip branch. Cố định offsets, skip threshold, cost weights TRƯỚC evaluation.
2. **Tại mỗi step t,** đọc instance-level signals (local view X, burden proxy b, shared-state discrepancy D_t nếu có).
3. **Score 5 actions:** skip (RO endpoint), compress(B) (bounded message under budget B — evaluate bằng compression criterion ∆U = ∆τ_saved − I_omit − Λ_C), raw (full context — giữ vì Bayes-sufficient compression vẫn có thể fail), escalate(C') (stronger receiver trên compressed message — score bằng gain–tax comparison), refresh (shared-state resynchronization — score bằng residual propagation Prop 7: D_{t+1} = k_t + λ_t[D_t − q_t]_+).
4. **J_t(α) = A* − τ − η_c·c(α) − η_r·r_t(α)** — receiver-relative utility trừ immediate cost (chi phí tức thời) trừ future residual risk (rủi ro dư tương lai); chọn α* = argmax.
5. **Execute once** bằng cached candidate (paper: 5-action path refresh/skip/raw/compress/refresh caches real compress + refresh messages trước 9 receiver probes, cap 4 tokens).
6. **Early-skip gate:** nếu local-sufficiency rate cao (receiver RO accuracy đã ≥ crossover ~0.63), skip message trước khi gọi sender (ToolSandbox online: early-skip 1.000 accuracy, 919.4 tokens, 6.60 s/step vs always-send 0.8056, 3,085.4 tokens, 9.56 s).
7. **Monitor closure:** đo artifact accuracy h_a VÀ conditional action-conversion h_action riêng — nếu h_a cao mà h_action thấp (closure-dominated, e.g. GLM-5 0.741/0.545, MiniMax-M2.5 0.613/0.053), lỗi nằm ở action closure, không phải message content → sửa receiver interface/format, không phải sender.

## Output mong đợi
- Protocol decision per step với accuracy–cost tốt hơn always-skip lẫn always-send: ContextBench static selector 0.7367 accuracy tại 1,735 tokens/step (vs always-skip 0.6500/1,300 và always-send 0.7867/3,235.4) — recovers +8.67pp over always-skip với 46.4% fewer tokens than always-send.
- Biết regime (helpful/noisy/boundary) per receiver-interface: compression sign flips theo benchmark (ContextBench +0.14, ToolSandbox −0.24, BFCL −0.23, τ-bench 0.00).
- Sender-upgrade threshold b* (paper: 0.6289, CI [0.552, 0.706]) — biết khi nào stronger sender giúp vs hurt.

## Ví dụ áp dụng
- Solopreneur chạy pipeline: researcher agent (sender, context rộng) → writer agent (executor, local view). Calibrate trên 10 bài: writer RO accuracy 0.7 (> threshold 0.63) → early-skip: researcher KHÔNG gửi message, writer làm trực tiếp — tiết kiệm ~2.000 tokens/step. Với bài writer RO 0.4 (< threshold) → compress researcher findings thành 128-token brief theo template writer quen → +8–20pp accuracy.

## Gotchas
- Bayes-sufficient ≠ receiver-usable: message đúng nội dung nhưng surface form sai vẫn lỗi (strict-recoding −13.5pp τ-bench) — luôn format theo receiver interface, test fixed-message replay trước deploy.
- Stronger sender HURT khi receiver burden thấp (ToolSandbox −26.4pp) — đừng mặc định dùng model mạnh nhất làm planner.
- Selector không luôn thắng: τ-bench rewriting beat selector 0.139 vs 0.083 ở similar cost — keep raw/rewrite trong action set.
- Calibration tốn 3× runs (RO/SF/MA) — chỉ đáng khi workflow chạy nhiều steps; với pipeline ngắn, dùng early-skip gate theo RO accuracy đơn giản hơn.
- Truncation: gains không phải artifact của truncation (capped +10.64pp, uncapped +32.89pp) — nhưng vẫn giữ cả decision fields trong capped messages.
- Action closure errors (outputs chọn read khi action là edit — 40.8–94.0% wrong-action rates) cần fix ở receiver prompt/tool schema, KHÔNG phải message.
- η_r = 0 trong static ablation — với shared-state workflows (residual persists), phải charge future residual risk (η_r > 0) hoặc lỗi nhân về phía trước (Prop 7).
