# [2609.10750v1] When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents

## Problem
- Các tác nhân LLM ngày càng dựa vào các kỹ năng (skills) được truy xuất tại thời gian chạy (runtime), khiến việc lựa chọn kỹ năng từ các kho lưu trữ lớn (large repositories) trở thành một thách thức quan trọng. Prior work chưa giải quyết được việc liệu việc điều chỉnh chi tiết (fine-tuning) trên dữ liệu tổng hợp (synthetic data) có làm suy yếu khả năng của model trong việc truy xuất kỹ năng cho các tác vụ thực tế hoặc ngoài phân phối (OOD tasks) hay không.

## Contribtuion
- Một bộ điều hướng kỹ năng (skill router) cho sản xuất (production) hơn 34,396 kỹ năng và một nghiên cứu lớn về việc truy xuất kỹ năng (skill retrieval) sử dụng limited real supervision và synthetic data.
- Hai đào tạo synthetic tracks: Track A (~15K pairs) tạo ra các tác vụ anchor-skill với retrieval-derived positives và hard negatives, trong khi Track B (~14K pairs) kết hợp real data, paraphrase generation, và multi-skill task synthesis.
- Đánh giá một số phương pháp fine-tuning giảm quên mất (forgetting mitigation fine-tuning approaches) lấy cảm hứng từ continual learning, bao gồm embedding-anchor regularization, Learning without Forgetting (LwF), Elastic Weight Consolidation (EWC), và L2-initialization.

## Method (tóm tắt cốt lõi)
- Kho lưu trữ (repository) hơn 34,396 kỹ năng (skills).
- Sử dụng các tác vụ từ SkillsBench và Terminal-Bench 2, thực hiện khoảng 1K trials trên 109 tác vụ (tasks) bằng các ống dẫn retrieval lai (hybrid retrieval pipelines) trong môi trường Harbor (Harbor environment).
- Xây dựng hai synthetic training tracks: Track A (~15K pairs) tạo ra các tác vụ anchor-skill với positives được lấy từ retrieval (retrieval-derived positives) và hard negatives, trong khi Track B (~14K pairs) kết hợp real data, paraphrase generation, và multi-skill task synthesis.
- Đánh giá các mô hình truy xuất nhỏ (compact retrieval models), như Qwen3-Embedding-0.6B dưới các chế độ fine-tuning khác nhau.
- Các phương pháp giảm quên mất (forgetting mitigation): embedding-anchor regularization, LwF, EWC, và L2-initialization.

## Key Findings
- 5 tác giả từ Manulife, category arXiv: cs.IR.
- Kho lưu trữ hơn 34,396 kỹ năng (skills).
- Khoảng 1K trials trên 109 tasks.
- Synthetic supervision cải thiện in-distribution retrieval nhưng cũng gây quên mất đáng kể (substantial forgetting) trên real và OOD data.
- Trong cấu hình fine-tuning mức độ cao nhất (most aggressive fine-tuning configuration), OOD recall giảm từ 0.850 xuống 0.650, chứng minh rằng các mức độ cải thiện (gains) trên dữ liệu đào tạo tổng hợp (synthetic training data) không nhất quán dịch chuyển thành hành vi triển khai mạnh mẽ (robust deployment behavior).
- Các phương pháp giảm quên misses (forgetting mitigation approaches) không chỉ giữ được hiệu suất trên việc truy xuất kỹ năng OOD mà còn cải thiện việc truy xuất trên các kỹ năng synthetic in-distribution bởi 13.98% cho 0.6B Qwen retriever và reranker.

## Actionable Insights
1. Việc điều chỉnh chi tiết (fine-tuning) trên dữ liệu tổng hợp (synthetic data) cải thiện in-distribution retrieval nhưng cũng gây quên mất (catastrophic forgetting) trên dữ liệu thực và ngoài phân phối (OOD data). Áp dụng: khi fine-tune model retrieval trên dữ liệu tổng hợp, hãy dùng các phương pháp giảm quên mất (forgetting mitigation) như LwF, EWC, L2-initialization.
2. Các phương pháp giảm quên misses (embedding-anchor regularization, LwF, EWC, L2-initialization) không chỉ giữ được hiệu suất trên OOD skills retrieval mà còn cải thiện việc truy xuất trên các kỹ năng synthetic in-distribution bởi 13.98% cho 0.6B Qwen retriever và reranker. Áp dụng: hãy luôn áp dụng các kỹ thuật giảm quên mất khi fine-tune trên dữ liệu tổng hợp.

## Assumptions & Limitations
- Khả năng thống kê (statistical power) hạn chế: Val-set 1 (n = 21) và Val-set 3 (n = 10) có kích thước nhỏ, nên sự biến thiên của một task đơn lẻ có thể chuyển RECALL@10 khoảng 5%.
- Đánh giá trên kho lưu trữ hơn 34,396 kỹ năng (skills).
- Tập trung vào mô hình Qwen3-Embedding-0.6B.

## Metadata
- Năm: 2026, tác giả: Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund (Manulife), category arXiv: cs.IR, link PDF: https://arxiv.org/pdf/2609.10750v1
