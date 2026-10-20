# Skill: conversation-trained-sales-agent

Source: 2610.25461v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần triển khai một AI sales agent cho trang web thương mại điện tử hoặc dịch vụ đặt chỗ, và có sẵn transcript lịch sử của cuộc trò chuyện chatlive hoặc tư vấn bán hàng.
- Khi muốn kiểm tra xem việc fine-tuned mô hình trên cuộc hội thoại thương mại thật có cải thiện conversion so với mô hình frontier general-purpose hay không.
- Khi cần đưa ra quyết định giữa triển khai AI agent và giữ nhân viên bán hàng live chat, dựa trên chi phí và conversion.

## Tình huống KHÔNG nên dùng
- Khi tác vụ là general Q&A không có kết quả kinh doanh đo lường được (ví dụ: agent trả lời câu hỏi về sản phẩm mà không yêu cầu mua hàng).
- Khi không có transcript cuộc hội thoại bán hàng thật để đào tạo (cần ít nhất 10,000+ cuộc trò chuyện có nhãn kết quả).
- Khi chỉ cần demo marketing nhanh mà không cần kiểm tra nghiêm ngặt bằng A/B test.

## Input cần có
- Corpus transcript cuộc hội thoại thương mại thật (ít nhất 10,000 cuộc trò chuyện, được de-identify và có nhãn kết quả: mua/hủy/lead).
- Danh sách các trang web mục tiêu với catalog hoặc kho hàng có thể đọc được bằng máy.
- Mô hình mở trọng số cơ sở (ví dụ: Qwen3-32B) và資 nguyên GPU (khuyến nghị 32 H100 hoặc tương đương).
- Công cụ agent scaffold: chat widget, catalog retrieval, tools (search catalog, get item, check availability, add to cart, get policy, capture lead, handoff to human), system prompt template, output guardrails.

## Các bước thực hiện
1. Thu thập và lọc corpus: loại bỏ các cuộc hội thoại nhắc đến trang web評 giá, thu thập với sự đồng ý của người dùng, de-identify (automated PII redaction + hashed identifiers + manual QA), kiểm tra tỷ lệ PII còn lại dưới 0.2%.
2. Chia dữ liệu: SFT examples (ít nhất 1 triệu), preference pairs (ít nhất 100,000 cặp, preferred turn dẫn đến tiến độ mua/đặt/lead, dispreferred turn dẫn đến stall/exit), constraint examples (ít nhất 30,000, dạy ràng buộc về giảm giá, yêu cầu ngoài catalog, khai báo AI, chuyển giao người).
3. Huấn luyện mô hình: SFT trên base model (2 epochs), sau đó preference optimization (DPO hoặc tương đương), cuối cùng train trên dữ liệu ràng buộc. Tổng thời gian ước tính 2,240 GPU-hours trên 32 H100.
4. Xây dựng agent scaffold: cùng widget, greeting, disclosure line ("Tôi là trợ lý mua sắm AI"), retrieval catalog làm tươi mỗi 24 giờ, tools, system prompt per site, guardrails (lọc giá, giảm giá, chính sách), ngân sách trễ 8 giây.
5. Triển khai A/B test: ngẫu nhiên hóa khách vào các arm (không agent, Javo, agent frontier), mỗi khách gán cố định cho một arm, chạy ít nhất 2–4 tuần, thu thập 14.8 triệu lượt khách như trong paper.
6. Đo lường kết quả: RPV (revenue per visitor), conversion, engaged conversion, CSAT, chi phí mỗi cuộc trò chuyện tham gia, các guardrails (tỷ lệ trả hàng, hủy, phàn nàn, yêu cầu không đượcSupported, chiến thuật áp lực cấm).
7. So sánh và ra quyết định: nếu Javo non-inferior so với nhân viên và vượt front model trên engaged conversion, triển khai rộng; nếu không, giữ model frontier hoặc điều chỉnh dữ liệu đào tạo.

## Output mong đợi
- Một AI sales agent đã được fine-tuned trên corpus thương mại domain-specific.
- Báo cáo A/B test với engaged conversion, RPV, CSAT, chi phí mỗi cuộc trò chuyện, và tất cả các chỉ số guardrail.
- Quyết định triển khai: triển khai rộng, giữ nguyên, hoặc dừng dự án.

## Ví dụ áp dụng
Một trang web bán mỹ phẩm và chăm sóc cá nhân có 50,000 lượt khách/tháng, muốn triển khai AI agent tư vấn và bán hàng. Họ thu thập 15,000 transcript chatlive cũ, gán nhãn kết quả (mua/hủy), SFT Qwen3-32B trên corpus này, sau đó chạy A/B test với agent frontier GPT-5.2 cùng widget và catalog trên 10% traffic trong 3 tuần. Kết quả mong đợi: engaged conversion tăng 15–25%, chi phí mỗi cuộc trò chuyện giảm từ $3.40 (nhân viên) xuống khoảng $0.06 (AI).

## Gotchas
- Không để từ tiếng Anh không giải thích: fine-tuned (điều chỉnh tối siêu), supervised fine-tuning (hu giám sát), preference optimization (tối ưu hóa ưu tiên), de-identify (bỏ mã hóa thông tin cá nhân), PII (thông tin nhận dạng cá nhân), scaffolding (khung necesarios), guardrail (rào cản an toàn), engagement-scaled (thang đo theo mức độ tương tác), intent-to-treat (mục đích điều trị), CACE (tác động tác nhân tuân thủ trung bình), winsorized (chống cực đoan), bot filtering (lọc robot), sample ratio (tỷ lệ mẫu), novelty effect (hiệu ứng tươi mới), interference (sự can thiệp), CUPED (sử dụng dữ liệu trước thí nghiệm để giảm phương sai), non-inferiority (không kém hơn), superiority (vượt trội), Holm adjustment (điều chỉnh Holm), Benjamini-Hochberg (điều chỉnh Benjamini-Hochberg), randomization (ngẫu nhiên hóa), sticky assignment (gán cố định), pre-period (khu vực trước), A/A test (thử A/A), sell-out (hết hàng), CACE estimation (ước lượng CACE), trimming bounds (giới hạn cắt bớt), ITT difference (sự khác biệt ITT), disclosure (khai báo), consent banner (banner đồng ý), data processing agreement (thỏa thuận xử lý dữ liệu), dark pattern (mẫu tối tăm), confirmshaming (xin cảm ơn từ chối).
- Scaffold phải giống hệt giữa các arm: bất kỳ chênh lệch về widget, prompt, tools, guardrails sẽ làm sai kết quả so sánh mô hình.
- Khai báo AI (AI disclosure) có thể giảm mua hàng (theo Luo et al., 2019); mọi hiệu ứng báo cáo là NET of honest disclosure.
- Không tự tin vào kết quả Study 1 một cách đơn độc — khách giả tạo (simulator) có thể reorder leaderboard.
- Tác giả có mâu thuẫn lợi ích (Founder/CEO của công ty vận hành Javo); không có independent statistical review.
- Kết quả có thể không chuyển sang ngôn ngữ ít được biểu diễn trong corpus đào tạo (cross-lingual consistency yếu).
- Không nghiên cứu buyer-side agents (khách mua qua agent AI).