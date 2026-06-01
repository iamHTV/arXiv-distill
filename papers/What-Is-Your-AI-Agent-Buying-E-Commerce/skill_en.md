# Skill: Agentic E-Commerce Audit
Source: 2508.02630
Type: evaluation-method

## When to use this skill
- When auditing AI agent behavior in e-commerce
- When evaluating biases of AI buying agents
- When designing seller-side agent optimization

## When NOT to use
- No access to AI agents
- Non-product contexts
- Static markets with no agent activity

## Required inputs
- Product catalog with multiple listings
- AI agent access (Claude, GPT, Gemini)
- ACES framework or similar audit tool
- Randomized trial capability

## Steps

### Step 1 — Test Rationality
1. Price sensitivity: test with different price points
2. Rating sensitivity: test with +0.1 rating bumps
3. Review sensitivity: test with different review counts
4. Expected: newer models more rational

### Step 2 — Test Biases
1. Position bias: randomize product positions
2. Sponsored tags: test sponsored vs organic
3. Platform endorsements: test endorsed vs non-endorsed
4. Expected: strong position biases, penalize sponsored, reward endorsed

### Step 3 — Test Choice Homogeneity
1. Run same query across multiple products
2. Check: do agents concentrate on few "modal" products?
3. Compare across models: different models prefer different products
4. Expected: winner-take-all dynamic

### Step 4 — Deploy Seller-Side Agent
1. Monitor which agent models query your products
2. Dynamically adjust descriptions based on querying model
3. "If Claude → emphasize X. If GPT → emphasize Y."
4. Track market share changes

### Step 5 — Monitor & Audit
1. Continuous auditing: agent preferences change with updates
2. Track model versions: preferences unstable across updates
3. Alert: if dominant agent shifts market share dramatically
4. Regulatory compliance: document agent-driven changes

## Expected output
- Agent bias report per model
- Market share analysis
- Seller-side optimization recommendations
- Regulatory compliance documentation

## Example application
**Scenario**: E-commerce platform wants to understand how AI agents affect marketplace.

**Application**:
1. Run ACES audit on 8 product categories
2. Find: agents concentrate demand on top 2-3 products per category
3. Find: sponsored listings penalized, endorsed rewarded
4. Deploy seller-side agent: adjust descriptions per querying model
5. Result: +15% market share for optimized listings

## Gotchas
1. **Winner-take-all risk**: Agent concentration → niche brands suffer. Platform needs countermeasures
2. **Position bias is strong**: Ranking affects agent choices significantly. Agent-aware ranking needed
3. **Model heterogeneity**: Different agents prefer different products. No universal optimization
4. **Preferences unstable**: Model updates reshuffle market shares. Continuous monitoring required
5. **Seller exploitation possible**: Simple description tweaks work. Ethical considerations needed
6. **Regulatory gap**: No framework for agent-driven market manipulation. Needs attention
