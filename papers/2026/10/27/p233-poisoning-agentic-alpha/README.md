# 2608.24069 Poisoning Agentic Alpha: Tấn công đối kháng vào hệ thống giao dịch đa tác nhân

## Problem
- Prior work (TradeTrap, AutoRedTrader) giả định adversary có white-box access (truy cập hộp trắng) vào tool server, orchestration state — nhưng deployed trading system là black-box; red-team finance trước đây chỉ đánh single-agent, không phải collaborative pipeline.
- Gap: chưa ai characterize được adversarial signal (tín hiệu đối kháng) ENTER (đi vào) qua role interface (giao diện vai trò) nào và SURVIVE (sống sót) bao xa qua communication topology (kiến trúc liên lạc) tới final decision trong multi-agent trading system (hệ thống giao dịch đa tác nhân).

## Contribution
- Threat model dân chủ hóa (democratized): adversary chỉ sửa source data (dữ liệu nguồn) và prompt agents consume — không cần instrument nội bộ.
- 2 trục phân tích: role axis (Analyst, Researcher, Trader, Risk Manager — mỗi vai trò paired với attack tương ứng interface) + structural axis (4 topology: linear, centralized, decentralized, hybrid).
- APS (Adversarial Signal Preservation Score — điểm bảo toàn tín hiệu đối kháng): closed-form lens APS = 1/(1+k(1−p)), k = số aggregation stage (giai đoạn tổng hợp), p=1 nếu voting.

## Method (tóm tắt cốt lõi)
- Pipeline theo TradingAgents: Analyst team (social/news/fundamental/market), Research team (bull/bear debate), Trader, Risk Manager → decision ŷ ∈ {Buy, Sell, Hold}.
- 5 attacks: data poisoning (Analyst social — LLM viết lại article đảo sentiment), indirect prompt injection (Analyst news — directive ẩn trong post), persuasive adversary (Researcher — FOMO/appeal-to-authority), objective hijacking (Trader — prompt đảo mục tiêu), jailbreaking (Risk Manager — hypothetical framing bypass guardrail).
- Backtest 2026 Q1 (Jan 1–Mar 31), 5 tài sản BTC-USD/MSFT/NVDA/TSLA/AAPL, 61 ngày NYSE → 305 asset-day/cấu hình; dữ liệu Alpha Vantage, yfinance, Reddit; post-cutoff tránh lookahead bias (thiên kiến nhìn trước); backbone GPT-4.1 + Qwen3-235B-A22B (deep-think), GPT-4.1-mini + Qwen3-30B-A3B (quick-think), temperature 0; attack ratio mặc định 1:9 (10%).
- ASR (Attack Success Rate — tỷ lệ thành công tấn công) = số ngày decision flipped to target / số attackable day; cả BUY-targeted và SELL-targeted; thêm signed EV (expected value — giá trị kỳ vọng) $/attempt trên portfolio $100K long-only.

## Key Findings
- Jailbreaking Risk Manager: ASR 98,9% (BUY) / 95,5% (SELL) — cao gấp 1,9× attack mạnh thứ hai; 4 attack còn lại chỉ 13,8–53,3%. Vì Risk Manager đồng thời là terminal decision node → compromise nó bypass hết aggregation/debate/validation phía trước.
- Persuasive adversary (Researcher): 41,9% (SELL) / 53,3% (BUY), cao hơn mọi data-level attack (p<0,005); jailbreaking cao hơn tất cả (p<0,001). Macro-average: persuasive 50,6%, indirect injection 34,9%, data poisoning 26,2%, objective hijacking 25,4%.
- Đa agent giảm ASR vs single agent: GPT-4.1 29,1–48,1% vs 70,2%; Qwen 60,1–82,2% vs 87,9% — nhưng không architecture nào robust bản chất (central finding).
- APS ordering (Dec 0,00 < Hyb 0,33 < Lin 0,50 < Cen 1,00) khớp ASR: correlation r=0,85 (GPT), r=0,88 (Qwen); GPT SELL-targeted Market attack 0,3% (Dec) → 55,7% (Cen).
- Quorum effect (hiệu ứng số đông): 44,6% attackable day đã có ≥1 benign analyst vote BUY → 1 compromised channel lập majority 2/3; decentralized ASR 44,2% (News) / 51,2% (Social) khi 1 channel bị compromise, lên 68,7% khi 2 channel. Majority vote chỉ robust khi compromised agent ở thiểu số.
- ASR không đồng nghĩa financial harm (thiệt hại tài chính): jailbreak 97,2% ASR nhưng median $0/success, EV −$43/attempt; objective hijacking EV +$40 nhưng median −$85; persuasive EV −$60 (tệ nhất). Poison ratio 10%→80%: ASR 19,1%→28,4%→30,6% (front-loaded +9,3 rồi +2,2), vẫn thấp hơn jailbreak 68 điểm.
- Cumulative return (GPT BUY-targeted): Dec clean tốt nhất (−2,68%) nhưng degrade lớn nhất D1 −12,01 pp / D2 −12,38 pp; Cen ổn định hơn (thấp nhất −1,45 pp) — clean performance tốt không kéo robustness.

## Actionable Insights
1. Terminal decision node là single point of failure (điểm lỗi đơn): jailbreak risk manager 98,9% ASR bỏ qua toàn bộ validation上游. Ví dụ: agent chăm sóc khách vừa soạn vừa tự gửi → tách thành proposer + independent checker có constraint hard (giá tối đa, tone), checker KHÔNG nhận prompt từ proposer.
2. Multi-agent không phải defense: vote majority chỉ an toàn khi attacker thiểu số (1/3 → 44–51% ASR, 2/3 → 68,7%). Ví dụ: 3 agent duyệt content đăng blog — dùng 3 agent nguồn độc lập + yêu cầu unanimous (nhất trí), hoặc threshold 3/3 cho action không đảo ngược; 2 agent cùng family model = correlated failure.
3. Đo hậu quả $, không chỉ tỷ lệ bị lừa: attack 97% ASR median $0 trong khi attack ASR thấp median −$85. Ví dụ: before deploying agent tự động đặt hàng/đăng tin, chạy simulate 1 flip decision = bao nhiêu $, xếp rủi ro theo EV không phải ASR.

## Assumptions & Limitations
- Điều kiện: adversary chỉ chạm data nguồn + prompt (black-box); attackable day loại trừ ngày clean decision đã là target; daily-close backtest.
- Paper thừa nhận: role evaluation 1 backbone (cost); 5 large-cap asset dense coverage ≠ thin-coverage security; bỏ execution timing, transaction cost (chi phí giao dịch), slippage, position management; absolute loss estimate chỉ so sánh dưới common protocol.
- Mày thấy thêm: Qwen denominator nhỏ (N=45–106) → ASR nhiễu; attack giả định adversary rewrite được news/Reddit content (hợp lý với system phụ thuộc news mining); daily decision, chưa cover intra-day.

## Metadata
- Năm: 2026 (25 Aug 2026), tác giả: CheolWon Na, Hao Ni, Lukasz Szpruch, Zhangyang Wang, Dhagash Mehta (BlackRock), Alejandro Lopez-Lira, Chanyeol Choi (LinqAlpha), Jee-Hyong Lee, Saurabh Nagrecha (Google), Yongjae Lee (UNIST/LinqAlpha), category: cs.AI, code: github.com/cwna97/multi_agent_trading_attack, link PDF: https://arxiv.org/pdf/2608.24069v1, citation count: không có dữ liệu (Semantic Scholar rate-limited)
