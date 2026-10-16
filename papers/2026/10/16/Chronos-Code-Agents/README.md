# [2610.11578v1] Chronos Enables Code Agents to Reason over Software Evolution

## Problem
Lịch sử pull requests ghi lại các quyết định thiết kế (design decisions), các ràng buộc tương thích (compatibility constraints), và các mẫu triển khai (implementation patterns) đằng sau trạng thái hiện tại của một codebase. Kinh nghiệm liên quan đến một tác vụ mới có thể trải dài qua các thay đổi liên quan mà các mô tả nhấn vào các mối quan tâm khác nhau. Các agent mã hiện tại thường không thể truy cập và sử dụng hiệu quả lịch sử này.

## Contribution
- Giới thiệu Chronos: một test-time framework làm cho lịch sử kết nối này sẵn sàng cho các đại lý ngôn ngữ lớn (LLM agents).
- Chronos raises the mean resolution rate from 69.2% to 72.9% (+3.7pp) and reaching 79.8% with MiniMax M2.5.
- With the same backbone, Chronos raises resolution rates from 48.3% to 51.7% on SWE-Bench Pro and from 41.0% to 43.5% on FEA-Bench Lite.
- Two single-agent variants reach 78.4% and 77.8%, compared with 76.4% for the base agent.
- Fraction of tasks receiving useful experience: 68% → 89% (compared with flat semantic retrieval).
- Graph-grounded retrieval: useful-card fractions 12.4% (Embedding) → 28.7% (Chronos); Hit from 68% → 89%.

## Method (tóm cốt lõi)
Chronos là một framework test-time làm cho lịch sử pull requests sẵn sàng cho LLM agents. Hệ thống sử dụng lịch sử pull requests để cung cấp kinh nghiệm liên quan cho các tác vụ mới, giúp agent đưa ra quyết định tốt hơn về việc sửa lỗi, triển khai tính năng, và tái cấu trúc code.

## Key Findings
- Chronos raises mean resolution rate from 69.2% to 72.9% (+3.7pp) and reaching 79.8% with MiniMax M2.5.
- With same backbone: SWE-Bench Pro 48.3% → 51.7%, FEA-Bench Lite 41.0% → 43.5%.
- Two single-agent variants: 78.4% and 77.8%, vs base agent 76.4%.
- Fraction of tasks receiving useful experience: 68% → 89% (vs flat semantic retrieval).
- Graph-grounded retrieval: useful-card fractions 12.4% → 28.7%; Hit from 68% → 89%.
- Full workflow: 79.8% resolution rate with graph-grounded retrieval, 79.0% with flat semantic search (+0.8pp).

## Actionable Insights
- Dùng lịch sử pull requests (pull request history) để cung cấp kinh nghiệm liên quan cho agent code, thay vì chỉ dựa vào kiến thức nội bộ của mô hình. Áp dụng: solopreneur xây agent hỗ trợ phát triển phần mềm nên tích hợp lịch sử pull requests để agent hiểu tại sao code được viết như vậy.
- Dùng graph-grounded retrieval (truy xuất dựa trên đồ thị) thay vì flat semantic retrieval (truy xuất ngữ nghĩa phẳng) để cải thiện chất lượng kinh nghiệm được truy xuất. Áp dụng: khi xây agent hỗ trợ phát triển phần mềm, hãy xây dựng đồ thị 지식 (knowledge graph) từ lịch sử pull requests để agent truy xuất kinh nghiệm chính xác hơn.

## Assumptions & Limitations
- Điều kiện: có lịch sử pull requests và dữ liệu codebase thật; không áp dụng nếu không có lịch sử pull requests.
- Paper thừa nhận: đánh giá trên SWE-Bench Pro và FEA-Bench Lite; có thể khác trên các tác vụ khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen khác ngoài phát triển phần mềm, chưa test chi phí thực tế của hệ thống.

## Metadata
- Năm: 2026
- Tác giả: Xin Yin, Yiang Zhang, Zhiyuan Peng, Chao Ni, Zhe Cui, Xiaohua Xin (Zhejiang University, Shanghai Jiao Tong University, Hithink Research, National Industrial Information Security Development Research Center)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.11578
