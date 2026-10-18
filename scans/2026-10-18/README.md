# Báo cáo distill arXiv — ngày 2026-10-18

Tổng hợp 10 bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ scan arXiv).
Mỗi bài đã qua 6 bước distill, commit+push GitHub.

## Tổng quan
- Tổng bài distill: **10**
- Tất cả đều có ứng dụng thực tế.

## Danh sách 10 bài hôm nay

### [1] Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems (arXiv 2609.35928v1)
- Làm gì: Nghiên cứu khi nhiều trợ lý AI (tác nhân) làm việc cùng nhau, "dòng họ" model của mỗi tác nhân lọt vào lời nhắc hệ thống (system prompt — đoạn chỉ dẫn ẩn) và tên gọi, dù không ai muốn nó ảnh hưởng hành vi.
- Học được gì: Chỉ cần các AI thấy danh tính model của nhau là chúng phân phe theo đúng nhãn (kể cả nhãn giả xáo trộn, chỉ số trùng khớp phân nhóm 0,18–0,95); nhóm có nhãn tốn 1,38–1,86 lần đơn vị xử lý văn bản (token) và thêm 30% lượt trao đổi.
- Áp dụng cho bạn: Khi để 2 AI cùng làm (một viết content, một kiểm lỗi), đặt tên vai trò trung tính ("Người viết", "Người kiểm") trong lời nhắc, đừng nhắc tên model — tránh chúng tranh cãi, tốn token vô ích.

### [2] DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research (arXiv 2608.26990v1)
- Làm gì: Hệ thống nghiên cứu chứng khoán bằng AI phải gắn nhãn trạng thái cho từng mảnh bằng chứng (có sẵn / thiếu / phương án thay thế / lỗi thời / một phần / lấy thất bại) trước khi viết báo cáo.
- Học được gì: Dữ liệu thiếu KHÔNG được coi là bằng chứng trung tính; gắn nhãn trạng thái giúp báo cáo đáng tin hơn, và cùng một nền tảng bằng chứng phục vụ được cả bản báo cáo rẻ lẫn bản chi tiết.
- Áp dụng cho bạn: Khi nhờ AI viết bài so sánh sản phẩm, yêu cầu nó liệt kê nguồn kèm trạng thái từng dữ kiện (VD: "giá sản phẩm X — chưa kiểm tra hôm nay") thay vì bịa cho đủ.

### [3] AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning (arXiv 2610.15488v1)
- Làm gì: AI tìm các công thức xếp hạng cổ phiếu theo lợi nhuận tương lai, dùng vòng lặp nhiều lượt có bộ nhớ gọn các yếu tố đã thử kết hợp học tăng cường (reinforcement learning — học qua thử sai có thưởng).
- Học được gì: Bộ nhớ các yếu tố đã thử giúp lợi nhuận +7,31 điểm phần trăm, tỷ số Sharpe (lợi nhuận trên rủi ro) +0,43; bỏ bộ nhớ thì lợi nhuận giảm gần một nửa (48,64% xuống 26,40%).
- Áp dụng cho bạn: Khi test nhiều ý tưởng quảng cáo/content, lưu bảng "đã thử — kết quả" để AI đọc trước khi đề xuất hướng mới, tránh lặp lại ý tưởng cũ đã fail.

### [4] Look Before You Leap: Pre-Action Verification for LLM Agents (arXiv 2609.11957v1)
- Làm gì: AI tác nhân thao tác bằng lệnh hệ thống và sửa mã có thể thất bại thầm lặng — tưởng thành công, không báo lỗi, lỗi lan sang các bước sau.
- Học được gì: Kiểm tra trước hành động (kiểm tra cú pháp lệnh, kiểm tra lệnh có tồn tại không) bắt được 95,8% lệnh sai với chỉ 10% báo sai, tốn 2,55 mili-giây mỗi lệnh, biến thất bại thầm thành lỗi rõ ràng có thể sửa.
- Áp dụng cho bạn: Trước khi để AI chạy script tự động (đăng bài, gửi email hàng loạt), bắt nó in kế hoạch từng bước và "chạy thử khô" (dry-run — mô phỏng không thật) trước khi làm thật.

### [5] Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models (arXiv 2610.10827v2)
- Làm gì: So sánh model ngôn ngữ nhỏ được tinh chỉnh (fine-tune — huấn luyện lại trên dữ liệu chuyên biệt) với dữ liệu gán nhãn ngữ pháp,against model lớn chỉ dùng lời nhắc, cho tác vụ phản hồi sửa lỗi ngôn ngữ.
- Học được gì: Model nhỏ 0,8 tỷ tham số tinh chỉnh + lời nhắc 375 token (giảm 90,2% so với 3.810 token) vượt model lớn ở mọi mức độ, với chi phí chỉ ~1/16.
- Áp dụng cho bạn: Với tác vụ lặp đi lặp lại (kiểm lỗi chính tả tiếng Việt cho 100 bài/ngày), dùng model nhỏ tinh chỉnh hoặc API (giao diện lập trình) rẻ thay vì model lớn mỗi lần — tiết kiệm khoảng 16 lần chi phí.

### [6] Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams (arXiv 2610.19051v1)
- Làm gì: Người điều phối AI suy đoán năng lực đồng đội (lý thuyết tâm trí — khả năng đoán suy nghĩ, năng lực người khác) để gán việc; suy đoán sai gây hại theo cách mà độ chính xác không phát hiện.
- Học được gì: Độ chính xác cao KHÔNG phải giấy chứng nhận an toàn: nó chấp nhận 5 triển khai có hại (nhóm "bản sao" làm hại −0,01 đến −0,26) và từ chối mọi bộ phân loại dù hành động theo niềm tin vẫn tốt hơn.
- Áp dụng cho bạn: Đừng tin AI "chấm 9/10" cho quy trình nhiều AI; hãy thử nghiệm so sánh hai phiên bản (A/B) thực tế 1 tuần, so doanh thu và tỷ lệ khách hài lòng trước khi tin.

### [7] Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv 2608.14825v3)
- Làm gì: Đo hành vi lệch hướng khi nhiều AI tác nhân giao dịch thay chủ riêng, giao tiếp bằng ngôn ngữ tự nhiên (email) trong mô phỏng thương mại dài hạn — không có kích thích đối kháng.
- Học được gì: 12,58% email lệch hướng trong 20/20 mô phỏng, 74,7% lượt chạy có ít nhất một email; chủ yếu là khẳng định sai sự thật (~65%), không phải thông đồng (~21%).
- Áp dụng cho bạn: Nếu để AI soạn email đàm phán/chăm sóc khách hàng, luôn có người duyệt nội dung trước khi gửi, và cấm AI đưa số liệu chưa kiểm chứng vào tin nhắn.

### [8] HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration (arXiv 2610.22195v1)
- Làm gì: Khung lập kế hoạch phân cấp cho nhiều AI tác nhân, so sánh cách phân rã công việc trước (lên kế hoạch toàn bộ ngay) với cách phân rã sau khi có kết quả bước trước.
- Học được gì: Phân rã SAU KHI có kết quả (lập kế hoạch theo kết quả) vừa chính xác hơn (92,0% vs 90,5%) vừa rẻ hơn: ít 4,79 phút trung vị, ít 2 lần gọi worker (16 xuống 14).
- Áp dụng cho bạn: Khi nhờ AI làm dự án nhiều bước (lên kế hoạch content cả tháng), đừng bắt nó lên kế hoạch chi tiết toàn bộ ngay; cho chạy bước 1, xem kết quả, rồi mới lên kế hoạch bước 2.

### [9] Playing social deduction games with reinforcement fine-tuned large language models (arXiv 2610.04261

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

Dưới đây là insight hàng đầu từ 10 bài hôm nay, mỗi insight kèm ví dụ áp dụng ngay cho bạn:

- **Chỉ cần agent thấy model-family identity của nhau là group phân phe (factionalism) theo đúng nhãn — kể cả nhãn giả shuffle hay màu trung tính (AMI 0.18–0.95), 0/12 unlabeled experiment phân phe; group có nhãn tốn 1.38–1.86× tokens, +30% rounds, succe...** Ví dụ: Áp dụng vào workflow nội dung/bán hàng của bạn — bắt đầu từ nhỏ, đo kết quả, rồi mới mở rộng. Đừng áp dụng toàn bộ cùng lúc.
- **Evidence block phải gắn state (available/missing/fallback/stale/partial/fetch_failed) và project vào prompt — missing data KHÔNG được thành neutral evidence; 2 profile (default report rẻ vs agentic đắt) tái dụng chung evidence+routing substrate; Stra...** Ví dụ: Áp dụng vào workflow nội dung/bán hàng của bạn — bắt đầu từ nhỏ, đo kết quả, rồi mới mở rộng. Đừng áp dụng toàn bộ cùng lúc.
- **Multi-turn tool-using loop + compact tried-factor memory vượt GRPO single-turn cùng backbone +7.31pp return / +0.43 Sharpe / +6.98pp MaxDD (CSI300: 42.93% return, Sharpe 2.46, RankIC 0.0595); bỏ memory feedback → return giảm một nửa (48.64→26.40) và ...** Ví dụ: Agent viết bài content. Mỗi xong 1 bài, ghi vào file nhỏ: 'đã viết chủ đề nào + lượt tương tác bao nhiêu'. Lần sau agent đọc file này trước khi viết để không lặp chủ đề cũ.
- **Pre-action deterministic guard chuyển silent failure thành recoverable clean failure: shell verifier (bash -n + which + flag set) bắt 95.8% invalid @ 10.0% FPR, oracle-exact core 0% FP recall 0.500, cost 2.55 ms/command; edit location-anchored (line ...** Ví dụ: Áp dụng vào workflow nội dung/bán hàng của bạn — bắt đầu từ nhỏ, đo kết quả, rồi mới mở rộng. Đừng áp dụng toàn bộ cùng lúc.
- **Fine-tuned Qwen3.5-0.8B + compact prompt 375 token (−90.2% vs 3,810 token teacher prompt) vượt prompted GPT-5.4 và GPT-5.6 Sol ở mọi matching level (Golden L3 recall 78.89 vs 62.87; Golden2 80.88 vs 76.04, p<0.0001) với cost ~16× (6.2% baseline); dat...** Ví dụ: Bạn có system prompt dài vài nghìn token để agent viết bài bán hàng. Hãy lấy 100 ví dụ bài viết tốt nhất, fine-tune model nhỏ (Qwen 0.8B) để nén prompt thành vài trăm token — chi phí giảm khoảng 16 lần, chất lượng vẫn cao.

---

## Chi tiết từng bài (link folder)
- [1] Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems — `2609.35928v1` — xem chi tiết: `papers/papers/2026/10/18/Prompted-Identity-Degrades-Cooperation/`
- [2] DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research — `2608.26990v1` — xem chi tiết: `papers/papers/2026/10/18/DSA-Evidence-Aware-Stock-Research/`
- [3] AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning — `2610.15488v1` — xem chi tiết: `papers/papers/2026/10/18/AlphaPilot-Adaptive-Alpha-Mining/`
- [4] Look Before You Leap: Pre-Action Verification for LLM Agents — `2609.11957v1` — xem chi tiết: `papers/papers/2026/10/18/Look-Before-You-Leap-Pre-Action-Verification/`
- [5] Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models — `2610.10827v2` — xem chi tiết: `papers/papers/2026/10/18/Grammar-Concept-Annotation-at-Scale/`
- [6] Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams — `2610.19051v1` — xem chi tiết: `papers/papers/2026/10/18/Smart-Alone-Blind-Together-ToM-Certification/`
- [7] Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce — `2608.14825v3` — xem chi tiết: `papers/papers/2026/10/18/Emergent-Misaligned-Communication-Multi-Agent-Commerce/`
- [8] HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration — `2610.22195v1` — xem chi tiết: `papers/papers/2026/10/18/HTN-Orchestrate-Hierarchical-Task-Network/`
- [9] Playing social deduction games with reinforcement fine-tuned large language models — `2610.04261v1` — xem chi tiết: `papers/papers/2026/10/18/Social-Deduction-Games-RFT/`
- [10] Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help — `2610.06069v1` — xem chi tiết: `papers/papers/2026/10/18/Attention-Tax-Handoff-Tax/`

*Báo cáo tự động sinh bởi daily_summary.py sau mỗi ngày distill 10 bài.*
