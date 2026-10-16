# Skill: adcoevo-co-evolving-multi-agent-advertising
Source: 2610.19454v1
Type: framework

## Khi nào dùng skill này
- Xây hệ thống quảng cáoDelivery (advertising delivery) cho doanh nghiệp.
- Muốn hệ thống quảng cáo tự thích ứng (co-evolve) với thị trường và hành vi người dùng.
- Cần giảm chi phí quảng cáo (CPA) và tăng giá trị cho nhà quảng cáo (ADV).

## Tình huống KHÔNG nên dùng
- Không có hệ thống quảng cáoDelivery.
- Chỉ cần quy tắc tĩnh (static rules) cho quảng cáo, không cần agent tự thích ứng.

## Input cần có
- Dữ liệu quảng cáoDelivery (người dùng, quảng cáo, kết quả, chi phí).
- Các agent LLM có thể phát triển cùng nhau (co-evolve).
- Cơ chế reinforcement learning để tối ưu hóa tham số và chiến lược.

## Các bước thực hiện
1. Xây hệ thống đa đại lý (multi-agent) cho quảng cáoDelivery, với các agent phụ trách các vai trò khác nhau (planner, optimizer, inspector, v.v.).
2. Dùng reinforcement learning để tối ưu hóa các tham số và chiến lược quảng cáo theo thời gian.
3. Thêm agent Inspector để giám sát và điều chỉnh các quyết định của các agent khác.
4. Dùng mô hình nhỏ (API cost thấp) để giảm chi phí vận hành.
5. Theo dõi ADV (advertiser value) và CPA (cost per acquisition) để điều chỉnh hệ thống.

## Output mong đợi
- ADV tăng 14.02%, CPA giảm 7.07% (vs Rule, Sparse).
- ADV tăng 3.96%, CPA giảm 1.24% (vs multi-agent fixed parameters).
- API cost thấp hơn 65.59% so với Gemini-3.1-Flash-Lite.

## Ví dụ áp dụng
Solopreneur chạy hệ thống quảng cáo sản phẩm trên nền tảng electronic commerce: xây hệ thống đa đại lý co-evolve, với agent lập kế hoạch quảng cáo, agent tối ưu hóa giá, agent giám sát (Inspector) kiểm tra kết quả. Dùng mô hình nhỏ để giảm chi phí API. Hệ thống tự thích ứng với thị trường và hành vi người dùng, tăng giá trị quảng cáo và giảm chi phí mỗi lượt mua hàng.

## Gotchas
- Cần hệ thống đa đại lý co-evolve, không dùng quy tắc tĩnh.
- Cần agent Inspector để giám sát và điều chỉnh, không chỉ để các agent hoạt động độc lập.
- Cần dữ liệu quảng cáo thật để huấn luyện và tối ưu hóa hệ thống.
