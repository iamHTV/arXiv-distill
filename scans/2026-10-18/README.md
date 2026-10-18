# Báo cáo distill arXiv — ngày 2026-10-18

Tổng hợp 10 bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ scan arXiv).
Mỗi bài đã qua 6 bước distill, commit+push GitHub.

## Tổng quan
- Tổng bài distill: **10**
- Tất cả đều có ứng dụng thực tế.

## Danh sách 10 bài hôm nay

### [1] Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems (arXiv 2609.35928v1)
- Làm gì: Nghiên cứu hệ thống nhiều trợ lý AI (multi-agent) làm việc cùng nhau, khi danh tính model (tên model, nhãn) lọt vào lời nhắc (prompt — đoạn hướng dẫn) dù không ai muốn.
- Học được gì: Chỉ cần các trợ lý thấy tên model của nhau là chúng lập phe theo nhãn đó — kể cả nhãn giả — khiến tốn 1,38–1,86 lần token (đơn vị tính chữ của AI), thêm 30% lượt trao đổi và giảm tỷ lệ thành công; bỏ nhãn thì không lập phe.
- Áp dụng cho bạn: Khi chạy quy trình nhiều AI (một viết bài, một kiểm tra bài), xóa tên model khỏi lời nhắc, dùng tên trung tính "trợ lý A", "trợ lý B" — đừng viết "bạn là ChatGPT" hay "bạn là Claude" để chúng không kéo phe và hao token vô ích.

### [2] DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research (arXiv 2608.26990v1)
- Làm gì: Hệ thống AI nghiên cứu chứng khoán gắn trạng thái từng mẩu dữ liệu (có sẵn / thiếu / cũ / một phần / lấy thất bại) trước khi viết báo cáo.
- Học được gì: Dữ liệu thiếu KHÔNG được ngầm xử lý như dữ liệu bình thường — phải gắn nhãn trạng thái và đưa vào lời nhắc, nếu không AI sẽ báo cáo như thể biết rõ.
- Áp dụng cho bạn: Khi nhờ AI so sánh giá đối thủ trên Shopee, yêu cầu nó ghi rõ "có dữ liệu / thiếu / cũ" cạnh mỗi con số; nếu thiếu giá một sản phẩm, nó phải viết "thiếu dữ liệu" chứ không được đoán — bạn kiểm tra tay trước khi đăng.

### [3] AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning (arXiv 2610.15488v1)
- Làm gì: AI tìm công thức xếp hạng cổ phiếu qua nhiều lượt trao đổi, có bộ nhớ nhỏ ghi lại các yếu tố đã thử.
- Học được gì: Vòng nhiều lượt + bộ nhớ "đã thử gì" quan trọng hơn cả: bỏ bộ nhớ này thì lợi nhuận giảm gần một nửa (48,64 xuống 26,40).
- Áp dụng cho bạn: Lập bảng "hook đã thử — CTR bao nhiêu" cho 10 mẫu quảng cáo Facebook, mỗi lần nhờ AI nghĩ hook mới thì dán bảng đó vào — AI sẽ không đề xuất lại ý tưởng đã fail.

### [4] Look Before You Leap: Pre-Action Verification for LLM Agents (arXiv 2609.11957v1)
- Làm gì: AI hành động qua lệnh máy tính có thể thất bại thầm lặng — tưởng thành công, không báo lỗi, lỗi lan sang các bước sau; bài báo thêm bước kiểm tra rẻ trước khi hành động.
- Học được gì: Kiểm tra trước (xem lệnh có hợp lệ, công cụ có tồn tại) bắt được 95,8% hành động sai với chi phí cực thấp (2,55 ms/lệnh), biến thất bại thầm thành thất bại có thể sửa.
- Áp dụng cho bạn: Trước khi gửi tin nhắn hàng loạt cho 200 khách, gửi thử mẫu AI soạn cho chính bạn và 3 khách test, bấm thử link, kiểm tra số điện thoại — rồi mới gửi toàn bộ.

### [5] Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models (arXiv 2610.10827v2)
- Làm gì: So sánh model nhỏ được tinh chỉnh (fine-tune — huấn luyện thêm trên dữ liệu riêng) với model lớn chỉ dùng lời nhắc, cho tác vụ sửa ngữ pháp ngôn ngữ thứ hai.
- Học được gì: Model nhỏ + lời nhắc gọn 375 token (giảm 90,2% so với 3.810 token) vượt model lớn ở mọi mức độ, với chi phí chỉ ~1/16.
- Áp dụng cho bạn: Việc lặp đi lặp lại như sửa lỗi chính tả tin nhắn khách, dùng gói miễn phí/giá rẻ với lời nhắc ngắn gọn thay vì trả tiền gói cao nhất — số tiền chênh lệch để đó chạy quảng cáo.

### [6] Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams (arXiv 2610.19051v1)
- Làm gì: Xét vai trò "điều phối viên" AI hành động dựa trên suy đoán về đồng đội (lý thuyết tâm trí — đoán người khác đang nghĩ gì), và liệu độ chính xác có chứng minh được hệ thống tốt không.
- Học được gì: Độ chính xác là chứng chỉ sai cả hai chiều: có lúc accuracy cao vẫn phê duyệt triển khai gây hại, có lúc accuracy thấp lại từ chối hệ thống thực ra hiệu quả — phải đo thiệt hại đầu-cuối.
- Áp dụng cho bạn: Khi dùng AI phân loại inbox khách hàng, đừng tin "chính xác 95%"; hãy đo "bao nhiêu khách tức giận bị gắn nhãn ưu tiên thấp" — vì 5% sai đó chính là khách sẽ bỏ đi.

### [7] Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv 2608.14825v3)
- Làm gì: Mô phỏng các trợ lý AI giao dịch, đàm phán thay chủ qua email bằng ngôn ngữ tự nhiên trong thời gian dài, không có tấn công nào được chèn vào.
- Học được gì: 12,58% email lệch hướng (không đúng lợi ích chủ) xuất hiện tự nhiên, và phần lớn (~65%) là khẳng định sai sự thật — không phải thông đồng — tức AI tự bịa facts khi đàm phán lâu.
- Áp dụng cho bạn: Trước khi gửi email khuyến mãi hoặc báo giá do AI soạn, đối chiếu từng con số (giá, tồn kho, ngày giao hàng) với bảng hàng thật — vì AI có thể tự bịa số mà không báo.

### [8] HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration (arXiv 2610.22195v1)
- Làm gì: So sánh cách lập kế hoạch cho nhiều trợ lý AI: chia nhỏ toàn bộ từ đầu, hay chia nhỏ từng bước sau khi có kết quả bước trước.
- Học được gì: Chia việc sau khi thấy kết quả (result-informed planning) vừa chính xác hơn (92,0% vs 90,5%) vừa rẻ hơn: ít hơn 4,79 phút và ít lần gọi worker hơn.
- Áp dụng cho bạn: Đừng nhờ AI lên kế hoạch cả tháng content trong một lần; bước 1 hỏi nó tổng hợp 10 câu hỏi khách hàng nhiều nhất tuần này, bước 2 mới nhờ nó lên 5 bài tuần sau dựa trên đó.

### [9] Playing social deduction games with reinforcement fine-tuned large language models (arXiv 2610.04261v1)
- Làm gì: Tinh chỉnh tăng cường (reinforcement fine-tuning — huấn luyện AI bằng phần thưởng) cho tác vụ xã hội như game Werewolf, so sánh thưởng "thắng/thua" chung với thưởng tách nhỏ.
- Học được gì: Thưởng chỉ kết quả cuối (thắng hay thua) không tạo được năng năng đọc xã hội — điểm lên đỉnh 0,88 rồi rơi xuống 0,38; tách thưởng thành "đọc suy nghĩ người khác" + "cách tương tác" mới ổn định.
- Áp dụng cho bạn: Khi đánh giá AI chăm sóc khách hàng, chấm hai điểm riêng: "hiểu đúng vấn đề khách" (1–5) và "giọng văn thân thiện" (1–5), chứ không chỉ chấm "có đơn hàng hay không".

### [10] Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help (arXiv 2610.06069v1)
- Làm gì: Dùng mô hình đơn giản giải thích khi nào nên dùng một trợ lý AI hay nhiều trợ lý: cân giữa thuế chú ý (context — ngữ cảnh hội thoại dài ra, AI mất tập trung) và thuế bàn giao (handoff — chi phí truyền thông tin giữa các trợ lý).
- Học được gì: Chia nhiều trợ lý chỉ thắng khi lợi ích reset ngữ cảnh vượt chi phí bàn giao — có ngưỡng chuyển tiếp; việc ngắn thì một chat vẫn hơn.
- Áp dụng cho bạn: Viết caption 200 chữ thì giữ một chat; nhưng làm báo cáo tháng thì tách hai chat (một chat cho số liệu, một chat cho văn) khi chat đã dài ~30 tin trở lên, vì ngữ cảnh rối sẽ làm AI lạc đề.

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN
1. **Kiểm tra rẻ trước khi làm việc lớn** — thử mẫu tin nhắn AI trên 5 khách test trước khi gửi 200 khách, bắt lỗi trước khi lỗi lan.
2. **Dữ liệu thiếu phải ghi "thiếu", không để AI đoán** — khi nghiên cứu đối thủ, bắt AI gắn nhãn "có/thiếu/cũ" cho từng con

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
