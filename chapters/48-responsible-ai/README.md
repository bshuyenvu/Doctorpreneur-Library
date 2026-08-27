# 48 — AI có trách nhiệm

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Quản trị fairness, transparency và accountability.
> **Sản phẩm của chương:** Bản đánh giá AI có trách nhiệm (Responsible AI review).

---

## 1. Tóm tắt điều hành

AI có trách nhiệm (responsible AI) là quản trị ba trục xuyên suốt vòng đời sản phẩm: công bằng (fairness — hiệu năng không thiên lệch giữa các nhóm), minh bạch (transparency — người dùng hiểu được mô hình dựa trên gì và giới hạn ra sao), và trách nhiệm giải trình (accountability — luôn có người chịu trách nhiệm cho quyết định cuối). Dữ liệu huấn luyện AI y tế thường phản ánh bất bình đẳng sẵn có trong hệ thống chăm sóc sức khỏe — nếu không chủ động kiểm tra, AI sẽ khuếch đại chứ không giảm bất công đó. Đầu ra là *bản đánh giá AI có trách nhiệm*: tài liệu kiểm tra công bằng theo phân nhóm, đánh giá mức minh bạch phù hợp, và phân bổ trách nhiệm giải trình rõ ràng cho một hệ thống AI.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu thiên lệch dữ liệu/thuật toán và cách nó gây bất công y tế; (b) đánh giá mức minh bạch/giải thích được phù hợp từng đối tượng; (c) phân bổ trách nhiệm giải trình rõ ràng giữa người và AI; (d) lập bản đánh giá AI có trách nhiệm.

## 3. Vì sao chương này sống còn với Doctorpreneur

Thiên lệch AI thường ảnh hưởng nặng nhất lên nhóm bệnh nhân vốn đã yếu thế — vùng sâu vùng xa, người nghèo, người ít tiếp cận dịch vụ. Điều này vừa gây hại thực, vừa là rủi ro danh tiếng và pháp lý nghiêm trọng cho startup. Nhà đầu tư, đối tác bệnh viện và cơ quan quản lý ngày càng đòi hỏi bằng chứng quản trị AI có trách nhiệm, không chỉ hiệu năng kỹ thuật.

## 4. Khái niệm cốt lõi và định nghĩa

**Fairness (công bằng):** hiệu năng và lợi ích tương đương giữa các nhóm dân số. **Bias (thiên lệch):** sai lệch hệ thống trong dữ liệu hoặc thuật toán ưu ái/bất lợi một nhóm. **Representation bias:** thiên lệch do một nhóm bị đại diện thiếu trong dữ liệu huấn luyện. **Explainability/interpretability:** khả năng giải thích lý do đằng sau một dự báo. **Accountability:** trách nhiệm giải trình — ai chịu trách nhiệm khi có sai sót. **Disparate impact:** tác động bất lợi không cân xứng lên một nhóm.

## 5. Khung tư duy nền tảng

Công bằng không tự nhiên xuất hiện — phải chủ động đo và thiết kế. Đánh giá hiệu năng tách theo phân nhóm liên quan (giới, tuổi, vùng miền, tình trạng kinh tế xã hội, loại thiết bị) thay vì chỉ nhìn chỉ số tổng, vì chỉ số tổng có thể che giấu thất bại ở nhóm nhỏ nhưng dễ tổn thương. Minh bạch cần đúng đối tượng: bác sĩ cần hiểu cơ chế và giới hạn để dùng đúng, bệnh nhân cần hiểu đơn giản để đồng thuận có ý nghĩa. Trách nhiệm giải trình phải được gán rõ trước khi triển khai — "AI quyết định" không bao giờ là câu trả lời đầy đủ, luôn phải có một người chịu trách nhiệm cuối cùng.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Dữ liệu y tế sẵn có ở Việt Nam thường thiên về nhóm dễ tiếp cận dịch vụ — thành thị, có bảo hiểm, đến khám sớm — trong khi nhóm vùng sâu vùng xa, dân tộc thiểu số, hoặc đến khám muộn thường bị đại diện thiếu. Một mô hình AI huấn luyện trên dữ liệu như vậy có nguy cơ hiệu năng kém hơn đáng kể cho chính những nhóm cần hỗ trợ nhất. Trước khi triển khai rộng, cần chủ động kiểm tra hiệu năng theo các phân nhóm này, không giả định công bằng chỉ vì mô hình "trung tính về mặt kỹ thuật".

## 7. Các bên liên quan

Bác sĩ và người bệnh (đặc biệt nhóm dễ tổn thương), khoa học dữ liệu, chuyên gia đạo đức/pháp lý, và ban lãnh đạo chịu trách nhiệm cuối. Đánh giá công bằng và accountability cần góc nhìn lâm sàng lẫn kỹ thuật cùng lúc — thiếu một bên dễ bỏ sót rủi ro thực.

## 8. Quy trình từng bước

1. **Xác định phân nhóm cần kiểm tra công bằng** (giới, tuổi, vùng miền, kinh tế xã hội, loại thiết bị...).
2. **Đo hiệu năng theo từng phân nhóm** và so sánh chênh lệch.
3. **Đánh giá mức minh bạch/giải thích được** phù hợp từng đối tượng sử dụng.
4. **Phân bổ trách nhiệm giải trình** — ai quyết định cuối, ai chịu trách nhiệm khi sai.
5. **Thiết kế cơ chế phản hồi/khiếu nại** khi người dùng nghi ngờ kết quả.
6. **Lập bản đánh giá AI có trách nhiệm** và kế hoạch giám sát định kỳ.

## 9. Công cụ và template áp dụng

- **Checklist kiểm tra công bằng (fairness audit).**
- **Bảng hiệu năng theo phân nhóm** và mức chênh lệch chấp nhận được.
- **Ma trận trách nhiệm giải trình** (vai trò · quyết định · trách nhiệm).
- **Model card/factsheet minh bạch** cho người dùng.

## 10. Ví dụ minh họa

Mô hình sàng lọc nguy cơ được kiểm tra hiệu năng theo nhóm tuổi, giới và vùng miền. Kết quả phát hiện độ nhạy thấp hơn rõ rệt ở nhóm bệnh nhân vùng sâu do dữ liệu huấn luyện thiếu đại diện nhóm này. Đội ngũ bổ sung dữ liệu, ghi rõ giới hạn hiện tại trong tài liệu sản phẩm, và xác định bác sĩ là người quyết định cuối cùng — AI chỉ hỗ trợ ưu tiên, không tự động ra quyết định điều trị. Có kênh phản hồi để bác sĩ hoặc bệnh nhân báo cáo khi nghi ngờ kết quả sai.

## 11. Sai lầm thường gặp

- **Không kiểm tra hiệu năng theo phân nhóm**, chỉ báo cáo chỉ số tổng.
- **Hộp đen không giải thích được** trong bối cảnh cần minh bạch cao.
- **Trách nhiệm mơ hồ** — không ai thực sự chịu trách nhiệm khi AI sai.
- **Bỏ qua phản hồi từ người dùng** thực tế sau triển khai.
- **Giả định công bằng** chỉ vì không cố ý thiên lệch.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Thiên lệch AI gây bất công y tế thực sự và vi phạm nguyên tắc đạo đức cơ bản trong chăm sóc sức khỏe. Thiếu accountability rõ ràng gây khó khăn khi truy trách nhiệm nếu có sự cố, cả về pháp lý lẫn đạo đức nghề nghiệp. Nhiều khung pháp lý và guideline quốc tế đang bắt đầu yêu cầu đánh giá công bằng và minh bạch cho AI y tế trước khi lưu hành — đây là xu hướng, không phải lựa chọn.

## 13. Chỉ số đo lường

Chênh lệch hiệu năng giữa các phân nhóm (độ nhạy, độ đặc hiệu, tỷ lệ dương giả), mức độ minh bạch/giải thích được đánh giá bởi người dùng thực tế, tỷ lệ khiếu nại/phản hồi được ghi nhận và xử lý, và mức độ rõ ràng của accountability trong tài liệu sản phẩm.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng tổng thể tốt **không đảm bảo công bằng theo phân nhóm** — phải đo trực tiếp, không suy luận. Tuyên bố "AI không thiên lệch" cần bằng chứng đo lường cụ thể, không phải mặc định vì thuật toán "trung lập về mặt kỹ thuật". Ghi rõ phân nhóm nào chưa được kiểm tra đầy đủ.

## 15. Tiêu chuẩn và guideline liên quan

Gắn thẩm định AI (chương 47), quản lý rủi ro (chương 24), quyền riêng tư và quản trị dữ liệu (chương 40), tác động–đạo đức–bền vững (chương 65), và giám sát công bằng liên tục trong MLOps (chương 50).

## 16. Liên hệ các chương khác

Xuyên suốt toàn nhánh AI **41–50**; gắn thẩm định **47**; đạo đức và tác động xã hội **65**; quản lý rủi ro **24**; dữ liệu **40**.

## 17. Bài tập thực hành — Bản đánh giá AI có trách nhiệm

Lập bản đánh giá AI có trách nhiệm cho một mô hình: xác định phân nhóm cần kiểm tra, đo (hoặc lên kế hoạch đo) chênh lệch hiệu năng, đánh giá mức minh bạch cần thiết cho từng đối tượng, xây ma trận trách nhiệm giải trình, và thiết kế cơ chế phản hồi. Nêu rõ phân nhóm chưa được kiểm tra và kế hoạch bổ sung.

## 18. Checklist tự đánh giá

- [ ] Hiệu năng được đo tách theo các phân nhóm liên quan.
- [ ] Mức minh bạch/giải thích được phù hợp từng đối tượng sử dụng.
- [ ] Trách nhiệm giải trình được phân bổ rõ, có người chịu trách nhiệm cuối.
- [ ] Có cơ chế phản hồi/khiếu nại khi nghi ngờ kết quả.
- [ ] Không giả định công bằng mà chưa đo lường.

## 19. Định nghĩa hoàn thành (Definition of Done)

Bản đánh giá AI có trách nhiệm đạt chuẩn khi đo được chênh lệch hiệu năng theo phân nhóm, xác định mức minh bạch phù hợp, phân bổ accountability rõ ràng, có cơ chế phản hồi hoạt động, và nêu rõ giới hạn chưa được kiểm tra đầy đủ.

## 20. Câu hỏi phản tư

Tôi đã kiểm tra hiệu năng AI của mình theo phân nhóm nào chưa? Người dùng có hiểu đủ về giới hạn của hệ thống để dùng đúng cách không? Nếu AI sai, ai là người chịu trách nhiệm — điều đó có rõ ràng với mọi người liên quan không? Tôi có kênh nào để phát hiện thiên lệch mới phát sinh sau triển khai?

## 21. Cạm bẫy quyết định

**Giả định công bằng mặc định**, **hộp đen không giải thích được**, **trách nhiệm mơ hồ**. Đối trọng: kiểm tra công bằng có kỷ luật, minh bạch đúng đối tượng, và ma trận trách nhiệm rõ ràng trước khi triển khai.

## 22. Nguồn dữ liệu động cần xác minh

Quy định và guideline về AI có trách nhiệm trong y tế đang phát triển nhanh ở nhiều quốc gia — là dữ liệu động. Tra nguồn chính thức và cập nhật định kỳ; ghi ngày kiểm tra.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md) và [Thư viện SOP](../../resources/sop-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Fairness:** công bằng. **Bias:** thiên lệch. **Explainability:** khả năng giải thích. **Accountability:** trách nhiệm giải trình. **Disparate impact:** tác động bất cân xứng.

## 25. Tóm tắt và bước tiếp theo

AI có trách nhiệm đòi hỏi chủ động kiểm tra công bằng theo phân nhóm, minh bạch đúng đối tượng, và phân bổ trách nhiệm giải trình rõ ràng — công bằng không tự nhiên xuất hiện, phải được thiết kế. Tiếp theo sang **[chương 49 — Tương tác người–AI](../49-human-ai-interaction/README.md)** để thiết kế giao diện và phân bổ trách nhiệm phù hợp trong thực hành hằng ngày.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục, không thay tư vấn đạo đức hoặc pháp lý chuyên môn. Công bằng AI phải được đo lường, không giả định; luôn cần một người chịu trách nhiệm giải trình cuối cùng cho quyết định có sự hỗ trợ của AI.
