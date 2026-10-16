# [2609.34821v1] CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets

## Problem
Cuộc cạnh tranh dài hạn (long-horizon competition) kiểm tra khả năng của agent phối hợp quyết định kinh doanh dưới sự bất đảm bảo và thích ứng với chiến lược đối thủ thay đổi. Các benchmark hiện tại chưa đánh giá được tác động của agent đối với đối thủ và thị trường một cách đồng thời.

## Contribution
- Giới thiệu CEO Arena: benchmark dùng matched replacement evaluation (đánh giá thay thế tương đương) để đánh giá operating returns (lợi nhuận hoạt động) cùng với tác động của agent đối với đối thủ và thị trường.
- Mỗi CEO agent được so sánh với reference policy (chính sách tham chiếu) trên cùng các điều kiện thị trường.
- Mô phỏng 500 ngày, 9 công ty, 8 CEO-agent LLM cạnh tranh trên giá (pricing), marketing, R&D.

## Method (tóm cốt lõi)
CEO Arena mô phỏng thị trường với 9 công ty, mỗi công ty do một CEO agent quản lý. MỗiCEO agent ra quyết định về giá, sản lượng, marketing, R&D trong 500 ngày. Matched replacement evaluation: thay thế một agent bằng agent khác trong cùng điều kiện thị trường, đo sự thay đổi của operating return và tác động đến đối thủ/thị trường. Có tender (dự thầu) enterprise, kho hàng, sản xuất, marketing, R&D.

## Key Findings
- Nhiều agent lỗ (negative operating return) trong khi vẫn có private gain (lợi nhuận cá nhân) có thể đi kèm market loss (thất suất thị trường).
- Win rate (tỷ lệ thắng) của các CEO-agent trên 24 runs: GPT-6 Astra 66% ($1333.8k), GPT-5.6 Sol 64% ($1739.2k), Qwen 3.8 Max 61% ($1268.2k), DeepSeek V4 Pro 62% ($2818.0k), DeepSeek V4 Flash 59% ($1523.2k), Gemini 3.8 Flash 56% ($1144.5k), Claude Sonnet 5 56% ($2459.6k), Doubao Seed 1.8 54% ($2143.5k), Rule 55% ($650.5k).
- Median innovation delays (trễ đổi mới trung bình) tiêu tốn 9–30% trong horizon 500 ngày.
- Unit margins ban đầu 35%, 36%, 37.04% cho sản phẩm A/B/C trước chi phí hoạt động.

## Actionable Insights
- Multi-agent doanh nghiệp không nhất định thắng: nhiều agent lỗ dù có lợi nhuận cá nhân, vì tác động đến đối thủ và thị trường (market loss) bị bỏ qua. Áp dụng: solopreneur dùng agent cho kinh doanh nên đoán ảnh hưởng toàn thị trường, không chỉ lợi nhuận của agent riêng lẻ.
- Đánh giá agent trong môi trường cạnh tranh thực tế (matched replacement) quan trọng hơn benchmark đơn lẻ. Áp dụng: trước khi triển khai agent quản lý giá/marketing, hãy thử thay thế agent hiện tại trong cùng điều kiện thị trường để xem tác động thực sự.

## Assumptions & Limitations
- Điều kiện: mô phỏng thị trường với 9 công ty, 500 ngày; kết quả có thể khác trên thị trường thực tế với số lượng công ty khác.
- Paper thừa nhận: matched replacement evaluation yêu cầu điều kiện thị trường giống hệt, khó thực hiện trên production thực tế.
- Limitation paper không nói: chưa đánh giá trên nhiều vòng lặp dài hơn 500 ngày, chưa test tác động của điều chỉnh chiến lược đối手 trong thời gian thực.

## Metadata
- Năm: 2026
- Tác giả: An Yan, Yu Huo, Zhiwei Shang, Yiran Peng, Chenglin Wu (DeepWisdom, Fudan, CUHK, CUHK-Shenzhen, HKUST-GZ)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.34821
