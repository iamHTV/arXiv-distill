# [2505.00951] Preserving Privacy and Utility in LLM-Based Product Recommendations

## Problem
LLM-based recommendation systems process textual/contextual information, often using cloud-based infrastructure. User data transmitted to remote servers → privacy concerns. Unlike traditional systems with structured data, LLM models process more personal information. Privacy risk: exposure and loss of control over personal data.

## Contribution
1. **Hybrid privacy-preserving framework**: Separates sensitive from nonsensitive data. Only shares nonsensitive with cloud for LLM recommendations.
2. **De-obfuscation module**: Reconstructs sensitive recommendations locally — does not transmit privacy-critical data to server.
3. **Results**: Almost same utility as sharing all data. Better HR@10 and category distribution alignment vs obfuscation-only.

## Method (core summary)
3 components: (1) BERT-based obfuscator identifies and removes sensitive products from purchase history; (2) Modified history (nonsensitive only) sent to cloud LLM for recommendations; (3) Local de-obfuscation module reconstructs sensitive-category recommendations on-device. Runs on consumer-grade hardware.

## Key Findings
- Baseline (full data): Categorical HR@10 = 0.6263, Semantic HR@10 = 0.3045, 100% privacy leakage
- Categorical Obfuscation: HR@10 = 0.4742, 0% privacy leakage — too much utility loss
- BERT Obfuscation: HR@10 = 0.5960 — better utility
- Our framework: almost same utility as baseline, large privacy preservation
- Runs on consumer-grade hardware (Llama 3.2 1B)
- Better category distribution alignment vs obfuscation-only

## Actionable Insights
1. **Separate sensitive data before sending to cloud**: When building LLM recommendation systems, classify products by sensitivity, only share nonsensitive with cloud. Example: health products → keep local. Electronics → share with cloud.

2. **Local de-obfuscation**: Reconstruct sensitive recommendations locally. Don't transmit privacy-critical data. Example: user bought vitamins → don't send to cloud. Local model predicts vitamin-related recommendations.

3. **Consumer-grade hardware feasible**: Privacy-preserving LLM recommendations run on standard devices. No need for specialized hardware. Example: mobile app can run de-obfuscation locally.

## Assumptions & Limitations
**Conditions for method to work:**
- BERT-based classifier for sensitivity detection
- Local LLM for de-obfuscation (Llama 3.2 1B)
- Cloud LLM for main recommendations

**Limitations the paper acknowledges:**
- Sensitivity classification errors (false negatives → leakage, false positives → utility loss)
- Fixed privacy definition (health-related only)
- Cumulative purchase history privacy leakage not addressed
- Input/output length constraints

**Limitations the paper does NOT mention:**
- BERT classifier bias — may miss non-health sensitive items
- User-adaptive privacy controls not implemented
- Cross-user pattern inference not addressed
- Real-world deployment challenges
- Cost of local inference on mobile devices

## Metadata
- Year: 2025
- Authors: Tina Khezresmaeilzadeh, Jiang Zhang, Dimitrios Andreadis, Konstantinos Psounis
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2505.00951
- Citation count: [EXTRACTION FAILED]
