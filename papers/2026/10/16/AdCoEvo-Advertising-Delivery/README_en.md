# [2610.19454v1] AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System

## Problem
Digital advertising is a complex system with many interacting factors. Current advertising systems often use static models or rigid rules, unable to co-evolve with market changes and user behavior.

## Contribution
- Introduce AdCoEvo: a co-evolving multi-agent advertising delivery system that can self-adapt over time.
- AdCoEvo increases advertiser value (ADV) by 14.02% while reducing cost per acquisition (CPA) by 7.07% (vs Rule, Sparse environment).
- Compared with a multi-agent system with fixed parameters, AdCoEvo increases ADV by 3.96% and reduces CPA by 1.24%.
- Adding Inspector increases ADV by 4.95% and reduces CPA by 9.57% relative to Planner–Optimizer.
- Average API cost: CNY 0.235 per period, 65.59% lower than Gemini-3.1-Flash-Lite.
- Even when budget reduced to 60%, AdCoEvo increases ADV by 7.17% and reduces CPA by 0.78% relative to AdCoEvo (Fixed).

## Method (core summary)
AdCoEvo is a multi-agent system for advertising delivery, with agents responsible for different roles (planner, optimizer, inspector, etc.) and co-evolving over time. The system uses reinforcement learning to optimize parameters and advertising strategies.

## Key Findings
- AdCoEvo: ADV +14.02%, CPA -7.07% (vs Rule, Sparse).
- AdCoEvo (Fixed): ADV +3.96%, CPA -1.24% (vs multi-agent fixed parameters).
- General environment: ADV +4.22%, CPA -2.21%.
- Adding Inspector: ADV +4.95%, CPA -9.57% (vs Planner–Optimizer).
- Average API cost: CNY 0.235 per period, 65.59% lower than Gemini-3.1-Flash-Lite.
- Budget 60%: ADV +7.17%, CPA -0.78% (vs AdCoEvo Fixed).

## Actionable Insights
- Use co-evolving multi-agent system for advertising delivery instead of static rules. Apply: solopreneur running advertising system should use co-evolving agents to self-adapt to market, not use rigid rules.
- Adding Inspector agent helps increase ADV and reduce CPA significantly. Apply: when building advertising system with agents, add an Inspector agent to monitor and adjust decisions of other agents.
- Use small model (API cost CNY 0.235, 65.59% lower than Gemini-3.1-Flash-Lite) to reduce operational cost. Apply: when building advertising system, use small model instead of large expensive model.

## Assumptions & Limitations
- Requires advertising delivery system and real market data; doesn't apply without real data.
- Paper admits: evaluated on Sparse and General environments; may differ on other environments.
- Limitation paper doesn't mention: not evaluated on many domains beyond advertising, not tested on real cost of maintaining co-evolving system.

## Metadata
- Year: 2026
- Authors: Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu (CAS, UCAS, USyd, JD.COM)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.19454
