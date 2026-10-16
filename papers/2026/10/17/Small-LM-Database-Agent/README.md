# 2609.21341 — What Stops a Small Language Model From Driving a Database Agent

## Problem
- Framing phổ biến: capability threshold — dưới parameter count nhất định model không sustain được tool-calling loop. Prediction: failure phải trông như model KHÔNG action. Thực tế quan sát được gần như ngược lại: đa số failure là model ĐÃ action, đã establish điều đúng, rồi mất nó ở biên model–server.

## Contribution
- Field record production scale: 11 ngày, 8,199 runs, 40 models (39 open-weight local + 1 hosted), 110,711 ledger events, 14,008 refused tool calls trên LibreDB Studio agent (6 surfaces)
- 4-class failure taxonomy (clock, capability, verification, transport) + transport decomposition từ captured tool-call arguments + 5 server-side interventions + 2 measurement confounds

## Method
- Agent constrained loop + verifier: mọi claim trong report phải cite artifact (correlation id của completed read, fingerprint schema snapshot) — anti-hallucination, cũng là nguồn loss lớn. Verifier (không human judge): answered/unanswered; succeeded ≠ pass (2,204 model-stopped runs, 1,405 unanswered).
- Classification theo thứ tự load-bearing: clock (timeout/turn-limit/deadline) → capability (không invoke tool nào) → verification (report filed rồi bị reject) → transport (invoked tools, hết thời gian, không deliverable).

## Key Findings
- 2,100 model-attributed agent-mode losses: transport 761 (36.2%), clock 542 (25.8%), verification 434 (20.7%), capability 363 (17.3%). 75.7% losses (1,590) từ runs đã invoke ≥1 tool — hold trong 99.7% clustered resamples, 15/22 models. Capability là class NHỎ NHẤT — capability-threshold framing sai.
- Transport decomposition: 69 stopping turns examined, 27 chứa complete tool call đúng (claims true, evidence populated, correlation id genuine) nhưng viết vào assistant text channel thay vì gọi tool. None of 27 parse được JSON; 24 fail giống nhau (array close twice); 20 dùng key "name", 7 dùng "action".
- 5 server changes (không đụng model/prompt/sampling): granite4.2:3b 21→28/30, mistral-nemo:12b 18→26, llama3.1:8b 10→24, cogito:8b 0→21, glm4:latest 0→16, deepseek-r1:8b 18→24/28. Isolated text-channel reader chỉ +1,0,0,−1 (within variance) — argument-shape readers mới là yếu tố move bảng.
- Pass rate by surface: planning 83.2% → data-analysis 38.8%; ordering tracks số schema-constrained objects model phải emit, không phải difficulty trực giác.

## Actionable Insights
- Đo failure bằng ledger structured (record arguments verbatim + refusal codes + verdict), không phải process exit — production ledger chỉ record refusal code, arguments vô hình 10 ngày; capture chúng exposed 5 server defects.
- Repair server-side trước khi blame model: 5 changes không đụng model/prompt/sampling đã move 6 models 6–21 cells/30 — transport failure là mechanical shapes, sửa được bằng reader nhận diện call theo naming chứ không strict JSON parse.
- Control confound memory trước khi kết luận "model yếu": cap serving context (12B model, 262k-token window, 51GB RAM trên 64GB machine → planning cell 0/5; cap 32k → 5/5); watch swap growth, không phải free memory.

## Assumptions & Limitations
- Uncontrolled field observations, không randomized; run counts/model 3–629 (operational interest); taxonomy shares trên 2,100 losses là figure robust hơn per-model rates.
- Section 5 figures lấy trước khi cap context → per-model rates là lower bound, bias unknown (large-context models bị penalize nhiều hơn).
- Single machine, single database, single harness; 450s run deadline là hard boundary (1 8B model pass 443–444s, fail tại deadline).

## Metadata
- 2026, Cevheri Bozoğlan, Yusuf Gündoğdu, Abdullah Kaya, Koray Şirin (independent researchers, LibreDB Studio contributors), cs.SE, https://arxiv.org/pdf/2609.21341
