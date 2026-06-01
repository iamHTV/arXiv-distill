# [2605.30207v1] Persona Conditioning of Brand Recommendations — Audit (Kiểm toán) Persona Ảnh hưởng đến Đề xuất Thương hiệu trong Chat AI Thương mại

## Vấn đề
Cùng một prompt "best CRM software" đến AI assistants từ buyers (người mua) trong context (ngữ cảnh) rất khác nhau: solo founder (người sáng lập đơn), enterprise VP (phó chủ tịch doanh nghiệp), UK SMB owner (chủ doanh nghiệp nhỏ Anh). Prior work chưa audit (kiểm toán) how strongly contextual variation (biến đổi ngữ cảnh) reshapes (định hình lại) brands mà model recommend (đề xuất). Các measurement protocol (giao thức đo lường) hiện tại aggregate (tổng hợp) across personas, systematically obscure (che giấu có hệ thống) sự variation.

## Đóng góp
1. **Prominence-stratified audit (kiểm toán phân tầng theo độ nổi bật)**: 2,000 runs trên 10 personas × 8 prompts × 3 model configurations (OpenAI, Anthropic). Kết quả: persona drops recommendation-set similarity (Jaccard) by Δ = -0.12 to -0.20
2. **Category leaders persona-resistant (kháng persona)**: L1 brands có ~80% same-brand consistency across personas. L3 mid-market brands swap up to 75% recommendation set khi persona thay đổi
3. **Cross-provider asymmetry (bất đối xứng xuyên nhà cung cấp)**: Anthropic model show larger effect — 43-52% recommendations without retrieval-layer evidence vs OpenAI 8-29%

## Phương pháp (tóm tắt cốt lõi)
Audit design: 10 hand-curated personas (solo founder, enterprise VP, UK SMB, etc.) × 8 commercial prompts ("best CRM software", "best project management tool", etc.) × 3 model cells (OpenAI high/low, Anthropic sonnet low) × N=10 reruns. Brand extraction bằng 2 LLM judges (claude-haiku, gpt-5-mini) với intersection classification (chỉ đếm khi cả 2 judges agree). Consensus recommendation set = union of consensus-recommended brands across 10 reruns. Metric: Jaccard similarity giữa recommendation sets của cùng persona vs cross-persona.

## Kết quả chính
- Cross-persona Jaccard: 0.22-0.35 vs within-persona reference: 0.42-0.51
- Persona-shift effect size: Δ = -0.12 to -0.20 (clustered 95% CIs exclude zero trên cả 3 cells)
- L1 category leaders: 0.20-0.29 swap rate (persona-resistant)
- L3 mid-market brands: up to 0.75 swap rate (persona-sensitive)
- Anthropic sonnet/low: larger effect magnitude than OpenAI cells
- Rerun-stability baseline: 0.50-0.61 (persona effect sits outside noise floor)
- |Δ| comparable to within-provider-minus-cross-provider Jaccard gap (~0.20)

## Insight có thể áp dụng ngay
1. **Đo lường AI brand perception phải conditioning on persona**: Khi audit brand visibility trên AI chatbots, KHÔNG dùng single generic prompt. Phải test với nhiều buyer personas khác nhau. Ví dụ: CRM company muốn biết brand có appear trong AI recommendations không → test với 5-10 personas (startup founder, enterprise buyer, budget-conscious, feature-focused) và compare results.

2. **Mid-market brands cần segment-targeted content**: Category leaders an toàn (persona-resistant), nhưng mid-market brands cần content strategy theo segment. Ví dụ: thay vì 1 page "Best Project Management Tool", tạo "Best PM Tool for Startups", "Best PM Tool for Enterprise", "Best PM Tool for Remote Teams" — mỗi page targeting 1 persona segment.

3. **AI retrieval vs priors affects persona sensitivity**: Models dùng nhiều training priors (ít retrieval) → persona effect lớn hơn. Models dùng retrieval → persona effect nhỏ hơn. Ví dụ: khi optimize brand content cho AI visibility, focus vào retrievable content (structured data, clear claims) thay vì relying on brand recognition alone.

## Giả định & Hạn chế
**Điều kiện để audit work:**
- 10 hand-curated personas, English-only, US/UK/EU geographic skew
- Single-day measurement — temporal drift không measured
- Persona-prefix syntax held constant

**Hạn chế paper thừa nhận:**
- L4 undersampled trên mọi cell; sonnet/high và opus cells không included
- 10 personas limited — future audits nên sample broadly hơn
- No pure-priors share co-measurement — hypothesis supported by cross-paper co-occurrence, không phải within-run
- Single-day measurement — temporal drift out of scope

**Hạn chế paper KHÔNG nói:**
- Chỉ audit 3 model configurations — không cover Google, Meta, open-source models
- 8 commercial prompts limited — không cover all product categories
- Jaccard metric simplistic — doesn't capture ranking order hoặc recommendation quality
- Không test non-English personas — global brands có thể khác
- Hand-curated personas có thể không represent real buyer diversity

## Metadata
- Năm: 2026
- Tác giả: Will Jack, Noah Lehman, Keller Maloney, Sarah Xu
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.30207v1
- Citation count: [EXTRACTION FAILED]
