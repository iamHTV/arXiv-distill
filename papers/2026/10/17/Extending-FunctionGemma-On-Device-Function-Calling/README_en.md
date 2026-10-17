# [2609.25373v1] Extending FunctionGemma for Practical On-Device Mobile Function Calling

## Problem
- On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. Prior work does not address extending a compact function-calling model (270M) to a broader set of on-device intents without catastrophically forgetting the original distribution.

## Contribution
- MOBILEACTIONSEXTENDED — a synthetic, schema-validated dataset of ~9,500 conversations covering fifteen device-control categories (messaging, phone calls, camera/screenshot, brightness control, device-status queries, flashlight control, application management).
- Fine-tune the 270M model with TRL supervised fine-tuning under completion-only loss, producing an extended specialist and a combined model trained jointly with Google's MOBILEACTIONSGOOGLE.
- On MOBILEACTIONSEXTENDED: end-to-end accuracy improves from 29.3% (base) and 17.2% (Google's Mobile-Actions variant) to 76.5%.
- Combined model retains 76.5% on MOBILEACTIONSEXTENDED and reaches 82.3% on MOBILEACTIONSGOOGLE (down from 90.3% of Google's specialist), an 8.0-percentage-point trade-off for doubling category coverage.
- Released dataset, fine-tuned models, reproducible training/evaluation pipeline, and Android demo.

## Method (core summary)
- Build MOBILEACTIONSEXTENDED dataset: ~9,500 synthetic conversations, 90/10 train/eval split, evaluation split contains 965 examples across 15 categories.
- Fine-tune FunctionGemma 270M-it with TRL supervised fine-tuning under completion-only loss.
- Mixed precision and gradient checkpointing enabled; 270M backbone fits on a single accelerator (CUDA or Apple Silicon MPS); no LoRA adapters; single set of weights replaces pretrained weights.
- Evaluate at three levels: function-name accuracy, argument accuracy, end-to-end accuracy.

## Key Findings
- 2 authors from UGrowAI, arXiv category: cs.LG.
- FunctionGemma 270M-it: 29.3% end-to-end accuracy on MOBILEACTIONSEXTENDED.
- Google fine-tuned variant: 17.2% (worse).
- Extended model: 76.5% on MOBILEACTIONSEXTENDED.
- Combined model: 76.5% on MOBILEACTIONSEXTENDED, 82.3% on MOBILEACTIONSGOOGLE (vs 90.3% for Google's specialist), 8.0pp trade-off for doubling category coverage.

## Actionable Insights
1. Fine-tuning a small 270M model on targeted mobile-action conversations can significantly extend its coverage. Application: when you need an on-device function-calling model, fine-tune a small (270M) model on a synthetic dataset covering specific domains.
2. Jointly training the fine-tuned model with the original model can maintain performance on both domains with a small trade-off (8.0pp). Application: when you need a model to handle both old and new domains, train jointly on both distributions.

## Assumptions & Limitations
- Dataset is synthetic.
- Focused on on-device mobile function calling.
- Only 15 device-control categories covered.
- Small 270M parameter model.

## Metadata
- Year: 2026, authors: Ali Rezagholizadeh, Soheila Samiee (UGrowAI), arXiv category: cs.LG, PDF link: https://arxiv.org/pdf/2609.25373v1
