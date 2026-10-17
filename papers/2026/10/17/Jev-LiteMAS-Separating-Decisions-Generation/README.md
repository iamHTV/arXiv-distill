# [2610.21411v1] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

## Problem
- Các tác nhân đa agent (multi-agent LLM systems) dựa vào mô hình ngôn ngữ generative cho chuyên gia thực thi, lập kế hoạch quy trình, và đánh giá artifacts. Tuy nhiên, nhiều thao tác điều phối chỉ cần ra quyết định có giới hạn (bounded decisions), như chọn chuyên gia tiếp theo hoặc đánh giá chất lượng artifact. Prior work chưa giải quyết được việc thay thế các thao tác này bằng mô hình quyết định chi phí thấp (low-cost decision model) mà vẫn giữ được chất lượng.

## Contribtuion
- Jev-LiteMAS — một framework đa agent kết hợp mô hình quyết định nhẹ (Jev) với thực thi và phản hồi generative.
- Jev chọn chuyên gia động từ nhiệm vụ và đầu ra chuyên gia trước đó, dùng ngữ cảnh tích lũy để căn cảnh thực thi sau này mà không cần khởi động lập kế hoạch trước (pre-generated trajectory).
- Jev lọc các artifact trung gian theo tiêu chí nhiệm vụ: artifact đạt tiêu chuẩn tiến hành trực tiếp, artifact bị cõi đánh dấu trải qua LLM re-review để chấp nhận hoặc phản hồi khắc phục.
- Trên bốn benchmark và hai backbone (backbone), Jev-LiteMAS giảm token generative-LLM bởi 12.7–54.6% so với LAS, duy trì độ chính xác trong 1.34 điểm phần trăm và giảm độ trễ trong bảy của tám thiết lập. Việc căn lộ trình (routing) vào output thực tế của chuyên gia ngăn mất mát độ chính xác lên đến 18.0 điểm.

## Method (tóm tắt cốt lõi)
- Framework Jev-LiteMAS gồm ba thành phần: Jev (mô hình quyết định nhẹ), thực thi generative, và phản hồi (feedback).
- Bước 1: Jev chọn chuyên gia động từ nhiệm vụ và đầu ra chuyên gia trước đó, dùng ngữ cảnh tích lũy để căn cảnh thực thi sau này mà không cần khởi động lập kế hoạch trước.
- Bước 2: Chuyên gia thực thi nhiệm vụ và tạo artifact trung gian.
- Bước 3: Jev sàng lọc artifact trung gian dựa trên tiêu chí nhiệm vụ: artifact đạt tiêu chuẩn tiếp tục trực tiếp, artifact bị cõi đánh dấu trải qua LLM re-review để chấp nhận (ACCEPT) hoặc phản hồi khắc phục (REVISE).
- Đánh giá trên bốn benchmark (IDRBench I3, API-Bank, v.v.) và hai backbone (DeepSeek-V4-Flash, GPT-5 expert).
- Jev screening phát hiện 91.33–95.33% các trường hợp bị nhiễm (corrupted cases).
- Cấu hình cascading tiêu thụ 14.6–21.7% ít token generative-LLM hơn LLM judgment.

## Key Findings
- 4 tác giả từ Đại học Jiao Tong Thượng Hải (Shanghai Jiao Tong University), category arXiv: cs.AI.
- Trên bốn benchmark và hai backbone, Jev-LiteMAS giảm token generative-LLM bởi 12.7–54.6% so với LAS.
- Độ chính xác thay đổi trong khoảng 1.34 điểm phần trăm.
- Giảm độ trễ trong bảy của tám thiết lập.
- Căn lộ trình (routing) vào output thực tế của chuyên gia ngăn mất mát độ chính xác lên đến 18.0 điểm.
- Cascaded configuration tiêu thụ 14.6–21.7% ít token generative-LLM hơn LLM judgment.
- Việc gắn buộc routing vào output thực tế của chuyên gia ngăn mất mát lên đến 18.0 điểm độ chính xác.

## Actionable Insights
1. Tách quyết định (decision) khỏi sinh (generation) trong multi-agent workflows: dùng model nhẹ (decision model) cho các quyết định điều phối, chỉ gọi LLM review khi artifact cần sửa. Áp dụng: thay LLM lớn cho mọi quyết định điều phối bằng decision model nhẹ (Jev), chỉ gọi LLM review khi artifact cần sửa, giảm 12.7–54.6% token.
2. Căn lộ trình (routing) vào output thực tế của chuyên gia (grounding routing in substantive expert outputs) để ngăn mất mát độ chính xác lên đến 18 điểm. Áp dụng: khi agent viết artifact, hãy kiểm tra artifact trước khi quyết định bước tiếp theo, không dựa vào suy luận trừu tượng.

## Assumptions & Limitations
- Feedback-driven routing hoạt động trên một nhóm chuyên gia (expert roles) và các hành động hợp lệ đã định trước (predefined).
- Framework không tạo động态 các chuyên gia mới.
- Đánh giá trên 4 benchmark và 2 backbone.
- Không nói rõ chi tiết về thời gian đào tạo và chi phí tính toán.

## Metadata
- Năm: 2026, tác giả: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li (Đại học Jiao Tong Thượng Hải), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2610.21411v1
