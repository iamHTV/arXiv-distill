# Skill: DeFi Agent Maturity Framework (Khung Trưởng thành Tác nhân DeFi)
Nguồn: 2605.29174v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi evaluate (đánh giá) AI agent investment projects trong DeFi/crypto
- Khi design (thiết kế) AI agent system cho financial applications (ứng dụng tài chính)
- Khi audit (kiểm toán) existing DeFi agent deployments (triển khai)

## KHÔNG nên dùng khi
- Không liên quan đến DeFi/crypto/financial agents
- Chỉ cần technical evaluation, không cần financial analysis
- Project chưa có token hoặc on-chain activity

## Input cần có
- Agent project documentation (tài liệu dự án)
- On-chain data: treasury addresses, token holders, trading activity
- Token metrics: market cap, AUM, trading volume
- Team information: developer interviews, code repositories
- Comparable projects: established DeFi protocols benchmarks

## Các bước thực hiện

### Bước 1 — Verify Autonomous Execution (xác minh thực thi tự động)
1. Check: agent có on-chain trade execution evidence không?
2. Distinguish: autonomous trading vs basic API integration
3. Interview developers: visible deployment có thực sự autonomous?
4. Red flags (cờ đỏ):
   - No on-chain evidence of autonomous trades
   - "AI agent" chỉ là wrapper cho existing API
   - Developer không disclose (công bố) execution methodology
5. Score: 0 (basic API) → 1 (partial autonomous) → 2 (fully autonomous)

### Bước 2 — Assess Risk-Adjusted Profitability (đánh giá lợi nhuận điều chỉnh rủi ro)
1. Compute treasury returns: gains vs losses over time
2. Calculate Sharpe ratio, max drawdown (rút lui tối đa)
3. Compare với established DeFi protocols benchmarks
4. Check: returns có justify (biện minh) risk không?
5. Red flags:
   - Median returns negative on platform
   - Returns peaked then declined to net losses
   - No risk management framework
6. Score: 0 (negative returns) → 1 (positive but low) → 2 (risk-adjusted positive)

### Bước 3 — Evaluate Stakeholder Alignment (đánh giá căn chỉnh bên liên quan)
1. Analyze token holder distribution: ai capture gains?
2. Compute Gini coefficient hoặc top 1% capture rate
3. Compare agent treasury gains vs token holder gains
4. Check: market-cap-to-AUM ratio — có disconnected?
5. Red flags:
   - Top 1% captures >80% of gains
   - Treasury gains while holders lose
   - Market-cap-to-AUM >1,000x
6. Score: 0 (extreme inequality) → 1 (moderate) → 2 (aligned)

### Bước 4 — Compute Maturity Score (tính điểm trưởng thành)
1. Total score = autonomous + profitability + alignment (range 0-6)
2. Classification:
   - 0-2: Early stage (giai đoạn đầu) — high risk, likely speculation
   - 3-4: Developing (đang phát triển) — partial evidence, moderate risk
   - 5-6: Mature (trưởng thành) — strong evidence across dimensions
3. Investment recommendation:
   - 0-2: AVOID (tránh)
   - 3-4: CAUTION (thận trọng) — small position only
   - 5-6: CONSIDER (cân nhắc) — due diligence required

### Bước 5 — Monitor và Reassess (giám sát và đánh giá lại)
1. Track on-chain activity monthly
2. Update maturity score quarterly
3. Alert (cảnh báo) if: returns decline, distribution worsens, execution becomes manual
4. Compare với evolving benchmarks

## Output mong đợi
- Maturity score (0-6) với breakdown theo 3 dimensions
- Investment recommendation: AVOID/CAUTION/CONSIDER
- Red flags list
- Comparable benchmark analysis

## Ví dụ áp dụng
**Tình huống**: Muốn evaluate AI trading agent project "TradeBot AI" trên Solana. Token: $50M market cap. Claim: "AI-powered autonomous trading."

**Áp dụng**:
1. Verify autonomous: check on-chain → thấy trades nhưng pattern giống manual (không autonomous) → Score 0
2. Profitability: treasury +$2M, nhưng token holders -$15M. Median returns -40% → Score 0
3. Alignment: top 1% wallets = 90% gains. Market-cap/AUM = 5,000x → Score 0
4. Maturity: 0/6 = AVOID
5. Conclusion: "TradeBot AI" là likely basic API wrapper với speculative token. Avoid.

## Lưu ý quan trọng
1. **"AI agent" có thể là marketing label**: Nhiều projects chỉ wrap existing API với "AI" label. Phải verify autonomous execution bằng on-chain evidence
2. **Paper gains ≠ real gains**: Treasury có thể show paper gains trong khi holders lose. Check actual holder P&L
3. **Early market = extreme inequality**: Top 1% captures 81% gains là typical cho permissionless markets. Don't expect fair distribution
4. **Market-cap/AUM ratio là key metric**: >10,000x = pure speculation. Compare với established DeFi (<1x)
5. **Solana-specific**: Analysis chỉ trên Solana. Ethereum, Base, khác có thể different dynamics
6. **Developer incentives**: Developers có thể benefit từ token launches regardless of agent performance. Check alignment
