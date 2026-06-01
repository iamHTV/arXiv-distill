# [2605.31404v1] Kiếm, Khiên, và Gót chân Achilles: Đặc trưng Hóa Thiên kiến Cảm ứng Ngôn ngữ của LLMs cho Suy luận Không gian

## Vấn đề
LLM-based navigation systems (hệ thống định hướng dựa trên LLM) commonly construct explicit spatial representations (biểu diễn không gian tường minh) và translate chúng thành textual descriptions (mô tả văn bản). Nhưng linguistic structures (cấu trúc ngôn ngữ) và contextual features (đặc trưng ngữ cảnh) trong representations thường treated as neutral engineering decisions (quyết định kỹ thuật trung tính) — KHÔNG ĐÚNG! Chúng actively shape (định hình chủ động) LLMs' behavior (hành vi).

## Đóng góp
1. **Dual-interventional framework (khung can thiệp kép)**: Disentangles (tách biệt) linguistic structures từ contextual cues. Representation intervention: varies linguistic format và compression degree. Context intervention: controls cue availability, injects conflicts
2. **3 metaphors (ẩn dụ)**: Topological info = Shield (khiên — backbone vững chắc). Linguistic format = Sword (kiếm — double-edged sword). Semantic info = Achilles' Heel (gót chân — fatal weakness)
3. **Engineering guidance**: Preserve topological integrity, calibrate compression to model capacity, ensure semantic correctness

## Phương pháp (tóm tắt cốt lõi)
Dual-interventional framework: (1) Representation intervention: vary linguistic format (text, graph, structured) và compression degree under strict information equivalence — clarify when representations support/inhibit planning; (2) Context intervention: control cue availability (topology, geometry, semantics), inject cue conflicts — reveal preferences và vulnerabilities. Experiments across diverse spatial reasoning tasks và multiple model scales.

## Kết quả chính
- Topological information = sturdy shield, backbone of robust planning — dominates geometry-based cues
- Linguistic format = double-edged sword: effect depends on model size, task demands, compression level
- Semantic information = fatal Achilles' heel: incorrect semantic cues systematically derail planning
- Pattern consistent across tasks và model scales
- Effective representations: preserve topology, calibrate compression, ensure semantic correctness

## Insight có thể áp dụng ngay
1. **Topological integrity là first-class constraint**: Khi build LLM navigation/reasoning systems, preserve topological structure. Không simplify connections. Ví dụ: khi build AI route planner, maintain accurate road connections — topology quan trọng hơn geometry details.

2. **Calibrate compression to model capacity**: Smaller models cần less compression. Larger models handle higher compression. Ví dụ: khi deploy navigation AI trên edge device (small model), use detailed representation. Cloud (large model) → more compression OK.

3. **Semantic correctness is mandatory**: Incorrect semantic cues derail planning systematically. Treat semantic disambiguation as mandatory, not auxiliary. Ví dụ: khi build AI logistics planner, ensure "warehouse A" always refers to same location — semantic ambiguity = planning failure.

## Giả định & Hạn chế
**Điều kiện để experiment work:**
- Controlled synthetic environments với strict information equivalence
- Multiple model scales tested
- Diverse spatial reasoning tasks

**Hạn chế paper thừa nhận:**
- Focus on controlled synthetic environments — real-world more complex

**Hạn chế paper KHÔNG nói:**
- Synthetic environments may not capture real-world noise
- Specific to spatial reasoning — generalizability to other domains unclear
- Model-scale dependency may change with future larger models
- Không test with multimodal inputs (images + text)

## Metadata
- Năm: 2026
- Tác giả: Xudong Zhang, Jian Yang, et al.
- Category: cs.CL, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31404v1
- Citation count: [EXTRACTION FAILED]
