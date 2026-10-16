# [2609.01736v1] Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives

## Problem
LLM augmented với external tools (công cụ bên ngoài) đã đạt thành công đáng kể, nhưng việc gọi tool (tool use) vẫn gặp vấn đề: độ chính xác giảm mạnh khi danh sách tool lớn (từ 8K đến 120K tokens), SFT-based models không tổng quát được cho dynamic agentic tool scenarios (các tình huống công cụ động), và chi phí API cao.

## Contribution
- Giới thiệu Tool Primitives (công cụ nguyên thủy): kho 25.519 hàm reusable (tái sử dụng) và ToolFace.
- Giới thiệu HEART (Planner-Router-Verifier): framework lập kế hoạch, định tuyến, xác thực cho tool use.
- HEART outperforms SFT-based models by 10% on average, surpasses GPT-5.4, Claude-4.6-Sonnet, Gemini-3.1-Pro by 6% on average while reducing API cost by up to 85%.
- On 50 real-world tasks: 84% task completion, 3.8× the average of three frontier commercial models (22%).

## Method (tóm cốt lõi)
Tool Primitives là một kho hàm đa hàm (25.519 hàm) được thiết kế để agent gọi tool bằng ngôn ngữ tự nhiên. ToolFace là giao diện giữa agent và tool primitives. HEART framework gồm 3 thành phần: Planner (lập kế hoạch), Router (định tuyến công cụ), Verifier (xác thực). Agent sử dụng tool primitives để gọi tool, HEART quản lý luồng gọi tool, verifier kiểm tra kết quả trước khi trả lời người dùng.

## Key Findings
- HEART outperforms SFT-based models by 10% on average, surpasses three commercial models by 6% on average while reducing token/API cost by up to 85%.
- On 50 real-world tasks: HEART achieves 84% task completion, 3.8× the average of three frontier commercial models (22%).
- ToolBench: Pass Rate 75.1%, Win Rate 75.7% (+1.7%/+1.9% over Claude-4.6-Sonnet; +7.8%/+12.6% over ToolLLaMA).
- ACEBench: Overall 86.9% (vs GPT-5.4 86.0%); Special 95.0% vs 94.0%; Agent 72.3% vs 69.5%.
- Web Search Overall 84.0%, Memory Overall 69.38% (surpassing Claude-Sonnet-4.6 by +3.0%/+1.10%).
- HEART achieves 0.0% ASR (attack success rate) under both prompt injection attack strategies.
- HEART (GPT-5.4 + Qwen3-8B) reduces cost by over 12× relative to HEART (GPT-5.4).

## Actionable Insights
- Dùng framework Planner-Router-Verifier (HEART) để quản lý tool use: lập kế hoạch, định tuyến công cụ, xác thực kết quả trước khi trả lời. Áp dụng: solopreneur xây agent gọi tool nên chia thành 3 giai đoạn này, không để LLM tự quyết định tất cả.
- Dùng tool primitives (công cụ nguyên thủy tái sử dụng) thay để LLM tự build tool call từ đầu. Áp dụng: tạo thư viện hàm tái sử dụng cho các tác vụ phổ biến (tìm kiếm, tính toán, lấy dữ liệu) để agent gọi lại.
- Giảm chi phí API lên đến 85% bằng cách kết hợp mô hình lớn và nhỏ (GPT-5.4 + Qwen3-8B) trong HEART. Áp dụng: dùng mô hình lớn cho kế hoạch, mô hình nhỏ cho thực hiện tool call đơn giản.

## Assumptions & Limitations
- Điều kiện: cần có kho tool primitives đã curate (25.519 hàm) và hệ thống gọi tool; không áp dụng nếu không có tool nào.
- Paper thừa nhận: SFT-based models fail almost entirely on dynamic agentic tool scenarios; HEART cần được đánh giá trên nhiều mô hình khác.
- Limitation paper không nói: chưa đánh giá chi phí triển khai thực tế (không chỉ API), chưa test trên agent multi-turn dài hạn.

## Metadata
- Năm: 2026
- Tác giả: Haibo Jin, Suijin Wang, Xucheng Yu, Haojing Luo, Haohan Wang (UIUC, Starc Institute)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.01736
