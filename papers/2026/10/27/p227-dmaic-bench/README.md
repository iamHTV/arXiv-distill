# 2610.32305 — DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks

## Giá trị cốt lẽ (1 câu)

DMAIC-Bench là tiêu chuẩn đánh giá khả năng "tự kiềm chế" (self-restraint) của agent: việc dừng hoặc chuyển hướng khi bằng chứng chỉ ra điều kiện tiên quyết chưa đạt — không phải chỉ phán xét chất lượng đầu ra. Kết quả cho thấy 13 mô hình đạt 92% độ chính xác trên quyết định tiếp tục (GO) nhưng chỉ 19% trên quyết định dừng (NO-GO), và 47% quyết định NO-GO được kiểm duyệt có báo cáo hành động trên bằng chứng không hợp lệ.

## Problem

Các tiêu chuẩn agent hiện đại đoán chủ yếu việc hoàn thành tác vụ (task completion) hoặc chất lượng artifacts cuối cùng, không kiểm tra xem agent có sử dụng bằng chứng trung gian để quyết định tiếp tục, chuyển hướng hay dừng ở mỗi giai đoạn phân tích đa giai đoạn. Việc tự phản biện (self-reflection) — agent phán xét đầu ra của mình — không chứng minh rằng bằng chứng đã thay đổi hành động tiếp theo. Khả năng đó gọi là "tự kiềm chế" (self-restraint) và chưa được đánh giá trong bất kỳ tiêu chuẩn agent nào.

## Contribution

1. **DMAIC-Bench**: Tiêu chuẩn đánh giá self-restraint với 97 tác vụ đa giai đoạn_seed_ (seeded) trải qua 15 trường hợp công nghiệp trong 4 lĩnh vực, xây dựng trên các điều kiện tiên quyết thống kê rõ ràng của Lean Six Sigma (chu kỳ Define–Measure–Analyze–Improve–Control).
2. **Biến thể đối lập kếp (paired counterfactual variants)**: Yêu cầu các hành động ngược lại ở cùng vị trí quy trình, phân biệt việc kiềm chế có lý do (warranted restraint) và việc dừng không phân biệt (indiscriminate stopping).
3. **Đánh giá bằng chấm điểm dấu vết thực thi (execution trace scoring)** và đánh giá chuyên gia độc lập (independent expert review): bất kỳ tính toán cấm đoán (forbidden downstream computation) nào sau khi chẩn đoán không đạt đều được tính là lỗi định tuyến (route error), ngay cả khi báo cáo không khẳng định kết quả đó.
4. **Mở rộng sinh học**: 16 tác vụ sinh học (RNA-seq, GWAS) chứng minh khung làm việc có thể đánh giá quyết định phụ thuộc bằng chứng ngoài quy trình công nghiệp.

## Method

DMAIC-Bench xây dựng mỗi trường hợp (case) là một đồ thị quyết định được bảo vệ (guarded decision graph) với các nút Entscheidung được đánh giá (graded forks). Tại mỗi nút, agent phải sử dụng bằng chứng chẩn đoán để quyết định tiến hành (GO), chuyển hướng (divert), thu thập dữ liệu khắc phục hoặc dừng (NO-GO).

**Đánh giá:**
- 13 mô hìnhranh giới (frontier models) từ 6 nhà cung cấp, mỗi mô hình hoàn thành 3 lần thử độc lập trên mỗi tác vụ.
- Mỗi tập phương án hoàn chỉnh đi qua 300 quyết định đã đánh giá: 52 quyết định NO-GO và 248 quyết định GO.
- 40 cặp đối lập (matched forks) ghép tất cả 52 trường hợp NO-GO với 146 GO tương đương về cấu trúc (topologically identical), cách ly vai trò của dữ liệu đã gieo (seeded data) giữ nguyên vị trí quy trình.
- Chấm điểm bằng điểm số riêng (private scorer) đọc dấu vết thực thi; khẳng định cuối cùng được đánh giá qua đánh giá chuyên gia độc lập (blinded expert review).
- Các số liệu: pass@k (tỷ lệ tác vụ thành công ít nhất một lần trong k lần thử) và pass_k (tỷ lệ thành công trên tất cả k lần thử).
- Không cung cấp khung agent độc quyền hoặc bộ điều chỉnh prompt tùy chỉnh (custom prompt adapters) để giữ tính trung lậpقييم.

## KNOWLEDGE — Số liệu & khái niệm

- 97 tác vụ đa giai đoạn seeded, 15 trường hợp công nghiệp, 4 lĩnh vực; 8 trường hợp cải编 từ báo cáo cải thiện thước đen (black-belt improvement projects) thực tế.
- 13 mô hình từ 6 nhà cung cấp.
- Độ chính xác định tuyến (routing execution-level accuracy) trung bình 92% trên quyết định GO khớp, khoảng tin cậy 86–97.
- Độ chính xác trên quyết định NO-GO chỉ 19%, khoảng tin cậy 8–30; khoảng cách 73 điểm (khoảng tin cậy 59–87).
- 174 trường hợp: agent chạy tính toán cấm đoán sau khi ghi chẩn đoán không đạt.
- Đánh giá chuyên gia mù (blinded expert audit) của 11 agent: 47% quyết định NO-GO đạt được có báo cáo hành động trên bằng chứng không hợp lệ, khoảng tin cậy 31%–61%.
- Chỉ 0–7 số trường hợp của một số agent nhận diện đúng tất cả các điều kiện tiên quyết không đạt.
- 12/13 agent vẫn dưới 50% độ chính xác NO-GO ngay cả sau khi được phép dừng rõ ràng (explicit stopping permission).
- Mở rộng sinh học: 16 tác vụ RNA-seq và GWAS cho thấy khung làm việc có thể truyền hóa (transfer).

## INSIGHT — Cơ chế & tại sao

[Khoảng cách 73 điểm giữa GO và NO-GO] xảy ra VÌ [agent đang tốt trong việc tiếp tục khi bằng chứng hỗ trợ, nhưng kém trong việc dừng khi bằng chứng phản đối — tự phản biện chỉ phán xét đầu ra mà không chứng minh bằng chứng đã thay đổi hành động tiếp theo]. Điều này nghĩa là [đánh giá agent chỉ bằng kết quả cuối cùng ẩn tẩy khuyết điểm trong việc quản lý hành trình phân tích (trajectory management)].

[Báo cáo hành động trên bằng chứng không đạt ở 47% quyết định NO-GO] xảy ra VÌ [các agent thường đưa ra chẩn đoán chính xác nhưng vẫn thực hiện các phân tích mà kết quả đó cấm đoán, hoặc báo cáo bỏ qua kết quả cấm đoán]. Điều này nghĩa là [khả năng chẩn đoán đúng không đủ — agent cần govern hành trình dựa trên bằng chứng đã tính toán].

[Quyền dừng rõ ràng giúp một số model nhưng không khôi phục nhất quán quyết định đúng ở cả hai nhánh GO và NO-GO] xảy ra VÌ [việc cho phép dừng không giải quyết vấn đề gốc: agent cần nhận diện điều kiện tiên quyết không đạt và hành động dựa trên nó, không chỉ được phép dừng]. Điều này nghĩa is [cần can thiệp vào cơ chế ra quyết định dựa trên bằng chứng, không chỉ là cho phép dừng].

## IDEA — Áp dụng được gì

1. Xây dựng nút kiểm tra (checkpoint) trong pipeline agent đa giai đoạn: trước khi agent thực hiện phân tích tốn kém, bắt buộc agent phải xác nhận điều kiện tiên quyết đã đạt từ kết quả bước trước. Bước đầu: thêm một bước "gate" giữa các giai đoạn xử lý dữ liệu, agent phải ghi nhận điều kiện tiên quyết OK/FAILED trước khi tiếp tục.

2. Dùng thiết kế tác vụ đối lập (counterfactual task design) để kiểm tra agent: tạo cặp tác vụ tương tự nhưng dữ liệu đầu vào gieo dẫn đến chẩn đoán ngược lại, yêu cầu agent thực hiện hành động ngược lại ở cùng vị trí quy trình. Bước đầu: trong bộ đánh giá agent nội bộ, tạo cặp tác vụ mirror với kết quả chẩn đoán đối lập và đo xem agent có thay đổi hành động hay không.

3. Áp dụng đánh giá chuyên gia mù (blinded expert review) vào báo cáo agent: chuyên gia không biết kết quả đánh giá tự động xem báo cáo của agent có hành động trên bằng chứng không hợp lệ hay không. Bước đầu: chọn mẫu báo cáo agent thất bại, gửi cho chuyên gia đánh giá mù xem có vi phạm bằng chứng hay không.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong hệ thống agent phân tích đa giai đoạn, khả năng dừng hoặc chuyển hướng dựa trên bằng chứng quan trọng bằng với khả năng tiếp tục — agent có thể đưa ra chẩn đoán chính xác nhưng vẫn thực hiện hành động cấm đoán nếu không kiềm chế được bản thân.
- Khi nào dùng: Quy trình agent phân tích có nhiều giai đoạn, mỗi giai đoạn phụ thuộc vào kết quả giai đoạn trước (ví dụ: phân tích dữ liệu kinh doanh, nghiên cứu khoa học, kiểm soát chất lượng).
- Khi nào KHÔNG dùng: Tác vụ đơn giai đoạn, không có điều kiện tiên quyết cần kiểm tra trước khi hành động.
- Ví dụ áp dụng ngoài domain gốc: Trong quy trình duyệt tín dụng ngân hàng, trước khi duyệt khoản vay, hệ thống phải xác nhận tất cả điều kiện tiên quyết (thu nhập, lịch sử tín dụng,담보) đã đạt — một agent có thể nhận diện được rủi ro nhưng vẫn phải được kiềm chế không duyệt nếu điều kiện không đạt.

## Assumptions & Limitations

- Điều kiện phải đúng: tác vụ có dữ liệu gieo (seeded data) với điều kiện tiên quyết thống kê rõ ràng; môi trường hộ cát (sandbox) có thể kiểm soát truy cập dữ liệu.
- Limitation paper thừa nhận: đây là preprint (chưa được đánh giá bằng đồng nghiệp); bộ đánh giá tự động là private scorer (không công khai hoàn toàn); 13 mô hìnhranh giới có thể không đại diện cho tất cả agent mã nguồn mở.
- Limitation paper KHÔNG nói: hiệu quả trên tác vụ không có điều kiện tiên quyết thống kê rõ ràng; chi phí đánh giá chuyên gia mù ở quy mô lớn; tính generalize qua các framework agent khác nhau bên ngoài Harbor 0.22.0.

## Metadata

- Năm: 2026
- Tác giả: Shan Peng, Shuaiqi Cheng, Miao Peng, Chenyi Zi, Jia Li
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.32305
- Citation count: chưa có (paper mới, Oct 2026)