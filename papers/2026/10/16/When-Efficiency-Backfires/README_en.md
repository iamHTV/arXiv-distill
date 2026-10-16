# [2605.17288v1] When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack

## Problem
Large Language Model (LLM) cascade systems are designed to balance efficiency and performance by processing queries with lightweight models while selectively escalating complex cases to more powerful ones. Such systems seek to reduce computational cost and latency while maintaining task performance, making it an appealing choice for large-scale deployment. However, the cascade design introduces new vulnerabilities.

## Contribution
- Uncover that LLM cascade systems can trigger cascade failure under adversarial attack.
- Attack method can reduce prediction accuracy by up to 84.6%, inflate normalized token cost by 148.9%, and increase execution time by up to 108.9%.
- In jailbreak scenarios, attack success rate increases by up to 81.4%.

## Method (core summary)
Study LLM cascade systems under adversarial attack. Measure prediction accuracy, token cost, execution time, and attack success rate. Test various adversarial attack methods on different cascade systems.

## Key Findings
- Attack method reduces prediction accuracy by up to 84.6%.
- Attack inflates normalized token cost by 148.9%.
- Attack increases execution time by up to 108.9%.
- Attack increases attack success rate by up to 81.4% (in jailbreak scenarios).
- Cascade systems are less robust than single models against adversarial attacks.

## Actionable Insights
- Don't trust cascade LLM systems to be safe against adversarial attacks: cascade design introduces new vulnerabilities. Apply: solopreneur using cascade LLM systems should add defense mechanisms like input sanitization, output validation, and rate limiting.
- Evaluate cascade system robustness before production deployment. Apply: when building cascade LLM systems, test against adversarial attacks to find vulnerabilities and fix them before shipping.

## Assumptions & Limitations
- Requires an LLM cascade system and real query data; doesn't apply if only a single model.
- Paper admits: evaluated on specific cascade systems; may differ on other systems.
- Limitation paper doesn't mention: not evaluated on many domains beyond tasks used, not tested on real cost of defense mechanisms.

## Metadata
- Year: 2026
- Authors: Zehan Sun, Dingfan Chen, Songze Li (Southeast University, Max Planck Institute for Intelligent Systems)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2605.17288
