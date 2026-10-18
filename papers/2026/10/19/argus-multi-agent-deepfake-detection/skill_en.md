# Skill: ARGUS Four-Perspective Forensic Audit
Source: 2608.06865v1
Type: framework / workflow

## When to use this skill
- You need to verify the authenticity of a face-containing video (marketing video, UGC — user-generated content, testimonial) against the latest deepfakes (Seedance 2.0, Sora 2, Kling...), especially generators NOT in the training set of conventional detectors.
- You need an explanation alongside the verdict for auditability — not just a binary real/fake.
- Do NOT use: videos without faces (the framework needs a face detection pipeline); real-time needs (<1s) — the 4-agent + judge pipeline costs ~5× inference; unseen FS/FR (face-swap/reenactment) generators — the OOD evaluation only tests EFS.

## Inputs required
- A video containing a face (scan frame-by-frame through a face detection pipeline, keep frames with faces).
- MLLM access for 4 observation agents + 1 judge agent (the paper uses Qwen2.5-VL-7B for all — small open-source is good enough; closed-source NOT required).
- Dimension-specific prompts for the 4 agents (Appendix F of the paper): texture (skin details, blending boundaries), lighting (light direction, shadows, illumination consistency), motion (continuity, movement, flicker, temporal instability), physics (hair, clothing, perspective, anatomical/geometric plausibility).
- Judge prompt: aggregate evidence, resolve conflicts, output binary real/fake + concise verdict-consistent explanation.

## Steps
1. **Sample frames:** uniformly sample a sequence of frames X(v) from the input video.
2. **4 observation agents in parallel:** each receives the SAME frames + its own dimension prompt → a textual observation describing suspicious traces, WITHOUT predicting the verdict. (The texture agent is usually strongest — texture-only F1 44.53, recall 97.40%.)
3. **Judge reconcile:** the judge receives the 4 textual observations + (optionally) the video frames → weighs supporting/conflicting evidence → binary real/fake + concise explanation. (Judge with video: F1 51.01→53.28 — give the judge the video.)
4. **(Optional training) SFT:** train observation agents on dimension-specific observation labels (autoregressive LM loss, LR 1e-4, 1 epoch, LoRA); then train the judge on concatenated observations + visual input. Joint training of both components beats either alone (Table 4).
5. **(Optional training) GRPO:** judge only (observation agents frozen), G=8 responses/prompt, binary accuracy reward r∈{0,1}, advantage A=(r−r̄)/(σ_r+ε), clipped surrogate + KL penalty against the frozen SFT policy (LR 5e-6).
6. **Report:** verdict + 4-dimensional evidence report (texture/lighting/motion/physics observations) — higher auditability than a binary label.

## Expected output
- Binary verdict (real/fake) + concise verdict-consistent explanation.
- 4-dimensional forensic evidence report.
- On OOD generators (20 held-out: CogVideoX1.5, HunyuanVideo, LTX-Video, SkyReels, Wan, Hailuo, Kling, Pika 2.2, PixVerse, Sora 2, Seedance 2.0...): Acc 69.87%, Recall 81.82%, F1 53.28% (w/ Video) — beats Gemini-2.5-Pro (F1 47.45%), GPT-4o (37.55%), Skyra (38.30%), VideoVeritas (43.22%) using small open-source models.

## Example application
- A solopreneur receives a testimonial video from a "customer" for their product: run the ARGUS audit — the texture agent finds overly smooth skin + plastic-like finger textures; the lighting agent finds a lighting mismatch when the background shifts indoor→outdoor; the motion agent finds finger shape/color changing across frames; the physics agent finds balloon-like fingers lacking fingernails. The judge weighs the 4 reports → verdict fake + explanation → reject the testimonial before publishing.

## Gotchas
- Texture cues are the strongest (texture-only recall 97.40%) — but a single agent is NOT enough: all-four F1 47.53 > texture-only 44.53 (w/o Video). Always run all 4 agents.
- Do NOT use CoT/multi-turn on a single MLLM — it hurts on Qwen2.5-VL-7B (CoT F1 11.29 < Single 13.24). The improvement comes from specialization + reconciliation, not longer reasoning.
- Judge with direct video access is better (+2.27pp F1) — don't just relay text reports.
- Recall-precision tradeoff: Only-Obs training has recall 99.58% but F1 40.46 (very low precision) — you need both agents + judge trained jointly + GRPO for balance.
- Dataset labels are produced by MLLM annotators + DeepSeek-V4 Pro aggregator, NOT human-verified — if building a similar dataset, sample human validation.
- The OOD split contains only EFS generators — unseen face-swap/reenactment generators are untested; be cautious applying to FS/FR.
- 18% of fake videos are still missed (OOD recall 81.82%) — use as one layer in defense-in-depth, not the sole arbiter.
- Efficiency: 4 agents + judge sequential ≈ 5× the inference cost of a single model — cache frame sampling, run the 4 observation agents in parallel if infrastructure allows.
