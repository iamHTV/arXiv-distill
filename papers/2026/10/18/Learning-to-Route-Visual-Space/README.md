# [2609.38743v2] Learning to Route in Visual Space via Multi-Step Embedding Retrieval

## Problem
LLM agents dựa trên công cụ retrieval để truy cập kiến thức bên ngoài, nhưng tìm kiếm tác nhân hình ảnh (visual agentic search) bị Bottlenecked bởi các retriever đơn bước chuẩn (single-step retrievers). Trong pipeline hiện tại, agent phải gửi truy vấn văn bản cho mọi bước trung gian, gặp khó khăn khi dấu hiệu hình ảnh khó mô tả bằng văn bản hoặc khi retriever không đưa ra bằng chứng trung gian cần thiết trong top kết quả. Agent chỉ nhìn thấy ít kết quả được trả về, không thể suy luận trên bằng chứng mà nó không nhận được.

## Contribution
- Giới thiệu VHop, một khung tạo dữ liệu (data generation framework) và benchmark linh hoạt với năm mức độ khó cốt lõi kiểm tra cả khớp hình ảnh và lập kế hoạch tìm kiếm.
- Phát triển VHop-Router, một pipeline huấn luyện end-to-end — kết hợp supervised fine-tuning, online imitation learning, và reinforcement learning — biến một mô hình embedding chuẩn thành một retriever đa bước tự hồi quy (autoregressive multi-step retriever).
- Hoạt động trực tiếp trong không gian embedding latent hình ảnh (visual latent space), VHop-Router lấy các chuỗi hình ảnh liên kết trong một công cụ gọi duy nhất không yêu cầu agent định nghĩa các truy vấn văn bản trung gian.

## Method
- VHop-Router biến đổi mô hình embedding chuẩn (Qwen3-VL-Embedding-2B) thành retriever đa bước qua 3 giai đoạn: (1) Supervised Fine-Tuning (SFT) dạy next-hop retrieval từ các tiền tố quỹ đạo vàng (gold trajectory prefixes) với mục tiêu InfoNCE; (2) Online Imitation Learning (Online IL) dạy khôi phục và dừng lại từ các trạng thái được thăm trong quá trình tìm kiếm; (3) Reinforcement Learning với phần thưởng có thể xác thực (RLVR) tối ưu hóa tỷ lệ thành công câu trả lời cuối cùng.
- Không gian trạng thái: hướng dẫn văn bản x, stack ảnh đang hoạt động σt = (q0, q1, ..., qdt). Không gian hành động: {Select(a) : a ∈ corpus} ∪ {Backtrack, Stop}.
- Mã hóa trạng thái Es và mã hóa hành động EA cùng bắt đầu từ Qwen3-VL-Embedding-2B, dùng LoRA. freeze EA sau SFT và tái sử dụng cached corpus embeddings.
- Điểm số ứng viên bằng cosine similarity, chọn từ top-K ứng viên bằng softmax với nhiệt độ τ.
- Hai cổng học điều khiển dừng và backtrack (hai lớp MLP).
- Ở thời điểm đánh giá, chính sách hoạt động决定论: dừng nếu p_stop ≥ 0.5, nếu không chọn ảnh có điểm số cao nhất.

## Key Findings
- VHop-Router nâng hiệu suất truy xuất từ dưới 5% lên 76,3%.
- Trong tìm kiếm tác nhân (agentic search), cải thiện tỷ lệ thành công nhiệm vụ 52,7% và giảm chiều dài token trung bình 61% từ 1886 xuống 728.
- Nâng cấp agent chỉ mang lại 3,7%gain, trong khi thay thế công cụ truy xuất bằng VHop-Router mang lại 52,7% tăng.
- So với baseline mạnh mẽ (agent lấy top-50 kết quả mỗi bước), VHop-Router duy trì hiệu suất vượt trội đồng thời giảm ảnh trong ngữ cảnh 23× và cắt tải trọng API cộng dồn 35×.
- Mô hình tổng quát hóa mạnh mẽ đến các mức độ khó chưa thấy và bộ kiểm tra thực tế.

## Actionable Insights
1. Offload multi-step navigation từ agent xuống công cụ retrieval — thay vì để agent construct các truy vấn trung gian, hãy để công cụ retrieval tự điều hướng trên toàn bộ không gian embedding. Áp dụng: khi xây dựng hệ thống tìm kiếm hình ảnh/multimodal, hãy huấn luyện một mô hình embedding đa bước thay vì để LLM agent tự làm multi-hop retrieval. Bước đầu: Xây dựng một retriever có thể trả về chuỗi hình ảnh liên kết trong một lần gọi duy nhất.
2. Cải thiện công cụ retrieval hiệu quả hơn đáng kể so với nâng cấp agent model. Áp dụng: trước khi bỏ tiền nâng cấp agent lên model lớn hơn, hãy đầu tư vào công cụ retrieval tốt hơn. Bước đầu: So sánh hiệu quả của việc thay thế retriever so với việc nâng cấp agent model trên task của bạn.
3. Giảm số lượng ảnh trong ngữ cảnh (in-context images) để cắt chi phí API. Áp dụng: thay vì lấy top-50 kết quả mỗi bước, hãy dùng retriever đa bước trả về chuỗi ảnh ngắn gọn. Bước đầu: Giới hạn số lượng ảnh gửi đến LLM agent, chỉ gửi ảnh liên quan nhất từ chuỗi retriever.

## Assumptions & Limitations
- Đánh giá trên benchmark VHop (synthetic image corpus), có thể khác trên dữ liệu hình ảnh thực tế.
- Chỉ dùng 2 mô hình embedding (Qwen3-VL-Embedding-2B, Gemini Embedding 2), không generalize sang tất cả mô hình embedding.
- Huấn luyện độc quyền trên L4 (mức độ khó đầu tiên có nhánh cục bộ nhưng sai toàn cục), đánh giá trên L1–L5.
- Các công cụ bên ngoài là synthetic stubs trong bản nguyên mẫu (cho một số phần), chưa kết nối API thực.

## Metadata
- Năm: 2026, tác giả: Tianyu Chen, Mingyuan Zhou (The University of Texas at Austin), Jiaxing Wu (Google DeepMind), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.38743v2