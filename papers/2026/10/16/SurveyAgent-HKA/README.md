# [2609.05938v1] SurveyAgent-HKA: A multi-agent framework for scientific survey generation with LLMs and human knowledge augmentation

## Problem
Tự động sinh bài khảo sát khoa học (automatic scientific survey generation) đang trở thành một nhiệm vụ quan trọng trong tài liệu khoa học, nhưng các hệ thống hiện tại chưa kết hợp hiệu quả giữa LLM và kiến thức của con người (human knowledge augmentation) để tạo ra bài khảo sát có chất lượng cao về cấu trúc và nội dung.

## Contribution
- Giới thiệu SurveyAgent-HKA: một multi-agent framework (hệ thống đa đại lý) để sinh bài khảo sát khoa học với LLM và human knowledge augmentation (tăng cường kiến thức của con người).
- Đánh giá trên hai miền: computer science và medicine.
- Citation quality: CS domain (14.95% Precision, 19.53% Recall, 16.94% F1), Medical domain (16.78% Precision, 22.95% Recall, 19.39% F1).
- Key-point recall: 53.85% (CS) và 57.07% (medicine).
- H1 match F1: 38.53%, H2 match F1: 33.42%.
- Với human knowledge augmentation: citation F1 tăng 3.86% (CS), H1 match +9.31%, H2 match +6.19%; Medical: citation F1 +2.62%, H1 +4.92%, H2 +6.71%.

## Method (tóm cốt lõi)
SurveyAgent-HKA là multi-agent framework kết hợp LLM và human knowledge augmentation để sinh bài khảo sát khoa học. Framework bao gồm các agent phụ trách các giai đoạn khác nhau (lập kế hoạch, tìm kiếm, viết, sửa chữa) và kết hợp kiến thức của con người để cải thiện chất lượng.

## Key Findings
- Citation quality: CS (14.95% P, 19.53% R, 16.94% F1), Medicine (16.78% P, 22.95% R, 19.39% F1).
- Key-point recall: 53.85% (CS), 57.07% (medicine).
- H1 match F1: 38.53%, H2 match F1: 33.42%.
- Human knowledge augmentation cải thiện citation F1 (+3.86% CS, +2.62% Medicine), H1 match (+9.31% CS, +4.92% Medicine), H2 match (+6.19% CS, +6.71% Medicine).
- Citation expansion, re-ranking, clustering, few-shot learning đều có tác động quan trọng đến chất lượng (loại bỏ mỗi thành phần làm giảm F1 từ 2.15% đến 7.02%).

## Actionable Insights
- Kết hợp kiến thức của con người vào quá trình sinh bài khảo sát bởi LLM giúp cải thiện chất lượng đáng kể. Áp dụng: solopreneur dùng LLM để viết bài khảo sát hoặc tài liệu tài nguyên nên kết hợp review và chỉnh sửa của con người, không để LLM viết hoàn toàn độc lập.
- Các thành phần như citation expansion, re-ranking, clustering, few-shot learning đều quan trọng. Áp dụng: khi xây hệ thống sinh tài liệu bởi LLM, hãy giữ lại các bước này, không bỏ qua để tối ưu hóa chi phí.

## Assumptions & Limitations
- Điều kiện: có tài liệu tham khảo và kiến thức của con người để augment; không áp dụng nếu không có nguồn tham khảo.
- Paper thừa nhận: đánh giá trên hai miền (CS và medicine); có thể khác trên domen khác.
- Limitation paper không nói: chưa đánh giá chi phí thực tế của human augmentation, chưa test trên nhiều domen khác ngoài khoa học.

## Metadata
- Năm: 2026
- Tác giả: Tong Bao, Mir Tafseer Nayeem, Yi Zhao, Davood Rafiei, Chengzhi Zhang (Nanjing University of Science and Technology, University of Alberta, Anhui University)
- Category arXiv: cs.AI, cs.CL
- Link PDF: https://arxiv.org/pdf/2609.05938
