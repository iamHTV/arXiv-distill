# [2610.19454v1] AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System

## Problem
Quảng cáo số (digital advertising) là một hệ thống phức tạp với nhiều yếu tố tương tác. Các hệ thống quảng cáo hiện tại thường dùng các mô hình tĩnh hoặc quy tắc cứng, không thể tự thích ứng (co-evolve) với sự thay đổi của thị trường và hành vi người dùng.

## Contribution
- Giới thiệu AdCoEvo: một multi-agent hệ thống quảng cáoDelivery共同 phát triển (co-evolving) với khả năng tự thích ứng.
- AdCoEvo increases advertiser value (ADV) by 14.02% while reducing cost per acquisition (CPA) by 7.07% (vs Rule, Sparse environment).
- Compared with a multi-agent system with fixed parameters, AdCoEvo increases ADV by 3.96% and reduces CPA by 1.24%.
- Adding Inspector increases ADV by 4.95% and reduces CPA by 9.57% relative to Planner–Optimizer.
- Average API cost: CNY 0.235 per period, 65.59% lower than Gemini-3.1-Flash-Lite.
- Even when budget reduced to 60%, AdCoEvo increases ADV by 7.17% and reduces CPA by 0.78% relative to AdCoEvo (Fixed).

## Method (tóm cốt lõi)
AdCoEvo là một hệ thống đa đại lý (multi-agent) cho quảng cáoDelivery, với các agent phụ trách các vai trò khác nhau (planner, optimizer, inspector, v.v.) và cùng phát triển (co-evolve) với thời gian. Hệ thống sử dụng reinforcement learning để tối ưu hóa các tham số và chiến lược quảng cáo.

## Key Findings
- AdCoEvo: ADV +14.02%, CPA -7.07% (vs Rule, Sparse).
- AdCoEvo (Fixed): ADV +3.96%, CPA -1.24% (vs multi-agent fixed parameters).
- General environment: ADV +4.22%, CPA -2.21%.
- Adding Inspector: ADV +4.95%, CPA -9.57% (vs Planner–Optimizer).
- Average API cost: CNY 0.235 per period, 65.59% lower than Gemini-3.1-Flash-Lite.
- Budget 60%: ADV +7.17%, CPA -0.78% (vs AdCoEvo Fixed).

## Actionable Insights
- Dùng hệ thống đa đại lý co-evolving (cùng phát triển) cho quảng cáoDelivery thay vì quy tắc tĩnh. Áp dụng: solopreneur chạy hệ thống quảng cáo nên dùng agent co-evolve để tự thích ứng với thị trường, không dùng quy tắc cứng.
- Thêm agent Inspector (giám sát kiểm tra) giúp tăng ADV và giảm CPA đáng kể. Áp dụng: khi xây hệ thống quảng cáo bằng agent, hãy thêm một agent giám sát để kiểm tra và điều chỉnh các quyết định của các agent khác.
- Dùng mô hình nhỏ (API cost CNY 0.235, 65.59% thấp hơn Gemini-3.1-Flash-Lite) giúp giảm chi phí vận hành. Áp dụng: khi xây hệ thống quảng cáo, hãy dùng mô hình nhỏ phù hợp thay vì mô hình lớn đắt tiền.

## Assumptions & Limitations
- Điều kiện: có hệ thống quảng cáoDelivery và dữ liệu thị trường thật; không áp dụng nếu không có dữ liệu thật.
- Paper thừa nhận: đánh giá trên các môi trường Sparse và General; có thể khác trên các môi trường khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen khác ngoài quảng cáo, chưa test chi phí thực tế của việc duy trì hệ thống co-evolve.

## Metadata
- Năm: 2026
- Tác giả: Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu (CAS, UCAS, USyd, JD.COM)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.19454
