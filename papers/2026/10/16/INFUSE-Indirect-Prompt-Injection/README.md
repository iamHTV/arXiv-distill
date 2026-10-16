# [2610.20776v1] INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems

## Problem
Các đại lý ngôn ngữ (LLM agents) ngày càng thực thi các luồng tác vụ end-to-end dài hạn liên quan đến shell commands, code modification, dependency installation, và tương tác với các dịch vụ từ xa. Sự tự chủ ngày càng mở rộng làm giãn rộng sự tiếp xúc với indirect prompt injection (IPI - tiêm lời nhắc gián tiếp), trong đó các chỉ thị đối thủ (adversarial instructions) nhúng trong nội dung bên ngoài được hiểu là các chỉ thị tác vụ hợp pháp. Tuy nhiên, các đánh giá hiện tại thường...

## Contribution
- Giới thiệu INFUSE: một unified surface benchmark (benchmark bề mặt thống nhất) cho indirect prompt injection trong agentic systems.
- Đánh giá trên 40 tasks với 56 attacks, định nghĩa lên đến 40 × 56 = 2,240 (task, attack) configurations per model.
- Across the benchmark, mean attack success reaches 19.6% under LLM-based evaluation (ASR-L) and 15.4% under heuristic verification (ASR-H).
- Per-model ASR-L ranges from 3.2% to 41.9%.
- Instructional hardening reduces mean attack success from 58.2% to 14.3%, revealing substantial but model-dependent security–utility trade-offs.
- 41,824 attack trajectories, explicit refusal is rare (RR ≤ 1.0% for every model).
- Highest-ASR tasks: T17 Tech Writing 51.6%, T13 File Org. 49.9%, T9 Security 49.1%, T3 Dep. Setup 47.9%.

## Method (tóm cốt lõi)
INFUSE là một benchmark thống nhất cho indirect prompt injection trong agentic systems. Đánh giá trên 40 tasks với 56 attacks, mỗi (task, attack) configuration được chạy trên mỗi model. Đo ASR-L (attack success rate theo đánh giá LLM) và ASR-H (theo đánh giá heuristik). So sánh các model khác nhau và các phương pháp phòng thủ (defense).

## Key Findings
- Mean attack success: 19.6% (LLM-based), 15.4% (heuristic).
- Per-model ASR-L: 3.2% to 41.9%.
- GPT-5: 26.3% ASR-L, Claude-Sonnet-4.6: 3.2% ASR-L, Gemini-3.1-Flash-Lite-Preview: 41.9% ASR-L.
- Instructional hardening reduces mean attack success from 58.2% to 14.3% (43.9 points reduction).
- Meta-SecAlign reduces ASR-L by 55% at 8B and 74% at 70B.
- Refusal remains rare (at most 1.0% for every model).
- Transfer: 9.3–35.7% of previously successful attacks transfer (102 of 456 cells pooled, 22.4%).

## Actionable Insights
- Không nên tin tưởng agent LLM là an toàn trước indirect prompt injection: mean attack success 19.6% cho thấy hệ thống dễ bị tấn công. Áp dụng: solopreneur dùng agent LLM nên thêm các cơ chế phòng thủ (defense mechanisms) như instructional hardening, input sanitization, output validation.
- Instructional hardening là phương pháp phòng thủ hiệu quả: giảm attack success từ 58.2% xuống 14.3%. Áp dụng: khi xây agent LLM, hãy thêm các lời nhắc hướng dẫn bảo mật (instructional hardening) để agent không tuân theo các chỉ thị đối thủ nhúng trong nội dung bên ngoài.
- Nên đánh giá độ bền (robustness) của agent trước khi triển khai production. Áp dụng: khi xây agent LLM, hãy thử nghiệm với các tấn công indirect prompt injection để tìm ra các lỗ hổng và khắc phục trước khi đưa ra sản phẩm.

## Assumptions & Limitations
- Điều kiện: có agent LLM và dữ liệu truy vấn thật; không áp dụng nếu chỉ có một mô hình đơn lẻ.
- Paper thừa nhận: đánh giá trên các hệ thống agent cụ thể; có thể khác trên các hệ thống khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen khác ngoài các tác vụ đã dùng, chưa test chi phí thực tế của các cơ chế phòng thủ.

## Metadata
- Năm: 2026
- Tác giả: Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas, Sreepriya Damuluru, Taylor T. Johnson, Kevin Leach (Vanderbilt University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.20776
