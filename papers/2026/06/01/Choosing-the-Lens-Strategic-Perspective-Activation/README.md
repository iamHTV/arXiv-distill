# [2605.31581v1] Choosing the Lens: Kích hoạt Perspective (góc nhìn) Chiến lược trong Argumentation (lập luận) Phụ thuộc Context (ngữ cảnh)

## Vấn đề
Các nghiên cứu trước chưa giải quyết được strategic manipulation (thao túng chiến lược) trong argumentation (lập luận) vì: Dung's framework và Value-Based Argumentation Frameworks (VAFs — khung lập luận dựa trên giá trị) đều treat evaluation regime (chế độ đánh giá) là fixed (cố định) — không có formal mechanism (cơ chế hình thức) để agent chọn "lens" (góc nhìn) nào áp dụng khi đánh giá arguments. VAF cho phép rerank (xếp hạng lại) values nhưng không deactivate (vô hiệu hóa) chúng, nên strategic options (tùy chọn chiến lược) bị giới hạn.

## Đóng góp
1. **Context-Dependent Argumentation Frameworks (CDAFs — khung lập luận phụ thuộc ngữ cảnh)**: Mở rộng Dung's theory — defeat function (hà hà số chiến thắng) δ xác định per-context (theo ngữ cảnh) attacks (cuộc tấn công) nào succeed (thành công), không phải fixed
2. **Perspective-labeled CDAF (CDAF gắn nhãn góc nhìn)**: Derive (suy ra) defeat function từ relevance set ρ (agent's action space — không gian hành động của tác nhân) và priority π (institutional structure — cấu trúc thể chế). Agent chọn ρ, không thay đổi được π
3. **ACTIVATION-MANIPULATION problem (bài toán kích hoạt-thao túng)**: Decision problem (bài toán quyết định) — agent có thể chọn ρ để target argument (lập luận mục tiêu) được accepted (chấp nhận)? Baseline complexity bounds (giới hạn độ phức tạp cơ sở) được ghi nhận

## Phương pháp (tóm tắt cốt lõi)
CDAF = ⟨𝒜, R, 𝒞, δ⟩: arguments 𝒜, attack relation R (quan hệ tấn công), contexts 𝒞, defeat function δ. Perspective-labeled specialization (chuyên hóa gắn nhãn góc nhìn): mỗi argument có source perspective src(a) ∈ Π (góc nhìn nguồn). Context c activates subset ρ(c) ⊆ Π (kích hoạt tập con) với priority π (ưu tiên). Attack (a,b) active khi src(a) ∈ ρ(c) ∧ π(src(a)) ≥ π(src(b)). Key asymmetry (bất đối xứng chính): deactivating a perspective removes attacks từ arguments thuộc perspective đó, nhưng arguments vẫn eligible for acceptance (đủ điều kiện được chấp nhận). Worked example (ví dụ minh họa): argument t bị reject (từ chối) under every full-relevance injective priority (mỗi ưu tiên tiêm đầy đủ liên quan) — structural trap (bẫy cấu trúc): defender b cũng attack t, nhưng accepted under ρ={β,γ} (deactivate α, d defends t against b — d bảo vệ t trước b).

## Kết quả chính
- [NO BENCHMARK] — purely theoretical (thuần lý thuyết), không có empirical evaluation (đánh giá thực nghiệm)
- Result 1: Under full relevance (ρ=Π), target argument t rejected cho MỌI injective priority — structural trap where defender cũng là attacker
- Result 2: Under partial activation (kích hoạt một phần, ρ={β,γ}), t accepted — deactivating α breaks the trap (phá vỡ bẫy)
- Key insight: Partial perspective activation có strategic power (sức mạnh chiến lược) mà VAF audience KHÔNG có — VAF chỉ rerank, không deactivate
- Complexity: ACTIVATION-MANIPULATION baseline bounds recorded, tight bounds left open

## Insight có thể áp dụng ngay
1. **Chọn evaluation lens trước khi argue (tranh luận)**: Khi propose idea (đề xuất ý tưởng), không fight trên mọi front (chiến đấu trên mọi mặt trận). Chọn subset stakeholders/lenses (tập con các bên liên quan/góc nhìn) mà proposal strongest (mạnh nhất). Ví dụ: proposal technical (kỹ thuật) → activate performance + reliability reviewers (người đánh giá hiệu suất + độ tin cậy), deactivate finance lens (góc nhìn tài chính) nếu cost argument (lập luận chi phí) yếu.

2. **Deactivate hostile perspectives (vô hiệu hóa góc nhìn thù địch)**: Nếu argument bị attack từ perspective bạn không thể win, deactivate nó thay vì counter-argue (phản biện). Ví dụ: product launch proposal bị finance reviewer attack về cost → thay vì argue cost, redirect discussion (chuyển hướng thảo luận) sang user impact lens (ρ={user_impact — tác động người dùng, market_share — thị phần}), finance perspective vẫn present nhưng không active attacker.

3. **Structural trap awareness (nhận thức bẫy cấu trúc)**: Khi defender cũng là attacker (cùng perspective), argument bị trap. Giải pháp:引入 external perspective (góc nhìn bên ngoài, d) để defend mà không attack back. Ví dụ: nếu engineering argument vừa defend vừa attack proposal →引入 customer success perspective (góc nhìn thành công khách hàng) để defend proposal mà không conflict.

## Giả định & Hạn chế
**Điều kiện để framework work:**
- Arguments và attack relations phải được xác định trước (fixed structure — cấu trúc cố định)
- Agent phải có influence (ảnh hưởng) over which perspectives are activated (ρ)
- Priority π là institutional structure (cấu trúc thể chế), agent không thay đổi được

**Hạn chế paper thừa nhận:**
- Chỉ worked example nhỏ, không scale study (nghiên cứu quy mô)
- Tight complexity bounds left open (giới hạn độ phức tạp chặt chưa giải)
- Multi-agent variants left open (biến thể đa tác nhân chưa giải)
- Fuller study beyond scope (nghiên cứu đầy đủ ngoài phạm vi)

**Hạn chế paper KHÔNG nói:**
- Không discuss how to determine perspectives Π in practice (trong thực tế)
- Không address dynamic argumentation (lập luận động — arguments evolve over time — phát triển theo thời gian)
- Không consider partial information (thông tin không đầy đủ — agent không biết π của others)
- Purely formal — no empirical validation on real decision scenarios (xác minh thực nghiệm trên tình huống quyết định thực tế)
- Không address persuasion ethics (đạo đức thuyết phục — deactivation = manipulation? — vô hiệu hóa = thao túng?)

## Metadata
- Năm: 2026
- Tác giả: Albert Sadowski, Jarosław A. Chudziak (Warsaw University of Technology)
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31581v1
- Citation count: [EXTRACTION FAILED]
