# 35 — EHR và khả năng liên thông

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Thiết kế tích hợp workflow, dữ liệu và hệ thống.
> **Sản phẩm của chương:** Integration map.

---

## 1. Tóm tắt điều hành

EHR (hồ sơ sức khỏe điện tử) và HIS là xương sống dữ liệu của bệnh viện. Sản phẩm HealthTech muốn được dùng thật thường phải liên thông với chúng — đọc dữ liệu bệnh nhân và/hoặc ghi kết quả vào luồng lâm sàng. Tích hợp kém là lý do phổ biến khiến sản phẩm bị bỏ. Đầu ra là *integration map*: bản đồ tích hợp mô tả hệ thống nguồn/đích, dữ liệu trao đổi, chuẩn liên thông, và điểm chạm workflow.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu vai trò EHR/HIS và bài toán liên thông; (b) phân biệt các mức liên thông (kỹ thuật, cú pháp, ngữ nghĩa); (c) xác định dữ liệu và điểm tích hợp cần; (d) phác integration map thực tế với ràng buộc CNTT.

## 3. Vì sao chương này sống còn với Doctorpreneur

Không liên thông thì sản phẩm tạo nhập liệu trùng lặp và bị bác sĩ bỏ dùng. Hiểu tích hợp giúp thiết kế để chèn vào luồng mà không tăng gánh nặng, và vượt qua technical buyer (CNTT) trong bán hàng (chương 16).

## 4. Khái niệm cốt lõi và định nghĩa

**EHR/HIS:** hồ sơ điện tử/hệ thống thông tin bệnh viện. **Interoperability:** khả năng liên thông. **Mức liên thông:** kỹ thuật (kết nối), cú pháp (định dạng), ngữ nghĩa (ý nghĩa dữ liệu). **API/interface:** giao diện trao đổi dữ liệu. **Chuẩn:** HL7, FHIR (chương 36), các bộ mã (ICD, LOINC, SNOMED). **Master data:** dữ liệu định danh nhất quán.

## 5. Khung tư duy nền tảng

Thiết kế theo ba mức liên thông: kết nối được (kỹ thuật), hiểu định dạng (cú pháp), hiểu ý nghĩa (ngữ nghĩa — dùng bộ mã chuẩn). Xác định dữ liệu tối thiểu cần đọc/ghi và điểm chạm workflow ít gián đoạn nhất. Nguyên tắc: tích hợp "vừa đủ" cho giá trị, tránh phụ thuộc sâu không cần; ưu tiên chuẩn mở (FHIR) để dễ mở rộng.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Bệnh viện Việt Nam dùng nhiều HIS khác nhau với mức chuẩn hóa và khả năng mở API khác nhau. Bệnh án điện tử và liên thông tuyến đang được thúc đẩy nhưng chưa đồng đều. Tích hợp thực tế thường cần làm việc với nhà cung HIS địa phương; đây là ràng buộc và cả rào cản cạnh tranh.

## 7. Các bên liên quan

CNTT bệnh viện, nhà cung HIS, bác sĩ/điều dưỡng (điểm chạm workflow), và bảo mật. Nhà cung HIS có thể vừa là đối tác tích hợp vừa là đối thủ — chiến lược quan hệ quan trọng (chương 11, 17).

## 8. Quy trình từng bước

1. **Xác định dữ liệu cần đọc/ghi** tối thiểu.
2. **Khảo sát hệ thống nguồn/đích** và khả năng API.
3. **Chọn chuẩn và mức liên thông** (ưu tiên FHIR — chương 36).
4. **Xác định điểm chạm workflow** ít gián đoạn.
5. **Thiết kế bảo mật và quản trị dữ liệu** cho tích hợp.
6. **Phác integration map** và kế hoạch phối hợp CNTT/nhà cung HIS.

## 9. Công cụ và template áp dụng

- **Integration map:** hệ thống nguồn/đích · dữ liệu · chuẩn · mức liên thông · điểm workflow · bảo mật.
- **Data mapping table** (trường ↔ bộ mã chuẩn).
- **Checklist bảo mật tích hợp.**

## 10. Ví dụ minh họa

Công cụ CDS cần đọc chẩn đoán và xét nghiệm, ghi khuyến nghị. Integration map: đọc từ HIS qua API/FHIR (chương 36), ánh xạ mã (ICD/LOINC), đưa khuyến nghị vào màn hình bác sĩ tại điểm quyết định, ghi log an toàn. Nếu HIS không mở API, cần phối hợp nhà cung — ràng buộc phải xác minh sớm.

## 11. Sai lầm thường gặp

- **Bỏ qua mức ngữ nghĩa** (không dùng bộ mã chuẩn).
- **Giả định HIS mở API** mà chưa kiểm.
- **Nhập liệu trùng lặp** vì tích hợp một chiều kém.
- **Điểm chạm workflow gây gián đoạn.**
- **Bỏ qua bảo mật/quản trị dữ liệu tích hợp.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Trao đổi dữ liệu bệnh nhân cần cơ sở pháp lý, bảo mật và kiểm soát truy cập (chương 39–40). Ánh xạ mã sai có thể gây sai lệch lâm sàng — validation ánh xạ là vấn đề an toàn. Ghi/đưa dữ liệu vào EHR phải bảo đảm toàn vẹn và truy vết.

## 13. Chỉ số đo lường

Mức liên thông đạt được, tỉ lệ ánh xạ mã đúng, độ trễ và độ tin cậy trao đổi dữ liệu, và mức giảm nhập liệu trùng lặp. Theo dõi lỗi tích hợp và thời gian khắc phục.

## 14. Bằng chứng và mức độ tin cậy

Khả năng tích hợp cụ thể phụ thuộc HIS và chính sách từng cơ sở — **phải khảo sát thực tế, không giả định**. Chương nêu nguyên tắc; chi tiết API/chuẩn của mỗi hệ thống là dữ liệu cần xác minh. Ánh xạ ngữ nghĩa cần validation lâm sàng.

## 15. Tiêu chuẩn và guideline liên quan

Gắn FHIR/HL7 (chương 36), bộ mã (ICD, LOINC, SNOMED), bảo mật (chương 39), privacy (chương 40), data engineering (chương 54). Tuân quy định bệnh án điện tử và liên thông dữ liệu y tế hiện hành.

## 16. Liên hệ các chương khác

Nền cho **36** (chuẩn cụ thể), **38** (CDS trong luồng), **54** (data engineering); bán cho CNTT **16**; bảo mật **39–40**.

## 17. Bài tập thực hành — Integration map

Lập integration map cho sản phẩm: xác định dữ liệu đọc/ghi tối thiểu, khảo sát khả năng API hệ thống đích, chọn chuẩn và mức liên thông, lập data mapping table với bộ mã, xác định điểm chạm workflow, và checklist bảo mật/quản trị. Nêu ràng buộc cần xác minh với CNTT/nhà cung HIS.

## 18. Checklist tự đánh giá

- [ ] Xác định dữ liệu tối thiểu cần trao đổi.
- [ ] Đạt cả ba mức liên thông (đặc biệt ngữ nghĩa).
- [ ] Điểm chạm workflow không gây gián đoạn.
- [ ] Ánh xạ mã được validation.
- [ ] Bảo mật và quản trị dữ liệu tích hợp.

## 19. Định nghĩa hoàn thành (Definition of Done)

Integration map đạt chuẩn khi xác định dữ liệu và điểm tích hợp, dùng chuẩn/bộ mã cho liên thông ngữ nghĩa, đặt điểm chạm workflow ít gián đoạn, validation ánh xạ, và bảo đảm bảo mật/quản trị dữ liệu.

## 20. Câu hỏi phản tư

Sản phẩm của tôi có gây nhập liệu trùng lặp không? Tôi đã đạt liên thông ngữ nghĩa (bộ mã) chưa? HIS đích có thực sự mở API không? Ánh xạ mã của tôi có được kiểm chứng an toàn không?

## 21. Cạm bẫy quyết định

**Giả định tích hợp dễ**, **bỏ mức ngữ nghĩa**. Đối trọng: khảo sát HIS thực tế sớm, dùng chuẩn mở, và validation ánh xạ với lâm sàng.

## 22. Nguồn dữ liệu động cần xác minh

Khả năng API của từng HIS, quy định bệnh án điện tử/liên thông, phiên bản bộ mã — là dữ liệu động. Khảo sát thực tế và tra văn bản hiện hành; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md) và [Thư viện bài báo](../../resources/paper-library.md). Chuẩn/quy định tra tại nguồn chính thức.

## 24. Thuật ngữ

**EHR/HIS:** hồ sơ điện tử/hệ thống thông tin bệnh viện. **Interoperability:** liên thông. **Ngữ nghĩa (semantic):** hiểu ý nghĩa dữ liệu. **Bộ mã:** ICD/LOINC/SNOMED. **Data mapping:** ánh xạ trường dữ liệu.

## 25. Tóm tắt và bước tiếp theo

Liên thông EHR/HIS — nhất là ở mức ngữ nghĩa — quyết định sản phẩm có được dùng thật hay bị bỏ. Tiếp theo sang **[chương 36 — FHIR, HL7 và API y tế](../36-fhir-hl7/README.md)** cho chuẩn liên thông cụ thể.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Khả năng tích hợp phụ thuộc từng HIS — khảo sát thực tế; trao đổi dữ liệu bệnh nhân cần cơ sở pháp lý và bảo mật; ánh xạ mã sai là rủi ro an toàn.
