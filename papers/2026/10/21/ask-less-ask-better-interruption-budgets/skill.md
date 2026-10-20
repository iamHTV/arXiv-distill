# Skill: interruption-budget-user-attention-cost

Source: 2610.24411v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần đánh giá gánh nặng người dùng khi agent LLM chủ động hỏi câu làm rõ trong dịch vụ khách hàng.
- Khi muốn giới hạn số câu hỏi agent hỏi mỗi phiên (interruption budget) và đo chất lượng câu hỏi (user-attention cost).
- Khi cần xây dựng agent memory-guided review để lọc câu hỏi không đáng hỏi trước khi đưa ra người dùng.

## Tình huống KHÔNG nên dùng
- Khi chỉ cần đếm số tương tác agent-người dùng đơn giản.
- Khi không có người dùng mô phỏng tiết lộ sở thích chỉ khi được hỏi.
- Khi không có LLM judge để đánh giá đọc nỗ lực và giá trị câu hỏi.

## Input cần có
- Yêu cầu ban đầu của người dùng và các tác vụ dịch vụ khách hàng.
- Công cụ để agent tìm kiếm thông tin (mã đơn hàng, hồ sơ khách hàng, v.v.).
- Người dùng mô phỏng tiết lộ thông tin chỉ khi được hỏi.
- LLM judge đánh giá đọc nỗ lực (5 chiều: mục tiêu rõ ràng, yêu cầu đơn lẻ, nỗ lực trả lời, khả năng hành động, tính súc tích) và giá trị câu hỏi (4 tiêu chí: thiếu, không truy xuất được, cần cho tác vụ, do người dùng cung cấp).
- Ngân sách câu hỏi N (1–3 câu hỏi cho dịch vụ khách hàng).
- Bộ nhớ持久 lưu câu trả lời trước của người dùng và bằng chứng tác vụ (dành cho MGR).

## Các bước thực hiện
1. Thiết lập interruption budget: giới hạn số câu hỏi sh�� đoán mỗi phiên (N=1–3 cho dịch vụ khách hàng).
2. Định nghĩa câu hỏi shifty: làm rõ, xác nhận, yêu cầu đáp lại gợi ý sau yêu cầu ban đầu; các giao dịch bắt buộc (xác thực, xác nhận bắt buộc) miễn trừ.
3. Tính user-attention cost: Afull(τ) = Σ(1 + κeff·e(q) + κval·w(q)), κeff=κval=1; e(q)=1−r(q)/20 (đọc nỗ lực, 5 chiều, 0–20); w(q)=1−v(q)/10 (giá trị câu hỏi, 4 tiêu chí, 0–10).
4. Chạy agent với ngân sách: khi ngân sách còn, câu hỏi shifty đi đến self-review (APPROVE/SUBSTITUTE/BLOCK); khi hết, từ chối các yêu cầu shifty tiếp theo.
5. Áp dụng memory-guided review (tùy chọn): self-review kiểm tra câu hỏi đối với bộ nhớ持久 (câu trả lời trước của người dùng, tóm tắt tác vụ, liên kết bằng chứng), APPROVE câu chỉ người dùng có thể trả lời, SUBSTITUTE câu rõ ràng hơn, BLOCK câu câu trả lời đã có trong bộ nhớ hoặc tìm bằng công cụ.
6. Đánh giá: phần thưởng tác vụ R(τ), chi phí chú ý người dùng Afull(τ), tiện ích Uλ(τ) = R(τ) − λAfull(τ) (λ=0.03), giá trị câu hỏi V(q).
7. So sánh các agent tại cùng chi phí chú ý thay vì cùng số câu hỏi.

## Output mong đợi
- Báo cáo đánh giá: phần thưởng tác vụ, chi phí chú ý người dùng, giá trị câu hỏi, tiện ích cho từng mô hình và từng ngân sách.
- Danh sách câu hỏi bị chặn (blocked) bởi memory-guided review.
- Quyết định ngân sách tối ưu cho từng mô hình (mô hình hỏi hiệu quả nhất nên được phép hỏi nhiều hơn).

## Ví dụ áp dụng
Một agent hỗ trợ khách hàng mua sắm trực tuyến. Khách yêu cầu "tôi muốn thay size lớn hơn cho nước hoa đã đặt". Agent không giới hạn hỏi 3 câu: "Mã đơn hàng là gì?", "Bạn muốn đổi size nào?", "Phương thức thanh toán?". Với interruption budget N=1 và memory-guided review, agent tra cứu đơn hàng bằng công cụ, thấy chỉ có 1 đơn hàng, và hỏi duy nhất một câu: "Tôi tìm thấy nước hoa woody 100ml lớn hơn. Bạn muốn đổi đơn hàng hiện tại của mình không?". Chi phí chú ý giảm từ 3 câu xuống 1 câu, phần thưởng tác vụ giữ nguyên.

## Gotchas
- Không để từ tiếng Anh không giải thích: interruption budget (ngân sách gián đoạn), user-attention cost (chi phí chú ý người dùng), reading effort (nỗ lực đọc), question value (giá trị câu hỏi), avoidability cost (chi phí có thể tránh), discretionary question (câu hỏi tự ý), policy-required exchange (giao dịch bắt buộc bởi chính sách), memory-guided review (xem lại được hướng dẫn bởi bộ nhớ), persistent memory (bộ nhớ持久), APPROVE/SUBSTITUTE/BLOCK (duyệt/thay thế/chặn), utility (tiện ích), break-even valuation (giá trị ngưỡng đá vỡ), asking efficiency (hiệu quả hỏi), judged question value (giá trị câu hỏi được đánh giá), elicitation recall (tỷ lệ thu thập lại), human-validated LLM judge (LLM thẩm phán được xác thực bởi con người).
- Không có chi phí inference thực tế của self-review và bộ nhớ (ước tính trước: 1.8 cuộc gọi mô hình + 15k token/phiên).
- Không đánh giá trên các tác vụ ngoài dịch vụ khách hàng và nghiên cứu tương tác.
- Không so sánh trực tiếp với các agent không hỏi.
- Kết quả phụ thuộc vào mức độ thẳng thắn của người dùng mô phỏng.