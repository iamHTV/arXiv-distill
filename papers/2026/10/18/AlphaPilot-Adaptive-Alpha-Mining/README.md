# 2610.15488v1 AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning

## Problem
- Formulaic alpha mining (khai thác alpha công thức) tìm biểu thức diễn giải được để xếp hạng asset theo future return. Khó vì 3 thách thức cùng lúc: search space combinatorial (toán tử × feature × lookback window), supervision yếu và bất ổn (return nhiễu, market regime thay đổi), redundancy (công thức tốt đơn lẻ có thể thừa khi vào pool lớn). Prior work chỉ dùng tập con tín hiệu: GP/symbolic regression (chỉ scalar fitness, dễ overfit), RL/generative (AlphaGen, AlphaForge — không dùng language prior để interpret regime), LLM-based (dùng prior nhưng thiếu real-data evaluation feedback loop).

## Contribution
- Khung RL (học tăng cường) multi-turn tool-using: agent condition trên market description, đề xuất factor expression, query real-data evaluator feedback, update retained factor pool qua các turn — đóng kín vòng information: regime-aware language prior + executable real-market data + turn-level evaluator feedback + pool-level memory trong 1 process trainable.
- GRPO training cải thiện financial decision ability trong small base model mà vẫn giữ inference efficiency — học từ multi-turn evaluator feedback thay vì dựa vào capability gốc của large general-purpose model.
- Daily adaptive inference + benchmarking framework: update factor pool từng ngày, đánh giá bằng factor-level diagnostics VÀ portfolio-level backtests.

## Method
- Daily market context c_t = (q_t, S_t, O): q_t = market-regime description (natural language), S_t = seed/carried-over factor manifest, O = supported operator set (DSL).
- Multi-turn rollout: turn k, small LLM policy quan sát context + compact memory (factor đã thử, retained-pool state, tool feedback trước) → đề xuất B DSL factors (expression + factor-family label); executable factor_evaluator validate syntax, execute trên rolling training window, áp universe/tradability filters, trả compact feedback (expression, family, IC, RankIC, stability, execution error); lặp tối đa H_max turns (training: 40 assistant turns, 8 rollouts/prompt).
- Retained factor pool: filter sơ (invalid, coverage không đủ, single-factor score không dương → discard); meta-alpha weights bằng NNLS/ridge-style fit trên recent training segment (w* = argmin||F(P)w - target||² + ρ||w||², w≥0); pool diagnostics từ cross-sectional ranks.
- Training: GRPO trong VERL, backbone Qwen3-4B-Instruct-2507, reward = sigmoid-mapped future-window IC/RankIC + minimum-positive-factor completeness penalty.
- Inference: day-by-day search + pool update (thích ứng regime shift); weights recent-window NNLS/ridge; portfolio long-only top-K, 10 bps transaction costs.
- Data: daily Chinese A-share panels CSI300 và CSI500, 3-year rolling history window; future window 21/63 ngày chỉ cho offline eval (KHÔNG cho inference policy); split 2024-01-01 validation, 2025-07-01 test; sample train/val mỗi 5 trading days, test inference hằng ngày.
- Baselines: Qwen3-4B/30B-A3B/235B-A22B (temp 0), AlphaGen (RL), AlphaForge (generative), GRPO single-turn controlled (cùng backbone/algorithm/splits/reward, one-shot pool), seed-factor linear regression, DeepSeek-R1 direct-propose.

## Key Findings
- CSI300 out-of-sample (3-run means): AlphaPilot total return 42.93%, Sharpe 2.46, MaxDD -9.34%, IC 0.0403, RankIC 0.0595 — cao nhất mean total return, Sharpe, RankIC. So sánh: Qwen3-4B 0.58%/0.16, Qwen3-30B -1.72%/-0.01, Qwen3-235B 6.88%/0.55, DeepSeek-R1 22.79%/1.21, Seed+LR 34.51%/1.82, AlphaGen 25.17%/2.26, AlphaForge 2.18%/0.07.
- CSI500: AlphaPilot 54.19%, Sharpe 2.86, MaxDD -14.34%, IC 0.0624, RankIC 0.0259 — cao nhất total return, Sharpe, IC, RankIC (AlphaGen 48.85%/2.82, AlphaForge 36.32%/1.97).
- Benchmark-relative: excess return 21.49% cumulative với excess Sharpe 1.65 (CSI300); 18.22% với 1.36 (CSI500) vs equal-weight benchmark cùng universe.
- Controlled multi-turn vs GRPO single-turn (cùng backbone/algorithm/splits/terminal reward): +7.31 pp total return, +0.43 Sharpe, +6.98 pp MaxDD, +0.0099 RankIC, IC tương đương (0.0403 vs 0.0407) — iterative tool-based refinement là nguồn gain, không phải RL training đơn thuần.
- Design ablations (CSI300, single-run): full method 5.24 turns/48.64%/2.74; no memory feedback 15.75 turns/26.40%/1.70 — bỏ memory feedback làm return giảm một nửa và rollout dài gấp 3×; no pool auxiliary 34.39%/2.06 nhưng IC/RankIC cao nhất (0.0419/0.0634) → training proxy không align với realized portfolio return; +reward auxiliary 44.49%/2.50 (yếu hơn full → giữ auxiliary trong pool score, bỏ khỏi reward).

## Actionable Insights
- Compact tried-factor memory là bộ lái tìm kiếm: mỗi turn feed lại cho agent "đã thử gì + điểm số + pool hiện tại" — bỏ nó, agent lang thang (15.75 vs 5.24 turns) và hiệu quả giảm một nửa. Ví dụ: agent tối ưu code/factor nào cũng nên có memory compact tương tự.
- Đánh giá candidate signal theo contribution vào pool (NNLS-weighted meta-alpha), không phải IC đơn lẻ: variant có RankIC cao nhất lại có return/Sharpe yếu nhất — optimize pool-level utility.
- Small model + task RL beats big model prompting: Qwen3-4B + GRPO multi-turn vượt Qwen3-235B và DeepSeek-R1 direct-propose — đầu tư fine-tune nhỏ hơn đầu tư API model lớn, với điều kiện có evaluator executable.

## Assumptions & Limitations
- Điều kiện: future-window data KHÔNG available cho inference policy (chỉ dùng tính reward offline); long-only top-K, daily rebalancing, 10 bps stylized costs.
- Limitation paper thừa nhận: chỉ train small open-weight model (multi-turn GRPO tốn compute); không benchmark top proprietary LLM trong full multi-turn setting; evaluation 1 contiguous period (7/2025–3/2026), 2 Chinese equity universes — cross-market generalization chưa test; reward dùng short-term future-window IC/RankIC proxy chứ không full backtest trong trajectory — có thể miss drawdown control, capacity, liquidity, transaction-cost sensitivity, risk exposure; protocol đơn giản (recent-window combination, long-only top-K) — không phải complete trading strategy.
- Limitation CHƯA nói: kết quả trên A-share CSI300/CSI500 (retail-heavy, limit-up/down rules) chưa chắc chuyển sang market khác; seed factor library cụ thể (Appendix) ảnh hưởng pool khởi tạo; 3-run mean cho AlphaPilot/AlphaGen/AlphaForge nhưng single-run cho baseline khác — so sánh variance không đồng đều; IC/RankIC reward proxy có thể khuyến khích overfit window ngắn.

## Metadata
- 2026, Peiqi Jiang, Fan Zhang, Xin Xu, Tianhao Chen, Can Yang (Department of Mathematics, Hong Kong University of Science and Technology), cs.CL, https://arxiv.org/pdf/2610.15488v1, citation count: không tìm thấy [NO BENCHMARK]
