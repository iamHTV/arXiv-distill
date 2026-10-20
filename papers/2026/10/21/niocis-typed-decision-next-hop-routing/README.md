# [2610.25985v1] NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents

## Giá trị cốt lõi (1 câu)
NIOCIS là một lớp định tuyến thay thế việc suy luận LLM mỗi lần quyết định (per-hop) bằng một typed-decision readout lấy từ một forward pass duy nhất, không sinh văn bản, đạt 32.8% khớp với hành động của đội agentes (35.6% trong không gian tùy chọn đã khai báo) trong 10 ms so với 2.2 giây mỗi hop LLM.

## Problem
Công cụ agent trả tiền cho mỗi quyết định: ở mỗi hop, LLM đọc lại trạng thái và suy nghĩ trong vài giây, mặc dù hành động hữu hạn và quyết định lặp lại. Các bản ghi thực thi đã chứa câu trả lời hàng nghìn lần, nhưng agent vẫn tính toán lại từ đầu mỗi lần.

## Contribution
1. Đồ thị hành động loop-collapsed (loop-collapsed action graph): gộp nhật ký thực thi thành một đồ thị có hướng các chuyển tiếp hành động tiến qua (E+) cùng các cạnh phục hồi (E−) cho rollback, backtrack và chuyển hướng nhiệm vụ.
2. Định tuyến typed-decision: chọn next-hop là một quyết định typed trên không gian tùy chọn được điều chế bởi nút (cạnh đi ra của nút hiện tại, cộng stop), triển khai bằng one-pass feature-MLP readouts đạt 32.8% đồng ý với lựa chọn của đội (35.6% trong không gian đã khai báo).
3. Vòng tự tiến hóa có cổng (gated self-evolution loop): mỗi tập thực thi thật trở thành dữ liệu huấn luyện, bản cập nhật chỉ được chấp nhận nếu hiệu năng đánh giá giữ nguyên ngoài ngưỡng δ = 0.005, ngược lại được hoàn tác (rollback).
4. Đo lường phân cấp route-level: độ sống nghiêm ngắt (strict survival) và khoảng cách nhầm lẫn (wrong-hop gap) trên toàn tập.

## Method
NIOCIS bao gồm: (i) đúc nhật ký thành đồ thị hành động loop-collapsed — các chuyển tiếp hành động tiến qua (E+) cùng các cạnh phục hồi (E−) mang rollback/backtrack/chuyển hướng nhiệm vụ; (ii) định tuyến bằng typed-decision router không gian tùy chọn là chính các cạnh đi ra của nút hiện tại (cộng stop), đầu ra là một phân phối được chuẩn bị mà người gọi có thể ngưỡng, các trường không chắc chắn được chuyển tới LLM; (iii) tự tiến hóa: mỗi tập thực thi thật trở thành dữ liệu huấn luyện, bản cập nhật vượt qua cổng hoàn tác và chỉ tồn tại nếu có bằng chứng, bất kỳ bản cập nhật nào thoái lui vượt ngưỡng dung sai (δ) được hoàn tác. Thiết kế đầy đủ có ngân sách bước B và giới hạn truy lại mỗi nút R. Router đọc từ một forward pass duy nhất, không sinh văn bản; các tùy chọn được định danh cấu trúc (mã định danh cạnh ổn định, không dùng tên bề mặt). Bộ xương Laya 0.3.21 (non-autoregressive typed-decision engine dựa trên ModernBERT-large encoder) với đầu về quyết định vị trí đánh dấu. Huấn luyện bằng 행동-cloning (cross-entropy) trên các tuple (trạng thái, mục tiêu, ngữ cảnh, next-hop) sao chép từ chuyển tiếp đã đăng nhập.

## KNOWLEDGE — Số liệu & khái niệm
- Bộ dữ liệu thực tế: 22.328 bản ghi (22.192 cuộc gọi công cụ + 136 bản ghi tạo văn bản) trên 1.656 vết trình từ đội agentes SOC sản xuất (tháng 9/2026), 1.615 tập, danh mục 154 tên công cụ, 4 miền (phát hiện 1.174, phản hồi 245, bảo vệ 139, nhận dạng 54, 3 tập nhỏ hợp nhất)
- Bước quyết định: 15.704 bước tiến + 2.364 lần giữ lại phục hồi = 18.068 trạng thái quyết định
- Sự kiện vòng: 4.124 lần thử lại (63,6% sự kiện vòng) + 2.364 lần quay lại (36,4%, 146 mỗi 100 tập) = 29,2% bước thực thi
- Từ vựng nút ngữ nghĩa: 77 nhãn hành động ở mẫu 50 tập → 124 ở 400 → 154 ở toàn bộ 1.615
- Cặp chuyển tiếp quan sát: 336 ở 50 tập → 1.267 ở 400 → 2.027 ở 1.000 → 2.536 ở 1.615 (702 cặp xuất hiện ở các lần quay lại phục hồi)
- 23 nhóm khả năng, 58 cạnh (50 cắt nặng nhất + 8 để không nhóm nào bị cô lập) mang 64,2% khối lượng chéo nhóm
- 3.709/14.089 bước tiến (26,3%) không rời khỏi nhóm của chúng
- Vòng săn caccia hai chiều (SIEM cảnh báo ↔ danh sách sự kiện 550/465, danh tính ↔ thông tin đe dọa 178/170, máy chủ ↔ thông tin đe dọa 171/142)
- Kết quả (Table 2, 3.875 quyết định kiểm tra): majority arm 26,8%; logistic regression 32,3%; feature MLP CE 32,8% (35,6% trong không gian đã khai báo); feature MLP CE+Brier 32,7% (35,5%); edge-ID CE 31,4% (34,1%); edge-ID CE+Brier 31,6% (34,3%); hidden-state probe CE 30,3% (32,9%); hidden-state probe CE+Brier 30,7% (33,3%); hidden-state probe edge-ID CE+Brier 28,9%; Laya zero-shot typed choice 26,6% (9,3% trong không gian đã khai báo)
- Kiểm tra cặp (Table 3): feature MLP CE+Brier − majority = +5,70 điểm, CI [+4,60, +6,9] (phân biệt rõ); edge-ID − class space (probe) = −3,79 điểm, CI [−5,01, −2,62] (phân biệt rõ)
- Nhánh theo số tùy chọn: ≤3 (263 trạng thái, 6,8%, MLP 93,9%/99,2% trong không gian); 4–10 (139 trạng thái, 3,6%, MLP 38,9%/54,0%); 11+ (3.473 trạng thái, 89,6%, MLP 27,6%/29,8%)
- Độ trễ: typed decode 10–19,5 ms p50 (GPU), MIMO Pro V2.6 LLM 2,2 s p50 (7,4 s p90), jpt-4b tinh chỉnh 244 ms/quyết định
- E3 (Table 5): MIMO Pro V2.6 mỗi hop 9,6% khớp, 100% cuộc gọi LLM/quyết định; hidden-state probe 30,7% khớp, 0% cuộc gọi LLM; typed+esc τ=0,55: 20,9% khớp, 74,1% cuộc gọi LLM; τ=0,75: 19,1%, 80,2%; τ=0,9: 16,5%, 85,0%
- Độ tin cậy: nhóm tin cậy nhất 15% giữ 91,9% độ chính xác; hành động thực tế rơi ngoài không gian tùy chọn đã khai báo ở 7,9% quyết định và ngoài top-20 của mô hình ở 9,3%
- E4: cổng từ chối 13/40 bản cập nhật ứng viên qua 10 chuỗi hạt giống đã gieo; δ = 0,005 (nửa điểm độ chính xác)
- E5 (nhật ký công khai): BPIC'12 (13.087 vụ, 262.200 sự kiện, 24 nhãn, khối lượng vòng 59,2%), BPIC'17 (31.509 vụ, 1.202.267 sự kiện, 26 nhãn, 59,3%), helpdesk (4.580 vụ, 21.348 sự kiện, 14 nhãn, 8,9%), receipt (1.434 vụ, 8.577 sự kiện, 27 nhãn, 2,9%), roadtraffic (10.002 vụ, 37.255 sự kiện, 11 nhãn, 1,4%), statechart (1 vụ, 17.912 sự kiện, 106 nhãn, 99,4%)

## INSIGHT — Cơ chế & tại sao
[Lớp typed-decision thay thế việc suy luận LLM mỗi hop] VÌ [hành động hữu hạn và quyết định lặp lại, trong khi bản ghi thực thi đã chứa câu trả lời hàng nghìn lần; một readout one-pass đọc phân phối đã chuẩn bị không sinh văn bản quyết định trong mili giây]. Điều này nghĩa là [chi phí suy luận có thể giảm hàng trăm lần đối với các quyết định định hướng lặp lại].
[Không gian tùy chọn được điều chế bởi nút勝 lợi hơn danh mục phẳng] VÌ [không gian tùy chọn được điều chế bởi nút đánh bại danh mục phẳng 155 lớp 3,5 điểm và không gian tần suất toàn cầu khớp kích thước 1,4 điểm, nhưng không thể phân biệt thống kê với không gian được điều chế bởi nút được xây dựng mà không cần duyệt đồ thị, vì vậy ích lợi đến từ việc hạn chế tùy chọn theo nút, không phải duyệt đồ thị]. Điều này nghĩa là [giới hạn ứng viên theo trạng thái hiện tại quan trọng hơn cấu trúc đồ thị].
[Vòng tự tiến hóa với cổng hoàn tác hấp thụ dégradación nhãn] VÌ [cổng từ chối bản cập nhật nếu hiệu năng đánh giá giữ nguyên ngoài δ = 0,005, và vòng hấp thụ nhiễm nhãn 12% ở vòng thứ ba]. Điều này nghĩa là [tự tiến hóa có thể an toàn nếu có cổngrollback được định rõ].
[Nhóm tin cậy nhất giữ độ chính xác cao] VÌ [phân phối đã chuẩn bị cho phép ngưỡng tin cậy, và các trường không chắc chắn được chuyển tới LLM]. Điều này nghĩa là [tính toán rẻ cho các quyết định dễ, chỉ gọi LLM khi thực sự không chắc].

## IDEA — Áp dụng được gì
1. Áp dụng [lớp định tuyến typed-decision] vào [giảm chi phí suy luận cho AI agent gọi công cụ]: bước đầu là thu thập nhật ký thực thi agent, gộp thành đồ thị hành động, sau đó huấn luyện một readout nhỏ chọn next-hop từ không gian tùy chọn của nút hiện tại, chỉ gọi LLM khi độ tin cậy thấp.
2. Áp dụng [vòng tự tiến hóa có cổng] vào [cải thiện agent theo thời gian mà không bị suy giảm]: bước đầu là thiết lập cổng đánh giá giữ nguyên với ngưỡng δ nhỏ (ví dụ 0,5 điểm), chỉ chấp nhận bản cập nhật nếu không thoái lui trên tập đánh giá giữ nguyên.
3. Áp dụng [ngưỡng tin cậy accept/escalate] vào [xếp hạng decisione rẻ vs đắt]: bước đầu là thiết lập hệ thống hai tầng: readout rẻ xử lý quyết định kiểm soát, LLM chỉ được gọi khi readout không chắc chắn (max phân phối < τ).

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Đối với các quyết định định hướng lặp lại, một readout rẻ trên không gian tùy chọn được giới hạn có thể thay thế phần lớn cuộc gọi LLM, chỉ giữ LLM cho các trường không chắc chắn. Áp dụng khi: xây dựng agent gọi công cụ với hành động hữu hạn và quyết định lặp lại. Không áp dụng khi: không có nhật ký thực thi lịch sử hoặc không gian hành động mở vô hạn.
2. Nguyên tắc: Hạn chế tùy chọn theo trạng thái hiện tại (node-conditioned option space) quan trọng hơn cấu trúc đồ thị phức tạp. Áp dụng khi: thiết kế lớp định tuyến cho agent. Không áp dụng khi: không có đồ thị hành động được điều chế từ nhật ký.

## Assumptions & Limitations
- Điều kiện phải đúng: có nhật ký thực thi agent lịch sử, hành động hữu hạn, không gian tùy chọn có thể được điều chế từ trạng thái hiện tại.
- Limitation paper thừa nhận: kết quả tham chiếu là một chính sách đại đạo thực sự thay vì một trình lập kế hoạch oracle, dữ liệu xuất đã bị xóa nội dung công cụ và nội dung trò chuyện agent, nhãn kết quả được suy ra yếu (được convention-derived, không độc lập chú thích), không có thông sốmoney/token được đoán (chỉ đoán độ trễ và cuộc gọi LLM).
- Limitation paper KHÔNG nói: không có đánh giá trên các tác vụ không phải bảo mật hoạt động; không so sánh trực tiếp với các hệ thống định tuyến mô hình/công cụ hiện có ngoài MIMO Pro V2.6 stand-in; không có chi phí triển khai thực tế của đồ thị hành động được duy trì.

## Metadata
- Năm: 2026
- Tác giả: Jin Han, Mingfeng Xin, Feng Liang, Jingtao Yu (Independent Researcher)
- Category arXiv: cs.CR
- Link PDF: https://arxiv.org/pdf/2610.25985
- arXiv ID: 2610.25985v1
- Nhãn: [applied]
- Citation count: [không tìm được]