# [2608.24034v1] TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising

## Problem
- Live-streaming advertising is an important monetization channel on short-video and e-commerce platforms. Existing generative recommenders are designed for stationary item domains and adapt inadequately at three levels: static semantic IDs (SID) cannot represent evolving live-ad targets, single-scale user behavior modeling cannot capture rapidly changing user intent, and preference optimization struggles to balance fresh on-policy feedback with training stability.

## Contribution
- TAGR (Temporally Adaptive Generative Recommendation) — a generative recommendation framework that performs temporal adaptation at three levels: live-ad tokenization, user intent modeling, and preference alignment.
- LSID (Live Semantic-Collaborative ID) — periodically updates each active live ad's SID assignment according to its current live scene and promoted products, while retaining a stable hierarchical token vocabulary for autoregressive generation.
- IAG (Intent-Aware Generation) — models live-room entry histories at multiple temporal granularities as the primary intent sequence, preserves auxiliary behavior sequences as separate input channels, and weights next-token prediction (NTP) using post-request intent evidence and business value.
- IOPO (Intermittent On-Policy Preference Optimization) — periodically samples fresh candidate groups from the current policy and performs behavior- and value-aligned preference updates interleaved with supervised NTP maintenance to preserve the learned behavior distribution.

## Method (core summary)
- For each user request at time t, the system observes user context C_u(t) including user profile, historical behaviors, and emerged targets.
- LSID: periodically updates each active live ad's SID assignment according to current live scene and promoted products, while retaining stable hierarchical token vocabulary for autoregressive generation.
- IAG: models live-room entry histories at multiple temporal granularities as primary intent sequence, preserves auxiliary behavior sequences as separate input channels, weights next-token prediction (NTP) using post-request intent evidence and business value.
- IOPO: periodically samples fresh candidate groups from current policy and performs behavior- and value-aligned preference updates interleaved with supervised NTP maintenance to preserve learned behavior distribution.

## Key Findings
- 10 authors from Kuaishou Technology and Tsinghua University, arXiv category: cs.IR.
- Deployed on a large-scale e-commerce live-stream advertising platform.
- TAGR improves live-room entry by 8.5% and shopping-cart click rates by 7.4%.
- Achieves 16.1% revenue lift in e-commerce live-stream advertising over production baseline.

## Actionable Insights
1. Temporal adaptation at three levels (live-ad tokenization, user intent modeling, and preference alignment) significantly improves live-streaming advertising recommendation. Application: when building a live-streaming advertising recommendation system, periodically update SID assignments based on current live scene and promoted products.
2. Intent-Aware Generation models live-room entry histories at multiple temporal granularities as primary intent sequence, preserves auxiliary behavior sequences as separate input channels, and weights next-token prediction using post-request intent evidence and business value. Application: when building a live-streaming recommendation system, model user intent at multiple temporal granularities and use post-request intent evidence to weight next-token prediction.

## Assumptions & Limitations
- Evaluated on a real-world e-commerce live-stream advertising platform.
- Only evaluated on a single platform (Kuaishou).
- No detailed information about training time and computational cost.

## Metadata
- Year: 2026, authors: Wencai Ye, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang (Kuaishou Technology, Tsinghua University), arXiv category: cs.IR, PDF link: https://arxiv.org/pdf/2608.24034v1
