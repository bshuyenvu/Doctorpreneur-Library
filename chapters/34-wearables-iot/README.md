# 34 — Thiết bị đeo và IoT y tế

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Thiết kế chuỗi dữ liệu cảm biến đáng tin cậy.
> **Sản phẩm của chương:** Sensor data plan.

---

## 1. Tóm tắt điều hành

Thiết bị đeo và IoT y tế tạo dòng dữ liệu sinh lý liên tục, mở ra theo dõi từ xa và phát hiện sớm. Nhưng giá trị lâm sàng phụ thuộc *chất lượng và độ tin cậy* của chuỗi dữ liệu từ cảm biến tới quyết định: độ chính xác cảm biến, xử lý nhiễu, dữ liệu thiếu, và diễn giải lâm sàng. Đầu ra là *sensor data plan*: kế hoạch bảo đảm chuỗi dữ liệu cảm biến đủ tin cậy để dùng lâm sàng, gồm validation, xử lý tín hiệu và quản lý cảnh báo.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu chuỗi từ cảm biến tới quyết định và các điểm sai lệch; (b) đánh giá độ chính xác và độ tin cậy cảm biến; (c) thiết kế xử lý dữ liệu thiếu/nhiễu và quản lý cảnh báo; (d) phác sensor data plan gắn giá trị lâm sàng.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Dữ liệu cảm biến kém tin cậy dẫn tới cảnh báo giả (alarm fatigue) hoặc bỏ sót — cả hai đều nguy hiểm. Là bác sĩ, bạn đánh giá được ý nghĩa lâm sàng của tín hiệu và ngưỡng cảnh báo hợp lý, lợi thế mà giải pháp thuần kỹ thuật thường thiếu.

## 4. Khái niệm cốt lõi và định nghĩa

**Cảm biến (sensor):** thiết bị đo tín hiệu sinh lý. **Signal-to-noise:** tỉ lệ tín hiệu/nhiễu. **Data pipeline:** chuỗi thu–truyền–xử lý–lưu–hiển thị. **Alarm fatigue:** mệt mỏi do cảnh báo quá nhiều. **Validation cảm biến:** chứng minh độ chính xác so với chuẩn. **Edge vs cloud:** xử lý tại thiết bị hay đám mây.

## 5. Khung tư duy nền tảng

Truy chuỗi dữ liệu end-to-end và xác định điểm sai lệch tại mỗi khâu: cảm biến (độ chính xác), truyền (mất gói/kết nối), xử lý (thuật toán, nhiễu), diễn giải (ngưỡng lâm sàng). Thiết kế quản lý cảnh báo để tối ưu tỉ lệ đúng và giảm alarm fatigue. Nguyên tắc: độ tin cậy chuỗi = mắt xích yếu nhất; validation phải trên toàn chuỗi, không chỉ cảm biến.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Ở tuyến cơ sở, IoT y tế hữu ích cho theo dõi bệnh mạn và cảnh báo sớm, nhưng vướng hạ tầng kết nối, chi phí thiết bị và bảo trì. Thiết kế phải tính mất kết nối, nguồn điện và bảo trì thực tế. Thiết bị đo phục vụ quyết định lâm sàng có thể là thiết bị y tế (chương 20).

## 7. Các bên liên quan

Bệnh nhân (đeo thiết bị), bác sĩ/điều dưỡng (nhận cảnh báo), CNTT (hạ tầng, bảo mật), và kỹ thuật thiết bị. Ai xử lý cảnh báo và quy trình đáp ứng phải rõ — cảnh báo không người xử lý là vô nghĩa hoặc nguy hiểm.

## 8. Quy trình từng bước

1. **Vẽ chuỗi dữ liệu** từ cảm biến tới quyết định.
2. **Đánh giá độ chính xác cảm biến** so chuẩn (validation).
3. **Thiết kế xử lý nhiễu/dữ liệu thiếu/mất kết nối.**
4. **Thiết kế quản lý cảnh báo** (ngưỡng, ưu tiên, giảm alarm fatigue).
5. **Xác định quy trình đáp ứng** cảnh báo và trách nhiệm.
6. **Gắn giá trị lâm sàng** và kế hoạch bằng chứng.

## 9. Công cụ và template áp dụng

- **Sensor data plan:** chuỗi dữ liệu · validation · xử lý nhiễu/thiếu · quản lý cảnh báo · quy trình đáp ứng · bảo mật.
- **Alarm management matrix** (ngưỡng · ưu tiên · người xử lý).
- **Data quality checklist.**

## 10. Ví dụ minh họa

Theo dõi dấu hiệu sinh tồn tại nhà. Sensor data plan: validation cảm biến so chuẩn; xử lý mất kết nối (đệm dữ liệu, cảnh báo mất tín hiệu); ngưỡng cảnh báo hiệu chỉnh theo lâm sàng để tránh alarm fatigue; quy trình rõ ai nhận và xử lý cảnh báo trong bao lâu. Ngưỡng và độ chính xác phải từ dữ liệu thật, không giả định.

## 11. Sai lầm thường gặp

- **Tin dữ liệu cảm biến chưa validation.**
- **Bỏ qua mất kết nối/dữ liệu thiếu.**
- **Ngưỡng cảnh báo gây alarm fatigue.**
- **Cảnh báo không có quy trình đáp ứng.**
- **Bỏ qua bảo mật/quyền riêng tư dữ liệu liên tục.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Cảnh báo giả gây alarm fatigue và bỏ sót; bỏ sót thật gây hại. Thiết kế phải cân bằng có căn cứ lâm sàng. Dữ liệu sinh lý liên tục rất nhạy cảm — bảo mật và cơ sở pháp lý (chương 40). Thiết bị phục vụ quyết định lâm sàng chịu quản lý thiết bị y tế (chương 20). Không hứa "phát hiện sớm" khi chưa có bằng chứng.

## 13. Chỉ số đo lường

Độ chính xác cảm biến (so chuẩn), tỉ lệ dữ liệu thiếu/mất kết nối, tỉ lệ cảnh báo đúng/giả, thời gian đáp ứng cảnh báo, và kết cục lâm sàng. Ưu tiên chỉ số an toàn và độ tin cậy.

## 14. Bằng chứng và mức độ tin cậy

Độ chính xác quảng cáo của thiết bị tiêu dùng **không tự động đủ cho dùng lâm sàng** — cần validation trong bối cảnh sử dụng. Giá trị "phát hiện sớm" cần bằng chứng (chương 25–30). Ghi rõ giới hạn cảm biến và điều kiện đo.

## 15. Tiêu chuẩn và guideline liên quan

Gắn quản lý thiết bị y tế (chương 20), quản lý rủi ro/alarm (chương 24), bảo mật/privacy (chương 39–40), FHIR cho dữ liệu (chương 36), MLOps nếu có mô hình (chương 50). Tham chiếu tiêu chuẩn an toàn thiết bị và quản lý cảnh báo.

## 16. Liên hệ các chương khác

Mảnh của **31**; dữ liệu gắn **36, 54**; cảnh báo/CDS **38**; rủi ro **24**; thiết bị y tế **20**; bảo mật **39–40**.

## 17. Bài tập thực hành — Sensor data plan

Lập sensor data plan: vẽ chuỗi dữ liệu end-to-end, kế hoạch validation cảm biến, xử lý nhiễu/dữ liệu thiếu/mất kết nối, ma trận quản lý cảnh báo (ngưỡng, ưu tiên, người xử lý), quy trình đáp ứng, và bảo mật. Gắn giá trị lâm sàng và kế hoạch bằng chứng. Ghi rõ điều cần validation thực tế.

## 18. Checklist tự đánh giá

- [ ] Chuỗi dữ liệu được vẽ và đánh giá điểm sai lệch.
- [ ] Cảm biến có kế hoạch validation.
- [ ] Xử lý dữ liệu thiếu/mất kết nối.
- [ ] Quản lý cảnh báo giảm alarm fatigue.
- [ ] Cảnh báo có quy trình đáp ứng rõ.

## 19. Định nghĩa hoàn thành (Definition of Done)

Sensor data plan đạt chuẩn khi validation toàn chuỗi, xử lý dữ liệu thiếu/mất kết nối, quản lý cảnh báo cân bằng có căn cứ lâm sàng, quy trình đáp ứng rõ, và bảo mật dữ liệu liên tục.

## 20. Câu hỏi phản tư

Mắt xích yếu nhất trong chuỗi dữ liệu của tôi ở đâu? Cảm biến đã validation trong bối cảnh dùng chưa? Cảnh báo của tôi có gây alarm fatigue không? Ai xử lý cảnh báo và trong bao lâu?

## 21. Cạm bẫy quyết định

**Tin số quảng cáo cảm biến**, **ngưỡng cảnh báo tùy tiện**. Đối trọng: validation trong bối cảnh, ngưỡng hiệu chỉnh theo lâm sàng, và quy trình đáp ứng rõ.

## 22. Nguồn dữ liệu động cần xác minh

Độ chính xác cảm biến trong bối cảnh, ngưỡng lâm sàng, quy định thiết bị/dữ liệu — là dữ liệu động. Validation và tra nguồn chính thức; không dùng số quảng cáo.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md) và [Open source](../../resources/open-source-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Signal-to-noise:** tỉ lệ tín hiệu/nhiễu. **Data pipeline:** chuỗi dữ liệu. **Alarm fatigue:** mệt mỏi vì cảnh báo. **Edge/cloud:** xử lý tại thiết bị/đám mây. **Validation cảm biến:** chứng minh độ chính xác.

## 25. Tóm tắt và bước tiếp theo

Giá trị của wearables/IoT phụ thuộc độ tin cậy toàn chuỗi dữ liệu và quản lý cảnh báo có căn cứ lâm sàng, không phải số cảm biến quảng cáo. Tiếp theo sang **[chương 35 — EHR và khả năng liên thông](../35-ehr-interoperability/README.md)** để đưa dữ liệu vào hệ thống hồ sơ.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Độ chính xác thiết bị tiêu dùng không tự đủ cho lâm sàng; dữ liệu sinh lý liên tục cần bảo mật; thiết bị phục vụ quyết định lâm sàng chịu quản lý thiết bị y tế.
