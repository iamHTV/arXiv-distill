# Skill: Multi-Turn Tool-Using Agent với Evaluator Feedback Loop (cho alpha mining)
Source: 2610.15488v1 (AlphaPilot)
Type: framework (training + inference workflow)

## Khi nào dùng skill này
- Cần LLM agent tự tìm kiếm/đề xuất ứng viên (factor, rule, query, prompt) lặp lại nhiều turn, có công cụ đánh giá executable chạy được.
- Cần thích ứng theo ngữ cảnh thay đổi theo ngày/phiên (market regime, dữ liệu drift) thay vì search một lần.
- KHÔNG nên dùng khi: không có evaluator executable để feedback từng turn (chỉ có LLM judge — khi đó dùng loop prompt thông thường); bài toán chỉ cần 1 lần đề xuất (single-shot đủ).

## Input cần có
- DSL (ngữ pháp biểu thức) + operator set rõ ràng (ví dụ alpha mining: ts_delta, ts_corr, rank, delay).
- Dataset dạng bảng với rolling training window (AlphaPilot dùng daily A-share CSI300/CSI500, 3-year rolling).
- Executable evaluator tool: validate syntax, execute candidate, trả compact feedback (IC, RankIC, stability, error).
- Seed factor library (manifest) + market-regime description cho mỗi ngày.
- Infra RL: VERL (hoặc framework GRPO tương đương), backbone nhỏ (AlphaPilot dùng Qwen3-4B-Instruct-2507).

## Các bước thực hiện
1. Build daily context c_t = (q_t, S_t, O): viết market-regime description (natural language) cho từng ngày, gộp seed/carried-over factor manifest, liệt kê operator set hỗ trợ.
2. Cài factor_evaluator: kiểm tra DSL syntax → execute trên rolling training window → áp universe/tradability filters → trả feedback compact (expression, family, IC, RankIC, stability, error).
3. Chạy multi-turn rollout: policy quan sát context + compact memory (factor đã thử, pool state, feedback trước) → đề xuất B candidates/turn; lặp tối đa H_max turns (AlphaPilot: 40 assistant turns, 8 rollouts/prompt khi training).
4. Duy trì retained factor pool: filter sơ (loại invalid / coverage không đủ / single-factor score không dương) → fit NNLS/ridge-style meta-alpha weights trên recent segment (w≥0) → tính pool diagnostics từ cross-sectional ranks.
5. Train GRPO: reward = sigmoid-mapped future-window IC/RankIC + minimum-positive-factor completeness penalty; KHÔNG đưa auxiliary pool terms vào reward (chúng thuộc pool score).
6. Inference day-by-day: mỗi ngày search lại + update pool; combine recent-window NNLS/ridge weights; portfolio long-only top-K, 10 bps transaction costs.
7. Đánh giá 2 tầng: factor-level diagnostics (IC/RankIC/turn statistics) VÀ portfolio-level backtests (total return, Sharpe, MaxDD, excess vs equal-weight benchmark), 3-run means cho các phương pháp sinh stochastic.

## Output mong đợi
- Retained factor pool ngày nào cũng adapt được với regime mới; factor expression diễn giải được (ví dụ "1 -rank(ts_delta(close, 1))" score 0.380); portfolio metrics như AlphaPilot CSI300: 42.93% return, Sharpe 2.46, MaxDD -9.34%.

## Ví dụ áp dụng
- Solopreneur phân tích VN stock (HOSE): DSL 20 operator kỹ thuật, evaluator tính IC trên rolling 3-year HOSE data, train Qwen3-4B + GRPO 8 rollouts/prompt; mỗi ngày agent search lại factor pool theo regime description viết tay; kết hợp pool bằng NNLS weights → long-only top-10, 10 bps phí.

## Gotchas
- Reward proxy ≠ realized portfolio return: ablation cho thấy variant có IC/RankIC cao nhất (0.0419/0.0634) lại có return/Sharpe yếu nhất (34.39%/2.06) — luôn kiểm tra pool-level utility, đừng tối ưu IC đơn thuần.
- Compact memory là bắt buộc: bỏ memory feedback → return giảm một nửa (48.64→26.40) và rollout dài gấp 3× (5.24→15.75 turns).
- Future-window data phải KHÔNG available cho inference policy — chỉ dùng tính reward offline, tránh leakage.
- Multi-turn GRPO tốn compute: AlphaPilot chỉ train được 4B model; plan GPU trước khi scale.
- Đánh giá trên 1 contiguous period / 1 thị trường thì chưa chứng minh generalization — cần cross-market test riêng.
