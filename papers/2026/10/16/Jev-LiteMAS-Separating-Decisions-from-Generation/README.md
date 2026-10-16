# [2610.21411v1] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

## Problem
Nhiều hệ thống multi-agent (MAS - hệ thống đa đại lý) dùng mô hình generative (tạo sinh) để làm mọi thứ, bao gồm cả việc chọn chuyên gia tiếp theo và đánh giá chất lượng artifact (phối phẩm trung gian). Việc này vô lý vì các thao tác điều phối chỉ ra ra quyết địnhBounded (giới hạn) như ID chuyên gia hoặc pass/escalate. Dùng LLM lớn cho mọi quyết định tốn token giữa các bước đóng góp của chuyên gia.

## Contribution
- Giới thiệu Jev-LiteMAS: kết hợp mô hình decision model (mô hình ra quyết định) nhẹ namens Jev với generative execution (thực thi tạo sinh) và feedback.
- Giải quyết planning gap (khoảng cách lập kế hoạch): Jev chọn chuyên gia dynamic (động) từ task và đầu ra chuyên gia trước, dùng accumulated context (bối cảnh tích lũy) để grounding (xác thực ngữ cảnh) cho bước thực thi sau, không cần pre-generated trajectory (quỹ đạo được tạo trước).
- Giải quyết review gap (khoảng cách xem xét): Jev lọc intermediate artifacts (phối phẩm trung gian) theo task criteria (tiêu chí tác vụ): artifact đạt chuẩn đi thẳng, artifact sai được gửi review.

## Method (tóm cốt lõi)
Pipeline gồm 2 thành phần chính: (1) Jev decision model nhận task rubric (thang đánh giá tác vụ), screen (lọc) artifact local check (kiểm tra cục bộ), ra quyết định PASS/ESCALATE. Nếu PASS, artifact đi thẳng; nếu ESCALATE, LLM review (xem xét bằng LLM) ra ACCEPT/REVISE + feedback, rồi cập nhật state (trạng thái chung). (2) Generative experts nhận artifact qua handoff (v exchanges công việc), tiếp tục xử lý trong trách nhiệm của mình. State được U (cập nhật) sau mỗi bước để chuyên gia sau tiếp cận được công việc trước.

## Key Findings
- Routing và review chiếm 31.7–43.5% token generative-LLM trên sáu MAS được đo.
- So với LAS, Jev-LiteMAS giảm 12.7–54.6% token generative-LLM, độ chính xác khác biệt trong 1.34 phần trăm điểm, latency (thời gian chờ) thấp hơn trong 7/8 cấu hình.
- Jev screening phát hiện 91.33–95.33% trường hợp artifact bị nhiễm (corrupted cases); cascaded configuration (cấu trúc cascaded) dùng 14.6–21.7% ít token hơn LLM judging.
- Jev chỉ chiếm 2.92–6.85% latency end-to-end và 1.56–2.14% chi phí mô hình LLM.

## Actionable Insights
- Không dùng LLM lớn cho mọi quyết định điều phối: thay bằng decision model nhẹ (mô hình ra quyết định nhỏ) để chọn chuyên gia và lọc artifact, chỉ gọi LLM khi artifact cần sửa. Áp dụng: solopreneur chạy pipeline AI/content automation có thể cắt chi phí inference hàng chục phần trăm.
- Giữ semantic feedback (phản hồi ngữ nghĩa) khi sửa artifact: bỏ feedback này làm accuracy giảm từ 75.33% xuống 57.33% trên IDRBench I3. Áp dụng: khi agent sửa code/văn bản, phải trả lời lại lý do sai để agent sau biết điều chỉnh.

## Assumptions & Limitations
- Điều kiện để hoạt động: cần có predefined pool (bộ sẵn có) các expert roles (vai trò chuyên gia) và legal actions (hành động hợp lệ); không tạo chuyên gia mới cho tác vụ chưa từng thấy.
- Paper thừa nhận: khi nhiều artifact cần generative review, tiết kiệm token và latency sẽ giảm.
- Limitation paper không nói: chưa đánh giá trên mô hình nhỏ hơn 4B, chưa test trên workflow dài hơn 8 bước.

## Metadata
- Năm: 2026
- Tác giả: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li (Shanghai Jiao Tong University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.21411
