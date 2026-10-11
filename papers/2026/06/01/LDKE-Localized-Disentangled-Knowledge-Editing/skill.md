# Skill: LDKE Knowledge Editing
Source: 2605.29826
Type: framework

## Khi nào dùng skill này

- Khi cần update specific facts trong LLM/MLLM mà không retrain from scratch — especially for correcting outdated/misinformed knowledge
- Khi knowledge edits cần generalize to related queries — not just specific sample fixes
- Khi preserving unrelated knowledge is critical — edits shouldn't cause unintended side effects

- KHÔNG dùng khi: model needs wholesale knowledge update (retrain better); gradient access unavailable (black-box API only); edits too numerous (batch editing may need different approach)

## Input cần có

- LLM/MLLM with gradient access
- Specific fact to edit (old → new)
- Related queries to test propagation
- Unrelated queries to test locality

## Các bước thực hiện

1. **Fast Localization** — Use gradient-based attribution to identify which layers store the target fact. Compute gradient of loss w.r.t. each layer's output for the target fact. Select top-K critical layers (typically 2-5 layers).

2. **Disentanglement Classification** — Train classifier to distinguish: (a) inputs relevant to edited fact → route through edited pathway; (b) inputs irrelevant → route through original pathway. Use contrastive examples (related vs unrelated queries) for training.

3. **Targeted Layer Update** — Update ONLY identified critical layers with new knowledge. Minimize interference: constrain updates to preserve original behavior on unrelated inputs.

4. **Propagation Testing** — Test: does edit generalize to logically related queries? Example: edit "CEO of X = A" → does model correctly answer "Who leads X?" and "What is X's CEO's name?"

5. **Locality Testing** — Test: is unrelated knowledge preserved? Example: edit "capital of France" → verify "capital of Italy", "capital of Germany" unchanged.

## Output mong đợi

- High propagation rate: edits generalize to related queries
- High locality: unrelated knowledge preserved
- Efficient: Fast Localization faster than brute-force layer search

## Ví dụ áp dụng

Scenario: Enterprise knowledge base update. Company X acquired by Company Y, CEO changes. (1) Localize layers storing "CEO of X" fact; (2) Update critical layers with new CEO name; (3) Test propagation: "Who runs X?", "X's leadership team" → should reflect new CEO; (4) Test locality: unrelated facts about X (products, revenue, employees) → should be unchanged.

## Gotchas

- Layer localization may not be exact — some facts distributed across layers
- Disentanglement boundary ambiguous for semi-related facts
- Edits may cascade — changing 1 fact may affect inference on related facts unexpectedly
- Gradient attribution quality varies by model architecture
