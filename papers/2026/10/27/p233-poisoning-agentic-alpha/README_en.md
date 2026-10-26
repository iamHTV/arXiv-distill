# 2608.24069 Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems

## Problem
- Prior work (TradeTrap, AutoRedTrader) presumes white-box access to tool servers and orchestration state, but deployed trading systems are black-box; prior finance red-teaming evaluated single agents, not collaborative pipelines.
- Gap: no one had characterized how an adversarial signal ENTERS through a role interface and how far it SURVIVES across a communication topology to the final decision in a multi-agent trading system.

## Contribution
- Democratized threat model: the adversary modifies only the source data and the prompts agents consume — no internal instrumentation needed.
- Two analysis axes: role axis (Analyst, Researcher, Trader, Risk Manager, each paired with an attack matched to its interface) and structural axis (4 topologies: linear, centralized, decentralized, hybrid).
- APS (Adversarial Signal Preservation Score): a closed-form lens APS = 1/(1+k(1-p)), k = number of aggregation stages, p = 1 if voting.

## Method (core summary)
- Pipeline follows TradingAgents: Analyst team (social/news/fundamental/market), Research team (bull/bear debate), Trader, Risk Manager -> decision in {Buy, Sell, Hold}.
- Five attacks: data poisoning (social Analyst — an LLM rewrites articles inverting sentiment), indirect prompt injection (news Analyst — directives hidden inside legitimate posts), persuasive adversary (Researcher — FOMO / appeal to authority), objective hijacking (Trader — prompt inverting the objective), jailbreaking (Risk Manager — hypothetical framing bypassing guardrails).
- Backtest over 2026 Q1 (Jan 1–Mar 31), 5 assets (BTC-USD, MSFT, NVDA, TSLA, AAPL), 61 NYSE days -> 305 asset-days per configuration; data from Alpha Vantage, yfinance, Reddit; post-cutoff data to avoid lookahead bias; backbones GPT-4.1 and Qwen3-235B-A22B (deep-think) with GPT-4.1-mini and Qwen3-30B-A3B (quick-think), temperature 0; default attack ratio 1:9 (10%).
- ASR (Attack Success Rate) = days the decision flips to the adversary's target / attackable days, reported for both BUY-targeted and SELL-targeted attacks; plus signed EV (expected value) in $ per attempt on a $100K long-only portfolio.

## Key Findings
- Jailbreaking the Risk Manager: ASR 98.9% (BUY) / 95.5% (SELL) — 1.9x the next most effective attack; the other four attacks sit at 13.8–53.3%. The Risk Manager is also the terminal decision node, so compromising it bypasses all upstream aggregation, debate, and validation.
- Persuasive adversary (Researcher): 41.9% (SELL) / 53.3% (BUY), significantly above all data-level attacks (p<0.005); jailbreaking above everything else (p<0.001). Macro-averages: persuasive 50.6%, indirect injection 34.9%, data poisoning 26.2%, objective hijacking 25.4%.
- Multi-agent reduces ASR vs single agent: GPT-4.1 29.1–48.1% vs 70.2%; Qwen 60.1–82.2% vs 87.9% — but no architecture is inherently robust (central finding).
- APS ordering (Dec 0.00 < Hyb 0.33 < Lin 0.50 < Cen 1.00) tracks ASR: correlation r=0.85 (GPT), r=0.88 (Qwen); GPT SELL-targeted Market attack 0.3% (Dec) -> 55.7% (Cen).
- Quorum effect: on 44.6% of attackable days at least one benign analyst already votes BUY, so one compromised channel completes a 2/3 majority; decentralized ASR 44.2% (News) / 51.2% (Social) with 1 compromised channel, rising to 68.7% with 2. Majority voting is robust only while compromised agents remain a minority.
- ASR does not track financial harm: jailbreaking flips 97.2% of decisions yet medians $0 per success (EV -$43/attempt); objective hijacking EV +$40 but median -$85; persuasive EV -$60 (worst). Poison ratio 10%->80%: ASR 19.1%->28.4%->30.6% (front-loaded, +9.3 then +2.2), still 68 points below jailbreaking.
- Cumulative returns (GPT, BUY-targeted): Dec has the best clean return (-2.68%) but the largest degradation (D1 -12.01 pp, D2 -12.38 pp); Cen is more stable (worst only -1.45 pp) — clean performance does not imply attack robustness.

## Actionable Insights
1. The terminal decision node is a single point of failure: jailbroken risk manager (98.9% ASR) bypasses all upstream validation. Example: if your support agent both drafts and auto-sends, split into a proposer plus an independent checker with hard constraints (price caps, tone rules) whose prompt never comes from the proposer.
2. Multi-agent is not a defense: majority voting is only safe while attackers are a minority (1/3 -> 44–51% ASR, 2/3 -> 68.7%). Example: for 3 agents approving blog content, require unanimity for irreversible actions and source the agents independently; two agents from the same model family are correlated failures.
3. Measure dollar consequences, not just flip rates: a 97% ASR attack medians $0 impact while a lower-ASR attack medians -$85. Example: before deploying an auto-ordering agent, simulate the $ impact of one flipped decision and rank risks by EV, not ASR.

## Assumptions & Limitations
- Conditions: adversary touches only source data and prompts (black-box); attackable days exclude days where the clean decision already equals the target; daily-close backtest.
- Acknowledged: role evaluation uses a single backbone (cost); five large-cap assets with dense coverage do not represent thin-coverage securities; execution timing, transaction costs, slippage, and position management omitted; absolute loss estimates valid only for comparison under a common protocol.
- Not stated but visible: Qwen attackable denominators are small (N=45–106), so its ASR values are noisy; the attacks assume the adversary can rewrite news/Reddit content (plausible for news-mining systems); daily decisions only, intra-day not covered.

## Metadata
- Year: 2026 (25 Aug 2026), authors: CheolWon Na, Hao Ni, Lukasz Szpruch, Zhangyang Wang, Dhagash Mehta (BlackRock), Alejandro Lopez-Lira, Chanyeol Choi (LinqAlpha), Jee-Hyong Lee, Saurabh Nagrecha (Google), Yongjae Lee (UNIST/LinqAlpha), category: cs.AI, code: github.com/cwna97/multi_agent_trading_attack, PDF: https://arxiv.org/pdf/2608.24069v1, citation count: no data (Semantic Scholar rate-limited)
