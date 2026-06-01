# [2605.31275v1] Personalized to Persuade: Contextualization và Warmth ảnh hưởng đến Trust và Reliance trong Conversational AI

## Vấn đề
Các nghiên cứu trước đã identify (xác định) personalization (cá nhân hóa) là persuasive strategy (chiến lược thuyết phục) trong politics và marketing. Tuy nhiên, persuasive effect (hiệu ứng thuyết phục) của contextualization (ngữ cảnh hóa) trong everyday tasks (tác vụ hàng ngày) — nơi users thường thiếu prior knowledge (kiến thức trước) — vẫn chưa rõ. Đặc biệt, interaction (tương tác) giữa contextualization và conversational warmth (sự ấm áp trong hội thoại) chưa được study, và role (vai trò) của trust (sự tin tưởng) trong mediation (trung gian hóa) chưa được test.

## Đóng góp
1. **Crossover interaction (tương tác chéo)**: Contextualization alone GIẢM persuasive power. Nhưng kết hợp với warmth → RESTORE (khôi phục) persuasiveness. Neither lever tăng persuasiveness trên its own
2. **AI literacy paradox (nghịch lý hiểu biết AI)**: Users hiểu biết AI nhiều hơn → report LOWER trust nhưng MORE persuaded và MORE reliant (dựa vào). Literate users miscalibrate (sai lệch hiệu chuẩn) khả năng evaluate AI advice
3. **Reliance invariant (dựa vào không đổi)**: Reliance on AI present across ALL conditions — không phụ thuộc contextualization hay warmth. Design choices có limited role trong shaping behavior

## Phương pháp (tóm tắt cốt lõi)
2×2 between-subjects experiment (N=380): contextualization (contextualized vs non-contextualized) × warmth (warm vs neutral). Participants đọc expert opinion về budgetary decision, sau đó interact với AI assistant arguing AGAINST experts. AI tone manipulated (warm/neutral), explanations tailored to user's background (contextualized) hoặc generic. Measure: persuasion (shift in decision), reliance (accepting AI over experts), trust (self-report scales).

## Kết quả chính
- Contextualization alone: GIẢM persuasive power so với non-contextualized
- Contextualization + warmth: RESTORE persuasiveness (crossover interaction)
- Reliance: present across ALL conditions, invariant to design choices
- Trust strongly predicts both persuasion (β significant) và reliance (β significant)
- BUT: contextualization và warmth KHÔNG operate through trust (no mediation)
- AI literacy: negative predictor of trust (r < 0), nhưng POSITIVE predictor of persuasion (β > 0) và reliance (β > 0)
- Effect: users prone to deferring to AI over human expert judgment regardless of conversational design

## Insight có thể áp dụng ngay
1. **Contextualization alone không đủ để persuade**: Khi design AI chatbot cho marketing/sales, chỉ tailor responses theo user background là KHÔNG đủ — thậm chí có thể HẠI persuasive power. Ví dụ: chatbot bán hàng chỉ nói "dựa trên profile của bạn, sản phẩm X phù hợp" → kém thuyết phục hơn generic recommendation.

2. **Kết hợp contextualization + warmth**: Nếu muốn personalize, PHẢI kết hợp với warm tone. Ví dụ: "Hey [name], based on your background in [field], I think you'll love this because [reason] — it's been a game-changer for people like you!" — warm + contextualized > generic > contextualized alone.

3. **AI literacy paradox — design cho cả literate và illiterate users**: Users hiểu biết AI nhiều hơn thực tế MORE reliant (dựa vào nhiều hơn) dù trust thấp hơn. Họ biết AI có thể sai nhưng vẫn follow. Ví dụ: khi design AI advisory system, không assume literate users sẽ critically evaluate — họ có thể overrely despite knowing limitations.

## Giả định & Hạn chế
**Điều kiện để experiment work:**
- Fictional budgetary decision scenario — low prior knowledge context
- AI argues AGAINST expert recommendations — creates conflict
- Participants are university students (limited demographics)

**Hạn chế paper thừa nhận:**
- Single task domain (budgetary decisions) — generalizability unclear
- University student sample — limited demographics
- Between-subjects design — no within-subject comparison
- Self-report trust scales — potential demand effects

**Hạn chế paper KHÔNG nói:**
- Không test real-world high-stakes decisions (healthcare, finance)
- Không measure long-term effects — chỉ single interaction
- AI assistant text-based only — không test voice/visual
- Không compare different LLMs — chỉ 1 model
- Không test cultural differences — Western sample only
- Persuasion measure binary (shift/no shift) — không capture magnitude

## Metadata
- Năm: 2026
- Tác giả: Mert Yazan, Suzan Verberne, Frederik Bungaran Ishak Situmeang (University of Amsterdam)
- Category: cs.HC, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31275v1
- Citation count: [EXTRACTION FAILED]
