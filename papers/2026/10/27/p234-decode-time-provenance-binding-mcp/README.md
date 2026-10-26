# 2610.31974 Decode-Time Provenance Binding cho MCP: Chống cross-modal trust laundering

## Problem
- Provenance defense (phòng thủ truy xuất nguồn gốc) hiện tại gán trust label (nhãn tin cậy) khi tool trả TEXT — giả định payload đi qua text channel. Prior work (NeuroTaint) cũng thừa nhận không cover multi-modal/semantic steganography (ẩn tin ngữ nghĩa), label không ký, audit trace offline thay vì block runtime.
- Gap: attacker giấu instruction trong logo chữ ký email (inline cid:/data: URI) qua steganography — text scanner chỉ thấy pixels, instruction chỉ thành instruction KHI tool decode (OCR/stego extractor/metadata parser) → laundered vào trusted control flow của multi-agent MCP pipeline. Email defense miss: AV (antivirus) match malware signature — PNG valid không phải malware; DLP (data loss prevention) inspect text/URL/attachment, không steganalysis inline logo; payload "inert" ở mail layer, chỉ "arms" sau khi decode.

## Contribution
- Cross-modal trust laundering (rửa tin cậy xuyên modalità): attack vector thực, zero-click, invisible — map tới OWASP LLM01/LLM02/LLM06/LLM08 và ASI01/02/06/07.
- Decode-time provenance binding: MCP layer mint HMAC (keyed-hash message authentication code — mã xác thực tin nhắn khóa)-signed Untrusted label ĐÚNG lúc concealment-reversing tool chạy + tự maintain provenance lineage (nguồn gốc) của mỗi critical call → block call có lineage untrusted kể cả agent bị compromise đưa valid label cho giá trị trusted không liên quan (valid-label substitution).
- Nguyên tắc contain, don't detect: không cố phát hiện ảnh có payload (arms race trước carrier ngày càng tốt — defender thua); giả định mọi decode output untrusted và contain nó.

## Method (tóm tắt cốt lõi)
- D = decode tools (stego extraction, metadata decode, Base64 decode, OCR); C = critical tools (side-effect sink: export_secrets, send_email, file write, payment). Mọi tool I/O mediated qua MCP layer (trusted).
- Algorithm 1 MintBinding: binding ℓ = (p, t, τ, π, δ, σ); δ = ID input dependency do LAYER resolve (không do agent assert); τ = Untrusted iff t∈D hoặc ∃ input τi=Untrusted (contagious — lây nhiễm); σ = HMACk(p∥t∥τ∥π∥δ), key k không bao giờ rời layer; Untrusted → thêm vào per-context taint set; agent chỉ nhận opaque handle (định danh mờ) id(ℓ).
- Algorithm 2 EnforceCritical (tại sink): resolve handle qua ledger → transitive dependency closure S; block nếu σ ≠ HMAC recompute (forged/stripped), τ=Untrusted trong S (untrusted data lineage), dependency unresolved, hoặc taint(c)\promoted(c) ≠ ∅ (untrusted context lineage); else allow.
- Invariant (điều kiện): key confined, mọi concealment-reversing tool registered trong D, layer mediate mọi critical call, layer record complete lineage kể cả inter-agent mediated message → trong fully mediated context, không critical call nào execute với lineage Untrusted (trừ khi audited trusted promotion).
- Testbed: FastMCP server thật qua stdio, Qwen2.5-0.5B-Instruct local; attack bank 24 payloads = 3 carrier (LSB ≈76 dB/SSIM≈1.000, DCT ≈18 dB/SSIM≈0.94, metadata PNG chunk lossless) × 8 evasion (plain, benign-worded, Base64, token-split, Cyrillic homoglyph, zero-width, Unicode-confusable, HTML-comment wrapping).

## Key Findings
- ASR (Attack Success Rate) trên 24 payloads: undefended 100% (24/24 leak); keyword/DLP scanner 62,5% (15/24); regex parser 62,5% (15/24); in-process taint baseline 0% trong 1 domain; decode-time provenance binding 0%. Scanner chỉ chặn plain/HTML-comment/confusable (Unicode normalization recover), fail benign-worded/Base64/token-split/homoglyph/zero-width.
- Valid-label substitution: verifier tin agent-supplied binding → allow (leak); layer-maintained lineage, dependency omitted → block; dependency in args → block; clean context → allow legitimate call.
- Ablation 4 component: full block cả 3 attack (honest/substitution/forged relay); −decode marking → LEAK hết; −sink mediation → LEAK hết; −HMAC → block in-domain nhưng leak forged relay cross-domain (remote verifier chỉ có signature); −lineage tracking → block forgery nhưng leak substitution (Trusted binding thật từ tool khác passes HMAC). HMAC và lineage necessary, non-interchangeable.
- Taint crosses mediated inter-agent message (block ở agent B context); unmediated side channel (agent paraphrase thành free text) → outside scope (boundary stated plainly).
- Relay: honest 1/3/5/10 hops → verify + block; rewrite payload/forge Trusted/strip HMAC → block (HMAC mismatch).
- Decode-set D: correct → block attack + allow legit; missing decoder (unregistered audio/document extractor) → LEAK (failure = unregistered decoder, không phải defeat mechanism); over-broad → false block legit call → recommend small audited allow-list tại tool registration.
- Utility: no promotion 2/3 (67%) legitimate task, 1 false block (OCR'd invoice number driving payment); audited trusted promotion (re-label giá trị cụ thể Trusted, logged) → 3/3 (100%), 0 false block, attack vẫn blocked.
- Overhead: MintBinding ≈8,3 µs + EnforceCritical ≈8,7 µs = ≈17 µs/critical call; decode round-trip ≈11 ms → +0,16%; full path linear theo closure depth (≈10 µs depth 1 → 0,68 ms depth 100 → 6,6 ms depth 1000; flat ≈6 µs theo số tainted context; realistic depth tens < 0,1 ms).

## Actionable Insights
1. Contain thay vì detect: với mọi tool "giải mã" content (OCR, metadata reader, web scraper, file parser, image analyzer) trong agent pipeline — mặc định output của nó untrusted và chặn nó tới critical action (gửi email, export dữ liệu, thanh toán, write file) trừ khi có promotion path audited. Ví dụ: agent đọc invoice ảnh → OCR → tự điền số tài khoản rồi chuyển tiền → require explicit promotion (human approval logged) cho giá trị originate từ OCR.
2. Trust decision phải do infrastructure viết ledger, không đọc label agent truyền: agent bị compromise có thể gắn nhãn "Trusted" giả — verifier tự maintain dependency lineage, quyết định trên lineage nó ghi. Ví dụ: pipeline agent của bạn thêm middleware logging mỗi tool call kèm source ID; final checker đọc log lineage chứ không đọc agent claim "đã kiểm tra".
3. D và C là allow-list ngắn audited tại registration point: missing decoder → leak; over-broad → false block (67% hoàn thành). Ví dụ: mỗi khi onboard tool mới cho agent, ngay tại registration đánh dấu D (tool parse/giải mã) và C (tool side-effect), review lại định kỳ — thay vì phân loại runtime.

## Assumptions & Limitations
- Điều kiện: key k confined trong MCP layer; mọi concealment-reversing tool registered trong D; layer mediate mọi critical call + inter-agent message (fully mediated context).
- Paper thừa nhận: controlled testbed (24 payload, 3 carrier, 8 evasion, 1 cover logo, 1 small local model, baseline keyword/regex/IFC — không production-scale, không learned detector, không production email workflow); proof sketch chưa machine-checked; giới hạn scope: in-model paraphrase ra ngoài mediated channel không capture (future work: taint output khi input context tainted); defense bảo vệ ACTION không phải summary prose (instruction vẫn có thể skew summary — residual unquantified); granularity message/tool-result không phải token-level; distributed enforcement cần shared key/public-key (trade simplicity cho scalability).
- Mày thấy thêm: PSNR/SSIM bound pixel distortion, không chứng minh perceptual invisibility (paper tự nói); 0,5B model nhỏ — though security decision deterministic (model-independent claim), realism với production model untested.

## Metadata
- Năm: 2026 (22 Oct 2026), tác giả: Eric Yocam (Cal Poly, corresponding), Varghese Vaidyan (Dakota State), Paris Kalathas (Cal Poly), Patrick Tague (Carnegie Mellon), Bruce DeBruhl (Cal Poly), Yong Wang (U Idaho), category: cs.CR, status: arXiv preprint, code: github.com/ericyoc/stego_provenance_defense, link PDF: https://arxiv.org/pdf/2610.31974v1, citation count: không có dữ liệu (Semantic Scholar rate-limited)
