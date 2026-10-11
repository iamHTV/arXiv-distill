# Skill: LLM-SAA Decision Simulation
Source: 2602.06357
Type: framework

## When to use this skill

- When lacking real consumer data for pricing, assortment, inventory decisions
- When wanting to simulate preferences/WTP/demand via LLM instead of expensive surveys
- When needing quick decision prototyping before investing in real data collection

- Do NOT use when: abundant real data available; products too niche for LLM knowledge; regulated industries

## Input needed

- Product description
- Decision problem type (pricing, assortment, inventory)
- LLM access
- Optional: few-shot real preference examples

## Steps

1. **Define Decision Problem** — Decision variable, objective, distribution needed.
2. **Design Simulation Prompts** — Zero-shot, persona-sampling, or few-shot strategies.
3. **Generate Distribution** — Run LLM 100-500 times, collect empirical distribution.
4. **Optimize Decision** — Standard optimization under simulated distribution.
5. **Evaluate with Decision Metrics** — Not Wasserstein distance. Compare decision quality, regret.

## Expected output

- Competitive decision quality in low-data regimes
- Useful for quick prototyping
- Persona-sampling improves realism

## Example application

SaaS startup pricing: simulate 200 B2B customers' WTP → optimize price at $29/month → validate with 20-person survey.

## Gotchas

- Description specificity matters
- Cultural bias in LLM simulation
- Wasserstein distance misleading — use decision quality
- Validate distribution shape before optimization
