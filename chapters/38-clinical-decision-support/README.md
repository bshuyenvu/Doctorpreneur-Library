# 38 — Hỗ trợ quyết định lâm sàng

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Thiết kế CDS đúng thời điểm, đúng người, đúng hành động.
> **Sản phẩm của chương:** CDS five-rights review.

---

## 1. Tóm tắt điều hành

Hệ hỗ trợ quyết định lâm sàng (CDS) cung cấp thông tin/khuyến nghị đúng lúc để cải thiện quyết định. Thất bại phổ biến nhất là alert fatigue — quá nhiều cảnh báo không phù hợp khiến bác sĩ bỏ qua tất cả, kể cả cảnh báo quan trọng. Khung "five rights" (đúng thông tin, đúng người, đúng định dạng, đúng kênh, đúng thời điểm trong workflow) giúp thiết kế CDS hiệu quả và an toàn. Đầu ra là *CDS five-rights review*: rà soát một can thiệp CDS theo năm tiêu chí.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu khung five rights của CDS; (b) phân biệt CDS chủ động/bị động và mức độ tự động; (c) thiết kế để giảm alert fatigue; (d) rà một CDS theo five rights với human oversight.

## 3. Vì sao chương này sống còn với Doctorpreneur

CDS chạm trực tiếp quyết định lâm sàng — giá trị lớn nhưng rủi ro cao. Là bác sĩ, bạn hiểu quyết định nào cần hỗ trợ và cảnh báo nào chỉ gây nhiễu — lợi thế thiết kế CDS được dùng thay vì bị tắt.

## 4. Khái niệm cốt lõi và định nghĩa

**CDS:** hệ hỗ trợ quyết định lâm sàng. **Five rights:** đúng thông tin · đúng người · đúng định dạng · đúng kênh · đúng thời điểm workflow. **Alert fatigue:** bỏ qua cảnh báo do quá tải. **CDS chủ động/bị động:** tự bật hay do người dùng gọi. **Interruptive vs non-interruptive:** ngắt luồng hay không. **Human oversight:** người giữ quyết định cuối.

## 5. Khung tư duy nền tảng

Thiết kế theo five rights, ưu tiên: chỉ cảnh báo khi thực sự thay đổi quyết định (giá trị cao, đặc hiệu), dùng cảnh báo ngắt luồng dè dặt (chỉ cho nguy cơ nghiêm trọng), và đặt hỗ trợ tại điểm quyết định trong workflow (chương 07). Nguyên tắc: CDS hỗ trợ phán đoán, không thay thế; mọi khuyến nghị phải minh bạch cơ sở và cho phép bác sĩ ghi đè (override) có lý do.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

CDS có giá trị lớn ở tuyến cơ sở nơi thiếu chuyên khoa sâu (hỗ trợ phác đồ, cảnh báo tương tác thuốc, nhắc sàng lọc). Nhưng phải tích hợp HIS (chương 35) và phù hợp phác đồ được ban hành. CDS dựa phác đồ Bộ Y tế/guideline cập nhật; cảnh báo phải hiệu chỉnh theo bối cảnh để tránh alert fatigue.

## 7. Các bên liên quan

Bác sĩ/điều dưỡng (người nhận CDS), dược (tương tác thuốc), CNTT (tích hợp), và hội đồng chuyên môn (nội dung khuyến nghị). Nội dung CDS phải được chuyên môn phê duyệt và cập nhật theo guideline.

## 8. Quy trình từng bước

1. **Xác định quyết định lâm sàng** cần hỗ trợ (giá trị cao).
2. **Thiết kế nội dung** dựa guideline/phác đồ đã duyệt.
3. **Áp five rights** cho can thiệp.
4. **Chọn mức ngắt luồng** theo mức nghiêm trọng.
5. **Thiết kế override có lý do** và human oversight.
6. **Rà five-rights review** và kế hoạch theo dõi alert fatigue.

## 9. Công cụ và template áp dụng

- **CDS five-rights review:** thông tin · người · định dạng · kênh · thời điểm · mức ngắt · override · oversight.
- **Bảng ưu tiên cảnh báo** (giá trị × nghiêm trọng).
- **Kế hoạch giám sát override/alert fatigue.**

## 10. Ví dụ minh họa

Cảnh báo tương tác thuốc. Five-rights: chỉ cảnh báo tương tác có ý nghĩa lâm sàng (đúng thông tin), tới bác sĩ kê đơn (đúng người), gọn rõ kèm cơ sở (đúng định dạng), trong màn hình kê đơn (đúng kênh), tại thời điểm kê (đúng thời điểm). Ngắt luồng chỉ cho tương tác nghiêm trọng; các mức nhẹ hiển thị không ngắt. Cho phép override kèm lý do. Theo dõi tỉ lệ override để hiệu chỉnh.

## 11. Sai lầm thường gặp

- **Cảnh báo quá nhiều/không đặc hiệu** → alert fatigue.
- **Ngắt luồng cho mọi mức** nghiêm trọng.
- **Khuyến nghị không minh bạch cơ sở.**
- **Không cho override** hoặc override không ghi lý do.
- **Nội dung không cập nhật guideline.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

CDS sai hoặc gây alert fatigue có thể dẫn tới quyết định sai — rủi ro an toàn nghiêm trọng. Human oversight bắt buộc: bác sĩ giữ quyết định cuối. CDS chạm quyết định lâm sàng có thể là thiết bị y tế (chương 19–20) và cần quản lý rủi ro (chương 24). Nội dung phải dựa bằng chứng cập nhật; khuyến nghị sai lệch là rủi ro pháp lý và đạo đức.

## 13. Chỉ số đo lường

Tỉ lệ override (cao = cảnh báo kém phù hợp), ảnh hưởng tới quyết định/kết cục, tỉ lệ chấp nhận khuyến nghị hữu ích, và dấu hiệu alert fatigue. Theo dõi liên tục để hiệu chỉnh.

## 14. Bằng chứng và mức độ tin cậy

Hiệu quả CDS phụ thuộc thiết kế và tích hợp cụ thể; **không khái quát "CDS cải thiện chăm sóc" chung**. Nội dung khuyến nghị phải dựa guideline/bằng chứng cập nhật, phân biệt rõ mức bằng chứng. Cần đánh giá tác động thực tế (chương 25–30).

## 15. Tiêu chuẩn và guideline liên quan

Nội dung dựa guideline Bộ Y tế/quốc tế cập nhật. Gắn quản lý thiết bị y tế (chương 19–20), rủi ro (chương 24), workflow (chương 07), tích hợp (chương 35–36), responsible AI nếu dùng AI (chương 48).

## 16. Liên hệ các chương khác

Đặt trong workflow **07**; tích hợp **35–36**; AI-based CDS gắn **41–48**; rủi ro **24**; thiết bị y tế **19–20**.

## 17. Bài tập thực hành — CDS five-rights review

Chọn một can thiệp CDS và rà theo five rights: đúng thông tin/người/định dạng/kênh/thời điểm; xác định mức ngắt luồng theo nghiêm trọng; thiết kế override có lý do và human oversight; nêu nguồn guideline của nội dung; và kế hoạch giám sát override/alert fatigue. Ghi rõ điều cần chuyên môn phê duyệt.

## 18. Checklist tự đánh giá

- [ ] Chỉ cảnh báo khi thay đổi quyết định (đặc hiệu).
- [ ] Ngắt luồng chỉ cho mức nghiêm trọng.
- [ ] Khuyến nghị minh bạch cơ sở/guideline.
- [ ] Cho phép override có lý do; giữ human oversight.
- [ ] Giám sát override/alert fatigue.

## 19. Định nghĩa hoàn thành (Definition of Done)

CDS five-rights review đạt chuẩn khi thỏa năm tiêu chí, dùng ngắt luồng dè dặt theo nghiêm trọng, nội dung dựa guideline cập nhật, cho override có lý do với human oversight, và có kế hoạch giám sát alert fatigue.

## 20. Câu hỏi phản tư

Cảnh báo của tôi có thực sự thay đổi quyết định không? Nó có đặc hiệu hay gây nhiễu? Bác sĩ có giữ quyết định cuối và override được không? Nội dung có dựa guideline cập nhật không?

## 21. Cạm bẫy quyết định

**Cảnh báo thừa** gây alert fatigue, **ngắt luồng quá mức**, **automation bias**. Đối trọng: five rights, ưu tiên cảnh báo giá trị cao, và giám sát override.

## 22. Nguồn dữ liệu động cần xác minh

Guideline/phác đồ nền của khuyến nghị, quy định CDS như thiết bị y tế — là dữ liệu động. Tra guideline cập nhật và văn bản hiện hành; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md) và [Thư viện SOP](../../resources/sop-library.md). Guideline tra tại nguồn chính thức.

## 24. Thuật ngữ

**CDS:** hỗ trợ quyết định lâm sàng. **Five rights:** năm tiêu chí CDS. **Alert fatigue:** mệt mỏi cảnh báo. **Override:** ghi đè khuyến nghị. **Interruptive:** cảnh báo ngắt luồng.

## 25. Tóm tắt và bước tiếp theo

CDS hiệu quả tuân five rights, cảnh báo đặc hiệu giá trị cao, giữ human oversight và cho override — để được dùng thay vì bị tắt. Đây khép nhánh y tế số. Tiếp theo sang **[chương 39 — An ninh mạng y tế](../39-cybersecurity/README.md)** để bảo vệ hệ thống và dữ liệu.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. CDS chạm quyết định lâm sàng cần human oversight, nội dung dựa guideline cập nhật, và có thể chịu quản lý thiết bị y tế; an toàn người bệnh trên hết.
