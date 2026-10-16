# [2610.10942v1] StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents

## Problem
Hầu hết các benchmark agentic (đa đại lý) còn static (tĩnh): thế giới chỉ di chuyển khi agent hành động, phần thưởng là verdict cuối cùng, ngưỡng đạt được đặt tùy ý. Điều này không phản ánh thương mại thực tế nơi khách hàng đặt hàng 24/7, nhà cung cấp thay đổi giá và lỗi, và震荡 thị trường đến với cảnh báo một phần hoặc không có cảnh báo.

## Contribution
- Giới thiệu StoreBench: live-commerce environment (môi trường thương mại sống) mà agent chạy một cửa hàng quần áo vừa trên production-grade commerce backend (hệ thống thương mại cấp sản xuất), kiểm tra long-horizon planning (lập kế hoạch dài hạn) và economic judgment (phán aquellos kinh tế) dưới sự bất đảm bảo.
- Agent tác động qua cùng 29 merchant tool (công cụ thương nhân) MCP surface.
- 11 dense tasks (nhiệm vụ dày đặc) × 3 seeds × 3 attempts, đánh giá 7 frontier models.
- Composite score: Business 70%, Reliability 20%, Continuity 10%, calibrated (điều chuẩn) chống lại scripted policies (chính sách script).

## Method (tóm cốt lõi)
StoreBench mô phỏng một cửa hàng quần áo vừa với khách hàng đặt hàng liên tục, nhà cung cấp thay đổi giá và lỗi, shock thị trường. Agent nhận task instruction và tool access, không biết scoring mechanics hay thresholds. Mỗi trial (thử nghiệm) được coi là "pass" nếu composite score vượt quá task-seed threshold. Full-year task chạy riêng với Claude Code, context compaction, extended thinking, 365-window episode.

## Key Findings
- Best model (DeepSeek-V4-Pro) đạt 49% task-seed cells vs heuristic's 97% (chính sách script).
- Human experts clear 97% of cells, ship 96% orders on time, handle 93% returns, reliability 0.944 (so với tối đa 0.85 của model).
- Mọi model khác đạt tối đa 36% cells.
- Trained policy: tỉ lệ episode kết thúc tại lợi nhuận tăng từ 3% lên 72%.
- Bỏ clock (đồng hồ) làm điểm GPT-5 tăng từ 0% lên 34.4%.

## Actionable Insights
- Agent chưa thay được judgment kinh tế (tư duy kinh doanh): trên môi trường thương mại thực tế, model tốt nhất chỉ đạt 49% so với heuristic 97%. Áp dụng: solopreneur dùng agent cho bán hàng/làm cửa hàng online nên dùng agent làm trợ thủ, không thay thế quyết định định giá và quản lý tồn kho.
- Benchmark live-commerce có giá trị để đánh giá agent trước khi triển khai production: StoreBench có 29 merchant tools, 11 dense tasks, có thể dùng làm môi trường test cho agent vận hành cửa hàng.

## Assumptions & Limitations
- Điều kiện: agent cần truy cập 29 merchant tools qua MCP surface.
- Paper thừa nhận: full-year task dùng harness khác (Claude Code), không so sánh trực tiếp với short-horizon suite.
- Limitation paper không nói: chưa đánh giá agent trên nhiều cửa hàng cùng lúc, chưa test chế độ multi-agent collaboration.

## Metadata
- Năm: 2026
- Tác giả: Daksh Raghuvanshi, Ved Vedere, Yifan Wang (AfterQuery)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.10942
