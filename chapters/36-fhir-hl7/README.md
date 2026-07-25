# 36 — FHIR, HL7 và API y tế

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Mô hình hóa tài nguyên và trao đổi dữ liệu.
> **Sản phẩm của chương:** FHIR resource map.

---

## 1. Tóm tắt điều hành

FHIR (Fast Healthcare Interoperability Resources) và HL7 là các chuẩn trao đổi dữ liệu y tế. FHIR — chuẩn dựa API và tài nguyên (resource) hiện đại — là lựa chọn ưu tiên cho tích hợp mới vì dễ dùng và mở. Founder không cần thành kỹ sư chuẩn, nhưng phải mô hình hóa được dữ liệu sản phẩm theo tài nguyên FHIR để tích hợp. Đầu ra là *FHIR resource map*: ánh xạ dữ liệu sản phẩm sang các tài nguyên FHIR và luồng API trao đổi.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu mô hình resource của FHIR và vai trò HL7; (b) ánh xạ dữ liệu sản phẩm sang tài nguyên FHIR; (c) hiểu profiles và bộ mã (terminology); (d) phác FHIR resource map và luồng API.

## 3. Vì sao chương này sống còn với Doctorpreneur

FHIR là "ngôn ngữ chung" ngày càng phổ biến để liên thông. Thiết kế dữ liệu theo FHIR từ đầu giảm chi phí tích hợp và tăng khả năng kết nối nhiều hệ thống — tránh phải làm lại khi mở rộng.

## 4. Khái niệm cốt lõi và định nghĩa

**HL7:** tổ chức và bộ chuẩn trao đổi dữ liệu y tế (gồm v2, CDA, FHIR). **FHIR:** chuẩn hiện đại dựa resource + REST API. **Resource:** đơn vị dữ liệu FHIR (Patient, Observation, Condition, Encounter...). **Profile:** ràng buộc/tùy biến resource cho ngữ cảnh. **Terminology:** bộ mã (LOINC, SNOMED, ICD) gắn ý nghĩa. **RESTful API:** giao diện trao đổi theo chuẩn web.

## 5. Khung tư duy nền tảng

Mô hình hóa dữ liệu sản phẩm theo resource FHIR chuẩn thay vì cấu trúc riêng: ánh xạ từng thực thể (bệnh nhân, quan sát, chẩn đoán) sang resource tương ứng, gắn bộ mã cho ngữ nghĩa, và dùng profile khi cần tùy biến. Ưu tiên API RESTful, bảo mật (OAuth/định danh). Nguyên tắc: theo chuẩn nhiều nhất có thể, tùy biến ít nhất cần thiết — tùy biến quá mức phá vỡ tính liên thông.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Mức áp dụng FHIR ở các HIS Việt Nam không đồng đều; nhiều hệ thống dùng chuẩn cũ hoặc định dạng riêng. Cần khảo sát khả năng thực tế của hệ thống đích (chương 35). Chính sách chuẩn dữ liệu y tế là dữ liệu động — tra văn bản hiện hành. Thiết kế theo FHIR vẫn đáng làm để sẵn sàng cho tương lai liên thông.

## 7. Các bên liên quan

Kỹ sư tích hợp, CNTT bệnh viện, nhà cung HIS, và chuyên gia terminology. Ánh xạ ngữ nghĩa (bộ mã) cần đầu vào lâm sàng để đúng ý nghĩa — sai mã là rủi ro an toàn (chương 35).

## 8. Quy trình từng bước

1. **Liệt kê thực thể dữ liệu** của sản phẩm.
2. **Ánh xạ sang resource FHIR** phù hợp.
3. **Gắn bộ mã** (LOINC/SNOMED/ICD) cho ngữ nghĩa.
4. **Xác định profile** nếu cần tùy biến.
5. **Thiết kế luồng API** (đọc/ghi, bảo mật, phân quyền).
6. **Phác FHIR resource map** và kế hoạch kiểm thử tích hợp.

## 9. Công cụ và template áp dụng

- **FHIR resource map:** thực thể · resource · bộ mã · profile · thao tác API.
- **API contract** (endpoint, quyền, bảo mật).
- **Terminology mapping table.**

## 10. Ví dụ minh họa

Công cụ CDS đọc kết quả xét nghiệm và ghi khuyến nghị. Resource map: kết quả → Observation (gắn LOINC), chẩn đoán → Condition (gắn ICD/SNOMED), khuyến nghị → resource phù hợp. Luồng API: đọc Observation qua REST có phân quyền, ghi kết quả với truy vết. Ánh xạ mã cần validation lâm sàng; khả năng FHIR của HIS đích phải xác minh.

## 11. Sai lầm thường gặp

- **Tùy biến quá mức**, phá liên thông.
- **Bỏ terminology**, mất ngữ nghĩa.
- **Giả định HIS hỗ trợ FHIR** mà chưa kiểm.
- **API thiếu bảo mật/phân quyền.**
- **Ánh xạ mã sai** gây rủi ro lâm sàng.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Ánh xạ ngữ nghĩa sai (mã sai) có thể dẫn tới sai lệch lâm sàng — validation là vấn đề an toàn. API trao đổi dữ liệu bệnh nhân cần xác thực, phân quyền, mã hóa và truy vết (chương 39–40). Tuân quy định dữ liệu y tế và cơ sở pháp lý trao đổi.

## 13. Chỉ số đo lường

Tỉ lệ dữ liệu ánh xạ đúng resource/bộ mã, độ tuân chuẩn (validation FHIR), độ tin cậy API, và mức tái sử dụng khi tích hợp hệ thống mới. Theo dõi lỗi ánh xạ và tích hợp.

## 14. Bằng chứng và mức độ tin cậy

Chi tiết resource, profile và phiên bản FHIR do chuẩn quy định và **cập nhật theo thời gian — tra bản chuẩn hiện hành**. Khả năng hỗ trợ của từng HIS phải xác minh thực tế. Chương nêu nguyên tắc mô hình hóa, không thay tài liệu chuẩn.

## 15. Tiêu chuẩn và guideline liên quan

FHIR, HL7 v2/CDA, bộ mã LOINC/SNOMED/ICD. Gắn interoperability (chương 35), bảo mật (chương 39), privacy (chương 40), data engineering (chương 54). Tuân quy định chuẩn dữ liệu y tế trong nước.

## 16. Liên hệ các chương khác

Chi tiết hóa **35**; nền dữ liệu cho **38** (CDS), **54** (data engineering), **41–47** (AI dùng dữ liệu); bảo mật **39–40**.

## 17. Bài tập thực hành — FHIR resource map

Lập FHIR resource map: liệt kê thực thể dữ liệu sản phẩm, ánh xạ sang resource FHIR, gắn bộ mã cho ngữ nghĩa, xác định profile nếu cần, và thiết kế luồng API (thao tác, bảo mật, phân quyền). Nêu ràng buộc khả năng FHIR của hệ thống đích cần xác minh. Có validation ánh xạ với lâm sàng.

## 18. Checklist tự đánh giá

- [ ] Dữ liệu ánh xạ sang resource FHIR chuẩn.
- [ ] Bộ mã gắn cho ngữ nghĩa.
- [ ] Tùy biến tối thiểu (giữ liên thông).
- [ ] API có bảo mật và phân quyền.
- [ ] Ánh xạ mã được validation lâm sàng.

## 19. Định nghĩa hoàn thành (Definition of Done)

FHIR resource map đạt chuẩn khi ánh xạ dữ liệu sang resource chuẩn với bộ mã, tùy biến tối thiểu qua profile, thiết kế API an toàn/phân quyền, và validation ánh xạ ngữ nghĩa.

## 20. Câu hỏi phản tư

Dữ liệu của tôi có ánh xạ sạch sang FHIR không? Tôi có giữ ngữ nghĩa bằng bộ mã chuẩn không? HIS đích thực sự hỗ trợ FHIR đến đâu? Ánh xạ mã đã được kiểm chứng an toàn chưa?

## 21. Cạm bẫy quyết định

**Tùy biến quá mức**, **giả định hỗ trợ FHIR**. Đối trọng: theo chuẩn tối đa, khảo sát HIS thực tế, và validation terminology.

## 22. Nguồn dữ liệu động cần xác minh

Phiên bản FHIR, profile, bộ mã cập nhật, khả năng hỗ trợ của HIS — là dữ liệu động. Tra bản chuẩn chính thức và khảo sát hệ thống; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md) và [Thư viện bài báo](../../resources/paper-library.md). Chuẩn tra tại nguồn chính thức HL7/FHIR.

## 24. Thuật ngữ

**FHIR/HL7:** chuẩn trao đổi dữ liệu y tế. **Resource:** đơn vị dữ liệu FHIR. **Profile:** ràng buộc resource. **Terminology:** bộ mã ngữ nghĩa. **RESTful API:** giao diện trao đổi theo chuẩn web.

## 25. Tóm tắt và bước tiếp theo

FHIR là ngôn ngữ chung để liên thông; mô hình hóa dữ liệu theo resource chuẩn với bộ mã, tùy biến tối thiểu và API an toàn giúp sản phẩm dễ kết nối. Tiếp theo sang **[chương 37 — Tin học hình ảnh y khoa](../37-medical-imaging/README.md)** cho dữ liệu hình ảnh.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Chi tiết chuẩn FHIR là dữ liệu động — tra bản chính thức; khả năng hỗ trợ của HIS phải xác minh; ánh xạ mã sai là rủi ro an toàn.
