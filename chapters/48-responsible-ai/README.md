# 48 — AI có trách nhiệm

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Quản trị fairness, transparency và accountability.
> **Sản phẩm của chương:** Responsible AI checklist.

---

## 1. Tóm tắt điều hành

AI có trách nhiệm bảo đảm hệ thống AI công bằng, minh bạch, an toàn và có trách nhiệm giải trình. Trong y tế, đây không phải "điểm cộng đạo đức" mà là điều kiện an toàn: AI thiên lệch có thể khuếch đại bất bình đẳng sức khỏe; AI thiếu minh bạch làm bác sĩ khó giám sát. Đầu ra là *responsible AI checklist*: danh mục kiểm soát về công bằng, minh bạch, trách nhiệm và giám sát áp dụng suốt vòng đời AI.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu các trụ cột của responsible AI (fairness, transparency, accountability, safety); (b) nhận diện và đo thiên lệch; (c) thiết kế minh bạch và phân bổ trách nhiệm; (d) phác responsible AI checklist.

## 3. Vì sao chương này sống còn với Doctorpreneur

AI thiên lệch trong y tế gây hại thật cho nhóm yếu thế và vi phạm y đức. Trách nhiệm giải trình rõ (ai chịu trách nhiệm khi AI sai) là điều kiện triển khai an toàn. Doctorpreneur có nghĩa vụ đạo đức đặt điều này lên trước tốc độ.

## 4. Khái niệm cốt lõi và định nghĩa

**Fairness:** công bằng, không thiên lệch có hại theo nhóm. **Bias:** thiên lệch (dữ liệu, mô hình, triển khai). **Transparency/explainability:** minh bạch/giải thích được. **Accountability:** trách nhiệm giải trình. **Health equity:** công bằng sức khỏe. **Contestability:** khả năng chất vấn/khiếu nại quyết định AI.

## 5. Khung tư duy nền tảng

Áp bốn trụ cột suốt vòng đời: (1) *fairness* — đo hiệu năng theo nhóm (giới, tuổi, dân tộc, kinh tế) và giảm chênh lệch có hại; (2) *transparency* — minh bạch về dữ liệu, giới hạn, và cơ sở khuyến nghị; (3) *accountability* — xác định rõ ai chịu trách nhiệm ở mỗi khâu, có cơ chế chất vấn; (4) *safety* — gắn quản lý rủi ro (chương 24) và oversight. Nguyên tắc: công bằng phải đo, không giả định; minh bạch phục vụ giám sát của con người, không phải để hợp thức hóa.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Dữ liệu huấn luyện thường thiếu đại diện nhóm yếu thế/vùng khó khăn, dễ tạo AI kém công bằng khi triển khai tuyến cơ sở. Cần đo hiệu năng theo nhóm địa phương và cân nhắc tác động tới tiếp cận công bằng. Không triển khai AI làm tăng bất bình đẳng sức khỏe.

## 7. Các bên liên quan

Bác sĩ, người bệnh (đặc biệt nhóm yếu thế), khoa học dữ liệu, lãnh đạo, và hội đồng đạo đức. Tiếng nói của nhóm chịu ảnh hưởng cần được đưa vào thiết kế và đánh giá.

## 8. Quy trình từng bước

1. **Xác định nhóm liên quan** và rủi ro công bằng.
2. **Đo thiên lệch** (hiệu năng theo nhóm) và tìm nguồn.
3. **Giảm thiểu thiên lệch** (dữ liệu, mô hình, ngưỡng).
4. **Thiết kế minh bạch** (giới hạn, cơ sở khuyến nghị, cảnh báo bất định).
5. **Xác định trách nhiệm giải trình** và cơ chế chất vấn.
6. **Lập responsible AI checklist** và giám sát vòng đời.

## 9. Công cụ và template áp dụng

- **Responsible AI checklist:** fairness · transparency · accountability · safety · giám sát.
- **Bias audit table** (hiệu năng theo nhóm).
- **Model card / datasheet** (mô tả mô hình, dữ liệu, giới hạn).

## 10. Ví dụ minh họa

AI sàng lọc nguy cơ. Bias audit cho thấy hiệu năng thấp hơn ở một nhóm do thiếu dữ liệu — cần bổ sung dữ liệu/hiệu chỉnh trước triển khai. Model card công bố dữ liệu huấn luyện, giới hạn và nhóm chưa đủ bằng chứng. Trách nhiệm: bác sĩ giữ quyết định cuối; có kênh để người bệnh chất vấn. Không triển khai cho nhóm mà mô hình chưa công bằng.

## 11. Sai lầm thường gặp

- **Giả định công bằng** thay vì đo theo nhóm.
- **Minh bạch hình thức** không giúp giám sát.
- **Trách nhiệm mờ** khi AI sai.
- **Bỏ qua nhóm yếu thế/thiếu dữ liệu.**
- **Coi responsible AI là việc làm cuối.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

AI thiên lệch gây hại và bất công — vi phạm y đức và có thể pháp lý. Thiếu trách nhiệm giải trình khiến sai sót không ai chịu. Minh bạch và contestability là quyền của người bệnh. An toàn và công bằng không đánh đổi vì hiệu năng hay tốc độ. Đây là chương đạo đức trung tâm của nhánh AI.

## 13. Chỉ số đo lường

Chênh lệch hiệu năng giữa các nhóm (fairness gap), độ phủ minh bạch (model card, giới hạn công bố), rõ ràng trách nhiệm, và số khiếu nại/chất vấn được xử lý. Giám sát công bằng liên tục vì drift có thể làm lệch.

## 14. Bằng chứng và mức độ tin cậy

Công bằng phải **đo bằng dữ liệu theo nhóm**, không tuyên bố suông. Không có định nghĩa fairness duy nhất — nêu rõ tiêu chí dùng và đánh đổi. Minh bạch về giới hạn là một phần của tính trung thực. Ghi rõ nhóm chưa đủ bằng chứng.

## 15. Tiêu chuẩn và guideline liên quan

Tham chiếu nguyên tắc AI có trách nhiệm/đáng tin của các tổ chức quốc tế (ví dụ WHO về AI y tế) và quy định AI khi áp dụng. Gắn quản lý rủi ro (chương 24), validation (chương 47), human–AI (chương 49), privacy (chương 40).

## 16. Liên hệ các chương khác

Xuyên suốt nhánh AI **41–50**; gắn rủi ro **24**, validation **47**, tương tác người–AI **49**, đạo đức chung **65**, dữ liệu **40**.

## 17. Bài tập thực hành — Responsible AI checklist

Lập responsible AI checklist cho một hệ AI: xác định nhóm và rủi ro công bằng, thiết kế bias audit (hiệu năng theo nhóm), kế hoạch giảm thiên lệch, thiết kế minh bạch (model card, công bố giới hạn), phân bổ trách nhiệm và cơ chế chất vấn, và giám sát công bằng vòng đời. Ghi rõ nhóm chưa đủ bằng chứng.

## 18. Checklist tự đánh giá

- [ ] Đo hiệu năng theo nhóm (không giả định công bằng).
- [ ] Có kế hoạch giảm thiên lệch.
- [ ] Minh bạch giới hạn phục vụ giám sát.
- [ ] Trách nhiệm giải trình rõ.
- [ ] Giám sát công bằng liên tục.

## 19. Định nghĩa hoàn thành (Definition of Done)

Responsible AI checklist đạt chuẩn khi đo và giảm thiên lệch theo nhóm, minh bạch giới hạn qua model card, xác định trách nhiệm và cơ chế chất vấn, và giám sát công bằng suốt vòng đời.

## 20. Câu hỏi phản tư

AI của tôi công bằng với nhóm nào và kém với nhóm nào? Ai chịu trách nhiệm khi nó sai? Người bệnh có chất vấn được không? Tôi có đang làm tăng bất bình đẳng sức khỏe không?

## 21. Cạm bẫy quyết định

**Giả định công bằng**, **minh bạch hình thức**, **trách nhiệm mờ**. Đối trọng: bias audit theo nhóm, model card trung thực, và phân bổ trách nhiệm rõ.

## 22. Nguồn dữ liệu động cần xác minh

Nguyên tắc/quy định AI có trách nhiệm, dữ liệu đại diện nhóm — là dữ liệu động. Tra nguồn chính thức và đo thực tế; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md). Nguyên tắc/quy định tra tại nguồn chính thức.

## 24. Thuật ngữ

**Fairness:** công bằng. **Bias:** thiên lệch. **Transparency/explainability:** minh bạch/giải thích. **Accountability:** trách nhiệm giải trình. **Contestability:** khả năng chất vấn. **Model card:** thẻ mô tả mô hình.

## 25. Tóm tắt và bước tiếp theo

AI có trách nhiệm — công bằng đo được, minh bạch phục vụ giám sát, trách nhiệm rõ, an toàn ưu tiên — là điều kiện đạo đức và an toàn để triển khai. Tiếp theo sang **[chương 49 — Tương tác người–AI](../49-human-ai-interaction/README.md)** cho thiết kế giao diện và phân bổ trách nhiệm.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. AI thiên lệch gây hại và bất công — công bằng phải đo theo nhóm; minh bạch và trách nhiệm giải trình là quyền của người bệnh; an toàn/công bằng không đánh đổi vì tốc độ.
