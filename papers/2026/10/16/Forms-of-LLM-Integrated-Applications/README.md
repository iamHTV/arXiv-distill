# [2610.11899v1] Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent Systems

## Problem
LLM ngày càng được nhúng làm thành phần trong các hệ thống phần mềm, được marketing dưới các nhãn như chatbot, copilot, retrieval-augmented generation (RAG), workflow, coding agent, và AI agent. Không rõ các nhãn này ký hiệu những dạng kiến trúc thực sự hay chỉ là branding (thương hiệu).

## Contribution
- Mô tả bảy dạng lặp lại (seven recurring forms) của hệ thống kết hợp LLM: LLM chats, custom agents, RAG, AI-enhanced workflows, copilots, coding agents, và agentic RAG (một phần).
- Mỗi dạng được đặc trưng bởi bốn kích thước cấu trúc (four structural dimensions): architectural pattern (mẫu kiến trúc), control of execution and point of user intervention (kiểm soát thực thi và điểm can thiệp của người dùng), number of agent calls per task (số lần gọi agent mỗi tác vụ), và tool use (sử dụng công cụ).
- Corpus minh họa 22 hệ thống từ nghiên cứu và tài liệu nhà cung cấp (vendor documentation).

## Method (tóm cốt lõi)
Khảo sát (survey) các hệ thống kết hợp LLM từ các nguồn nghiên cứu và tài liệu nhà cung cấp, mô tả bảy dạng trong một từ vựng chung của agent và tools. Mỗi dạng được đặc trưng theo bốn kích thước cấu trúc trên.

## Key Findings
- Các nhãn có nội dung kiến trúc (architectural content), rõ ràng nhất trong sử dụng của nhà cung cấp: copilot ký hiệu một kiến trúc router-worker (máy định tuyến-nhân viên) chạy ứng dụng host dưới xác nhận bước-dlbum của người dùng; nhãn agent gần hơn với việc thực thi nhiều bước được lập kế hoạch bởi AI (AI-planned multi-step execution) mà người dùng chỉ thấy kết quả.
- Coding agents của bốn nhà cung cấp lớn chia sẻ một kiến trúc: reason-and-act loop delegating to subagents (vòng lặp lý do-hành động ủy thác cho các đại lý phụ).

## Actionable Insights
- Không nên confuses (lỗ supports) các nhãn marketing với kiến trúc thực tế: copilot ≠ agent ≠ workflow. Áp dụng: solopreneur chọn công cụ AI nên xem xét kiến trúc thực tế (router-worker, multi-step, v.v.) chứ không chỉ dựa vào tên gọi marketing.
- Dùng từ vựng chung (7 dạng, 4 kích thước cấu trúc) để so sánh các công cụ AI. Áp dụng: khi đánh giá công cụ AI, hãy phân loại theo kiến trúc, số lần gọi agent, kiểm soát con người, và công cụ sử dụng.

## Assumptions & Limitations
- Điều kiện: dựa trên khảo sát 22 hệ thống từ nghiên cứu và tài liệu nhà cung cấp; có thể không bao quát hết tất cả các hệ thống trên thị trường.
- Paper thừa nhận: agentic RAG chỉ được mô tả một phần (partially).
- Limitation paper không nói: chưa đánh giá hiệu quả thực tế của mỗi dạng, chưa test trên nhiều domen ngoài phần mềm kỹ thuật.

## Metadata
- Năm: 2026
- Tác giả: Irene Weber (University of Applied Sciences Kempten, Đức)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.11899
