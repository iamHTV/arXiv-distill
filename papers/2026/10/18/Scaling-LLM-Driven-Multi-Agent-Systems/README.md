# [2607.27942v1] Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis

## Problem
Hệ thống multi-agent (MAS) dựa trên LLM có tiềm năng giải quyết tác vụ phức tạp thông qua phối hợp nhiều agent chuyên môn, nhưng không gian thiết kế kiến trúc vẫn chưa được hệ thống hóa. Không có sự thuyết phục nhất quán về cách xây dựng MAS mạnh mẽ, và việc mở rộng (scaling) agent hệ thống vô tình tạo ra các mode lỗi mới: quá tải truyền thông, sự không nhất quán giữa các agent, mất hiệu quả, và mất định hướng nhiệm vụ hệ thống (system-wide task alignment). Các nghiên cứu trước chỉ xét một chiều mở rộng (số agent, vòng tranh luận) và báo cáo lợi ích bị giới hạn, chưa hệ thống tính cả độ chính xác, chi phí và độ tin cậy cùng lúc dưới kiến trúc nguyên tắc.

## Contribution
- Đưa ra 4 nguyên tắc thiết kế kiến trúc MAS khả dìng mở rộng: đơn giản (P1), phản hồi linh hoạt (P2), workflow tuyến tính với vòng lặp tùy chọn (P3), truyền thông dựa trên tóm tắt (P4).
- Xây dựng kiến trúc tham chiếu (reference architecture) hoạt diện các nguyên tắc qua kênh nhóm chia sẻ tóm tắt agent và tập quy tắc thiết kế topology.
- Đánh giá 4 cấu hình độ phức tạp tăng dần (từ 1 agent đến 7 agents) trên benchmark terminal-bench (80+ tác vụ hệ thống kỹ thuật) với 2 LLM khác nhau (GPT-5-mini, GPT-5-nano).

## Method
Kiến trúc tham chiếu có 2 thành phần cốt lõi: (1) Kênh nhóm tóm tắt (group chat of summaries) — mỗi agent hoàn thành sub-task thì đăng một tóm tắt ngôn ngữ tự nhiên vào kênh chung; agent sau nhận toàn bộ lịch sử kênh làm ngữ cảnh. (2) Workflow có hướng với vòng lặp tùy chọn (directed workflow with optional loops) — topology được biểu diễn là đồ thị hướng Gw=(A,E,s,T) với ràng buộc: mỗi agent không phải terminal có ít nhất 1 Nachfolger, mỗi agent không phải start agent có thể tiếp cận, mỗi agent tối đa 3 Nachfolger. Mỗi agent tự quyết định khi nào xong và kích hoạt agent kế tiếp qua tag [<next_agent>] trong tóm tắt cuối. Ba cấu hình MAS được đánh giá: MAS-S (3 agents, 1 loop), MAS-M (5 agents, 3 loops), MAS-L (7 agents, 5 loops), cùng baseline Singleton.

## Key Findings
- Trên terminal-bench, GPT-5-mini với MAS-M đạt accuracy 0.348, so với Singleton 0.296 (+15,2% tương đối), nhưng MAS-L giảm xuống 0.315 (−9,7% so với MAS-M).
- Chi phí completion tokens tăng tuyến tính với độ phức tạp: baseline → +1× → +1,4× → +3,2× (GPT-5-mini).
- Consistency (tỷ lệ tác vụ được giải quyết trong tất cả các lần chạy) dưới 50% ở mọi cấu hình: 42%, 46%, 36%, 46% (GPT-5-mini).
- Với GPT-5-nano (model kém hơn), accuracy gần như phẳng (0,097 → 0,090 → 0,105 → 0,105) — kiến trúc phức tạp không bù đắp cho model yếu.

## Actionable Insights
1. Kiến trúc phức tạp hơn không phải luôn tốt — khi LLM cơ bản không đủ năng lực, thêm agent chỉ tốn token và gây lỗi lan truyền. Áp dụng: trước khi xây dựng multi-agent, hãy test model cơ bản trên task đơn lẻ và chỉ mở rộng khi model đạt ngưỡng chấp nhận được.
2. Hiệu suất đạt đỉnh ở độ phức tạp trung bình (MAS-M: 5 agents, 3 loops), không phải cấu hình phức tạp nhất. Áp dụng: bắt đầu với kiến trúc đơn giản nhất, mở rộng từng bước theo nhu cầu thực tế, theo dõi trade-off chi phí–độ chính xác ở mỗi bước.
3. Tính nhất quán (consistency) là nút thắt trung tâm — agent dưới stream chấp nhận và củng cố khung vấn đề do agent trên stream thiết lập. Áp dụng: thiết kế agent kiểm soát chất lượng (QA) với định hướng đối đầu (adversarial), được khuyến khích tracer và kích hoạt vòng lặp phản hồi chủ động.

## Assumptions & Limitations
- Đánh giá trên terminal-bench (tác vụ hệ thống kỹ thuật trong terminal), kết quả có thể không chuyển thẳng sang domain khác (content, marketing, business).
- Chỉ dùng 2 model (GPT-5-mini, GPT-5-nano), không generalize sang tất cả LLM.
- Consistency được đo trên 3 lần chạy, số lần chạy ít có thể không bắt được toàn bộ biến động ngẫu nhiên.
- Paper không nói rõ chi phí đào tạo và thời gian chạy thực tế chi tiết.

## Metadata
- Năm: 2026, tác giả: Linus Sander, Fengjunjie Pan, Vahid Zolfaghari, Andre Schamschurko, Nenad Petrovic, Alois Knoll (Technical University of Munich), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2607.27942v1