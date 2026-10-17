# [2610.11602v1] Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery

## Problem
- LLM agents có thể tiêu thụ hàng triệu token trong quá trình khám phá lỗ hổng (vulnerability discovery) mà không tạo ra bản minh chứng hoạt động (working PoC). Prior work chưa giải quyết được việc chẩn đoán chi phí này và hiểu tại sao nó lại thất bại trong việc sinh ra kết quả — chi tiêu được chi tiêu ở đâu, và tại sao nỗ lực đó lại không tạo ra PoC hoạt động?

## Contribution
- Nghiên cứu mã nguồn mở đa trục (multi-axis open-coding) trên 200 dấu vết CyberGym, trải qua bốn agent (Codex, OpenCode, Cybench, EnIGMA) dưới cơ bản không hỗ trợ (unaided baseline) và bốn phương pháp hiệu quả hiện có.
- Ba phát hiện chính: (1) các agent khác nhau đáng kể về thành công và chi phí, chi tiêu cao hơn không nhất quán cho kết quả tốt hơn; (2) bản địa hóa và hiểu mã nguồn, cùng với suy luận về lỗ hổng và thiết kế kích hoạt (trigger design), chiếm 60.4% token và là hai bottlenecks chính trong các lần chạy thất bại; (3) chỉ 24.4% so sánh đôi khớp duy trì thành công với chi phí tổng thấp hơn; tín hiệu không phù hợp và chi phí phụ trợ hạn chế lợi ích của các phương pháp hiện có.
- AVRI (Agent-centric Vulnerability Reasoning Interface) được xây dựng xung quanh Bidirectional Evidence Trace (BET) bền vững (persistent). BET kết nối cách harness tiêu thụ đầu vào với các điều kiện cần thiết để một thao tác được chọn trở nên không an toàn, giữ các tương quan được nguồn minh chứng (source-supported correspondences) cùng với giả thiết và câu hỏi mở của agent. Lệnh đọc, phân tích, và lưu trữ giúp agent xây dựng và tái sử dụng bằng chứng này thay vì liên tục truy xuất và tái cấu trúc lại.

## Method (tóm tắt cốt lõi)
- Thiết kế nghiên cứu thực nghiệm: 200 dấu vết, bốn agent, năm cấu hình mỗi agent (cơ bản và bốn phương pháp hiệu quả), cùng mười nhiệm vụ mỗi cấu hình. Mỗi kết hợp được thực thi một lần.
- Bốn phương pháp hiệu quả được đánh giá: AgentDiet (nén lịch sử tương tác), Revelio (phân tích tĩnh nhẹ nhàng để tạo giả thuyết lỗ hổng được xếp hạng), PAgent (phản hồi thông qua độ bao phủ để dẫn dắt sinh PoC), CodeGraph (xây dựng đồ thị gọi và tham chiếu cấp kho lưu trữ được truy xuất qua giao diện truy vấn).
- AVRI: giao diện trung tâm agent (agent-centric) xung quanh BET bền vững — kết nối cách harness tiêu thụ đầu vào với điều kiện cần để một thao tác được chọn trở nên không an toàn; giữ các tương quan được nguồn minh chứng cùng với giả thiết và câu hỏi mở của agent; lệnh đọc, phân tích, và lưu trữ giúp agent xây dựng và tái sử dụng bằng chứng.
- Đánh giá: 20 nhiệm vụ CyberGym, Codex và OpenCode, so sánh AVRI với cơ bản và bốn phương pháp hiện có, đo thành công (success), nhớ lại (recall), thời gian, và chi phí.

## Key Findings
- 4 tác giả từ Đại học Khoa học và Kỹ thuật Huazhong (HUST), category arXiv: cs.CR.
- Các agent khác nhau đáng kể về thành công và chi phí; chi tiêu cao hơn không nhất quán cho kết quả tốt hơn.
- Bản địa hóa và hiểu mã nguồn + suy luận về lỗ hổng và thiết kế kích hoạt chiếm 60.4% token, là hai bottlenecks chính trong các lần chạy thất bại.
- Chỉ 24.4% so sánh đôi khớp duy trì thành công với chi phí tổng thấp hơn.
- Bảng 3: Codex — Baseline chi phí $132.65 → AVRI $108.75 (−18.0%), thành công 85% → 85%, nhớ lại 65% → 75%, thời gian 50,968s → 33,313s.
- OpenCode — Baseline chi phí $4.38 → AVRI $3.34 (−23.7%), thành công 100% → 100%, nhớ lại 90% → 90%, thời gian 25,324s → 24,017s.

## Actionable Insights
1. Bản địa hóa và hiểu mã nguồn cùng suy luận về lỗ hổng và thiết kế kích hoạt chiếm 60.4% token và là bottleneck chính trong các lần chạy thất bại. Áp dụng: tập trung tối ưu hóa vào các hoạt động này thay vì cắt bớt lịch sử tương tác mù quáng.
2. Chỉ 24.4% so sánh đôi duy trì thành công với chi phí thấp hơn — tín hiệu không phù hợp và chi phí phụ trợ hạn chế lợi ích của các phương pháp hiệu quả hiện có. Áp dụng: đánh giá hiệu quả cùng với chi phí, không chỉ nhìn vào một con số đơn lẻ.

## Assumptions & Limitations
- Đánh giá 20 nhiệm vụ, một lần chạy mỗi cấu hình — không thiết lập độ mạnh mäßige trước sự thay đổi giữa các lần chạy.
- Đánh giá AVRI tập trung vào Codex và OpenCode (Cybench và EnIGMA có tỷ lệ thành công thấp hơn).
- Hạn chế thời gian chạy 7,200 giây mỗi nhiệm vụ.
- Không nói rõ: hiệu quả trên các ngôn ngữ lập trình ngoài C/C++ và các loại lỗ hổng khác.

## Metadata
- Năm: 2026, tác giả: Li Lu, Hongjie Chen, Yanjie Zhao, Haoyu Wang (Đại học Khoa học và Kỹ thuật Huazhong), category arXiv: cs.CR, link PDF: https://arxiv.org/pdf/2610.11602v1
