# Skill: DeFi Agent Maturity Framework
Source: 2605.29174v1
Type: evaluation-method

## When to use this skill
- When evaluating AI agent investment projects in DeFi/crypto
- When designing AI agent systems for financial applications
- When auditing existing DeFi agent deployments

## When NOT to use
- Not related to DeFi/crypto/financial agents
- Only need technical evaluation, no financial analysis
- Project has no token or on-chain activity

## Required inputs
- Agent project documentation
- On-chain data: treasury addresses, token holders, trading activity
- Token metrics: market cap, AUM, trading volume
- Team information: developer interviews, code repositories
- Comparable projects: established DeFi protocols benchmarks

## Steps

### Step 1 — Verify Autonomous Execution
1. Check: does agent have on-chain trade execution evidence?
2. Distinguish: autonomous trading vs basic API integration
3. Interview developers: is visible deployment truly autonomous?
4. Red flags:
   - No on-chain evidence of autonomous trades
   - "AI agent" is just a wrapper for existing API
   - Developer does not disclose execution methodology
5. Score: 0 (basic API) → 1 (partial autonomous) → 2 (fully autonomous)

### Step 2 — Assess Risk-Adjusted Profitability
1. Compute treasury returns: gains vs losses over time
2. Calculate Sharpe ratio, max drawdown
3. Compare with established DeFi protocols benchmarks
4. Check: do returns justify risk?
5. Red flags:
   - Median returns negative on platform
   - Returns peaked then declined to net losses
   - No risk management framework
6. Score: 0 (negative returns) → 1 (positive but low) → 2 (risk-adjusted positive)

### Step 3 — Evaluate Stakeholder Alignment
1. Analyze token holder distribution: who captures gains?
2. Compute Gini coefficient or top 1% capture rate
3. Compare agent treasury gains vs token holder gains
4. Check: is market-cap-to-AUM ratio disconnected?
5. Red flags:
   - Top 1% captures >80% of gains
   - Treasury gains while holders lose
   - Market-cap-to-AUM >1,000x
6. Score: 0 (extreme inequality) → 1 (moderate) → 2 (aligned)

### Step 4 — Compute Maturity Score
1. Total score = autonomous + profitability + alignment (range 0-6)
2. Classification:
   - 0-2: Early stage — high risk, likely speculation
   - 3-4: Developing — partial evidence, moderate risk
   - 5-6: Mature — strong evidence across dimensions
3. Investment recommendation:
   - 0-2: AVOID
   - 3-4: CAUTION — small position only
   - 5-6: CONSIDER — due diligence required

### Step 5 — Monitor and Reassess
1. Track on-chain activity monthly
2. Update maturity score quarterly
3. Alert if: returns decline, distribution worsens, execution becomes manual
4. Compare with evolving benchmarks

## Expected output
- Maturity score (0-6) with breakdown by 3 dimensions
- Investment recommendation: AVOID/CAUTION/CONSIDER
- Red flags list
- Comparable benchmark analysis

## Example application
**Scenario**: Want to evaluate AI trading agent project "TradeBot AI" on Solana. Token: $50M market cap. Claim: "AI-powered autonomous trading."

**Application**:
1. Verify autonomous: check on-chain → trades seen but pattern looks manual (not autonomous) → Score 0
2. Profitability: treasury +$2M, but token holders -$15M. Median returns -40% → Score 0
3. Alignment: top 1% wallets = 90% gains. Market-cap/AUM = 5,000x → Score 0
4. Maturity: 0/6 = AVOID
5. Conclusion: "TradeBot AI" is likely basic API wrapper with speculative token. Avoid.

## Gotchas
1. **"AI agent" may be marketing label**: Many projects just wrap existing API with "AI" label. Must verify autonomous execution via on-chain evidence
2. **Paper gains ≠ real gains**: Treasury may show paper gains while holders lose. Check actual holder P&L
3. **Early market = extreme inequality**: Top 1% captures 81% of gains is typical for permissionless markets. Don't expect fair distribution
4. **Market-cap/AUM ratio is key metric**: >10,000x = pure speculation. Compare with established DeFi (<1x)
5. **Solana-specific**: Analysis is Solana only. Ethereum, Base, others may have different dynamics
6. **Developer incentives**: Developers may benefit from token launches regardless of agent performance. Check alignment
