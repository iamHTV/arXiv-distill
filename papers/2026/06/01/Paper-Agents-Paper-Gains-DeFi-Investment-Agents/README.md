# [2605.29174v1] Paper Agents, Paper Gains: Phân tích Thực nghiệm DeFi Investment Agents (Tác nhân Đầu tư DeFi)

## Vấn đề
DeFi investment agents (tác nhân đầu tư DeFi) — systems dùng AI cho autonomous on-chain trading (giao dịch tự động trên blockchain) — đã đạt hơn USD 3 billion trong combined token valuations (định giá token kết hợp) từ cuối 2024. Tuy nhiên, chưa có empirical analysis (phân tích thực nghiệm) nào đánh giá: (1) bao nhiêu projects thực sự autonomous (tự động) vs chỉ là API integrations (tích hợp API) cơ bản; (2) ai thực sự benefit từ agents — developers hay token holders; (3) token valuations có connected (liên kết) với fundamentals (cơ bản) không.

## Đóng góp
1. **Survey 1,900 AI-tagged crypto projects**: Filter (lọc) xuống 10 representative projects, deep-dive architectural analysis (phân tích kiến trúc sâu) của ElizaOS và Virtuals Protocol
2. **On-chain performance analysis**: 11 Solana-based agent treasuries, 925,323 token holders. Tìm thấy: agent treasuries retain $30M+ paper gains (lợi nhuận trên giấy) trong khi token holders collectively lost (mất tổng cộng) $191.7M
3. **Maturity framework (khung trưởng thành)**: 3 dimensions — autonomous execution (thực thi tự động), risk-adjusted profitability (lợi nhuận điều chỉnh rủi ro), stakeholder alignment (căn chỉnh bên liên quan)

## Phương pháp (tóm tắt cốt lõi)
Survey 1,900 AI-tagged crypto projects → filter investment-focused agents → curate 10 representative projects. Deep-dive: ElizaOS và Virtuals Protocol architectures. Quantitative on-chain analysis: 11 Solana agent treasuries, 925,323 token holders, track trading activity, gains/losses, token performance. Propose maturity framework: autonomous execution (có thực sự autonomous không?), risk-adjusted profitability (lợi nhuận có justify risk không?), stakeholder alignment (ai benefit?).

## Kết quả chính
- Top 1% wallets capture 81.4% of ALL gains ($1.81B) — extreme wealth concentration
- Agent treasuries retain $30M+ paper gains, token holders collectively lost $191.7M
- Market-cap-to-AUM ratios: >10,000x cho agent tokens vs <1x cho established DeFi protocols
- User gains peaked at $2.4B → declined to net losses, median returns NEGATIVE on every platform
- Tokens declined 93% average from all-time highs
- Many projects không provide clear evidence of autonomous trade execution — basic API integrations
- Developer interviews: many visible deployments remain basic API integrations

## Insight có thể áp dụng ngay
1. **Đánh giá AI agent projects bằng maturity framework**: Khi evaluate AI agent investment, check 3 dimensions: (a) có autonomous execution thật không — hay chỉ API wrapper? (b) risk-adjusted profitability — returns justify risk? (c) stakeholder alignment — ai benefit? Ví dụ: trước khi invest vào AI trading agent, yêu cầu proof of autonomous execution (on-chain evidence), risk-adjusted returns (Sharpe ratio), và transparent stakeholder alignment.

2. **Token valuation ≠ fundamentals**: Market-cap-to-AUM >10,000x = pure speculation. Khi evaluate DeFi agent tokens, compare market cap với actual AUM và revenue. Ví dụ: nếu agent token có $100M market cap nhưng chỉ $10K AUM → valuation disconnected, avoid.

3. **Top 1% captures 81.4% gains — early market dynamics**: Permissionless markets enable rapid experimentation nhưng cũng allow wealth concentration. Khi participate, aware rằng early movers/insiders capture majority gains. Ví dụ: nếu tham gia AI agent crypto market, expect extreme inequality — don't assume fair distribution.

## Giả định & Hạn chế
**Điều kiện để analysis work:**
- On-chain data phải publicly attributable (có thể quy cho công khai)
- Solana-based projects — ecosystem-specific
- Survey methodology: AI-tagged projects có thể miss (bỏ sót) non-tagged projects

**Hạn chế paper thừa nhận:**
- Sample curated (được tuyển chọn) — không representative of all projects
- Many projects early stage — không đủ data cho long-term analysis
- On-chain analysis limited to publicly attributable activity

**Hạn chế paper KHÔNG nói:**
- Không compare với non-AI DeFi agents — có phải AI-specific problem?
- Solana ecosystem only — Ethereum, Base, khác có thể khác
- Survey methodology opaque — filter criteria không rõ
- Không address regulatory implications
- Không analyze developer incentives — tại sao launch agents?
- 93% token decline có thể do market-wide crypto downturn, không chỉ agent-specific

## Metadata
- Năm: 2026
- Tác giả: Jay Yu, Amy Zhao, Danning Sui
- Category: cs.AI, cs.CR
- Link PDF: https://arxiv.org/pdf/2605.29174v1
- Citation count: [EXTRACTION FAILED]
