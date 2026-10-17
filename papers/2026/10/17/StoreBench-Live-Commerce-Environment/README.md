# [2610.10942v1] StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents

## Problem
- Các bài đánh giá agent (agent benchmarks) hiện đại vẫn kiểm tra các tác vụ có biên (bounded tasks) trong môi trường bị kiểm soát (controlled environments) bị reset giữa các lần chạy. Chúng hiếm khi đo đẳng những yêu cầu của công việc vận hành thực tế: độ tin cậy maintained (sustained reliability), sự thích nghi với sự thay đổi (adaptation to change), và khả năng vận hành dưới sự giám sát hạn chế của con người (limited human supervision).

## Contribtuion
- StoreBench — một môi trường thương mại điện tử trực tuyến (live-commerce environment) mà một agent chạy một cửa hàng áo phông trung bình (mid-size online apparel store) trên một nền tảng thương mại (commerce backend) cấp doanh nghiệp (production-grade), kiểm tra sự lập kế hoạch dài hạn (long-horizon planning) và phán quyết kinh tế (economic judgment) dưới sự không chắc chắn (uncertainty).
- Khách hàng đặt hàng quanh giờ (around the clock), nhà cung cấp thay đổi giá và thất bại, và các chấn đoạn thị trường (market shocks) đến với thông tin phần hoặc không có cảnh báo.
- Agent hành động qua cùng 29 công cụ bán hàng (merchant tools) mà một nhà vận hành nhân (human operator) sẽ dùng, dưới một ngân sách thao tác cửa sổ (windowed operation budget) làm thời gian mô phỏng (simulated time) trở thành hàm của các hành động (actions) được thực hiện, do đó độ trễ (latency) của mô hình không thể ảnh hưởng đến thời gian mô phỏng.
- Ngưỡng vượt qua (pass thresholds) được chuẩn hóa (calibrated) dựa trên chính sách trick脚本 (scripted anchor policies), phần thưởng (reward) được làm cứng (hardened) chống lại một danh sách các lỗ hổng thưởng (reward hacks), và mọi bản mô phỏng (episode) phát lại giống hệt nhau sau một chuỗi hành động (sequence of actions) nhất định.

## Method (tóm tắt cốt lõi)
- Môi trường StoreBench đặt agent phụ trách Ostrelle, một cửa hàng áo phông trung gian (mid-size online apparel store), trong một lượt liền mạch (contiguous shift) từ 30 đến 365 ngày mô phỏng (simulated days).
- Cửa hàng không phải là một mô hình giả lập (mock): nó chạy trên Medusa v2, một nền tảng thương mại nguồn mở (open-source) cấp doanh nghiệp (production-grade).
- Agent tương tác độc quyền thông qua 29 công cụ (tools) qua Giao diện Mô hình Bối cảnh (Model Context Protocol), bao gồm danh mục (catalog), giá cả (pricing), tồn kho (inventory), xử lý đơn hàng (fulfillment), trả hàng (returns), nguồn cung (sourcing), và báo cáo (reporting).
- Môi trường kết hợp 18 tháng lịch sử vận hành, một nền tảng nhà cung cấp 40 nhà (40-vendor supplier market), 29 công cụ bán hàng (merchant tools), nhu cầu ẩn (hidden demand), và các chấn đoạn (shocks) kịch bản đối với nhà cung cấp, chi phí, và đối thủ cạnh tranh trong một nền tảng thương mại cấp doanh nghiệp (production-grade commerce backend).
- Đánh giá bảy mô hình tiền datetime (frontier LLMs) trên 11 kịch bản (scenarios) từ 30 đến 45 ngày và một năm mô phỏng đầy đủ (full simulated year), trên ba thế giới hạt nhân (three world seeds) với nỗ lực lý luận tương đương (matched reasoning effort).

## Key Findings
- 3 tác giả từ AfterQuery, category arXiv: cs.AI.
- 7 mô hình tiền datetime (frontier LLMs) được đánh giá: DeepSeek-V4-Pro, Claude Opus 4.8, Claude Fable 5, Qwen3.8-Max, Gemini 3.8 Flash, GPT-5.6 Sol, và Muse Spark 1.2.
- Không một mô hình nào khớp với chính sách tìm kiếm thông minh viết sẵn (scripted smart-triage policy) trên trung bình: mô hình tốt nhất, DeepSeek-V4-Pro, đạt 49% so với heuristic 97%.
- Các chuyên gia nhân (human experts) làm việc qua cùng các công cụ và ngân sách vượt qua mọi mô hình (mean composite 0.708 vs. 0.700).
- Trong một năm mô phỏng đầy đủ (full simulated year) dưới Claudio Code harness, hầu hết các mô hình thể hiện sự cải thiện劇烈 (dramatic performance improvement).
- Trong một lần đào tạo hậu kỳ (GRPO post-training), Qwen3.5-27B được đào tạo trên chỉ năm tác vụ rời rạc (five disjoint tasks) nâng điểm tổng hợp (mean composite) trên các tác vụ đánh giá riêng biệt (held-out evaluation tasks) từ 0.136 lên 0.373.
- Phát hành năm tác vụ mẫu phần huấn luyện (five example training-split tasks), mười mẫu quỹ đạo (ten sample trajectories), và công cụ chấm điểm và xác thực (scoring and verification tooling); toàn bộ môi trường và bộ đánh giá (evaluation suite) bị giữ kín (withheld) để giữ bộ đánh giá không bị ô nhiễm (uncontaminated).

## Actionable Insights
1. Agent chưa thay thế được judgment kinh tế (economic judgment): model tốt nhất đạt 49% vs heuristic 97%; dùng agent làm trợ thủ, không thay thế quyết định định giá/tồn kho. Áp dụng: khi xây dựng agent cho thương mại điện tử, hãy dùng agent làm trợ thủ cho quyết định định giá và tồn kho, không thay thế hoàn toàn quyết định định giá/tồn kho của con người.
2. Dùng môi trường mô phỏng live-commerce (live-commerce environment) để đánh giá agent dưới sự không chắc chắn (uncertainty). Áp dụng: khi xây dựng agent cho bán hàng trực tuyến, hãy dùng môi trường mô phỏng với khách hàng đặt hàng liên tục, nhà cung cấp thay đổi giá và thất bại, và các chấn đoạn thị trường (market shocks) để đánh giá sự ổn định dài hạn (long-horizon stability) của agent.

## Assumptions & Limitations
- Đánh giá trên một cửa hàng áo phông đơn lẻ (single apparel business) với đối thủ được viết kịch bản (scripted competitors) và nhu cầu tham số (parametric demand).
- Môi trường (engine) bị giữ kín (withheld) để giữ bộ đánh giá không bị ô nhiễm (uncontaminated).
- Đào tạo hậu kỳ (post-training) dùng một mô hình cơ sở (base model) và một lần chạy (one run).

## Metadata
- Năm: 2026, tác giả: Daksh Raghuvanshi, Ved Vedere, Yifan Wang (AfterQuery), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2610.10942v1
