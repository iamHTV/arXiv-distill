# [2609.26760v2] Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents

## Problem
Các agent LLM thường xử lý luồng các tác vụ liên quan, nhưng standard harnesses (khung làm việc chuẩn) lại hỏi lại mô hình lần lượt tái thiết (reconstruct) những quyết định điều khiển (control decisions) giống nhau bên trong context (bối cảnh) của mỗi tác vụ. Điều này gây lãng phí token và chi phí inference.

## Contribution
- Nghiên cứu xem task feedback (phản hồi tác vụ) có thể biến các quyết định điều khiển thường xuyên thành cấu trúc tái sử dụng (reusable specialist agents - đại lý chuyên gia tái sử dụng) thay vì để LLM xử lý lặp lại.
- Growing Harness: thay thế inference bằng code, biến feedback thành thành phần điều khiển tái sử dụng, cắt 76–92% LLM calls và 74–99% inference cost.
- Được đánh giá trên BrowseComp-Plus và WebArena-Verified, thành công vẫn ở mức 44.7–45.3% qua các mô hình quy mô, trong khi Tool-Calling sụt xuống 6.7% với mô hình 4B.

## Method (tóm cốt lõi)
Growing Harness học 'harness' (khung làm việc) agent từ feedback (phản hồi thất bại được hướng dẫn), biến control (điều khiển) thành code tái sử dụng thay vì để LLM xử lý lặp lại. Có function-level guidance (hướng dẫn cấp hàm), gate validation (xác thực cổng), và trace-local edits (chỉnh sửa theo vết dấu địa phương). Mỗi lần tối ưu hóa, harness tăng cường bản thân dựa trên feedback từ các lần chạy trước.

## Key Findings
- Giảm 76.0–91.8% LLM calls và 74.4–98.6% online cost so với Tool-Calling trên sáu thiết lập (setting).
- Trên WebArena-Verified: thành công vẫn ở mức 44.7–45.3% qua ba mô hình triển khai, trong khi Tool-Calling giảm từ 30.0% (gpt-oss-120b) xuống 6.7% (Qwen3.5-4B).
- BrowseComp-Plus: +17.3 pp, -90% cost; WebArena-Verified: +38.6 pp, -99% cost; +32.0 pp, -91% cost; +15.3 pp, -96% cost tùy cấu hình.
- Thay thế inference bằng code: 76–92% ít LLM calls hơn ở 74–99% chi phí thấp hơn.
- Bỏ function-level guidance làm giảm thành công cuối cùng từ 36% xuống 18%.

## Actionable Insights
- Thay vì để LLM suy nghĩ lại toàn bộ trong mỗi tác vụ, hãy xây dựng harness tái sử dụng (code điều khiển) từ feedback của các lần chạy trước. Áp dụng: solopreneur chạy agent xử lý nhiều tác vụ liên quan (ví dụ duyệt web, lấy dữ liệu) nên lưu lại các quyết định điều khiển thành code reusable, chỉ gọi LLM khi thực sự cần.
- Dùng few-shot hoặc function-level guidance để giữ độ chính xác khi giảm LLM calls. Áp dụng: khi xây pipeline agent, thêm hướng dẫn cấp hàm và gate validation để agent không suy nghĩ quá nhiều.

## Assumptions & Limitations
- Điều kiện: tác vụ có luồng liên quan nhau để feedback có thể tích luỹ; không áp dụng cho tác vụ độc lập hoàn toàn.
- Paper thừa nhận: thành công trên WebArena-Verified chỉ ở mức 44.7–45.3%, còn thấp so với triển khai thực tế cao cấp.
- Limitation paper không nói: chưa đánh giá trên các tác vụ ngoài web browsing, chưa test multi-agent collaboration.

## Metadata
- Năm: 2026
- Tác giả: Laizhen Li, Jiarui Li, Juanjuan Zhao, Kejiang Ye, Ye Li, Cheng-zhong Xu, Xitong Gao
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.26760
