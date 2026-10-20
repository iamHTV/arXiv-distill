# Skill: cxbench-process-compliance-evaluation

Source: 2610.25954v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần đánh giá tuân thủ quy trình của agent LLM trong các quy trình dịch vụ khách hàng được điều chỉnh (tài chính, y tế, bảo hiểm, v.v.).
- Khi muốn phát hiện các thất bại bị ẩn bởi kết quả đúng (false-pass): agent đạt kết quả kinh doanh nhưng vi phạm quy trình.
- Khi cần thiết kế hệ thống đánh giá hai tầng: kiểm tra định trị (thứ tự, quyền) + LLM judge (yêu cầu ngữ nghĩa).

## Tình huống KHÔNG nên dùng
- Khi tác vụ không có yêu cầu quy trình rõ ràng (chỉ cần kiểm tra trạng thái cuối).
- Khi không có môi trường công cụ riêng miền hoặc khách giả lập.
- Khi không có dữ liệu quy định để xây dựng rule cards.

## Input cần có
- Danh sách tác vụ với mục tiêu khách hàng, trạng thái kinh doanh ban đầu, fact riêng của khách, giao diện công cụ riêng miền, bối cảnh quy định và yêu cầu quy trình.
- Rule cards: mỗi thẻ gắn nghĩa vụ quy định trích dẫn với điều kiện áp dụng, hành động yêu cầu, bằng chứng vết tích có thể quan sát, và tiêu chí đánh giá.
- Khách giả lập (LLM cố định) mô phỏng phản hồi khách hàng.
- LLM judge (ví dụ gpt-5.6-sol) cho đánh giá yêu cầu ngữ nghĩa.
- Runtime chung để ghi lại vết tích và kiểm soát submitting.

## Các bước thực hiện
1. Xây dựng rule cards từ nghĩa vụ quy định: mỗi thẻ ghi mã định danh, nguồn trích dẫn, nghĩa vụ, bằng chứng yêu cầu, và kiểm tra định trị hoặc mục LLM judge.
2. Thiết kế tác vụ: mỗi tác vụ bao gồm yêu cầu khách, môi trường công cụ, yêu cầu quy trình, xác nhận hợp đồng (trường cần khách xem xét và xác nhận).
3. Chạy agent: agent tương tác với khách giả lập qua cuộc trò chuyện và sử dụng công cụ qua runtime chung; runtime ghi lại vết tích và kiểm soát submitting (default: agent chuẩn bị draft, runtime chỉ submit sau khi khách xác nhận).
4. Đánh giá outcome: outcome checker kiểm tra trạng thái kinh doanh cuối cùng có đáp ứng kết quả mong đợi của nhiệm vụ hay không.
5. Đánh giá process: hybrid grader kết hợp kiểm tra định trị (thứ tự sự kiện, quyền công cụ, sự đồng nhất giữa trường đã xác nhận và đã gửi) và LLM judge (danh sách kiểm tra riêng nhiệm vụ) cho yêu cầu ngữ nghĩa.
6. Tính verdict: overall success chỉ khi cả outcome và process pass; false-pass = outcome pass ∧ process fail.
7. So sánh mô hình: theo dõi outcome-pass rate, both-pass rate, false-pass rate theo từng mô hình.

## Output mong đợi
- Báo cáo đánh giá: outcome-pass rate, both-pass rate, false-pass rate theo từng mô hình và từng miền.
- Danh sách false-pass để xem xét rủi ro tuân thủ tiềm ẩn.
- Quyết định cải thiện agent: thêm quy trình kiểm tra, điều chỉnh prompt, hoặc thay đổi runtime submitting.

## Ví dụ áp dụng
Một ngân hàng sử dụng agent LLM để xử lý kháng cáo giao dịch không được phép. CXBENCH đánh giá agent không chỉ dựa trên việc kháng cáo đã được nộp hay chưa (outcome), mà còn xem agent đã cung cấp thông báo xác nhận viết liền khi nhận thông báo lỗi bằng lời hay không (process). Nếu agent nộp đúng kháng cáo nhưng thiếu thông báo, đây là false-pass — outcome-only scoring sẽ đếm là thành công, nhưng CXBENCH đánh dấu là vi phạm quy trình theo Regulation E.

## Gotchas
- Không để từ tiếng Anh không giải thích: process compliance (tuân thủ quy trình), outcome (kết quả), false-pass (lượt qua kết quả nhưng trượt quy trình), rule card (thẻ quy tắc), hybrid grader (bo chấm điểm lai), deterministic check (kiểm tra định trị), LLM judge (LLM làm thẩm phán), mediated-submit (submit được trung gian), direct-submit (submit trực tiếp), confirmation contract (hợp đồng xác nhận), customer simulator (khách giả lập), trace (vết tích), semantic requirement (yêu cầu ngữ nghĩa), Wilson 95% CI (khoảng tin cậy Wilson 95%), McNemar test (kiểm tra McNemar), Holm correction (điều chỉnh Holm), Kendall's τb (hệ số Kendall tau-b), regulated domain (miền được điều chỉnh), disclosure (thông báo), consent (đồng ý), submission authority (thẩm quyền gửi), draft confirmation (xác nhận bản thảo), written confirmation (xác nhận viết), regulatory obligation (nghĩa vụ quy định), trace evidence (bằng chứng vết tích), event ordering (thứ tự sự kiện), tool permission (quyền công cụ), confirmation-submission agreement (sự đồng nhất xác nhận-gửi).
- Không có dữ liệu chi phí inference thực tế của hybrid grader.
- Không so sánh trực tiếp với các benchmark khác ngoài bảng 1.
- Không đánh giá trên các tác vụ ngoài dịch vụ khách hàng được điều chỉnh.
- Judge development không phải tập xác thực độc lập (chỉ là vết định khía).