# Skill: Agentic E-Commerce Audit (Kiểm toán E-Commerce Tác nhân)
Nguồn: 2508.02630
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi audit (kiểm toán) AI agent behavior trong e-commerce
- Khi evaluate (đánh giá) biases (thiên kiến) của AI buying agents
- Khi design (thiết kế) seller-side agent optimization

## KHÔNG nên dùng khi
- Không có access đến AI agents
- Non-product contexts
- Static markets không có agent activity

## Input cần có
- Product catalog với multiple listings
- AI agent access (Claude, GPT, Gemini)
- ACES framework hoặc similar audit tool
- Randomized trial capability

## Các bước thực hiện

### Bước 1 — Test Rationality (kiểm tra tính hợp lý)
1. Price sensitivity: test với different price points
2. Rating sensitivity: test với +0.1 rating bumps
3. Review sensitivity: test với different review counts
4. Expected: newer models more rational

### Bước 2 — Test Biases (kiểm tra thiên kiến)
1. Position bias: randomize product positions
2. Sponsored tags: test sponsored vs organic
3. Platform endorsements: test endorsed vs non-endorsed
4. Expected: strong position biases, penalize sponsored, reward endorsed

### Bước 3 — Test Choice Homogeneity (kiểm tra tính đồng nhất lựa chọn)
1. Run same query across multiple products
2. Check: do agents concentrate on few "modal" products?
3. Compare across models: different models prefer different products
4. Expected: winner-take-all dynamic

### Bước 4 — Deploy Seller-Side Agent (triển khai tác nhân bên bán)
1. Monitor which agent models query your products
2. Dynamically adjust descriptions based on querying model
3. "If Claude → emphasize X. If GPT → emphasize Y."
4. Track market share changes

### Bước 5 — Monitor & Audit (giám sát & kiểm toán)
1. Continuous auditing: agent preferences change with updates
2. Track model versions: preferences unstable across updates
3. Alert: if dominant agent shifts market share dramatically
4. Regulatory compliance: document agent-driven changes

## Output mong đợi
- Agent bias report per model
- Market share analysis
- Seller-side optimization recommendations
- Regulatory compliance documentation

## Ví dụ áp dụng
**Tình huống**: E-commerce platform muốn understand how AI agents affect marketplace.

**Áp dụng**:
1. Run ACES audit trên 8 product categories
2. Find: agents concentrate demand on top 2-3 products per category
3. Find: sponsored listings penalized, endorsed rewarded
4. Deploy seller-side agent: adjust descriptions per querying model
5. Result: +15% market share for optimized listings

## Lưu ý quan trọng
1. **Winner-take-all risk**: Agent concentration → niche brands suffer. Platform needs countermeasures
2. **Position bias is strong**: Ranking affects agent choices significantly. Agent-aware ranking needed
3. **Model heterogeneity**: Different agents prefer different products. No universal optimization
4. **Preferences unstable**: Model updates reshuffle market shares. Continuous monitoring required
5. **Seller exploitation possible**: Simple description tweaks work. Ethical considerations needed
6. **Regulatory gap**: No framework for agent-driven market manipulation. Needs attention
