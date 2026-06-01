# Skill: Mô phỏng Marketing bằng Đa tác nhân LLM
Nguồn: 2510.18155
Loại: workflow (quy trình làm việc)

## Khi nào dùng skill này
- Khi cần test marketing strategy (chiến lược tiếp thị) trước khi deploy (triển khai) thực tế — giảm risk (rủi ro) và cost (chi phí)
- Khi cần simulate (mô phỏng) consumer behavior (hành vi người tiêu dùng) dưới các scenarios (kịch bản) khác nhau — pricing, promotions, product launches
- Khi cần observe (quan sát) emergent social dynamics (động lực xã hội mới phát sinh) — word-of-mouth, habit formation, social coordination

## KHÔNG nên dùng khi
- Cần quantitative accuracy (độ chính xác định lượng) cao — simulation chỉ cho qualitative insights (insights định tính)
- Market quá lớn (10K+ consumers) — LLM simulation tốn kém
- Cần real-time results (kết quả tức thời) — simulation chạy chậm

## Input cần có
- Virtual environment design (thiết kế môi trường ảo): locations, spatial dynamics (động lực không gian)
- Agent personas (hồ sơ tác nhân): demographics, income, preferences, needs
- Marketing strategy to test (chiến lược cần test): discount, promotion, pricing, etc.
- LLM access: DeepSeek-V3 hoặc tương đương
- Simulation parameters (tham số mô phỏng): duration, agent count, location count

## Các bước thực hiện

### Bước 1 — Design Virtual Environment (thiết kế môi trường ảo)
1. Tạo town map với locations: residential, business, shopping, dining, leisure
2. Define spatial dynamics (định nghĩa động lực không gian): distances, paths between locations
3. Place shops/stores strategically (đặt cửa hàng chiến lược): maximize exposure (tiếp xúc)
4. Define shared resources (tài nguyên chung): location tracker, time system

### Bước 2 — Create Agent Personas (tạo hồ sơ tác nhân)
1. Diverse demographics (nhân khẩu học đa dạng): ages, professions, income levels
2. Unique preferences (sở thích riêng): food, activities, social tendencies
3. Needs system (hệ thống nhu cầu): grocery, energy, finance — triggers (kích hoạt) behavior
4. Memory system (hệ thống nhớ): short-term và long-term memory cho mỗi agent

### Bước 3 — Implement Agent Cognition (triển khai nhận thức tác nhân)
1. LLM-powered planning: agents plan daily routines dựa trên needs, preferences, memory
2. Decision logic: agents make choices (dining, shopping, socializing) dựa trên context
3. Conversation system: agents interact, share information, make plans together
4. Reflection: agents review past experiences, update preferences

### Bước 4 — Run Simulation & Analyze (chạy mô phỏng & phân tích)
1. Inject marketing strategy (tiêm chiến lược): discount, promotion, new product
2. Run simulation N days, track all agent decisions
3. Analyze: sales performance, market share, loyalty patterns, social dynamics
4. Compare: treatment group (có promotion) vs control (không promotion)
5. Extract insights: substitution vs expansion, habit formation, word-of-mouth

## Output mong đợi
- Sales impact (tác động doanh số): revenue change, market share shift
- Consumer behavior patterns (khuôn mẫu hành vi): loyalty, exploration, switching
- Social dynamics (động lực xã hội): word-of-mouth, coordination, habit formation
- Strategy recommendations (khuyến nghị chiến lược): optimal discount level, timing, targeting

## Ví dụ áp dụng
**Tình huống**: Coffee chain muốn test "buy 1 get 1 free" promotion cho new product launch. Không muốn spend real budget trước khi know effectiveness.

**Áp dụng**:
1. Virtual town: 10 coffee shops, 20 agents với diverse coffee preferences
2. Agents có needs: caffeine, social, budget. Memory: past coffee experiences
3. Inject BOGO promotion ở 1 shop, days 3-5
4. Run 7-day simulation
5. Analyze: did promotion attract new customers? Did they return? Did word-of-mouth spread? Did it cannibalize other shops?

## Lưu ý quan trọng
1. **Qualitative, not quantitative**: Simulation cho behavioral patterns, KHÔNG cho exact numbers — dùng để generate hypotheses, không phải predict exact ROI
2. **Scale limitation**: 11 agents quá ít — cần scale lên 100+ cho meaningful market simulation
3. **LLM hallucination**: Agents có thể generate unrealistic behavior — validate (xác minh) against known consumer psychology
4. **Cost**: LLM calls tốn kém at scale — tính budget trước khi run large simulations
5. **Environment design matters**: Spatial layout ảnh hưởng behavior mạnh — design carefully
6. **Single scenario limitation**: Paper chỉ test discount — cần test multiple strategies để generalize
