# 2610.32004 — CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments

## Giá trị cốt lẽ (1 câu)

CRM-Agent-Bench là tiêu chuẩn đánh giá agent sử dụng công cụ (tool-using agents) trong môi trường doanh nghiệp có trạng thái (stateful), gồm 555 tác vụ đa lượt (multi-turn) trải qua 9 miền kinh doanh và 36 thẻ năng lực (capability tags) —strict success trên 16 hệ thống nằm trong khoảng 64,32% đến 83,60%, cho thấy agent hiện tại vẫn khó thực hiện quy trình kinh doanh đa giai đoạn một cách chính xác và tuân thủ chính sách.

## Problem

Triển khai agent ngôn ngữ trong ứng dụng thực tế đòi hỏi nhiều hơn chỉ trả lời đúng: agent phải thực hiện đúng quy trình kinh doanh đa giai đoạn, tuân thủ quy tắc đặc thù miền (domain-specific rules), và tương tác với người dùng qua các cuộc đối thoại. Khoảng cách giữa "nói" và "làm" (saying vs doing) là khoảng cách giữa khách hàng hài lòng và tổn thất thực. Các tiêu chuẩn hiện tại thường chỉ đánh giá câu trả lời cuối cùng, không kiểm tra xem agent có thực hiện đúng công cụ, tham số, thứ tự và trạng thái mục tiêu hay không.

## Contribution

1. **CRM-Agent-Bench**: Tiêu chuẩn đánh giá thực thi-grounded (execution-grounded) gồm 555 tác vụ trạng thái (stateful), đa lượt (multi-turn) trên 9 miền kinh doanh và 36 thẻ năng lực.
2. **Hợp đồng thực thi (executable contract)**: Mỗi tác vụ cung cấp hợp đồng thực thi đặc thù, được rút ra từ các kiểm tra trên hành động, đối số, thứ tự, phản hồi, trạng thái mục tiêu và trạng thái được bảo vệ (protected state); thành công là sự kết hợp chặt chẽ (strict conjunction) của các kiểm tra được khai báo cho tác vụ đó.
3. **Đánh giá hệ thống agent đầy đủ**: Đánh giá toàn bộ hệ thống agent thông qua các hợp đồng này và báo cáo coverage được chấm điểm (scored coverage), độ trễ (latency) và chi phí (cost).
4. **Kết quả**: Trên 16 hệ thống được đánh giá trên bản phát hành đã kiểm toán (audited final release), strict success nằm trong khoảng 64,32% đến 83,60%; các hệ thống dẫn đầu nhóm chặt chẽ khác biệt mạnh về chi phí và độ tin cậy theo từng miền.

## Method

CRM-Agent-Bench xây dựng mỗi tác vụ như một hợp đồng thực thi (executable contract) bao gồm:

1. **Kiểm tra trên hành động (action checks)**: Agent có gọi đúng công cụ hay không.
2. **Kiểm tra trên đối số (argument checks)**: Agent có truyền đúng tham số hay không.
3. **Kiểm tra trên thứ tự (order checks)**: Agent có thực hiện các thao tác theo thứ tự đúng hay không.
4. **Kiểm tra trên phản hồi (response checks)**: Agent có trả lời đúng nội dung hay không.
5. **Kiểm tra trên trạng thái mục tiêu (target state checks)**: Trạng thái hệ thống sau khi thực hiện có đúng không.
6. **Kiểm tra trên trạng thái được bảo vệ (protected state checks)**: Agent có thực hiện hành động cấm trên trạng thái bảo vệ hay nicht.

Thành công là sự kết hợp chặt chẽ của tất cả các kiểm tra được khai báo cho tác vụ. Tiêu chuẩn báo cáo scored coverage (tỷ lệ các kiểm tra được đáp ứng), latency (độ trễ thực thi) và cost (chi phí thực thi).

## KNOWLEDGE — Số liệu & khái niệm

- 555 tác vụ trạng thái, đa lượt, trải qua 9 miền kinh doanh.
- 36 thẻ năng lực (capability tags).
- 16 hệ thống agent được đánh giá.
- Strict success: 64,32% đến 83,60%.
- Các hệ thống dẫn đầu khác biệt mạnh về chi phí và độ tin cậy theo từng miền.
- Dự án: https://github.com/salesforce-misc/crm-agent-bench
- Trang dự án: https://crm-agent-bench.github.io/

## INSIGHT — Cơ chế & tại sao

[Strict success thấp (64,32%–83,60%)] xảy ra VÌ [agent hiện tại vẫn gặp khó khăn trong việc thực hiện quy trình kinh doanh đa giai đoạn một cách chính xác — gọi sai công cụ, truyền sai tham số, thực hiện sai thứ tự, hoặc vi phạm trạng thái được bảo vệ]. Điều này nghĩa là [đánh giá chỉ bằng câu trả lời cuối cùng ẩn tẩy các lỗi thực thi trong quá trình làm việc].

[Các hệ thống dẫn đầu khác biệt mạnh về chi phí và độ tin cậy theo miền] xảy ra VÌ [không có hệ thống nào tối ưu tất cả — một số hệ thống đạt độ chính xác cao nhưng tốn kém, một số hệ thống rẻ nhưng kém tin cậy ở một số miền]. Điều này nghĩa là [cần cân bằng giữa chất lượng, chi phí và độ tin cậy theo miền khi chọn agent cho doanh nghiệp].

## IDEA — Áp dụng được gì

1. Xây dựng hợp đồng thực thi (executable contract) cho agent nội bộ: Trước khi triển khai agent xử lý quy trình kinh doanh, hãy định nghĩa các kiểm tra rõ ràng trên hành động, đối số, thứ tự, phản hồi, trạng thái mục tiêu và trạng thái được bảo vệ. Bước đầu: liệt kê các bước bắt buộc trong quy trình và viết kiểm tra tự động cho mỗi bước.

2. Đánh giá agent theo scored coverage, latency và cost: Không chỉ đo accuracy cuối cùng, mà hãy đo tỷ lệ các kiểm tra được đáp ứng, độ trễ thực thi và chi phí mỗi tác vụ. Bước đầu: thiết lập metrics theo ba chiều này cho mỗi agent ứng viên.

3. Kiểm tra trạng thái được bảo vệ (protected state): Xác định các trạng thái hệ thống không được phép agent thay đổi (ví dụ: số dư tài khoản, mức giảm giá tối đa) và xây dựng kiểm tra chặn agent thực hiện hành động cấm. Bước đầu: liệt kê các trạng thái bảo vệ trong hệ thống của bạn và viết rule chặn.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong hệ thống agent doanh nghiệp, khả năng thực thi đúng quy trình quan trọng bằng với khả năng trả lời đúng — agent không được phép chỉ "nói" đã làm mà phải thực sự "làm" đúng mọi bước.
- Khi nào dùng: Khi xây dựng agent thực hiện quy trình kinh doanh có trạng thái (CRM, kế toán,供应�en, v.v.).
- Khi nào KHÔNG dùng: Agent chỉ trả lời câu hỏi, không thực hiện hành động trên hệ thống.
- Ví dụ áp dụng ngoài domain gốc: Trong ngân hàng, agent duyệt khoản vay không được chỉ trả lời "duyệt" mà phải thực hiện đúng mọi bước kiểm tra thu nhập, lịch sử tín dụng,담보 và không được phép thay đổi trạng thái bảo vệ như mức vốn điều lệ.

## Assumptions & Limitations

- Điều kiện phải đúng: tác vụ có trạng thái (stateful) với các kiểm tra có thể thực thi; môi trường doanh nghiệp có quy tắc rõ ràng.
- Limitation paper thừa nhận: tiêu chuẩn tập trung vào môi trường CRM; 16 hệ thống được đánh giá có thể không đại diện cho tất cả agent trong thị trường.
- Limitation paper KHÔNG nói: hiệu quả trên các miền không phải CRM; chi phí duy trì hợp đồng thực thi ở quy mô lớn; tính generalize qua các framework agent khác nhau.

## Metadata

- Năm: 2026
- Tác giả: Monojit Banerjee, Zhujun Lan, Defu Cao
- Category arXiv: cs.AI (Salesforce)
- Link PDF: https://arxiv.org/pdf/2610.32004
- Citation count: chưa có (paper mới, Oct 2026)