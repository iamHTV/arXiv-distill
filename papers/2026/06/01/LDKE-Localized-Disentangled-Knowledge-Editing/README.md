# 2605.29826 LDKE: Localized and Disentangled Knowledge Editing for Multimodal LLMs

## Problem

Existing Multimodal Knowledge Editing (MKE — chỉnh sửa kiến thức đa phương thức) methods cho MLLMs exhibit critical limitation: while effectively modifying target factual pairs (cặp sự kiện mục tiêu), they fail to generalize edits (không tổng quát hóa được chỉnh sửa) cho logically related queries (truy vấn liên quan logic) và often cause unintended alterations (thay đổi không mong muốn) cho unrelated nhưng visually/semantically linked information. Hai failure modes: (1) Causal Misalignment (sai lệch nhân quả) — edits confined to specific sample; (2) Feature Entanglement (rối loạn đặc trưng) — unintended alterations cho coupled nhưng irrelevant information.

## Contribution

1. Identify và formalize 2 failure modes: Causal Misalignment và Feature Entanglement — đây là inherent issues trong MKE methods.
2. Propose LDKE — framework achieves precise và generalized editing bằng (a) localizing fact-specific model layers và (b) disentangling target-relevant inputs từ irrelevant ones.
3. Fast Localization module — identify và update critical layers efficiently. Disentanglement Classifier — route inputs appropriately để preserve unrelated knowledge.

## Method (tóm tắt cốt lõi)

LDKE framework: (1) Fast Localization — identify which layers trong MLLM store specific facts, use gradient-based attribution để find critical layers efficiently (không brute-force search); (2) Targeted Update — update only identified critical layers với new knowledge, minimize interference với other knowledge; (3) Disentanglement Classifier — train classifier to distinguish target-relevant inputs từ irrelevant ones. Relevant inputs → edited pathway. Irrelevant inputs → original pathway. Prevent unintended alterations; (4) Evaluation: test propagation (edits generalize to related queries?) và locality (unrelated knowledge preserved?).

## Key Findings

- LDKE achieves superior performance trên propagation — edits generalize to related contexts
- High locality maintained — unrelated knowledge preserved
- Solves both Causal Misalignment và Feature Entanglement
- Tested across various benchmarks và MLLMs
- Fast Localization more efficient than brute-force layer search
- Disentanglement Classifier effectively routes inputs to prevent unintended alterations

## Actionable Insights

1. Khi edit knowledge trong LLM/MLLM, KHÔNG update all layers — localize fact-specific layers first. Ví dụ: update "CEO of company X" fact → chỉ update layers 15-20 (where this fact is stored), không touch layers 0-14 hoặc 21-32.
2. Disentanglement quan trọng — khi update 1 fact, phải ensure related-but-irrelevant facts không bị unintentionally altered. Ví dụ: update "capital of France = Paris" → shouldn't alter "capital of Italy = Rome" even though both are European capitals.
3. Fast Localization module có thể apply cho other model editing tasks — identify critical layers efficiently thay vì brute-force. Ví dụ: bias mitigation — identify layers storing gender bias, targeted update only those layers.

## Assumptions & Limitations

- Giả sử: facts are stored in identifiable layers — some facts may be distributed across many layers
- Limitation: Disentanglement Classifier needs training data — relevant/irrelevant labeling can be ambiguous
- Limitation: Tested on MLLMs — may need adaptation for text-only LLMs
- Limitation: Fast Localization accuracy depends on gradient attribution quality
- Limitation (tự thấy): Knowledge editing inherently risky — even with localization, edits may have unforeseen cascading effects on model behavior

## Metadata

- Năm: 2026
- Tác giả: Leijiang Gu, Zhen Zeng, Feng Li, Xinjian Gao, Zenglin Shi
- Category: cs.AI, cs.CL
- Link PDF: https://arxiv.org/pdf/2605.29826
- Citation count: N/A
- Nhãn: [applied]
- Skill: ldke-knowledge-editing
