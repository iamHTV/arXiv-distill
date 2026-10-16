# [2610.05750v1] Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks

## Problem
Hệ thống thông tin hiện đại, bao gồm nhiều agentic workflow, dùng dense retrieval (truy xuất mật độ) để khám phá lượng lớn dữ liệu không cấu trúc. Tuy nhiên, dense retrieval dựa trên semantic similarity (tương đồng ngữ nghĩa) bề mặt, không đủ cho các ứng dụng tìm kiếm phức tạp ngày càng tăng.

## Contribution
- Nghiên cứu agentic retrieval kết hợp reasoning ability (khả năng suy luận) của LLM với efficient corpus exploration (khám phá bộ ngữ liệu hiệu quả) của retriever trong một ReAct agentic loop (vòng lặp agent ReAct).
- Thử nghiệm cho thấy agentic retrieval hiệu quả hơn standard retrieval: cải thiện nDCG@10 bằng 8.7 điểm bằng cùng embedding model.
- Agentic retrieval có tính generalizable (khả năng tổng quát hóa) cao: cùng pipeline đạt kết quả cạnh tranh trên cả ViDoRe v3 và BRIGHT leaderboards.

## Method (tóm cốt lõi)
Agentic retrieval kết hợp khả năng suy luận của LLM với khả năng khám phá bộ ngữ liệu của retriever trong vòng lặp ReAct agentic. Agent sử dụng reasoning để quyết định truy vấn gì, kiểm tra đoạn nào, và khi nào dừng, thay vì chỉ dựa vào semantic similarity một lần.

## Key Findings
- Agentic retrieval cải thiện nDCG@10 bằng 8.7 điểm so với standard retrieval, dùng cùng embedding model.
- Có tính generalizable cao: cùng pipeline đạt kết quả cạnh tranh trên cả ViDoRe v3 và BRIGHT leaderboards, trong khi specialized retrieval methods (phương pháp truy xuất chuyên biệt) gặp khó khăn trên out-of-domain tasks (nhiệm vụ ngoài miền).
- Chi phí: agentic retrieval trung bình 107.4 giây, so với 0.67 giây cho standard retrieval.
- Tiêu tốn 764.1K input tokens và 5.8K output tokens per query (mỗi truy vấn).

## Actionable Insights
- Chỉ dùng agentic retrieval cho các tác vụ tìm kiếm phức tạp where standard retrieval không đủ: chi phí cao (107s, 764K tokens) nên chỉ bật khi cần. Áp dụng: solopreneur làm hệ thống tìm kiếm nội dung nên dùng standard retrieval cho tìm kiếm đơn giản, chỉ bật agentic retrieval cho truy vấn phức tạp cần suy luận đa bước.
- Agentic retrieval tổng quát hóa tốt trên các domain khác nhau (ViDoRe, BRIGHT) nên có thể dùng một pipeline cho nhiều loại truy vấn. Áp dụng: xây một hệ thống agentic retrieval duy nhất thay vì nhiều specialized retrieval methods cho mỗi domain.

## Assumptions & Limitations
- Điều kiện: cần có hệ thống retriever và LLM có khả năng reasoning; không áp dụng nếu chỉ có dense retrieval đơn thuần.
- Paper thừa nhận: chi phí cao (107s, 764K tokens/query) làm hạn chế triển khai quy mô lớn.
- Limitation paper không nói: chưa đánh giá trên nhiều ngôn ngữ khác ngoài tiếng Anh, chưa test trên tập dữ liệu cực lớn (triệu documents).

## Metadata
- Năm: 2026
- Tác giả: Reza Esfandiarpoor, Radek Osmulski, Yauhen Babakhin, Gabriel de Souza P. Moreira, Oliver Holworthy, Jie He, Ronay Ak, Jiarui Cai, Ryan Chesler, Bo Liu, Even Oldridge (NVIDIA, University of Edinburgh)
- Category arXiv: cs.AI, cs.IR
- Link PDF: https://arxiv.org/pdf/2610.05750
- Code: https://github.com/NVIDIA/NeMo-Retriever/tree/main/retrieval-bench
