# [2609.37454v1] Governing the Edge: Automating Commercial Property and Casualty Insurance Underwriting via a Hybrid Local-Cloud Multi-Agent Framework

## Problem
Underwriter trong bảo hiểm thương mại Tài sản và Trách nhiệm Thương mại (Commercial Property and Casualty, P&C) bỏ phần lớn thời gian vào công việc hành chính thay vì phán đoạn rủi ro. Nghiên cứu ngành ước tính 30–40% thời gian của underwriter bị chi cho công việc quản lý hồ sơ như đọc tài liệu, tra cứu dữ liệu, và nhập lại; một đơn minh bạch (submission) có thể mất khoảng 40 phút xử lý thủ công. Các tiếp cận AI hiện tại chỉ giải quyết một phần: một prompt lớn đơn thuần không thể thi hành tuân thủ, không thể gọi ra dữ liệu अधिकार, và thường gửi dữ liệu nhạy cảm lên API đám mây. Các agent pipeline như CrewAI chia công việc nhưng phối hợp dựa trên phụ thuộc nhiệm vụ chứ không phải tuân thủ, và agent suy luận trên văn bản đơn 대신 truy vấn nguồn dữ liệu chính thức.

## Contribution
- Trình bày Governing the Edge, một multi-agent framework lấy đi lớp xử lý hành chính của underwriting P&C.
- Sử dụng 13 nút (11 agent chuyên môn và 2 nút điều khiển định nhâtre,其中 một là người điều khiển leo thang con người) sắp xếp thành một đồ thị workflow hướng trong LangGraph, chia làm hai tầng: agent chạm dữ liệu nhạy cảm chạy cục bộ trên Gemma 2, agent chỉ cần suy luận trên điểm số đã làm ẩn danh chạy trên Claude Sonnet qua LiteLLM.
- Tuân thủ được xây dựng vào cấu trúc đồ thị: quy tắc làm điều kiện trên các cạnh giữa các agent, nên một đơn không tuân thủ không thể đến đích lập giá mà bị chặn ngay từ đầu, chứ không phải phát hiện sau sự việc.
- Đánh giá qua kịch bản end-to-end (đơn xe thương mại có tài xế chủ yếu có vi phạm nghiêm trọng), hiển thị mọi cuộc gọi agent, mọi lần gọi công cụ, và quyết định định tuyến kết quả.

## Method
- Kiến trúc LangGraph StateGraph với 13 nút và 3 điểm nhánh. Hai tầng: tầng cục bộ chạy Gemma 2 (ollama/gemma2, temp=0) xử lý mọi thứ chạm dữ liệu nhạy cảm; tầng đám mây chạy Claude Sonnet 4.6 qua LiteLLM xử lý suy luận nặng hơn trên dữ liệu đã ẩn danh.
- Luồng: Document Parser (1) → Intake Agent (2) trích xuất trường ACORD 125 → 3 risk sub-agents song song (3a Property/Fleet, 3b Geo/Driver, 3c Business/Ops) mỗi người gọi công cụ được ràng buộc → Risk Aggregator (3d) là agent đám mây đầu tiên hợp nhất điểm số → Compliance Agent (4) chạy 10 quy tắc P&C → Nếu PASS thì Coverage Gap (5) và Pricing (6) chạy song song → Explainability Agent (7) tổng hợp dấu vết kiểm tra → Human Escalation (8) là interrupt đơn thuần khi confidence < 0.80 hoặc compliance thất bại.
- Lớp quản trị: Compliance Agent chạy 10 quy tắc (5 STOP, 5 WARN). STOP gửi đơn thẳng đến con người bất kể độ tin cậy. WARN không làm dừng nhưng giảm điểm số và ghi vào dấu vết. Cạnh từ Compliance Agent đến Coverage Gap và Pricing chỉ mở khi kiểm tra trả về PASS.
- Biên riêng tư: trường nhạy cảm (raw_document, parsed_fields) bị loại khỏi đối tượng trạng thái gửi đến agent đám mây, agent đám mây chỉ thấy anonymized risk_profile, compliance_result, coverage_gaps.

## Key Findings
- Xử lý một đơn cần khoảng 40 phút công việc thủ công trong vài phút trên một thiết bị cạnh đơn (268,8 giây end-to-end trung bình trên 20 kịch bản).
- Điểm số tuân thủ tổng thể 70% trên benchmark 20 kịch bản, khoảng trống tập trung ở các tầng mềm dựa trên phán đoán.
- Trên tier vi phạm cứng (hard-stop) — những trường quan trọng nhất đối với cơ quan quản lý — framework thi hành mọi quy tắc một cách chính xác và có thể tái tạo (6/6), vì hard-stop là các thực thể định danh (deterministic predicates) trên các trường được trích xuất ở nhiệt độ 0.
- Độ trễ: suy luận trên thiết bị làm framework chậm hơn mỗi đơn so với một prompt đám mây đơn lẻ, một giao dịch được định lượng và thảo luận.
- Giữ dấu vết kiểm tra đầy đủ và tôn trọng ranh giới riêng tư suốt quá trình, bao gồm cơ sở hệ thống theo dõi lỗi mỗi agent trong tám phân loại lỗi để giám sát vận hành.

## Actionable Insights
1. Xây dựng tuân thủ vào cấu trúc đồ thị workflow chứ không phải kiểm tra sau sự việc. Áp dụng: khi xây dựng multi-agent cho quy trình doanh nghiệp có yêu cầu tuân thủ, hãy đặt quy tắc làm điều kiện trên các cạnh giữa các agent — một đơn không tuân thủ không thể tiếp nối đến bước tiếp theo. Bước đầu: Thiết kế LangGraph state graph với các edge condition kiểm tra compliance trước khi cho phép chuyển trạng thái.
2. Phân layer dữ liệu nhạy cảm và dữ liệu ẩn danh. Áp dụng: agent chạm dữ liệu nhạy cảm chạy cục bộ, agent chỉ xử lý điểm số đã ẩn danh chạy trên đám mây. Bước đầu: Xác định trường dữ liệu nhạy cảm trong state và loại bỏ chúng khỏi state gửi đến agent đám mây.
3. Dùng quy tắc định danh (deterministic rules) cho hard-stop, không cần LLM phán đoán. Áp dụng: các quy tắc chặn cứng (ví dụ: từ chối hồ sơ có vi phạm quá nhiều) nên được viết bằng Python định danh, không phụ thuộc vào output LLM. Bước đầu: Viết các hàm Python kiểm tra điều kiện chặn cứng trước khi gọi agent LLM.

## Assumptions & Limitations
- Các công cụ bên ngoài là synthetic stubs (dữ liệu ngẫu nhiên, chưa kết nối API thực), chưa tái tạo bit-by-bit giữa các lần chạy.
- Các kịch bản là synthetic, ground-truth quyết định do một chuyên gia duy nhất đặt ra, giới hạn khả năng generalize.
- Thời gian xử lý thủ công từ benchmark đã công bố [9], không phải do tác giả tự đo.
- Chỉ đánh giá trên Gemma 2 (cục bộ) và Claude Sonnet 4.6 (đám mây), không generalize sang tất cả LLM.

## Metadata
- Năm: 2026, tác giả: Vivek Kumar Singh, Gautam Bhowmick (Independent Researchers), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.37454v1