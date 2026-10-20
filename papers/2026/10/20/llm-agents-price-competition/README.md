# [2610.21711v1] How language model agents reshape price competition

## Problem
- Lý thuyết trò chơi lặp lại (repeated game theory) chỉ là existence theory (lý thuyết tồn tại): nó nói outcome nào CÓ THỂ duy trì, không dự đoán process học cụ thể sẽ CHỌN outcome nào. Các thuật toán học online chuẩn (Exp3, UCB, PPO) trong cạnh tranh Bertrand (Bertrand competition) hàng hóa đồng nhất gần như luôn hội tụ về Nash equilibrium (giá = marginal cost (chi phí biên)) — benchmark tốt cho consumer welfare (phúc lợi người tiêu dùng). Nhưng nobody biết LLM pricing agent (agent định giá) sẽ chọn regime (chế độ giá) dài hạn nào khi vào thị trường.

## Contribution
- Chứng minh cùng một foundation model có thể chọn regime đối lập (monopoly-level vs Nash-level) chỉ bằng cách thay DEPLOYMENT interface (giao diện triển khai): output (point price (giá điểm) vs probability distribution (phân phối xác suất)), history (raw (thô) vs summarized (tóm tắt)), rival-price visibility (có thấy giá đối thủ), update cadence (tần suất cập nhật).
- Tách biệt 2 nguồn lợi nhuận riêng của LLM agent: (a) exploitation (khai thác) slow-learning qua undercut (định giá thấp hơn), (b) high-price anchoring (neo giá cao) + anchor-and-harvest (neo rồi thu hoạch) — P-R-1 vs D-S-25.
- Xây DBBS (downward-biased belief search (tìm kiếm niềm tin nghiêng xuống)) — surrogate algorithm (thuật toán đại diện) reconstruct được policy D-S-25 on held-out data, giải thích mechanism dưới dạng ordered payoff-feedback search with inertia (tìm kiếm theo vùng lợi nhuận có quán tính).

## Method (tóm tắt cốt lõi)
- Market mô phỏng: (a) homogeneous winner-takes-all (người thắng nhận hết): K=21 giá grid, c=0.10, ceiling 0.36, T=2,000; (b) differentiated multinomial-logit market (thị trường sản phẩm phân hóa theo logit đa thức): pNash≈1.473, pmonopoly≈1.925.
- 7 experiment families: round-robin 7 standard learners (T=10^7 periods, 10 seeds); LLM vs learners; LLM self-play (tự chơi); protocol ablations (từ control thay đổi từng thành phần deployment); mixed deployments (P-R-1 vs D-S-1/P-S-1, 3-4 agents, visible/hidden rival price); robustness families (prompt, model GPT-5.6 Terra, demand).
- Deployment ký hiệu output-history-interval: P-R-1 (point/raw-100/1 period), D-S-25 (distr/summary-75/25), D-S-50 (distr/summary-150/50), base model Gemini 3 Flash Preview, temp 0.7. Outcome measures: price-elevation index ∆ (0 = Nash, 1 = joint-profit (lợi nhuận chung)), profit share, consumer share.

## Key Findings
- Benchmark: 20/21 markets không có UCB hội tụ competitive region sau 10^7 periods; UCB self-play price index 0.93 (217 profit units — outlier duy nhất cùng PPO-WFP 87, UCB-PPO 47, các thị trường khác ≤7.1).
- D-S-25 vs Exp3/BM-RM/PPO/UCB (2,000 periods, 10 seeds): 71–72% cumulative industry profit (lợi nhuận ngành tích lũy); 10% cuối: giá THẤP hơn đối thủ 57–60% periods — lợi từ undercut nhanh, KHÔNG từ giá cao.
- P-R-1 vs Exp3 (n=1, 300 periods): 63% industry profit; vs win-up–lose-down heuristic: match giá từ period 3, ceiling period 21, split 50%; vs coin betting: coin betting earns 71%, P-R-1 bỏ anchor ~period 200, giá đổ về ~0.19.
- Self-play cùng market homogeneous: P-R-1 elevation 0.88 (n=5) vs D-S-25/D-S-50 = 0.05 (n=10) — 2 regime đối lập.
- Ablation: change action representation alone (point→grid→distribution) → index 0.97/1.05/1.03/1.01 (VẪN cao); change information interface: hide rival 0.56, summary 0.53, both 0.31, full D-S-50 bundle 0.13 (n=5 mỗi row) — information interface, không phải output type, chọn regime.
- P-R-1–D-S-1: visible rival → lock-in ceiling 0.356, joint profit 98% monopoly, D-S-1 lấy 66%; hidden rival → anchor-and-harvest cycles, giá trung bình 0.26, D-S-1 lấy 71%. 4×P-R-1: ceiling 0.36 from period 74, split 25% each; 3×P-R-1: recurrent resets 0.11–0.35, profit 42/34/23%.
- Welfare: consumers keep 15% surplus under P-R-1 self-play vs 95% under D-S-25/D-S-50 self-play; D-S-25 undercutting learners: 72–84%. Logit market: Fish-style control loses 12.9% Nash welfare; D-S-50 bundle còn 0.8%.
- Traces: opponent-facing motifs (ngôn ngữ hướng đối thủ) 94% P-R-1 vs 34% D-S-25; payoff-region motifs 98% D-S-25 vs 21% P-R-1; raw+visible → 96–99% opponent-facing, summarized+hidden → 3–6%.

## Actionable Insights
- Định giá agent LLM: audit deployment 6 thành phần (H, A, O, ∆, M, P) TRƯỚC launch, vì cùng model + prompt khác interface → regime đối lập. Ví dụ: thay raw rival-price history bằng summarized history + distribution output + interval 25 (D-S-25-style) chuyển self-play 0.88→0.05, consumer surplus 15%→95%.
- Nếu đỐiph thủ là thuật toán online chuẩn (Exp3/UCB), LLM agent lợi từ tốc độ adapting (D-S-25 lấy 71–72% qua undercut) — nhưng lợi thế MẤT against full-information learners (coin betting beats P-R-1 71%). Đừng giả định LLM luôn thắng.
- Platform/marketplace operator: cung cấp feedback lagged/aggregated (tổng hợp trễ) thay vì raw rival-price history → giảm khả năng high-price convention; yêu cầu logging model version + prompt + observation stream + memory state + price recommendation + human overrides cho audit.

## Assumptions & Limitations
- Điều kiện: market lặp lại với feedback loop; grid action space; demand model known to researchers (agents KHÔNG được biết demand model (mô hình cầu)).
- Paper thừa nhận: market stylized (không có inventory, search, consumer heterogeneity, multi-product, platforms, asynchronous updates); traces là behavioral artefact (sản phẩm quan sát hành vi), không phải hidden computation; collusive outcomes có thể KHÔNG thấy trong chain-of-thought; single-run heterogeneous cells (n=1) là representative paths, không phải treatment-effect estimates; DBBS không phải no-regret guarantee.
- Limitation paper KHÔNG nói: chỉ 2 base models (Gemini 3 Flash Preview, GPT-5.6 Terra) — vendor-dependent; D-S-25/D-S-50 frozen qua configuration screen trên self-play → opponent-ecology overfitting risk; P-R-1-vs-learner replicated evidence chỉ vs Exp3, các learner khác illustrative.

## Metadata
- Năm: 2026 | Tác giả: Martin Bichler, Philip Hierhager, Kassian Köck, Fabian Pieroth (TU Munich) | Category: cs.GT (lí thuyết trò chơi máy tính) | PDF: https://arxiv.org/pdf/2610.21711v1 | Citation: [NO DATA — published 15 Oct 2026]
