# Skill: On-device function-calling fine-tuning for device control

Source: 2609.25373v2
Type: workflow

## When to use this skill

- You need a small model (under 1B parameters) to control local device actions (flashlight on/off, SMS, phone calls, open app, check battery) without sending requests to the cloud.
- You have a tool catalog with clear JSON schemas and want to extend an existing function-calling model to new action categories.
- You want to maintain capability on old tools while adding new tools (avoid catastrophic forgetting).

## When NOT to use this skill

- Each task category requires absolute accuracy on a fixed tool set and cannot tolerate shared weights across categories.
- Target device is iOS or does not support LiteRT-LM / local model execution.
- You need sub-1-second response per turn (latency ~13 seconds on Pixel 8 Pro may be too slow).

## Required inputs

- Tool catalog in JSON: function name, natural-language description, parameter schema (required/optional arguments).
- A function-calling backbone model that is instruction-tuned (e.g., FunctionGemma 270M-it).
- A strong teacher LLM to generate synthetic conversations.
- A validator script to check function names are in the catalog, required arguments are present and of correct type.
- Single-GPU training environment (CUDA or Apple Silicon MPS), Hugging Face Transformers + TRL.

## Steps to execute

1. Define 10-15 target device actions and write JSON schema for each function (name, description, required/optional parameters).
2. Generate synthetic data: prompt the strong teacher LLM with the JSON tool list and a worked output example, producing ~300 prompts per single tool and ~5,000 multi-call prompts.
3. Validate data: run the validator script over every assistant record — drop or repair with json_repair records with invalid function names, missing required arguments, or wrong data types.
4. Complete records: add metadata (train/eval), tool declarations, and messages (developer, user, assistant) in the model's chat format.
5. (Optional) Merge with existing tool dataset (e.g., MOBILEACTIONSGOOGLE) to create a combined dataset, preserving per-source train/eval flags.
6. Fine-tune the model: full fine-tuning (no LoRA/PEFT) via TRL SFTTrainer under completion-only loss, 2 epochs, learning rate 1×10⁻⁵, batch size 32, bf16 mixed precision, gradient checkpointing enabled.
7. Export a lightweight model (.litertlm) with INT8 quantization (8-bit weights, 32-bit float activations) for local device deployment.
8. Evaluate: compute function-name accuracy, argument exact-match, and end-to-end accuracy on held-out sets; use execution-aware scoring to separate wrong-tool-selection errors from fixable format errors.

## Expected output

- A small function-calling model fine-tuned and running locally on device, achieving 70%+ end-to-end accuracy on the new test set.
- A schema-validated synthetic dataset ready for training or evaluation.
- An on-device demo app (Android) that can call system functions through natural language interface.

## Example application

A small business in Vietnam wants to build a function-calling assistant for field sales staff: list 12 actions (call customer, SMS order confirmation, turn on flashlight to photograph product, check order status, open inventory app). Generate synthetic data with a strong LLM, validate by schema, fine-tune a 270M-parameter model to run on the salesperson's phone. Result: staff says "call Nguyen Van A about order #123", the model generates the correct phone call function with the right contact name and number.

## Gotchas

- Strict exact match understates real success: omitting optional arguments (e.g., dial_call, create_chooser) is counted as wrong even though the action is still executable. Use execution-aware scoring to avoid overreacting to errors that don't affect real outcomes.
- Narrow fine-tuning on one tool group can hurt performance on other tools (Google Mobile Actions variant dropped from 29.3% to 17.2% on the extended set). Always use combined-domain training if you need to maintain multiple categories.
- Synthetic data does not capture real-world ASR errors, incomplete requests, or diverse phrasing from actual users.
- Latency ~13 seconds per turn on a mid-range device (Pixel 8 Pro) may not suit tasks needing instant response.
- Only evaluated on English and Android; not tested on iOS or other languages.