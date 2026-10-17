# Skill: synthetic-data-forgetting-mitigation
Source: 2609.10750v1
Type: framework

## Khi nào dùng skill này
- Đang fine-tune một mô hình retrieval (ví dụ: Qwen3-Embedding-0.6B) trên dữ liệu tổng hợp (synthetic data) cho việc truy xuất kỹ năng (skill retrieval) cho LLM agents.
- Muốn cải thiện in-distribution retrieval mà không gây quên mất (catastrophic forgetting) trên dữ liệu thực và ngoài phân phối (OOD).
- Có dữ liệu thực (real data) hạn chế và dữ liệu tổng hợp (synthetic data).

## Tình huống KHÔNG nên dùng
- Không có dữ liệu tổng hợp (synthetic data) để fine-tune.
- Không cần fine-tune model retrieval (chỉ dùng model có sẵn).
- Không quan tâm đến hiệu suất trên dữ liệu OOD (chỉ quan tâm đến in-distribution).

## Input cần có
- Dữ liệu tổng hợp (synthetic data) cho fine-tuning (ví dụ: Track A ~15K pairs hoặc Track B ~14K pairs).
- Dữ liệu thực (real data) để đánh giá OOD performance.
- Mô hình retrieval nhỏ (compact retrieval model) như Qwen3-Embedding-0.6B.
- Bộ dữ liệu đánh giá (evaluation dataset) với các kỹ năng (skills) và truy vấn (queries).

## Các bước thực hiện
1. Xây dựng dữ liệu tổng hợp (synthetic data): Track A (~15K pairs) tạo các tác vụ anchor-skill với positives được lấy từ retrieval (retrieval-derived positives) và hard negatives; Track B (~14K pairs) kết hợp real data, paraphrase generation, và multi-skill task synthesis.
2. Fine-tune mô hình retrieval (ví dụ: Qwen3-Embedding-0.6B) trên dữ liệu tổng hợp bằng các chế độ fine-tuning khác nhau.
3. Áp dụng các phương pháp giảm quên mất (forgetting mitigation): embedding-anchor regularization, Learning without Forgetting (LwF), Elastic Weight Consolidation (EWC), và L2-initialization.
4. Đánh giá trên dữ liệu tổng hợp (in-distribution) và dữ liệu thực/OOD (out-of-distribution).
5. So sánh hiệu suất trước và sau khi áp dụng các phương pháp giảm quên misses.

## Output mong đợi
- Mô hình retrieval có hiệu suất tốt trên dữ liệu tổng hợp (in-distribution) mà không gây quên mất trên dữ liệu thực và OOD.
- Các phương pháp giảm quên misses cải thiện retrieval trên các kỹ năng synthetic in-distribution bởi 13.98% cho 0.6B Qwen retriever và reranker.

## Ví dụ áp dụng
- Xây dựng hệ thống truy xuất kỹ năng (skill retrieval) cho LLM agents: fine-tune mô hình Qwen3-Embedding-0.6B trên dữ liệu tổng hợp về các kỹ năng (skills), áp dụng phương pháp giảm quên mất (ví dụ: LwF hoặc EWC) để giữ được hiệu suất trên dữ liệu thực và OOD.

## Gotchas
- Việc fine-tune trên dữ liệu tổng hợp cải thiện in-distribution retrieval nhưng gây quên mất (catastrophic forgetting) trên dữ liệu thực và OOD.
- Trong cấu hình fine-tuning mức độ cao nhất (most aggressive fine-tuning configuration), OOD recall giảm từ 0.850 xuống 0.650.
- Các phương pháp giảm quên misses không chỉ giữ được hiệu suất trên OOD skills retrieval mà còn cải thiện việc truy xuất trên các kỹ năng synthetic in-distribution.
