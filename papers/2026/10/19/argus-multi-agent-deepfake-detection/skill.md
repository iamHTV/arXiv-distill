# Skill: ARGUS Four-Perspective Forensic Audit
Source: 2608.06865v1
Type: framework / workflow

## Khi nào dùng skill này
- Cần xác thực (verify) authenticity video có mặt (marketing video, UGC — user-generated content, testimonial — lời chứng thực) trước deepfake mới nhất (Seedance 2.0, Sora 2, Kling...), đặc biệt generators KHÔNG thuộc tập training của detector thông thường.
- Cần explanation (giải thích) kèm verdict (phán quyết) để audit (kiểm toán) — không chỉ binary real/fake.
- Tình huống KHÔNG nên dùng: video không có mặt (framework cần face detection pipeline); cần real-time (<1s) — pipeline 4 agents + judge ≈ 5× inference cost; FS/FR (face swap/reenactment) generators chưa thấy — OOD evaluation chỉ test EFS.

## Input cần có
- Video có chứa face (quét frame-by-frame qua face detection pipeline, giữ frames có mặt).
- MLLM access cho 4 observation agents + 1 judge agent (paper dùng Qwen2.5-VL-7B cho tất cả — small open-source đủ tốt; KHÔNG cần closed-source).
- Dimension-specific prompts cho 4 agents (Appendix F của paper): texture (skin details, blending boundaries), lighting (light direction, shadows, illumination consistency), motion (continuity, movement, flicker, temporal instability), physics (hair, clothing, perspective, anatomical/geometric plausibility).
- Judge prompt: aggregate evidence, resolve conflicts, output binary real/fake + concise verdict-consistent explanation.

## Các bước thực hiện
1. **Sample frames:** uniformly sample a sequence of frames X(v) từ video input.
2. **4 observation agents song song:** mỗi agent nhận SAME frames + dimension prompt riêng → textual observation MÔ TẢ dấu vết nghi ngờ, KHÔNG predict verdict. (Texture agent thường strongest — texture-only F1 44.53, recall 97.40%.)
3. **Judge reconcile:** judge nhận 4 textual observations + (tuỳ chọn) video frames → weigh supporting/conflicting evidence → binary real/fake + concise explanation. (Judge có video: F1 51.01→53.28 — nên cho judge xem video.)
4. **(Training tuỳ chọn) SFT:** train observation agents trên dimension-specific observation labels (autoregressive LM loss, LR 1e-4, 1 epoch, LoRA); rồi train judge trên concatenated observations + visual input. Joint training cả 2 components better than either alone (Table 4).
5. **(Training tuỳ chọn) GRPO:** judge only (observation agents frozen), G=8 responses/prompt, binary accuracy reward r∈{0,1}, advantage A=(r−r̄)/(σ_r+ε), clipped surrogate + KL penalty vs frozen SFT policy (LR 5e-6).
6. **Report:** verdict + 4-dimensional evidence report (texture/lighting/motion/physics observations) — auditability cao hơn binary label.

## Output mong đợis
- Binary verdict (real/fake) + concise verdict-consistent explanation.
- 4-dimensional forensic evidence report.
- Trên OOD generators (20 held-out: CogVideoX1.5, HunyuanVideo, LTX-Video, SkyReels, Wan, Hailuo, Kling, Pika 2.2, PixVerse, Sora 2, Seedance 2.0...): Acc 69.87%, Recall 81.82%, F1 53.28% (w/ Video) — beats Gemini-2.5-Pro (F1 47.45%), GPT-4o (37.55%), Skyra (38.30%), VideoVeritas (43.22%) bằng small open-source models.

## Ví dụ áp dụng
- Solopreneur nhận video testimonial từ "khách hàng" cho sản phẩm: chạy ARGUS audit — texture agent phát hiện skin overly smooth + plastic-like finger textures; lighting agent phát hiện lighting mismatch khi background chuyển indoor→outdoor; motion agent phát hiện finger shape/color thay đổi qua frames; physics agent phát hiện fingers balloon-like, thiếu fingernails. Judge weigh 4 reports → verdict fake + explanation → reject testimonial trước khi đăng.

## Gotchas
- Texture cues mạnh nhất (texture-only recall 97.40%) — nhưng single agent KHÔNG đủ: all-four F1 47.53 > texture-only 44.53 (w/o Video). Luôn chạy đủ 4 agents.
- KHÔNG dùng CoT/multi-turn trên single MLLM — hại trên Qwen2.5-VL-7B (CoT F1 11.29 < Single 13.24). Improvement đến từ specialization + reconciliation, không phải longer reasoning.
- Judge có video trực tiếp tốt hơn (+2.27pp F1) — đừng chỉ relay text reports.
- Recall-precision tradeoff: Only-Obs training recall 99.58% nhưng F1 40.46 (precision rất thấp) — cần both agents + judge trained jointly + GRPO để cân bằng.
- Dataset labels do MLLM annotators + DeepSeek-V4 Pro aggregator tạo, KHÔNG human-verified — nếu tự build dataset tương tự, cần sample human validation.
- OOD split chỉ chứa EFS generators — face-swap/reenactment generators mới chưa được test; thận trọng khi apply cho FS/FR.
- 18% fake videos still missed (OOD recall 81.82%) — dùng như 1 layer trong defense-in-depth, không phải sole arbiter (người phán quyết duy nhất).
- Efficiency: 4 agents + judge sequential ≈ 5× inference cost của single model — cache frame sampling, chạy 4 observation agents song song (parallel) nếu infrastructure cho phép.
