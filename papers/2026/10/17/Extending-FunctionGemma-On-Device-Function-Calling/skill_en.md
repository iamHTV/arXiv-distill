# Skill: functiongemma-on-device-extension
Source: 2609.25373v1
Type: framework

## When to use this skill
- Need a small on-device function-calling model for specific mobile intents (phone calls, SMS, camera, flashlight, app management, ...).
- Have a synthetic dataset of mobile-device conversations.
- Want to extend a small model (270M parameter) without catastrophic forgetting.

## When NOT to use this skill
- Need a server-side model, not on-device.
- No synthetic dataset of device conversations available.
- Don't need to fine-tune a small model (just use existing model as-is).

## Input needed
- Synthetic dataset of device-control conversations (~9,500 conversations across 15 categories).
- FunctionGemma 270M-it (or similar small function-calling model).
- Accelerator: CUDA or Apple Silicon MPS.
- TRL library for supervised fine-tuning.

## Steps to execute
1. Build synthetic dataset covering fifteen device-control categories.
2. Split 90% train / 10% evaluation (965 examples in eval split).
3. Fine-tune FunctionGemma 270M-it with TRL supervised fine-tuning under completion-only loss.
4. Enable mixed precision and gradient checkpointing.
5. Evaluate at three levels: function-name accuracy, argument accuracy, end-to-end accuracy.
6. To maintain performance on both old and new domains, jointly train the fine-tuned model with the original model (Google's MOBILEACTIONSGOOGLE).

## Expected output
- Small (270M) function-calling model with 76.5% end-to-end accuracy on MOBILEACTIONSEXTENDED (up from 29.3% base).
- Combined model: 76.5% on MOBILEACTIONSEXTENDED, 82.3% on MOBILEACTIONSGOOGLE (vs 90.3% for Google's specialist), 8.0pp trade-off for doubling category coverage.

## Application example
- Build a mobile assistant that can perform phone calls, SMS, flashlight control, screenshot capture, app opening via natural language. Use FunctionGemma 270M-it fine-tuned on a synthetic dataset of these actions.

## Gotchas
- Dataset is synthetic, not real user data.
- Only 15 device-control categories covered.
- Small 270M parameter model — can run on mobile devices.
