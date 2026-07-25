# 54 — Kỹ thuật dữ liệu y tế

> **Nhánh 6 — Sản phẩm, công nghệ và tổ chức** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Xây pipeline dữ liệu có chất lượng và lineage.
> **Sản phẩm của chương:** Data lineage map.

---

## 1. Tóm tắt điều hành

Chất lượng mọi phân tích, AI và bằng chứng phụ thuộc chất lượng dữ liệu nền — "rác vào, rác ra". Kỹ thuật dữ liệu xây các pipeline thu thập, làm sạch, chuẩn hóa, lưu trữ và cung cấp dữ liệu đáng tin, có thể truy vết nguồn gốc (lineage). Trong y tế, lineage và chất lượng dữ liệu là vấn đề an toàn và tuân thủ, không chỉ kỹ thuật. Đầu ra là *data lineage map*: bản đồ dòng dữ liệu từ nguồn tới sử dụng, gồm biến đổi và kiểm soát chất lượng.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu các thành phần pipeline dữ liệu; (b) thiết kế kiểm soát chất lượng dữ liệu; (c) hiểu và ghi lineage; (d) phác data lineage map.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Dữ liệu kém chất lượng làm hỏng AI, phân tích và quyết định — nguy hiểm trong y tế. Lineage cho phép truy nguồn khi có vấn đề và đáp ứng yêu cầu tuân thủ. Hiểu điều này giúp bạn đầu tư đúng vào nền dữ liệu thay vì chạy theo mô hình hào nhoáng trên dữ liệu rác.

## 4. Khái niệm cốt lõi và định nghĩa

**Data pipeline:** chuỗi thu–biến đổi–lưu–cung cấp dữ liệu. **ETL/ELT:** trích xuất–biến đổi–nạp. **Data quality:** đầy đủ, chính xác, nhất quán, kịp thời. **Data lineage:** nguồn gốc và biến đổi dữ liệu. **Metadata:** dữ liệu mô tả dữ liệu. **Data validation:** kiểm tra chất lượng tự động.

## 5. Khung tư duy nền tảng

Thiết kế pipeline với kiểm soát chất lượng tại mỗi khâu (validation tự động, phát hiện bất thường) và ghi lineage đầy đủ (nguồn, biến đổi, phiên bản). Định nghĩa tiêu chí chất lượng theo mục đích sử dụng (fit-for-purpose — chương 30). Nguyên tắc: chất lượng và lineage là thuộc tính thiết kế, không phải kiểm tra sau; dữ liệu bệnh nhân cần bảo mật và quản trị (chương 39–40) trong toàn pipeline.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Dữ liệu HIS/EHR tuyến cơ sở thường thiếu chuẩn hóa, có lỗi nhập liệu và định dạng không nhất quán. Pipeline phải xử lý thực tế này (làm sạch, ánh xạ bộ mã — chương 36) và ghi lineage để truy vết. Ràng buộc hạ tầng đòi hỏi thiết kế khả thi, không quá phức tạp.

## 7. Các bên liên quan

Kỹ sư dữ liệu, khoa học dữ liệu (người dùng dữ liệu), bác sĩ (hiểu ý nghĩa dữ liệu), và bảo mật/tuân thủ. Chất lượng dữ liệu cần đầu vào lâm sàng để định nghĩa "đúng".

## 8. Quy trình từng bước

1. **Lập bản đồ nguồn dữ liệu** và mục đích sử dụng.
2. **Thiết kế biến đổi** (làm sạch, chuẩn hóa, ánh xạ mã).
3. **Định nghĩa tiêu chí chất lượng** fit-for-purpose và validation tự động.
4. **Ghi lineage và metadata** cho mỗi bước.
5. **Thiết kế bảo mật/quản trị** trong pipeline.
6. **Lập data lineage map** và giám sát chất lượng.

## 9. Công cụ và template áp dụng

- **Data lineage map:** nguồn · biến đổi · kiểm soát chất lượng · đích · phiên bản.
- **Data quality rules** (validation tự động).
- **Data dictionary/metadata catalog.**

## 10. Ví dụ minh họa

Pipeline chuẩn bị dữ liệu cho phân tích. Lineage map: nguồn (HIS), biến đổi (làm sạch ngày tháng, ánh xạ ICD, xử lý thiếu), kiểm soát chất lượng (validation định dạng, phát hiện giá trị bất thường), đích (bảng phân tích). Ghi phiên bản để tái lập. Khi kết quả phân tích sai, lineage giúp truy về khâu lỗi. Bảo mật trong toàn chuỗi.

## 11. Sai lầm thường gặp

- **Bỏ kiểm soát chất lượng** ("rác vào, rác ra").
- **Không ghi lineage** — không truy được nguồn lỗi.
- **Xử lý dữ liệu thiếu tùy tiện.**
- **Bỏ ánh xạ bộ mã** (mất ngữ nghĩa — chương 36).
- **Bỏ bảo mật** trong pipeline.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Dữ liệu sai làm hỏng quyết định lâm sàng/AI — vấn đề an toàn. Lineage cần cho truy vết và tuân thủ; thiếu nó gây rủi ro pháp lý. Dữ liệu bệnh nhân trong pipeline cần bảo mật, phân quyền và cơ sở pháp lý (chương 39–40). Ánh xạ mã sai là rủi ro lâm sàng (chương 35).

## 13. Chỉ số đo lường

Điểm chất lượng dữ liệu (đầy đủ, chính xác, nhất quán), tỉ lệ bản ghi qua validation, độ phủ lineage, và thời gian phát hiện/khắc phục lỗi dữ liệu. Giám sát liên tục.

## 14. Bằng chứng và mức độ tin cậy

Chất lượng dữ liệu phải **đo, không giả định**; "fit-for-purpose" phụ thuộc mục đích. Lineage cung cấp bằng chứng truy vết. Kết quả downstream (phân tích/AI) chỉ đáng tin bằng chất lượng dữ liệu nền — ghi rõ giới hạn dữ liệu.

## 15. Tiêu chuẩn và guideline liên quan

Gắn interoperability/bộ mã (chương 35–36), RWE (chương 30), AI/ML (chương 41–47), bảo mật/privacy (chương 39–40), kiến trúc (chương 53). Tham chiếu tiêu chuẩn quản trị và chất lượng dữ liệu khi áp dụng.

## 16. Liên hệ các chương khác

Nền dữ liệu cho **30, 41–47, 56**; dùng chuẩn **35–36**; bảo mật **39–40**; kiến trúc **53**.

## 17. Bài tập thực hành — Data lineage map

Lập data lineage map cho một pipeline: bản đồ nguồn tới đích, các biến đổi (làm sạch, chuẩn hóa, ánh xạ mã), kiểm soát chất lượng và validation tự động tại mỗi khâu, ghi lineage/metadata và phiên bản, và bảo mật trong chuỗi. Định nghĩa tiêu chí chất lượng fit-for-purpose. Ghi rõ giới hạn dữ liệu.

## 18. Checklist tự đánh giá

- [ ] Kiểm soát chất lượng tại mỗi khâu.
- [ ] Lineage và metadata được ghi.
- [ ] Xử lý dữ liệu thiếu có nguyên tắc.
- [ ] Ánh xạ bộ mã giữ ngữ nghĩa.
- [ ] Bảo mật/phân quyền trong pipeline.

## 19. Định nghĩa hoàn thành (Definition of Done)

Data lineage map đạt chuẩn khi vẽ dòng dữ liệu nguồn–đích với biến đổi, kiểm soát chất lượng tự động, ghi lineage/metadata, giữ ngữ nghĩa qua bộ mã, và bảo mật toàn chuỗi.

## 20. Câu hỏi phản tư

Dữ liệu của tôi có đủ chất lượng cho mục đích không? Khi có lỗi, tôi truy về nguồn được không (lineage)? Tôi có giữ ngữ nghĩa qua ánh xạ mã không? Dữ liệu bệnh nhân có được bảo mật suốt pipeline không?

## 21. Cạm bẫy quyết định

**"Rác vào, rác ra"**, **bỏ lineage**, **làm sạch tùy tiện**. Đối trọng: kiểm soát chất lượng thiết kế sẵn, ghi lineage, và đầu vào lâm sàng cho định nghĩa chất lượng.

## 22. Nguồn dữ liệu động cần xác minh

Chất lượng nguồn dữ liệu thực tế, phiên bản bộ mã, tiêu chuẩn quản trị dữ liệu — là dữ liệu động. Đo thực tế và tra chuẩn; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md), [Thư viện bài báo](../../resources/paper-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**ETL/ELT:** trích xuất–biến đổi–nạp. **Data quality:** chất lượng dữ liệu. **Lineage:** nguồn gốc/biến đổi. **Metadata:** dữ liệu mô tả dữ liệu. **Data validation:** kiểm tra chất lượng tự động.

## 25. Tóm tắt và bước tiếp theo

Kỹ thuật dữ liệu tốt bảo đảm chất lượng và lineage — nền cho mọi phân tích, AI và bằng chứng đáng tin. Tiếp theo sang **[chương 55 — DevOps và cloud y tế](../55-devops-cloud/README.md)** cho triển khai và vận hành.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Dữ liệu kém chất lượng làm hỏng quyết định lâm sàng/AI; lineage cần cho truy vết và tuân thủ; dữ liệu bệnh nhân trong pipeline cần bảo mật và cơ sở pháp lý.
