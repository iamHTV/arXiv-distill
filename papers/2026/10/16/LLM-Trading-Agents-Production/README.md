# [2609.05663v1] What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets

## Problem
Các agent giao dịch tự chạy bằng LLM (autonomous language-model trading agents) đang hoạt động trong production với vốn thật, nhưng không có bản ghi đo lường quy mô lớn về cách chúng thực sự hoạt động, rủi ro và hiệu quả.

## Contribution
- Trình bày bản ghi đo lường liên tục, quy mô dân số (population-scale measurement record) của các agent giao dịch tự chạy trong điều kiện production trên hai hệ thống chia cùng một dòng thiết kế: DX Terminal Pro (3,505 user-funded vaults giao dịch ETH thật trên Base memecoin markets trong 21 ngày, tháng 2-3/2026) và DXAP live alpha fleet (500-599 user-created agents all-history, 91-117 agents đồng thời hoạt động).
- ∼300K onchain actions, ∼$20M, ∼70B inference tokens.

## Method (tóm cốt lõi)
Đo lường liên tục hai flotte agent giao dịch LLM trong production: DX Terminal Pro (vaults由 người dùng cấp vốn, giao dịch ETH thật) và DXAP (flotte alpha trực tiếp, agents do người dùng tạo). Theo dõi P&L, leverage, liquidation, win rate, và hành vi giao dịch qua 69 ngày.

## Key Findings
- Fleet chạy 41% roundtrip win rate so với retail 50%, ở median hold times gần như giống nhau (2.05h vs 2.18h).
- Chỉ 15% của agents active trong tuần là net-positive vs 53% của retail accounts.
- Agents lean structurally long (∼78% of entries vs ∼60%) ở khoảng 4-5× effective leverage (median 0.096× vs 0.022× notional-to-equity, chosen-leverage median 5.0×).
- Median true return là 0.492×; 16.2% of vaults finished profitable; 92% of deposited ETH was withdrawn.
- 43.2% of positions (≥ +300 bps favorable excursion within 24h), nhưng 49.3% of those closed with negative trade return; chỉ 13.3% kept half the excursion.
- Positions held 24h+ earn +0.23% median account return while sub-1h positions earn −0.15%.
- 46.5% of entries in rendered symbols (leaderboard) against 8.9% random-availability baseline, 5.2× over-selection.
- Users who wrote concrete numeric instructions were profitable 4.2× as often as median.
- 87 UI-only owners who never used chat were highest-profit cohort (41% in profit).
- Sizing là volatility-blind: median leverage là 5.0× trong mọi volatility sextile.
- Liquidation rate tăng từ 0.7% lên 4.3% khi volatility tăng.

## Actionable Insights
- Agent giao dịch LLM trong production chưa thật sự linh động: chỉ 16.2% vaults lời, 41% win rate so với retail 50%. Áp dụng: solopreneur dùng agent giao dịch nên mong đợi hiệu quả thấp hơn retail và không coi agent là cách kiếm tiền dễ dàng.
- Giữ vị thế hơn 24h có lợi (+0.23% median return) còn giao dịch ngắn hạn (<1h) mất tiền (−0.15%). Áp dụng: nếu dùng agent giao dịch, hãy đặt horizon dài hơn và tránh scalpbing ngắn hạn.
- Users viết hướng dẫn số cụ thể (concrete numeric instructions) lời 4.2× so với median. Áp dụng: khi cấu hình agent giao dịch, hãy viết hướng dẫn số치ên thức (ví dụ stop-loss 2%, take-profit 4%) thay vì mô tả mờ mà.
- Cảnh báo: 43.2% vị thế đạt ≥ +300 bps lợi nhuận tiềm năng nhưng 49.3% đóng với kết quả âm — agent không nắm giữ lợi nhuận. Áp dụng: cần cơ chế stop/target cứng rắn (fixed bracket) chứ không để agent tự quyết định thời điểm đóng.

## Assumptions & Limitations
- Điều kiện: dữ liệu từ hai hệ thống cụ thể (DX Terminal Pro, DXAP) trên Base memecoin markets; có thể khác trên các thị trường khác.
- Paper thừa nhận: All cross-era P&L is operator-reported figures (số liệu do người điều khiển báo cáo).
- Limitation paper không nói: chưa đánh giá trên nhiều loại tài sản ngoài memecoin ETH, chưa test nhiều hơn 69 ngày.

## Metadata
- Năm: 2026
- Tác giả: T.J. Barton, Chris Constantakis, Patti Hauseman, Annie Mous, Alaska Hoffman, Brian Bergeron, Hunter Goodreau (DX Research Group)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.05663
