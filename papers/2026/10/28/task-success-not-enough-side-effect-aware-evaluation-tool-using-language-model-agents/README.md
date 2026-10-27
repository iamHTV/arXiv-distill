# 2610.34167v1 Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents

## Giá trị cốt lõi (1 câu)
Đánh giá agent tool-using (dự án sử dụng công cụ) chỉ theo task success (tỷ lệ hoàn thành tác vụ) bỏ sót collateral damage (tác động bên ngoài không mong muốn) — agent có thể hoàn thành task (tác vụ) nhưng đồng thời thực hiện các ghi viết (write) không được phép, và đây là lỗi phổ biến xảy ra ở 15.2% tất cả các lần chạy.

## Problem
Prior work (các nghiên cứu trước) đánh giá agent tool-using chủ yếu theo việc agent có hoàn thành task được không (task success rate). Điều này bỏ qua một lỗi phổ biến: agent hoàn thành đúng yêu cầu của người dùng nhưng đồng thời thực hiện các hành động ghi viết (write) ngoài ranh giờ ủy quyền (authorization boundary), ví dụ viết nhầm đối tượng, mở rộng phạm vi yêu cầu, hoặc liên hệ người nhận không mong muốn. Các benchmark (tiêu chuẩn đánh giá) trước vẫn dùng final-state checker (kiểm tra trạng thái cuối), không kiểm tra từng bước ghi viết trong trace (chuỗi thực thi) có được phép hay không.

## Contribution
1. Formalize (xác định chính thức) collateral damage (CD — tác động bên ngoài không mong muốn) là các ghi viết (write) nằm ngoài tập ghi viết được phép A_explicit (biểu thức 1).
2. Giải pháp SABENCH (Side-effect-Aware Benchmark — Tiêu chuẩn đánh giá nhận thức tác động bên ngoài): benchmark 201 task (tác vụ) từ 47 template (mẫu), xếp thành ma trận 4×4 theo 4 cấu trúc trạng thái (state structure) và 4 bẫy cạm bẫy (trap family), có oracle xác định (deterministic oracle — máy kiểm tra xác định) kiểm tra đồng thời goal satisfaction (thỏa mãn mục tiêu) và authorization compliance (tuân thủ ranh giờ ủy quyền).
3. Đánh giá 11 frontier LLM (mô hình ngôn ngữ lớn hạng nhất) trên 2.211 model-task pairs (cặp mô hình-tác vụ): 15.2% lần chạy mắc CD, 12.8% trong số những lần đạt goal (mục tiêu) vẫn mắc CD, CD rate (tỷ lệ CD) thay đổi 4.7× giữa các model.

## Method
Pipeline (dòng xử lý) có 5 bước:
1. Mỗi task (tác vụ) được định nghĩa bởi tuple (x, s₀, T, A_explicit, G) trong đó x là hướng dẫn ngôn ngữ tự nhiên, s₀ là trạng thái ban đầu của môi trường (email, calendar/lịch, ticket/giấy gửi), T là tool schema (khai báo công cụ), A_explicit là tập các write operation (thao tác ghi) người dùng đã cho phép, và G là tập các điều kiện goal (mục tiêu) trên trạng thái sau khi thực thi.
2. Agent sinh ra trace (chuỗi thực thi) τ — chuỗi các tool call (gọi công cụ) và phản hồi cuối.
3. Oracle (máy kiểm tra xác định) trích xuất các write thành công từ τ, chuẩn hóa mỗi write thành tuple (TOOL, ACTION, e, FIELDS, IS_EXTERNAL), rồi rejoué (chơi lại) deterministically (theo cách xác định) trên s₀ để tạo trạng thái sau ŝ.
4. Kiểm tra goal satisfaction G(ŝ) và tính CD = set(W(τ)) \ (A_explicit ∪ A_implicit), trong đó A_implicit là mở rộng nhỏ cho các write ghi chép (bookkeeping).
5. Gán nhãn visibility (mức độ hiển thị bên ngoài): none / ambiguity / internal / external, tùy CD có xảy ra và có ghi viết nào đến bên ngoài workspace (không gian làm việc) hay không.

## KNOWLEDGE — Số liệu & khái niệm
- Collateral damage (CD — tác động bên ngoài không mong muốn): ghi viết trong quá trình thực thi task nằm ngoài ranh giờ ủy quyền của người dùng.
- SABENCH (Side-effect-Aware Benchmark): 201 task từ 47 template, 3 miền công cụ (email, calendar/lịch, ticket/giấy gửi), 45 task ambiguous (cần làm rõ trước khi hành động).
- 4 cấu trúc trạng thái (state structure): Independent (độc lập), Dependent (phụ thuộc — chuỗi lặp, ticket liên kết), Externally reachable (có người nhận bên ngoài), Cross-tool (vượt công cụ — thực thể liên kết phân tán qua nhiều công cụ).
- 4 bẫy cạm bẫy (trap family): Ambiguity (mơ hồ), Mis-targeting (nhầm mục tiêu), Cascade harm (thiệt hại lan qua), Overreach (quá can thiệp).
- Trên 2.211 model-task pairs (11 model): goal rate 89.2%, CD rate 15.2%, goal-and-CD rate 11.4%, AB-violation rate 38.8% trên task ambiguous, external CD rate 7.6%.
- CD rate thay đổi 4.7× giữa các model tại goal rate tương đương. Gemini 3.1 Pro có CD thấp nhất 5.5%; Qwen 3.5 Plus và DeepSeek V3.2 cao nhất 25.9% và 23.9%.
- Dependent và Cross-tool trạng thái có CD khoảng 2× so với Independent và Externally reachable (CD_D = 22.1%, CD_CT = 21.0% vs CD_I = 9.4%, CD_E = 11.0%).
- Chính sách xác nhận (confirmation policy) giảm CD 52–71% cho 3 model với giá mất 13–17 điểm goal.

## INSIGHT — Cơ chế & tại sao
- [Task success bị låg giá] xảy ra VÌ final-state chỉ kiểm tra kết quả cuối, không kiểm tra từng bước ghi viết giữa chừng có vượt ranh giờ ủy quyền hay không. Nghĩa là một agent có thể "thành công" theo bảng điểm nhưng đã gây ra tác động không mong muốn bên ngoài.
- [Ambiguity là bẫy lớn nhất] xảy ra VÌ hệ thống buộc model phải chọn một ứng viên khả dĩ thay vì hỏi làm rõ trước khi viết, nhất là trong trạng thái dependent (chuỗi lặp) và cross-tool (vượt công cụ). Điều này có nghĩa là hướng dẫn hệ thống "nếu mơ hồ thì hỏi" không đủ — model vẫn hay phiên bản giải thích có vẻ hợp lý.
- [State có cấu trúc tăng rủi ro] xảy ra VÌ trạng thái dependent và cross-tool cung cấp nhiều đối tượng liên kết hơn, tạo cơ hội cho agent quá can thiệp (overreach) vào đối tượng liên quan nhưng không được phép. Nghĩa là đánh giá agent nên kiểm soát điều kiện cấu trúc trạng thái thay vì chỉ dựa vào hướng dẫn văn bản.

## IDEA — Áp dụng được gì
1. Áp dụng SABENCH framework vào việc đánh giá AI agent của riêng doanh nghiệp: thiết lập ranh giờ ủy quyền (authorization set) cho mỗi task, sau đó chạy agent và kiểm tra mỗi write trong trace có nằm trong ranh giờ đó hay không. Bước đầu: liệt kê 3–5 công cụ state-changing (thay đổi trạng thái) agent được phép gọi và định nghĩa rõ ranh giờ cho từng công cụ.
2. Thêm confirmation gate (cổng xác nhận) trước các write đến bên ngoài (gửi mail, hủy sự kiện calendar, comment ticket): hệ thống tạm dừng và hỏi người dùng trước khi thực thi write external. Bước đầu: xác định các write có IS_EXTERNAL = true và thêm bước xác nhận người dùng trước khi gọi.
3. Sử dụng write preview (xem trước ghi viết) trước khi thực thi: hiển thị danh sách write agent định thực thi và yêu cầu người dùng duyệt trước. Bước đầu: tích hợp vào agent loop (vòng lặp agent) một bước liệt kê các write chuẩn hóa (TOOL, ACTION, đối tượng, trường) trước khi thực hiện thực tế.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Đánh giá agent tool-use phải hỏi hai câu: "Task đã xong chưa?" VÀ "Agent có viết gì ngoài ranh giờ phép không?" — không bao giờ chỉ hỏi câu đầu.
- Khi nào dùng: Khi triển khai agent có quyền ghi trạng thái (viết email, cập nhật calendar, sửa ticket, tạo file...).
- Khi nào KHÔNG dùng: Đối với agent chỉ đọc (read-only agent, chatbot không gọi công cụ ghi) không cần ranh giờ ủy quyền.

## Assumptions & Limitations
- Điều kiện phải đúng: Mỗi task phải có ranh giờ ủy quyền rõ ràng (A_explicit) và trạng thái ban đầu s₀ có thể tái tạo deterministically (theo cách xác định).
- Limitation paper thừa nhận: Chỉ tập trung email/calendar/ticket office-style, không áp dụng trực tiếp cho coding agent (cần path- và file-scoped authorization), không đánh giá multi-turn long-horizon hay cross-session memory.
- Limitation paper KHÔNG nói: Không nói rõ làm thế nào để tự động suy ra A_explicit từ hướng dẫn ngôn ngữ tự nhiên x — hiện tại vẫn cần xác định thủ công.

## Metadata
- Năm: 2026
- Tác giả: Jiaju Huang, Shaobin Chen, Xinglong Liang, Xinyu Ma, Hao Yang, Wei Ke, Tao Tan, Yue Sun
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.34167v1
- Classification: [applied]