# Skill: AI Brand Persona Audit (Kiểm toán Persona Thương hiệu AI)
Nguồn: 2605.30207v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi audit (kiểm toán) brand visibility (tầm nhìn thương hiệu) trên AI chatbots và assistants
- Khi muốn biết brand có appear (xuất hiện) trong AI recommendations không
- Khi thiết kế AI brand perception measurement protocol (giao thức đo lường nhận thức thương hiệu AI)

## KHÔNG nên dùng khi
- Chỉ cần test 1 prompt đơn giản (không cần persona variation)
- Không có access (truy cập) đến multiple AI models
- Sản phẩm không phải consumer-facing (hướng đến người tiêu dùng)

## Input cần có
- Danh sách brands cần audit (bao gồm competitor — đối thủ)
- Danh sách buyer personas (tối thiểu 5, đề xuất 10)
- Commercial prompts liên quan đến sản phẩm (tối thiểu 4)
- Access đến AI models (OpenAI, Anthropic, hoặc others)
- Rerun capability (khả năng chạy lại): N=10 per cell

## Các bước thực hiện

### Bước 1 — Define Buyer Personas (định nghĩa persona người mua)
1. Tạo 5-10 personas đại diện cho buyer segments (phân khúc người mua):
   - Solo founder (người sáng lập đơn)
   - Enterprise VP (phó chủ tịch doanh nghiệp)
   - SMB owner (chủ doanh nghiệp nhỏ)
   - Budget-conscious buyer (người mua quan tâm giá)
   - Feature-focused buyer (người mua quan tâm tính năng)
   - Geographic variants (US, UK, EU, APAC)
2. Mỗi persona: 2-3 câu mô tả context, role, priorities

### Bước 2 — Design Prompts (thiết kế prompts)
1. Tạo 4-8 commercial prompts:
   - "best [category] software"
   - "top [category] for [use case]"
   - "[category] comparison"
   - "recommend [category] for [persona need]"
2. Prompts phải generic enough để persona variation có effect

### Bước 3 — Run Audit (chạy kiểm toán)
1. Với mỗi (persona × prompt × model) combination:
   - Prefix user message với persona description
   - Run N=10 reruns (chạy lại)
   - Record all brand mentions trong response
2. Test trên multiple models (OpenAI, Anthropic, others)
3. Control: run same prompts WITHOUT persona prefix (baseline)

### Bước 4 — Extract Brand Mentions (trích xuất nhắc thương hiệu)
1. Dùng 2 LLM judges (khác nhau) để extract brand mentions
2. Intersection classification: chỉ đếm brand khi CẢ 2 judges agree
3. Consensus recommendation set = union of brands across N reruns
4. Track: brand name, frequency, context of mention

### Bước 5 — Compute Persona Effect (tính hiệu ứng persona)
1. Within-persona Jaccard: similarity giữa recommendation sets của cùng persona across reruns
2. Cross-persona Jaccard: similarity giữa recommendation sets của khác personas
3. Persona-shift effect Δ = cross-persona Jaccard - within-persona Jaccard
4. Stratify (phân tầng) theo brand prominence: L1 (leader), L3 (mid-market), L5 (niche)

### Bước 6 — Analyze & Act (phân tích & hành động)
1. Nếu Δ < -0.10 → persona conditioning substantial (đáng kể)
2. Identify (xác định) persona-sensitive brands vs persona-resistant brands
3. Design segment-targeted content cho persona-sensitive brands
4. Re-run audit periodically (định kỳ) để track temporal drift (trôi thời gian)

## Output mong đợi
- Brand visibility score per persona segment
- Persona-shift effect size (Δ)
- List of persona-sensitive vs persona-resistant brands
- Actionable content strategy recommendations

## Ví dụ áp dụng
**Tình huống**: CRM company muốn audit brand visibility trên AI chatbots. Brands: Salesforce (L1 leader), HubSpot (L1), Freshworks (L3 mid-market), Pipedrive (L3 mid-market).

**Áp dụng**:
1. Personas: startup founder, enterprise VP, UK SMB owner, budget-conscious, feature-focused
2. Prompts: "best CRM software", "top CRM for small business", "CRM comparison"
3. Run 10 reruns per (persona × prompt × model) trên OpenAI + Anthropic
4. Results: Salesforce 80% consistency across personas (persona-resistant). Freshworks 25% consistency, 75% swap (persona-sensitive)
5. Action: Freshworks tạo segment-targeted pages: "Best CRM for Startups", "Best CRM for Enterprise" thay vì 1 generic page

## Lưu ý quan trọng
1. **Jaccard metric limitation**: Chỉ measure set similarity, không capture ranking order. Brand #1 vs Brand #5 có same Jaccard contribution
2. **Temporal drift**: Persona effects có thể change theo thời gian khi models update → re-run quarterly (hàng quý)
3. **Non-English personas**: Audit chỉ English → global brands cần test thêm với non-English personas
4. **Retrieval vs priors**: Models dùng retrieval nhiều hơn → persona effect nhỏ hơn. Check model architecture khi interpret results
5. **Sample size**: N=10 reruns minimum. N=30+ cho tighter confidence intervals
6. **Judge agreement**: Nếu 2 judges disagree nhiều (>30%) → extraction quality thấp, cần refine prompts
