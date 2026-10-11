# [2605.29659] Opir: Phân loại An toàn Đa nhiệm cho Độc tính, Jailbreak, Ngôn từ Thù ghét

## Vấn đề
Real-time safety filtering cho LLM applications cần classifiers phát hiện unsafe prompts, toxic language, jailbreak attempts, unsafe responses — mà không tốn kém như large guardrail models. Cần distinguish (phân biệt) benign sensitive text (văn bản nhạy cảm vô hại) từ genuinely covert harmful content (nội dung có hại thực sự).

## Đóng góp
1. **Opir family**: Encoder-based guardrail models trên GLiClass architecture. Multi-task: binary safe/unsafe, multi-label toxicity, jailbreak, zero-shot categorization
2. **996 categories**: 3-level taxonomy — 16 top-level, 126 mid-level, 854 leaf labels
3. **Edge variants**: <100M parameters cho binary classification. Sub-10ms latency
4. **Competitive/outperform**: Best open-weight baselines trên majority benchmarks

## Phương pháp (tóm tắt cốt lõi)
Opir: encoder-based models trên GLiClass. Training data: taxonomy-grounded unsafe prompts, adversarially mined hard negatives, benign safety-preserving examples, generated responses, multilingual translations, Aegis2 + WildGuard subsets. Multi-task training: binary classification, toxicity, jailbreak, prompt safety, response safety. Edge variants: <100M parameters.

## Kết quả chính
- Opir-multitask-large: highest average macro F1 trên safety classification
- Wins 11 of 17 rows trên categorization accuracy
- Binary encoder: sub-10ms p50 latency at 1024 tokens — 10× faster than decoder-based baselines
- 996 categories across 3 levels
- Competitive with strongest open-weight baselines

## Insight có thể áp dụng ngay
1. **Encoder-based guardrails faster than decoder**: Sub-10ms latency cho safety classification. Use encoder models cho real-time filtering. Ví dụ: khi deploy LLM chatbot, use Opir edge model (<100M params) cho real-time prompt safety check — fast, cheap.

2. **Multi-task safety**: Single model handles toxicity, jailbreak, hate speech. Don't need separate models per task. Ví dụ: khi build content moderation system, use Opir multi-task model thay vì 4 separate classifiers.

3. **Edge deployment**: <100M parameters — runs on edge devices. Ví dụ: mobile app with LLM → use Opir edge model cho on-device safety filtering.

## Giả định & Hạn chế
**Điều kiện để method work:**
- GLiClass architecture available
- Training data với safety taxonomy
- Encoder-based inference

**Hạn chế paper thừa nhận:**
- Safety labels policy-dependent và subjective
- Over-refusal problem
- Generator và judge biases trong data construction
- Multilingual performance varies

**Hạn paper KHÔNG nói:**
- Real-world performance may change với evolving attack strategies
- Policy standards change over time
- Not for high-impact decisions (legal, employment, credit)
- Cultural context affects safety labels

## Metadata
- Năm: 2026
- Tác giả: Ihor Stepanov, Aleksandr Smechov
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.29659
- Citation count: [EXTRACTION FAILED]
