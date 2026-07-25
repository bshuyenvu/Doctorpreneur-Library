# 37 — Tin học hình ảnh y khoa

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Hiểu DICOM, PACS và quy trình AI hình ảnh.
> **Sản phẩm của chương:** DICOM/PACS workflow.

---

## 1. Tóm tắt điều hành

Hình ảnh y khoa (X-quang, CT, MRI, siêu âm) là lĩnh vực có nhiều ứng dụng AI nhất, nhưng cũng có hạ tầng chuẩn hóa riêng: DICOM (định dạng và giao thức) và PACS (hệ thống lưu trữ và truyền hình ảnh). Sản phẩm hình ảnh phải chèn vào quy trình chẩn đoán hình ảnh hiện có mà không phá vỡ nó. Đầu ra là *DICOM/PACS workflow*: bản đồ quy trình hình ảnh từ chụp tới đọc kết quả, và điểm chèn sản phẩm/AI.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu vai trò DICOM và PACS trong luồng hình ảnh; (b) nắm quy trình từ chỉ định tới báo cáo; (c) xác định điểm chèn AI và ràng buộc tích hợp; (d) phác DICOM/PACS workflow với kiểm soát an toàn.

## 3. Vì sao chương này quan trọng với Doctorpreneur

AI hình ảnh chỉ tạo giá trị khi tích hợp mượt vào luồng đọc của bác sĩ chẩn đoán hình ảnh và không tăng gánh nặng. Hiểu DICOM/PACS giúp thiết kế điểm chèn đúng và tránh sản phẩm "đứng ngoài" luồng.

## 4. Khái niệm cốt lõi và định nghĩa

**DICOM:** chuẩn định dạng và truyền hình ảnh y khoa. **PACS:** hệ thống lưu trữ và truyền hình ảnh. **RIS:** hệ thống thông tin chẩn đoán hình ảnh (quản lý quy trình). **Modality:** thiết bị chụp (CT, MRI...). **Worklist:** danh sách công việc chụp/đọc. **Hanging protocol:** cách bố trí hình để đọc.

## 5. Khung tư duy nền tảng

Truy luồng hình ảnh end-to-end: chỉ định → chụp (modality) → lưu PACS → bác sĩ đọc → báo cáo. Xác định điểm chèn AI phù hợp: tiền xử lý, hỗ trợ phát hiện/ưu tiên (triage), hay hỗ trợ đo lường. Nguyên tắc: AI hỗ trợ, không thay bác sĩ đọc; kết quả AI phải hiển thị trong công cụ đọc quen thuộc với human oversight, và tích hợp qua DICOM/chuẩn để không tạo luồng song song.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Ở tuyến cơ sở, thiếu bác sĩ chẩn đoán hình ảnh là điểm đau lớn — AI hỗ trợ và teleradiology (đọc từ xa) có giá trị cao. Nhưng hạ tầng PACS/kết nối không đồng đều. Sản phẩm AI hình ảnh phục vụ chẩn đoán thường là thiết bị y tế (chương 20) và cần bằng chứng validation trên quần thể địa phương (chương 47).

## 7. Các bên liên quan

Bác sĩ chẩn đoán hình ảnh, kỹ thuật viên, CNTT/PACS admin, và bác sĩ lâm sàng nhận kết quả. Sản phẩm phải được bác sĩ chẩn đoán hình ảnh chấp nhận — họ là người dùng và người gác cổng chất lượng.

## 8. Quy trình từng bước

1. **Vẽ luồng hình ảnh** hiện tại (chỉ định → đọc → báo cáo).
2. **Xác định điểm chèn** AI/sản phẩm phù hợp.
3. **Thiết kế tích hợp DICOM/PACS** (đầu vào/ra, hiển thị kết quả).
4. **Thiết kế human oversight** và luồng xử lý kết quả AI.
5. **Xác định bằng chứng validation** cần (chương 47).
6. **Phác DICOM/PACS workflow** với kiểm soát an toàn.

## 9. Công cụ và template áp dụng

- **DICOM/PACS workflow map:** bước · hệ thống · điểm chèn AI · hiển thị · oversight.
- **Integration checklist DICOM/PACS.**
- **Bảng kế hoạch validation** (liên kết chương 47).

## 10. Ví dụ minh họa

AI hỗ trợ phát hiện bất thường X-quang ngực. Workflow: hình từ PACS → AI xử lý → kết quả (đánh dấu vùng nghi ngờ + độ tin cậy) hiển thị trong công cụ đọc của bác sĩ, kèm khuyến cáo bác sĩ xác nhận. Không tự động kết luận. Cần validation trên dữ liệu địa phương và quản lý trường hợp AI sai (chương 24, 47).

## 11. Sai lầm thường gặp

- **Tạo luồng đọc song song** thay vì tích hợp PACS.
- **AI kết luận thay bác sĩ** (thiếu oversight).
- **Bỏ qua validation trên quần thể địa phương.**
- **Không quản lý AI sai** (dương/âm tính giả).
- **Tăng gánh nặng đọc** thay vì giảm.

## 12. Rủi ro an toàn, pháp lý và đạo đức

AI hình ảnh sai (bỏ sót/dương tính giả) gây hại trực tiếp; phải có human oversight và quản lý rủi ro (chương 24). Sản phẩm phục vụ chẩn đoán chịu quản lý thiết bị y tế (chương 20) và cần bằng chứng (chương 47). Automation bias (tin AI quá mức) là rủi ro — thiết kế để bác sĩ giữ phán đoán. Dữ liệu hình ảnh chứa thông tin định danh, cần ẩn danh và bảo mật (chương 40).

## 13. Chỉ số đo lường

Hiệu năng AI (độ nhạy/đặc hiệu trên dữ liệu địa phương), ảnh hưởng tới thời gian/độ chính xác đọc, tỉ lệ bác sĩ chấp nhận/bác bỏ gợi ý, và kết cục. Ưu tiên an toàn và giá trị đọc thực.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng AI trên dữ liệu nhà phát triển **không đảm bảo hiệu năng tại cơ sở khác** — cần validation ngoại bộ/tiền cứu (chương 47). Ghi rõ quần thể, thiết bị chụp và điều kiện. Không tuyên bố độ chính xác chung chung.

## 15. Tiêu chuẩn và guideline liên quan

DICOM, tích hợp IHE (hồ sơ tích hợp hình ảnh), quản lý thiết bị y tế (chương 20), AI validation (chương 47), rủi ro (chương 24), privacy (chương 40). Tham chiếu hướng dẫn AI hình ảnh của cơ quan quản lý khi áp dụng.

## 16. Liên hệ các chương khác

Mảnh của **31**; dữ liệu **36**; AI **41–47** (đặc biệt computer vision **46**, validation **47**); thiết bị y tế **20**; bảo mật **40**.

## 17. Bài tập thực hành — DICOM/PACS workflow

Vẽ DICOM/PACS workflow: luồng hình ảnh hiện tại, điểm chèn AI/sản phẩm, thiết kế tích hợp và hiển thị kết quả trong công cụ đọc, human oversight và xử lý AI sai, và kế hoạch validation trên dữ liệu địa phương. Nêu ràng buộc PACS và điều cần xác minh với bác sĩ chẩn đoán hình ảnh.

## 18. Checklist tự đánh giá

- [ ] Tích hợp PACS, không luồng song song.
- [ ] AI hỗ trợ với human oversight, không thay bác sĩ.
- [ ] Có kế hoạch validation trên quần thể địa phương.
- [ ] Quản lý AI sai (dương/âm tính giả).
- [ ] Dữ liệu hình ảnh ẩn danh và bảo mật.

## 19. Định nghĩa hoàn thành (Definition of Done)

DICOM/PACS workflow đạt chuẩn khi chèn AI vào luồng đọc hiện có với oversight, tích hợp qua chuẩn, có kế hoạch validation địa phương và quản lý AI sai, và bảo mật dữ liệu hình ảnh.

## 20. Câu hỏi phản tư

Sản phẩm của tôi có nằm trong luồng đọc quen thuộc không? Bác sĩ có giữ phán đoán cuối không? Tôi có validation trên dữ liệu địa phương chưa? Tôi xử lý AI sai thế nào?

## 21. Cạm bẫy quyết định

**Automation bias**, **tin hiệu năng nhà phát triển**. Đối trọng: human oversight, validation ngoại bộ/tiền cứu, và quản lý rủi ro AI sai.

## 22. Nguồn dữ liệu động cần xác minh

Hiệu năng AI theo cơ sở/thiết bị, quy định AI hình ảnh, khả năng PACS — là dữ liệu động. Validation thực tế và tra nguồn chính thức; không dùng số quảng cáo.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md) và [Case Studies](../../case-studies/viz-ai.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**DICOM:** chuẩn hình ảnh y khoa. **PACS/RIS:** hệ thống lưu trữ/thông tin hình ảnh. **Modality:** thiết bị chụp. **Worklist:** danh sách công việc. **Hanging protocol:** bố trí hình để đọc.

## 25. Tóm tắt và bước tiếp theo

AI hình ảnh tạo giá trị khi tích hợp vào luồng đọc, giữ human oversight, và được validation địa phương — không phải khi khoe hiệu năng phòng thí nghiệm. Tiếp theo sang **[chương 38 — Hỗ trợ quyết định lâm sàng](../38-clinical-decision-support/README.md)** để thiết kế hỗ trợ đúng thời điểm.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. AI hình ảnh phục vụ chẩn đoán chịu quản lý thiết bị y tế và cần validation địa phương; giữ human oversight; dữ liệu hình ảnh cần ẩn danh và bảo mật.
