# Skill: llm-trading-agents-production-lessons
Source: 2609.05663v1
Type: framework

## Khi nào dùng skill này
- Xây hoặc dùng agent giao dịch tự động (trading agent) với vốn thật.
- Muốn hiểu rủi ro và hiệu quả thực tế của LLM trading agents trong production.
- Cần bài học về cách cấu hình agent giao dịch (leverage, stop/target, horizon).

## Tình huống KHÔNG nên dùng
- Không có vốn thật để giao dịch.
- Chỉ muốn giao dịch tự động mà không quan tâm đến rủi ro失控.

## Input cần có
- Vốn giao dịch thật (ETH hoặc tài sản khác trên Base/chain).
- Hệ thống agent giao dịch có thể cấu hình (leverage, stop, target).
- Dữ liệu thị trường thực tế.

## Các bước thực hiện
1. Đặt horizon giao dịch dài hơn 24h (lợi thế +0.23% median return) thay vì scalpbing ngắn hạn (<1h, −0.15%).
2. Viết hướng dẫn số cụ thể cho agent (ví dụ stop-loss 2%, take-profit 4%) thay vì mô tả mờ.
3. Giới hạn leverage: agents dùng median 5.0× và bị liquidation hơn khi volatility cao (tăng từ 0.7% lên 4.3%).
4. Không theo trạng thái leaderboard (rendered symbols): 46.5% entries trong rendered symbols vs 8.9% random baseline — over-selection 5.2× không mang lại lợi ích.
5. Đặt cơ chế stop/target cứng rắn (fixed bracket) khi vào lệnh, không để agent tự quyết định thời điểm đóng (49.3% vị thế đạt lợi nhuận tiềm năng nhưng đóng âm).

## Output mong đợi
- Hiểu rõ: agent giao dịch LLM chỉ 41% win rate so với retail 50%, 16.2% vaults lời.
- Biết cách cấu hình agent để giảm rủi ro (horizon dài, hướng dẫn số cụ thể, giới hạn leverage).

## Ví dụ áp dụng
Solopreneur dùng agent giao dịch ETH trên Base: đặt lệnh với stop 2%/target 4% (fixed bracket), giữ vị thế ít nhất 24h, viết hướng dẫn số cụ thể ("nếu giá ETH giảm 2% thì bán ngay"), không theo mã code trên leaderboard. Hy vọng giảm liquidation và nắm giữ nhiều lợi nhuận hơn.

## Gotchas
- 43.2% vị thế đạt ≥ +300 bps lợi nhuận tiềm năng nhưng 49.3% đóng âm — agent không nắm giữ lợi nhuận, cần stop/target cứng.
- Agents lean structurally long (∼78% entries) và kích thước vị thế không tuân theo volatility (median 5.0× leverage mọi sextile) — dễ bị liquidate khi thị trường biến động mạnh.
- Chỉ 15% agents net-positive so với 53% retail accounts — agent chưa vượt trội so với người giao dịch bán lẻ.
