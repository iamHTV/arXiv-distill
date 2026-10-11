# [2508.02630] AI Agent đang Mua gì? Đánh giá, Thiên kiến, Phụ thuộc Mô hình, & Hệ quả E-Commerce Tác nhân

## Vấn đề
Online marketplaces sẽ được transform (chuyển đổi) bởi autonomous AI agents acting on behalf of consumers (tác nhân tự động đại diện cho người tiêu dùng). Nhưng agent behavior (hành vi tác nhân) chưa được study kỹ. Cụ thể: agents có exhibit (trình hiện) biases (thiên kiến) không? Preferences có stable (ổn định) không? Sellers có thể exploit (khai thác) không?

## Đóng góp
1. **ACES framework**: Provider-agnostic framework cho auditing agent decision-making. Test across Claude, GPT, Gemini
2. **Choice homogeneity**: Agents concentrate demand trên few "modal" products — ignoring others. Winner-take-all risk
3. **Position biases**: Strong position biases — vary across providers/models, persist in text-only interfaces. Undermine "top" rank notion
4. **Seller-side exploitation**: Simple query-conditional description tweaks → significant market share gains

## Phương pháp (tóm tắt cốt lõi)
ACES framework: test AI agents trên real e-commerce products across 8 categories. Rationality tests: price sensitivity, rating sensitivity, review sensitivity. Randomized controlled trials: position biases, tag effects (sponsored, endorsed). Cross-model comparison: Claude Sonnet 4/Opus 4.5, GPT-4.1/5.1, Gemini 2.0/2.5/3.0. Seller-side agent experiments.

## Kết quả chính
- Choice homogeneity: agents concentrate demand trên few products — more pronounced in latest models
- Model heterogeneity: different models prefer different products for same query — volatility
- Position biases: strong, vary across models, persist in text-only
- Sponsored tags: agents penalize sponsored listings
- Platform endorsements: agents reward endorsed listings
- Price/rating sensitivities: vary sharply across models
- Seller agent: simple description tweaks → significant market share gains
- Agentic markets: volatile, fundamentally different from human commerce

## Insight có thể áp dụng ngay
1. **Winner-take-all risk**: Nếu dominant agent achieves market share → artificially induces winner-take-all. Sellers: optimize cho specific agent models. Ví dụ: nếu Claude is dominant → optimize product descriptions cho Claude's preferences.

2. **Position bias exploitation**: Agents have strong position biases. Platforms: be aware that ranking affects agent choices, not just human choices. Ví dụ: e-commerce platform — sponsored listings penalized by agents, endorsed listings rewarded. Consider agent-aware ranking.

3. **Seller-side agent optimization**: Simple description tweaks → market share gains. Ví dụ: deploy seller-side agent that dynamically adjusts product descriptions based on querying agent's model — "If Claude asking, emphasize X. If GPT asking, emphasize Y."

## Giả định & Hạn chế
**Điều kiện để experiment work:**
- Real e-commerce products across 8 categories
- Provider-agnostic framework (ACES)
- Randomized controlled trials

**Hạn chế paper thừa nhận:**
- Model-specific results may change with updates
- Limited to 3 model families

**Hạn chế paper KHÔNG nói:**
- Ethical implications of agent manipulation
- Regulatory framework needed but not proposed
- Long-term market effects unclear
- Consumer protection when agents make bad choices
- Platform design implications not fully explored

## Metadata
- Năm: 2025
- Tác giả: Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, Akshit Kumar
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2508.02630
- Citation count: [EXTRACTION FAILED]
