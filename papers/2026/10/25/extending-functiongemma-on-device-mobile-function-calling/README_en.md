# [2609.25373v2] Extending FunctionGemma for Practical On-Device Mobile Function Calling

## Core Value (1 sentence)

A 270M-parameter function-calling model can be fine-tuned for local on-device Android control with 76.5% end-to-end accuracy across 15 device-action categories, using only ~9,500 synthetic samples and without needing a large cloud model for every request.

## Problem

Prior work has not solved local on-device device control with small models, because public benchmarks (BFCL, Big-CodeBench, APIGen) focus on web APIs (REST endpoints, search, calendars, SaaS tools) rather than Android system actions (turn on flashlight, send SMS, open app, check battery). FunctionGemma 270M-it currently supports only about 7 mobile workflows (calendar event creation, contact creation, mapping, email, Wi-Fi settings, flashlight on/off), missing common everyday intents like phone calls, SMS, brightness control, camera, screenshots, and app opening.

## Contribution

(i) Open mobile-actions dataset: MOBILEACTIONSEXTENDED, a ~9,500-example function-calling corpus generated through schema-grounded synthetic prompting, post-validated for tool-call legality, split 90/10 train/eval, covering 15 device-control categories.
(ii) Two fine-tuned FunctionGemma 270M models: FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-EXTENDED and FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-COMBINED.
(iii) Multi-axis evaluation: compares 4 model versions on 2 held-out sets using exact-match metrics for function names, arguments, and end-to-end correctness.
(iv) On-device demo app (Handy Chat): Android app packaged with Buildozer, running LiteRT-LM on Pixel 8 Pro CPU.

## Method

The pipeline has 5 stages: (1) Schema-grounded synthetic generation: a strong teacher model generates user/assistant pairs from the JSON tool list and a worked output example, producing ~300 prompts per single tool and ~5,000 multi-tool prompts. (2) Validation and completion: a validator script checks that every called function name is in the catalog, all required arguments are present and of declared type; failing records are dropped or repaired with json_repair. (3) Merge with Google's MOBILEACTIONSGOOGLE to create MOBILEACTIONSCOMBINED, preserving per-source train/eval flags. (4) Fine-tuning: FunctionGemma 270M-it is full fine-tuned (no LoRA/PEFT) via TRL SFTTrainer under completion-only loss, 2 epochs, learning rate 1×10⁻⁵, batch size 32, bf16 mixed precision. (5) On-device deployment: export .litertlm bundle quantized INT8 (dynamic_wi8_afp32: 8-bit weights, 32-bit float activations), run in Handy Chat app on Android via LiteRT-LM CPU backend.

## KNOWLEDGE — Data & Concepts

- FunctionGemma 270M-it (270M-parameter function-calling model, instruction-tuned): 29.3% end-to-end accuracy on MOBILEACTIONSEXTENDED.
- Google Mobile Actions variant (Google's 7-category mobile specialist): 17.2% on MOBILEACTIONSEXTENDED, 90.3% on MOBILEACTIONSGOOGLE.
- FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-EXTENDED (our model fine-tuned on extended set): 100% function-name accuracy, 76.5% end-to-end accuracy on MOBILEACTIONSEXTENDED (+47.2 points over base model).
- FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-COMBINED (combined model): maintains 76.5% on MOBILEACTIONSEXTENDED, achieves 82.3% on MOBILEACTIONSGOOGLE (8.0-point drop vs 90.3% specialist).
- MOBILEACTIONSEXTENDED: ~9,500 records, 90/10 train/eval split, 965 eval examples across 15 categories, ~one-third multi-call prompts.
- Execution-aware accuracy: MA-Extended reaches 100.0% (from 76.5% strict exact match), MA-Combined reaches 96.0% on EXTENDED and 82.6% on GOOGLE.
- .litertlm bundle: 285.6 MB on device (after INT8 quantization).
- Latency: ~13 seconds per function-call turn on Pixel 8 Pro (pass 1 ~9s, tool execution ~2s, pass 2 ~2s).

## INSIGHT — Mechanism & Why

[Narrow fine-tuning on 7 original categories] harms generalization because the model confidently emits in-distribution calls (e.g., open_wifi_settings) instead of correct extended calls → accuracy drops from 29.3% (base) to 17.2%. This means over-specialization causes overfitting to old tools and missing new intents.

[Combined-domain training] on both datasets maintains 76.5% on extended functions and reaches 82.3% on original functions (only 8.0 points below the 90.3% specialist). This means mixing two-domain data is better than having two separate specialist models, because the model learns to separate different tools without forgetting the old ones.

[Completion-only loss] masks loss over the prompt (system tools block, developer message, user turn) so the model is graded only on its assistant continuation. This stabilizes training when prompt length dominates, which is common here because the tool catalog alone is several hundred tokens long.

[Strict exact match] understates real-world success because it penalizes omissions that are still executable; execution-aware re-scoring shows MA-Extended reaches 100.0% (from 76.5% strict), meaning most remaining "errors" are recoverable formatting issues (e.g., omitted optional booleans), not wrong tool selection.

## IDEA — Actionable Applications

Apply [schema-grounded synthetic generation] to building device-control agents for small businesses in Vietnam: step 1 is to list 10-15 common system actions (phone calls, SMS, toggle devices, open apps), generate a synthetic dataset with a strong LLM, validate by schema before fine-tuning a small model to run locally.

Apply [execution-aware accuracy] to evaluating function-calling agents: instead of only strict exact match, classify errors as "wrong tool selection" (dangerous) vs "wrong argument format" (fixable with safe defaults) so you don't overreact to errors that don't affect real outcomes.

Apply [combined-domain training] to maintaining multiple capabilities in one agent model: instead of training separately per task, mix data from related tasks in one fine-tuning run to avoid forgetting old capabilities when expanding scope.

## WISDOM — General Principle

Principle: Combined-domain training (multiple domains in one fine-tuning run) is usually better than multiple narrow specialist models when the goal is to maintain capability across many tool categories simultaneously.

When to use: When you need a small model to handle many different device actions/tools on a local device.

When NOT to use: When each domain requires absolute accuracy on a fixed set of tools and cannot tolerate shared weights.

Example outside original domain: Customer support chatbot across multiple channels (email, chat, SMS, phone) — one small model fine-tuned on data from all 4 channels instead of 4 separate models, maintaining ability to switch channels without reloading models.

## Assumptions & Limitations

- Conditions for success: High-quality synthetic data validated by schema; Android device with LiteRT-LM support; user accepts ~13 second latency per function-call turn.
- Paper's acknowledged limitations: MOBILEACTIONSEXTENDED is synthetically generated, not collected from real users; evaluation uses strict exact match which may underestimate executable success; only evaluated on one model family (FunctionGemma 270M-it); dataset and demo mainly English and Android.
- Limitations paper does NOT mention: No comparison with other same-size models (Qwen, SmolLM2); no iOS evaluation; no adversarial input robustness evaluation; 13-second latency may be too slow for some real-time tasks.

## Metadata

- Year: 2026
- Authors: Ali Rezagholizadeh, Soheila Samiee
- arXiv category: cs.LG
- PDF link: https://arxiv.org/pdf/2609.25373v2
- Citation count: no information available