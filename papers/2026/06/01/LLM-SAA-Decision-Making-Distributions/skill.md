# Skill: LLM-SAA Decision Simulation
Source: 2602.06357
Type: framework

## Khi nào dùng skill này

- Khi thiếu real consumer data cho pricing, assortment, inventory decisions — startup launching new product, market entry without historical data
- Khi muốn simulate consumer preferences/willingness-to-pay/demand bằng LLM thay vì expensive surveys
- Khi cần quick decision prototyping trước khi invest vào real data collection

- KHÔNG dùng khi: abundant real data available (real data > LLM simulation); products quá niche mà LLM lacks world knowledge; regulated industries requiring validated data

## Input cần có

- Product description (features, category, target market)
- Decision problem type (pricing, assortment, inventory/newsvendor)
- LLM access for simulation
- Optional: few-shot examples of real consumer preferences

## Các bước thực hiện

1. **Define Decision Problem** — Xác định: (a) Decision variable (price, assortment set, inventory level); (b) Objective (maximize revenue, minimize cost); (c) Distribution needed (willingness-to-pay, preference ranking, demand).

2. **Design Simulation Prompts** — 3 strategies: (a) Zero-shot: "Simulate 100 consumers' willingness-to-pay for {product description}. Output as list of prices."; (b) Persona-sampling: "Simulate WTP from a {demographic} consumer for {product}."; (c) Few-shot: include 3-5 real examples of consumer preferences.

3. **Generate Simulated Distribution** — Run LLM N times (N=100-500) với varied personas/temperatures → collect empirical distribution F̂. Parse outputs into numerical values. Validate: check distribution shape is reasonable (not degenerate).

4. **Optimize Decision Under F̂** — Apply standard optimization: (a) Pricing: price* = argmax E_{w~F̂}[revenue(price, w)]; (b) Assortment: select subset maximizing expected revenue under preference distribution; (c) Newsvendor: inventory* = quantile of demand distribution at critical ratio.

5. **Evaluate with Decision Metrics** — KHÔNG dùng Wasserstein distance. Compare: (a) Decision quality from LLM-SAA vs. real data decisions; (b) Regret = (optimal revenue - LLM-SAA revenue) / optimal revenue; (c) Test in low-data (10-50 real samples) vs. high-data (500+ samples) regimes.

## Output mong đợi

- Decision quality competitive with real data in low-data regimes (<50 samples)
- Useful for quick prototyping before investing in surveys
- Persona-sampling improves distribution realism

## Ví dụ áp dụng

Scenario: SaaS startup pricing new feature tier. (1) No historical data; (2) Prompt GPT-4: "Simulate 200 B2B customers' willingness-to-pay for a project management tool with {features}. Include company size, industry."; (3) Parse 200 WTP values → distribution F̂; (4) Optimize: price* = $29/month (maximizes expected revenue under F̂); (5) Validate: run small survey with 20 real customers → compare. If similar → confidence to launch. If divergent → adjust.

## Gotchas

- LLM simulation quality depends on product description specificity — vague descriptions → generic/unrealistic distributions
- Cultural bias: LLM trained on Western data may not simulate non-Western consumer preferences well. Add demographic context to prompts.
- Wasserstein distance is MISLEADING for evaluation — always evaluate by decision quality, not distribution similarity
- Degenerate distributions: LLM may output same value repeatedly → validate distribution shape before optimization
