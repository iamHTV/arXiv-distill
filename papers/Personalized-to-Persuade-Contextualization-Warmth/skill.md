# Skill: AI Persuasion — Contextualization + Warmth
Nguồn: 2605.31275v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi design (thiết kế) AI chatbot/assistant cho persuasive contexts (bối cảnh thuyết phục): sales, marketing, advisory
- Khi muốn maximize (tối đa hóa) persuasiveness (sức thuyết phục) của AI responses
- Khi evaluate (đánh giá) effectiveness (hiệu quả) của personalization strategies (chiến lược cá nhân hóa)

## KHÔNG nên dùng khi
- Task không cần persuasion (information retrieval, pure Q&A)
- Users có high prior knowledge (kiến thức trước cao) về topic
- Context không cho phép warm tone (formal, legal, medical)

## Input cần có
- Target user personas (persona người dùng mục tiêu)
- Persuasive goal (mục tiêu thuyết phục): buy, adopt, change opinion
- Conversational tone guidelines (hướng dẫn giọng hội thoại)
- User background data (dữ liệu nền tảng người dùng) cho contextualization

## Các bước thực hiện

### Bước 1 — Assess Persuasion Context (đánh giá bối cảnh thuyết phục)
1. Xác định: users có prior knowledge về topic không?
   - Low prior knowledge → contextualization có thể ineffective
   - High prior knowledge → contextualization có thể work better
2. Xác định: AI đang argue FOR hay AGAINST existing opinion/expert?
   - Against experts → users prone to defer anyway
3. Xác định: stakes (mức độ quan trọng) — low vs high

### Bước 2 — Design Conversational Style (thiết kế giọng hội thoại)
1. KHÔNG dùng contextualization alone — có thể REDUCE persuasiveness
2. PHẢI combine contextualization + warm tone
3. Warm tone elements:
   - Personal greeting ("Hey [name]!")
   - Empathetic language ("I understand your situation")
   - Enthusiastic framing ("This is a game-changer!")
   - Personal experience references ("People in your field love this")
4. Contextualization elements:
   - Reference user's background/profession
   - Use domain-specific examples
   - Connect to user's goals/situation

### Bước 3 — Test Persuasion Effectiveness (kiểm tra hiệu quả thuyết phục)
1. A/B test: contextualized-only vs warm+contextualized vs generic
2. Measure: persuasion (attitude shift), reliance (behavioral acceptance), trust (self-report)
3. Control: non-contextualized versions
4. Key metric: persuasion shift magnitude, not just binary

### Bước 4 — Handle AI Literacy Paradox (xử lý nghịch lý hiểu biết AI)
1. Don't assume literate users will critically evaluate AI
2. Literate users may MORE reliant despite lower trust
3. Design implications:
   - Add explicit uncertainty indicators ("I'm 70% confident")
   - Provide source citations
   - Include "consult expert" prompts
   - Don't rely on user literacy as safeguard

### Bước 5 — Monitor Reliance Patterns (giám sát patterns dựa vào)
1. Track: are users accepting AI advice over expert recommendations?
2. Reliance invariant across design choices — don't expect design to reduce it
3. Instead: design for calibrated reliance (dựa vào đúng mức):
   - Show confidence levels
   - Provide counter-arguments
   - Highlight when AI disagrees with experts

## Output mong đợi
- Conversational style guidelines cho AI persuasive contexts
- A/B test results: which combination maximizes persuasion
- Reliance monitoring dashboard
- Design patterns cho calibrated reliance

## Ví dụ áp dụng
**Tình huống**: E-commerce chatbot persuade users to buy premium product. Users lack prior knowledge về premium features.

**Áp dụng**:
1. Context: low prior knowledge, AI argues FOR purchase (not against experts)
2. Design: warm + contextualized
   - BAD: "Based on your profile, the Premium plan includes X, Y, Z" (contextualized only)
   - GOOD: "Hey [name]! I know you're juggling [their situation] — the Premium plan has been a lifesaver for folks in [their industry]. Imagine not having to worry about [pain point] anymore! 🎯" (warm + contextualized)
3. Test: A/B test 3 versions, measure conversion rate
4. Monitor: are users buying without checking alternatives? → reliance indicator
5. Add: "Want to compare with Basic plan?" → calibrated reliance

## Lưu ý quan trọng
1. **Contextualization alone HURTS**: Không personalize mà không warm tone. Kết quả: worse than generic
2. **Trust ≠ behavior**: Trust predicts behavior nhưng design không operate through trust. Trust là individual difference, không phải design lever
3. **Reliance is invariant**: Design choices không giảm reliance. Thay vào đó, design cho calibrated reliance
4. **AI literacy paradox**: Literate users MORE reliant. Không assume knowledge = critical evaluation
5. **Single interaction limitation**: Experiment chỉ 1 interaction. Long-term effects có thể khác
6. **Cultural bias**: Sample Western. Warm tone có thể interpret khác ở different cultures
