# [2605.31581v1] Choosing the Lens: Kích hoạt Perspective Chiến lược trong Argumentation Phụ thuộc Context

## Vấn đề
Prior work chưa giải quyết được strategic manipulation trong argumentation vì: Dung's framework và Value-Based Argumentation Frameworks (VAFs) đều treat evaluation regime là fixed — không có formal mechanism để agent chọn "lens" nào áp dụng khi đánh giá arguments. VAF cho phép rerank values nhưng không deactivate chúng, nên strategic options bị giới hạn.

## Đóng góp
1. **Context-Dependent Argumentation Frameworks (CDAFs)**: Mở rộng Dung's theory — defeat function δ xác định per-context attacks nào succeed, không phải fixed
2. **Perspective-labeled CDAF**: Derive defeat function từ relevance set ρ (agent's action space) và priority π (institutional structure). Agent chọn ρ, không thay đổi được π
3. **ACTIVATION-MANIPULATION problem**: Decision problem — agent có thể chọn ρ để target argument được accepted? Baseline complexity bounds được ghi nhận

## Phương pháp (tóm tắt cốt lõi)
CDAF = ⟨𝒜, R, 𝒞, δ⟩: arguments 𝒜, attack relation R, contexts 𝒞, defeat function δ. Perspective-labeled specialization: mỗi argument có source perspective src(a) ∈ Π. Context c activates subset ρ(c) ⊆ Π với priority π. Attack (a,b) active khi src(a) ∈ ρ(c) ∧ π(src(a)) ≥ π(src(b)). Key asymmetry: deactivating perspective removes attacks từ arguments thuộc perspective đó, nhưng arguments vẫn eligible for acceptance. Worked example: argument t bị reject under every full-relevance injective priority (structural trap: defender b cũng attack t), nhưng accepted under ρ={β,γ} (deactivate α, d defends t against b).

## Kết quả chính
- [NO BENCHMARK] — purely theoretical, không có empirical evaluation
- Result 1: Under full relevance (ρ=Π), target argument t rejected cho MỌI injective priority — structural trap where defender cũng là attacker
- Result 2: Under partial activation (ρ={β,γ}), t accepted — deactivating α breaks the trap
- Key insight: Partial perspective activation có strategic power mà VAF audience KHÔNG có — VAF chỉ rerank, không deactivate
- Complexity: ACTIVATION-MANIPULATION baseline bounds recorded, tight bounds left open

## Insight có thể áp dụng ngay
1. **Chọn evaluation lens trước khi argue**: Khi propose idea, không fight trên mọi front. Chọn subset stakeholders/lenses mà proposal strongest. Ví dụ: proposal technical → activate performance + reliability reviewers, deactivate finance lens nếu cost argument yếu.

2. **Deactivate hostile perspectives**: Nếu argument bị attack từ perspective bạn không thể win, deactivate nó thay vì counter-argue. Ví dụ: product launch proposal bị finance reviewer attack về cost → thay vì argue cost, redirect discussion sang user impact lens (ρ={user_impact, market_share}), finance perspective vẫn present nhưng không active attacker.

3. **Structural trap awareness**: Khi defender cũng là attacker (cùng perspective), argument bị trap. Giải pháp:引入 external perspective (d) để defend mà không attack back. Ví dụ: nếu engineering argument vừa defend vừa attack proposal →引入 customer success perspective để defend proposal mà không conflict.

## Giả định & Hạn chế
**Điều kiện để framework work:**
- Arguments và attack relations phải được xác định trước (fixed structure)
- Agent phải có influence over which perspectives are activated (ρ)
- Priority π là institutional structure, agent không thay đổi được

**Hạn chế paper thừa nhận:**
- Chỉ worked example nhỏ, không scale study
- Tight complexity bounds left open
- Multi-agent variants left open
- Fuller study beyond scope

**Hạn chế paper KHÔNG nói:**
- Không discuss how to determine perspectives Π in practice
- Không address dynamic argumentation (arguments evolve over time)
- Không consider partial information (agent không biết π của others)
- Purely formal — no empirical validation on real decision scenarios
- Không address persuasion ethics (deactivation = manipulation?)

## Metadata
- Năm: 2026
- Tác giả: Albert Sadowski, Jarosław A. Chudziak (Warsaw University of Technology)
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31581v1
- Citation count: [EXTRACTION FAILED]
