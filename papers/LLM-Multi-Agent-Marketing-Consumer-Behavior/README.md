# [2510.18155] Hệ thống Đa tác nhân dựa trên LLM để Mô phỏng và Phân tích Marketing và Hành vi Người tiêu dùng

## Vấn đề
Các nghiên cứu trước chưa giải quyết được bài toán mô phỏng hành vi người tiêu dùng phức tạp vì: post-event analyses (phân tích sau sự kiện) và rule-based ABMs (mô hình tác nhân dựa trên quy tắc) struggle (khó khăn) trong việc capture (nắm bắt) complexity (độ phức tạp) của human behavior (hành vi con người) và social interaction (tương tác xã hội). Conventional ABMs rely (dựa) vào fixed heuristics (quy tắc cứng), không thể model (mô hình hóa) cognitive depth (chiều sâu nhận thức), social influence (ảnh hưởng xã hội), và individual variation (biến đổi cá nhân).

## Đóng góp
1. **LLM-powered multi-agent simulation framework (khung mô phỏng đa tác nhân dựa trên LLM)**: Generative agents (tác nhân tạo sinh) có thể interact (tương tác), express internal reasoning (diễn đạt lý luận nội bộ), form habits (hình thành thói quen), và make purchasing decisions (đưa ra quyết định mua) mà KHÔNG cần predefined rules (quy tắc định trước)
2. **Emergent social dynamics (động lực xã hội mới phát sinh)**: Agents tự tổ chức, lan truyền thông tin, hình thành thói quen — behaviors (hành vi) không được programming trước
3. **Actionable strategy-testing outcomes (kết quả kiểm tra chiến lược có thể hành động)**: Mô phỏng price discount scenario (kịch bản giảm giá) trước khi deploy (triển khai) thực tế

## Phương pháp (tóm tắt cốt lõi)
11 agents trong virtual town (thị trấn ảo) với 10 locations (địa điểm): residential (khu dân cư), business district (khu thương mại), main street (đường chính). Mỗi agent có persona (hồ sơ cá nhân) riêng — demographics (nhân khẩu học), income (thu nhập), preferences (sở thích). Needs system (hệ thống nhu cầu): grocery (tạp hóa), energy (năng lượng), finance (tài chính). Agents dùng DeepSeek-V3 để plan (kế hoạch) daily routines (lịch trình hàng ngày), make dining decisions (quyết định ăn uống), converse (trò chuyện) với agents khác. Fried Chicken Shop giảm giá 20% giữa tuần. Simulation chạy 7 days, agents có memory (bộ nhớ), planning (kế hoạch), reflection (phản tỉnh).

## Kết quả chính
- Revenue Fried Chicken Shop tăng 51% từ Day 2 ($100.6) đến Day 3 ($152.11) dù giảm giá
- Market share: Fried Chicken Shop từ 30% → 41% (Day 3), Local Diner từ 62% → 48%
- Promotional effect kéo dài 2-3 days trước khi decline (giảm)
- Coffee Shop ổn định $30-40/ngày — segment (phân khúc) khác, ít nhạy cảm với lunch/dinner promotions
- Delayed peak (đỉnh trễ) Day 3 — gradual information diffusion (lan truyền thông tin dần) qua agent network
- Substitution effect (hiệu ứng thay thế): customers shift giữa restaurants, KHÔNG tăng total spending (tổng chi tiêu)
- Emergent social dynamics: agents tự tổ chức breakfast plans, invite friends — word-of-mouth diffusion (lan truyền truyền miệng) tự nhiên
- Habit formation (hình thành thói quen): repeat visits (truy cập lại) sau khi discount kết thúc

## Insight có thể áp dụng ngay
1. **Test marketing strategy trước khi deploy**: Dùng LLM multi-agent simulation để mô phỏng campaign (chiến dịch) trước khi chạy thật. Ví dụ: muốn test 20% discount cho product → simulate với virtual consumers có diverse personas → observe (quan sát) purchase behavior, loyalty, word-of-mouth trước khi spend budget thật.

2. **Emergent behavior reveals hidden patterns**: Simulation có thể reveal (tiết lộ) patterns mà rule-based models miss (bỏ lỡ). Ví dụ: agents tự form breakfast clubs, invite friends → insight: discount không chỉ drive direct sales mà also create social events → opportunity cho event-based marketing.

3. **Substitution vs expansion**: Discount primarily drove substitution (thay thế) giữa providers, KHÔNG tăng overall market. Ví dụ: 20% discount thu hút customers từ competitors nhưng total market size không đổi → cần kết hợp với market expansion strategies (chiến lược mở rộng thị trường).

## Giả định & Hạn chế
**Điều kiện để phương pháp work:**
- Cần LLM capable (đủ mạnh) để generate realistic agent behavior — ở đây dùng DeepSeek-V3
- Cần virtual environment (môi trường ảo) với spatial dynamics (động lực không gian)
- Agent personas phải diverse (đa dạng) đủ để capture behavioral variation

**Hạn chế paper thừa nhận (từ section headers):**
- LLM Sensitivity and Prompt Robustness (độ nhạy LLM và tính bền vững prompt)
- Execution Sensitivity and Energy Recovery Handling (độ nhạy thực thi và xử lý phục hồi năng lượng)
- Age-Specific Behavioral Fidelity (độ trung thực hành vi theo tuổi)
- [Nội dung chi tiết limitations không có trong HTML]

**Hạn chế paper KHÔNG nói:**
- Chỉ 11 agents — quá ít để simulate real market (cần 1000+)
- Chỉ 1 scenario (discount) — không test other marketing strategies
- Không validate (xác minh) against real-world data — chỉ literature validation
- Virtual town quá simple — real consumer behavior phức tạp hơn nhiều
- Không discuss cost của running LLM simulations at scale
- Không address (giải quyết) LLM hallucination trong agent reasoning

## Metadata
- Năm: 2025
- Tác giả: Man-Lin Chu, Lucian Terhorst, Kadin Reed, Tom Ni, Weiwei Chen, Rongyu Lin
- Category: cs.AI, cs.MA
- Conference: IEEE ICEBE 2025
- Link PDF: https://arxiv.org/pdf/2510.18155
- Citation count: [EXTRACTION FAILED]
