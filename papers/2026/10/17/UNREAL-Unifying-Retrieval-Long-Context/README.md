# [2610.08463v1] UNREAL: Unifying Retrieval and Long-Context with a Single Model

## Problem
- Suy luận ngữ cảnh dài (long-context inference) và Tăng cường Tạo Nhiếp Ảnh (Retrieval-Augmented Generation — RAG) xử lý việc lựa chọn bằng chứng (evidence selection) ở các thang độ vastly khác nhau, từ một lời nhặn duy nhất (single long prompt) đến một toàn bộ corpus (entire corpus). Prior work chưa giải quyết được việc liệu một cơ chế nội bộ duy nhất của model có thể chọn bằng chứng qua toàn bộ phạm vi này hay không — hai phương pháp được nghiên cứu như các phương án thay thế (alternative approaches) thay vì hai thang độ của một cơ chế duy nhất.

## Contribution
- UNREAL (UNifying REtrieval And Long-Context with a Single Model) — một khung làm việc chọn bằng chứng bản địa của mô hình (model-native evidence selection framework) để khép (span) truy xuất corpus và suy luận ngữ cảnh dài.
- UNREAL mã hóa các đoạn văn bản (chunks) và lấy các truy vấn truy xuất (retrieval queries) trực tiếp từ các biểu diễn nội bộ (internal representations) của LLM đóng băng (frozen LLM).
- Thêm ít hơn 500K tham số có thể huấn luyện (trainable parameters) và để xương sống (backbone) không thay đổi (unchanged).

## Method (tóm tắt cốt lõi)
- Xây dựng trên INTRA (Hoffer et al., 2026), nhưng INTRA dựa trên một máy mã hóa riêng (separate encoder) và tránh chú ý chéo (cross-attention), ngăn chặn việc áp dụng trực tiếp vào các mô hình LLM chỉ giải mã (decoder-only LLMs) phổ biến hiện nay.
- UNREAL loại bỏ hạn chế này bằng cách mã hóa các đoạn văn bản ứng viên (candidate chunks) và lấy các truy vấn truy xuất trực tiếp từ các trạng thái nội bộ (internal states) của LLM đóng băng.
- UNREAL thêm ít hơn 500K tham số có thể huấn luyện, được đào tạo bằng tổn thất đối lập (contrastive loss), trên xương sống LLM đóng băng: một soft prompt để khơi gợi chế độ truy xuất (retrieval mode) và trọng số lớp (layer weights) kết hợp các trạng thái nội bộ cho việc xếp hạng bằng chứng (evidence ranking).
- Vì nó đọc từ luồng còn lại (residual stream), cùng một cơ chế áp dụng qua các kiến trúc chú ý dày (dense-attention), chú ý tuyến tính (linear-attention), và không gian trạng thái (state-space).
- Tại thang độ corpus (corpus scale): UNREAL truy xuất từ một chỉ mục Wikipedia 21M đoạn văn bản (chunk), 3B token. Tất cả bốn xương sống (backbone) được kiểm tra vượt qua các hệ thống truy xuất-đánh giá lại (retriever-reranker) nhất tỉnh (state-of-the-art).
- Tại thang độ ngữ cảnh dài (long-context scale): UNREAL xếp hạng các đoạn văn bản trong một lời nhắn dài (long-context prompt) và chỉ trả về văn bản đã chọn (selected text) cho cùng một LLM đóng băng để trả lời.

## Key Findings
- 7 tác giả từ NVIDIA và Viện Công nghệ Georgia (Technion), category arXiv: cs.CL.
- Chỉ mục Wikipedia 3B token, 21M đoạn văn bản (chunk).
- HotpotQA: recall tăng từ 49.1% lên 73.2%.
- 2WikiMultiHopQA: recall tăng từ 31.7% lên 60.1%.
- MuSiQue: recall tăng từ 8.8% lên 14.4%.
- NoLiMa: accuracy từ 1.0% lên 24.83% ở độ dài ngữ cảnh tối đa 128K token.
- LV-Eval: F1 từ 49.97% lên 54.66% ở 256K.
- UNREAL cũng giảm FLOPs và thời gian đến token đầu tiên (time-to-first-token) so với suy luận ngữ cảnh đầy đủ (full-context inference) từ khoảng 32K token trở đi, với lợi ích lớn hơn khi ngữ cảnh dài hơn.

## Actionable Insights
1. Lựa chọn bằng chứng nội bộ (internal evidence selection) có thể áp dụng đồng chiều cho cả truy xuất corpus và suy luận ngữ cảnh dài. Áp dụng: thay vì dùng hai mô hình riêng (trình truy xuất + LLM), dùng cùng một mô hình để xếp hạng bằng chứng và tạo câu trả lời.
2. Thêm ít hơn 500K tham số có thể huấn luyện lên trên backbone đóng băng có thể cải thiện đáng kể khả năng chọn bằng chứng. Áp dụng: khi muốn thêm khả năng truy xuất vào LLM hiện tại, dùng UNREAL-style soft prompt + trọng số lớp thay vì đào tạo lại toàn bộ mô hình.

## Assumptions & Limitations
- Đánh giá trên 4 xương sống (backbone models).
- Corpus là Wikipedia (3B token, 21M đoạn văn bản).
- Các tác vụ ngữ cảnh dài: NoLiMa, LV-Eval, HELMET.

## Metadata
- Năm: 2026, tác giả: Edan Kinderman, Elad Hoffer, Yochai Blau, Brian Chmiel, Ron Banner, Daniel Soudry, Boris Ginsburg (NVIDIA, Viện Công nghệ Georgia), category arXiv: cs.CL, link PDF: https://arxiv.org/pdf/2610.08463v1
