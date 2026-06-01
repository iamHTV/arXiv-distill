# [2605.29659] Opir: Efficient Multi-Task Safety Classification for Toxicity, Jailbreaks, Hate Speech, and Harmful Content

## Problem
Real-time safety filtering for LLM applications requires classifiers that detect unsafe prompts, toxic language, jailbreak attempts, unsafe responses — without the cost of large guardrail models. Need to distinguish benign sensitive text from genuinely covert harmful content.

## Contribution
1. **Opir family**: Encoder-based guardrail models on GLiClass architecture. Multi-task: binary safe/unsafe, multi-label toxicity, jailbreak, zero-shot categorization.
2. **996 categories**: 3-level taxonomy — 16 top-level, 126 mid-level, 854 leaf labels.
3. **Edge variants**: <100M parameters for binary classification. Sub-10ms latency.
4. **Competitive/outperform**: Best open-weight baselines on majority of benchmarks.

## Method (core summary)
Opir: encoder-based models on GLiClass. Training data: taxonomy-grounded unsafe prompts, adversarially mined hard negatives, benign safety-preserving examples, generated responses, multilingual translations, Aegis2 + WildGuard subsets. Multi-task training: binary classification, toxicity, jailbreak, prompt safety, response safety. Edge variants: <100M parameters.

## Key Findings
- Opir-multitask-large: highest average macro F1 on safety classification
- Wins 11 of 17 rows on categorization accuracy
- Binary encoder: sub-10ms p50 latency at 1024 tokens — 10× faster than decoder-based baselines
- 996 categories across 3 levels
- Competitive with strongest open-weight baselines

## Actionable Insights
1. **Encoder-based guardrails faster than decoder**: Sub-10ms latency for safety classification. Use encoder models for real-time filtering. Example: when deploying LLM chatbot, use Opir edge model (<100M params) for real-time prompt safety check — fast, cheap.

2. **Multi-task safety**: Single model handles toxicity, jailbreak, hate speech. Don't need separate models per task. Example: when building content moderation system, use Opir multi-task model instead of 4 separate classifiers.

3. **Edge deployment**: <100M parameters — runs on edge devices. Example: mobile app with LLM → use Opir edge model for on-device safety filtering.

## Assumptions & Limitations
**Conditions for method to work:**
- GLiClass architecture available
- Training data with safety taxonomy
- Encoder-based inference

**Limitations the paper acknowledges:**
- Safety labels are policy-dependent and subjective
- Over-refusal problem
- Generator and judge biases in data construction
- Multilingual performance varies

**Limitations the paper does NOT mention:**
- Real-world performance may change with evolving attack strategies
- Policy standards change over time
- Not for high-impact decisions (legal, employment, credit)
- Cultural context affects safety labels

## Metadata
- Year: 2026
- Authors: Ihor Stepanov, Aleksandr Smechov
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.29659
- Citation count: [EXTRACTION FAILED]
