# Skill: Decode-Time Provenance Binding cho agent dùng tool
Source: 2610.31974
Type: framework (khung phương pháp) / defense-implementation (triển khai phòng thủ)

## Khi nào dùng skill này
- Agent pipeline (quy trình) gọi tool qua MCP (Model Context Protocol) hoặc tương đương, trong đó tool "giải mã" content (OCR, metadata extractor, Base64/zip parser, web scraper, image analyzer) và pipeline có critical sink (điểm cuối quan trọng) side-effect: gửi email, write file, gọi API thanh toán, export secret.
- Multi-agent: worker relay output cho nhau trước khi action — cần label sống sót qua handoff (giao tiếp chuyển giao).
- KHÔNG nên dùng: agent chỉ chat không action (không có sink); hoặc không kiểm soát được layer tool call (dùng third-party agent framework đóng không cho chèn middleware).

## Input cần có
- Danh sách tool của agent, phân thành D (decode tool — tool đảo concealment transform: OCR, stego/metadata extractor, Base64 decoder, parser file) và C (critical tool — sink side-effect).
- MCP layer (hoặc middleware proxy) bạn kiểm soát được, giữ signing key k (khóa ký) — key không bao giờ rời layer.
- In-memory ledger (sổ cái): binding store (ID → signed record) + per-context taint set (tập nhiễm theo context).
- Chính sách trusted promotion (thăng cấp tin cậy) có audit log cho giá trị decode hợp lệ (ví dụ OCR invoice được phép dùng).

## Các bước thực hiện
1. Đăng ký allow-list tại tool registration: gán mỗi tool vào D hoặc C (danh sách ngắn, reviewed — KHÔNG phân loại runtime). Thiếu decoder trong D = leak; over-broad = false block.
2. MintBinding tại tool return (trong tool handler): binding ℓ = (payload p, tool t, label τ, provenance π, dependency ID δ, chữ ký σ); τ = Untrusted nếu t∈D hoặc bất kỳ input nào Untrusted (contagious); δ do LAYER resolve từ handle nó đã issue (không nghe agent); σ = HMAC_k(canonical(ℓ)); τ=Untrusted → thêm ID vào taint set của context; trả agent opaque handle id(ℓ) — agent không thấy key, không edit ledger.
3. Truyền binding kèm tool result qua mọi hop: inter-agent message cũng mediated qua layer → binding được bind lại nguồn + taint propagate sang context đích.
4. EnforceCritical trước mọi call thuộc C: resolve handle qua ledger → dependency closure S; BLOCK nếu: σ ≠ HMAC recompute (forged/stripped), τ=Untrusted trong S, dependency unresolved trong ledger, hoặc taint(context) ∖ promoted(context) ≠ ∅; ALLOW nếu clean. KHÔNG bao giờ đọc label agent truyền — chỉ đọc lineage layer ghi.
5. Trusted promotion có audit: khi giá trị decode hợp lệ phải drive critical action (ví dụ số invoice OCR), explicit re-label giá trị cụ thể đó Trusted dưới authorization human/policy, log clearance kèm binding gốc.

## Output mong đợi
- Critical call chỉ execute khi transitive lineage (data lineage + context lineage) toàn Trusted, binding verify HMAC, promotion (nếu có) logged; mọi ngõ khác block — attack success 0% trên ngân hàng payload adaptive (per paper: 100% undefended → 0%), false block 0 với promotion, overhead ≈17 µs/call (0,16% decode round-trip).

## Ví dụ áp dụng
- Agent chăm sóc khách đọc ảnh CC (credit card — thẻ tín dụng) khách gửi: OCR là tool∈D → số card mint Untrusted; agent viết email xác nhận (critical send_email∈C): EnforceCritical thấy lineage Untrusted → block; nhân viên duyệt qua promotion UI (log) → giá trị card Trusted → send_email allow. Attacker nhúng instruction trong logo signature email → decode → relay → critical call block dù agent bị compromise gắn label giả.

## Gotchas
- Contain ≠ detect: bạn KHÔNG phát hiện ảnh có payload — payload vẫn decode vào context agent và có thể skew summary text (prose), defense chỉ chặn nó tới sink. Nếu cần summary an toàntoo, phải taint/output-check riêng (paper để future work).
- Agent paraphrase instruction thành free text gửi qua channel không mediated (Slack DM cá nhân, ghi chú) → taint không record được → ensure MỌI inter-agent communication đi qua layer mediated.
- Relay cross-host/domain: HMAC shared key cần secured channel, hoặc đổi sang public-key signature (algorithm không đổi).
- Over-broad D gây false block 33% legitimate task (paper: 67% completion without promotion) → promotion path là bắt buộc để deploy, không phải optional.
- PSNR/SSIM high không = ảnh innocent-looking asserts invisibility — nhưng irrelevant: defense block dù carrier visible hay không (containment independent of carrier quality).
