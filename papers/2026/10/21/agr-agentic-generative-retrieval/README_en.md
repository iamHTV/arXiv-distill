# 2610.26831 AGR: Agentic Generative Retrieval with Tool-Augmented Search

## Problem
- Generative retrieval (GR) represents items by hierarchical Semantic IDs (SIDs), but large-scale search/recommendation systems live on rich features: user profiles, behavioral histories, freshness cues. Existing methods either append all signals to the input (raising serving cost, adding noise) or inject them by a predetermined scheme — none adaptively decides when a feature is needed, which to select, or where it should influence SID generation.

## Contribution
- AGR: a tool-augmented paradigm that interleaves SID generation with on-demand feature acquisition.
- Conditioned on the request and decoded SID prefix, AGR decides whether to invoke a tool, which feature to acquire, and where the observation influences decoding — steering generation toward feature-consistent SID branches.
- Supervision: tool-augmented trajectories built from feature applicability and information gain along the SID hierarchy.

## Method
- Extend the vocabulary V = S ∪ T ∪ O (SID + tool + observation tokens): each tool token t triggers a function call f_t(q, u, s≤i) whose result is an observation token o_t — unifying SID generation and tool invocation in one autoregressive process.
- Inference: model–tool interaction per beam candidate during decoding.
- Training: SID pretraining followed by tool-augmented fine-tuning.
- Tools: CF (categorical features), GSU (General Search Unit — user behavioral sequences), QU (query text + user features).

## Key Findings
- 4 datasets (1 industrial + 3 public benchmarks): AGR has the best Recall and MRR at every cutoff; relative gains over TIGER: Recall +6.4% to +14.0%, MRR +5.2% to +19.7%.
- vs direct encoding of 400 GSU tokens: Recall@50 0.3237 vs 0.3241 (comparable) but training time 1.969 vs 10.794 sec/step (−81.8%) and serving cost 4.76 vs 8.33 GPUs/1K requests (−42.9%).
- Online A/B test on Kuaishou production search (mean latency 35ms, 7-day A/A then 7-day A/B, 10% traffic per arm): Relevance +0.205% [+0.12%, +0.28%]; Query reformulation rate −0.690% [−1.13%, −0.20%]; Search penetration rate +0.060% [+0.03%, +0.14%].

## Actionable Insights
1. Do not stuff every feature into the prompt/input — let the agent fetch on demand. Example: a product-recommendation agent queries the history tool only when the SID prefix signals a behavioral need, instead of sending the full profile each call — same quality, ~43–82% lower cost.
2. Teach the model "when to call a tool" with information-gain-labeled trajectories, not blind rules. Example: log each feature fetch with its quality delta (ΔPPL) to build supervision data.
3. Run a 7-day A/A test before the A/B test to confirm the traffic split is unbiased. Example: only trust differences whose 95% CI excludes 0.

## Assumptions & Limitations
- Training trajectories use predefined rules, not learned policies → future work: agentic reinforcement learning under sparse rewards.
- The tool ecosystem is currently limited; more tools and retrieval domains are needed.
- Trajectories are built along golden SID prefixes via target-side agreement → exposure bias.
- AGR still costs ~2× the no-feature baseline serving — GPU budget required.

## Metadata
- 2026; authors: Ming Yang (Fudan University), Yaqi Yin, Zhibo Wang, Xiaoze Jiang, Jingwei Zhuo, Chao Zhang, Quanzhi Zhu, Weiguo Zheng, Liang Zeng, Yunfeng Zhao, Jiaqiang Liu, Kefeng Wang, Yupeng Huang, Kaiqiao Zhan, Xuanping Li (Kuaishou Technology); category: cs.IR; PDF: https://arxiv.org/pdf/2610.26831; citation count: [NO DATA — published 2026-10-19]
