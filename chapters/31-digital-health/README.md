# 31 — Y tế số nền tảng

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Hiểu hệ sinh thái digital health và giá trị lâm sàng.
> **Sản phẩm của chương:** Digital health architecture.

---

## 1. Tóm tắt điều hành

Y tế số là việc dùng công nghệ thông tin và truyền thông để cải thiện chăm sóc, quản lý và nghiên cứu y tế. Nó là "nền" của nhánh này: telemedicine, mHealth, wearables, EHR, CDS đều là các mảnh trong một hệ sinh thái. Founder cần bản đồ hệ sinh thái để định vị sản phẩm và thiết kế kiến trúc tích hợp thay vì xây "ốc đảo" không kết nối. Đầu ra là *digital health architecture*: sơ đồ kiến trúc mức cao đặt sản phẩm trong hệ sinh thái dữ liệu và luồng lâm sàng.

## 2. Mục tiêu học tập

Bạn sẽ: (a) nắm các thành phần chính của hệ sinh thái y tế số; (b) phân biệt giá trị lâm sàng thực với "công nghệ vì công nghệ"; (c) định vị sản phẩm trong hệ sinh thái; (d) phác kiến trúc mức cao có tính tích hợp.

## 3. Vì sao chương này sống còn với Doctorpreneur

Sản phẩm y tế số thất bại khi không tích hợp được vào hạ tầng và luồng hiện có. Hiểu hệ sinh thái sớm giúp thiết kế để kết nối (EHR, FHIR — chương 35–36), tránh ốc đảo dữ liệu và tăng khả năng được chấp nhận.

## 4. Khái niệm cốt lõi và định nghĩa

**Hệ sinh thái y tế số:** tập các hệ thống, dữ liệu, tác nhân và luồng. **Kiến trúc (architecture):** cách các thành phần kết nối. **Interoperability:** khả năng liên thông dữ liệu (chương 35–36). **Data silo (ốc đảo dữ liệu):** hệ thống không kết nối. **Point solution vs platform:** giải pháp điểm so với nền tảng.

## 5. Khung tư duy nền tảng

Định vị sản phẩm theo ba câu hỏi: nó nằm ở đâu trong luồng lâm sàng (chương 07)? Nó lấy/đưa dữ liệu từ/tới đâu? Giá trị lâm sàng thực là gì? Thiết kế kiến trúc "tích hợp trước" (interoperable by design) thay vì ốc đảo. Nguyên tắc: công nghệ chỉ có giá trị khi cải thiện quyết định/kết cục/quy trình, không phải vì mới.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Chuyển đổi số y tế Việt Nam đang thúc đẩy HIS, bệnh án điện tử và kết nối tuyến — nhưng mức độ số hóa và chuẩn hóa khác nhau giữa các cơ sở. Ở tuyến cơ sở, sản phẩm phải tích hợp với HIS sẵn có và chịu ràng buộc hạ tầng. Chính sách chuyển đổi số là dữ liệu động, cần theo dõi văn bản mới.

## 7. Các bên liên quan

CNTT/CMIO, lãnh đạo, bác sĩ/điều dưỡng, nhà cung HIS, và cơ quan quản lý. Kiến trúc phải được CNTT chấp nhận (bảo mật, tích hợp, vận hành) — đây là technical buyer trong bán hàng (chương 16).

## 8. Quy trình từng bước

1. **Lập bản đồ hệ sinh thái** liên quan sản phẩm.
2. **Định vị sản phẩm** trong luồng lâm sàng và dữ liệu.
3. **Xác định điểm tích hợp** (nguồn/đích dữ liệu, chuẩn).
4. **Phác kiến trúc mức cao** (thành phần, luồng, bảo mật).
5. **Xác định giá trị lâm sàng** và cách đo.
6. **Đánh dấu ràng buộc** hạ tầng và tuân thủ.

## 9. Công cụ và template áp dụng

- **Digital health architecture diagram** (thành phần, luồng dữ liệu, tích hợp, bảo mật).
- **Ecosystem map** đặt sản phẩm trong bối cảnh.
- **Bảng điểm tích hợp** (hệ thống · chuẩn · dữ liệu).

## 10. Ví dụ minh họa

Công cụ quản lý bệnh mạn. Kiến trúc mức cao: lấy dữ liệu bệnh nhân từ HIS/EHR qua chuẩn liên thông (chương 36), xử lý, đưa nhắc/cảnh báo vào luồng bác sĩ, và ghi log an toàn. Định vị: bổ sung cho HIS, không thay thế. Giá trị lâm sàng: cải thiện tuân thủ theo dõi — đo bằng kết cục quy trình. Không xây ốc đảo tách rời HIS.

## 11. Sai lầm thường gặp

- **Xây ốc đảo dữ liệu** không tích hợp.
- **Công nghệ vì công nghệ**, thiếu giá trị lâm sàng.
- **Bỏ qua ràng buộc hạ tầng** tuyến cơ sở.
- **Không tính bảo mật/tuân thủ** từ đầu.
- **Đối đầu trực diện HIS** thay vì bổ sung.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Kiến trúc phải tính bảo mật, quyền riêng tư và an toàn từ thiết kế (chương 39–40). Luồng dữ liệu bệnh nhân cần cơ sở pháp lý. Hệ thống chạm quyết định lâm sàng phải có kiểm soát an toàn và human oversight (chương 24, 38).

## 13. Chỉ số đo lường

Mức độ tích hợp (số điểm kết nối hoạt động), giá trị lâm sàng đo được, độ chấp nhận của CNTT, và độ tin cậy hệ thống. Tránh chỉ số "công nghệ" không gắn kết cục.

## 14. Bằng chứng và mức độ tin cậy

Chương nêu **khung định vị và kiến trúc**; giá trị lâm sàng phải chứng minh bằng bằng chứng (chương 25–30), không suy từ tính năng. Mô tả hệ sinh thái là tổng quan, cần xác minh hạ tầng cụ thể của từng cơ sở.

## 15. Tiêu chuẩn và guideline liên quan

Gắn interoperability (chương 35), FHIR/HL7 (chương 36), cybersecurity (chương 39), privacy (chương 40), CDS (chương 38). Tuân chính sách chuyển đổi số y tế và quy định dữ liệu hiện hành.

## 16. Liên hệ các chương khác

Nền cho toàn nhánh **32–40**; dùng workflow **07**; giá trị lâm sàng gắn **25**; bán cho CNTT **16**.

## 17. Bài tập thực hành — Digital health architecture

Phác digital health architecture cho sản phẩm: lập ecosystem map, định vị sản phẩm trong luồng lâm sàng/dữ liệu, vẽ kiến trúc mức cao (thành phần, luồng, tích hợp, bảo mật), xác định giá trị lâm sàng và cách đo, và liệt kê ràng buộc hạ tầng/tuân thủ. Ghi rõ giả định cần xác minh với CNTT.

## 18. Checklist tự đánh giá

- [ ] Sản phẩm được định vị trong hệ sinh thái.
- [ ] Kiến trúc tích hợp, không ốc đảo.
- [ ] Giá trị lâm sàng rõ và đo được.
- [ ] Bảo mật/tuân thủ tính từ đầu.
- [ ] Ràng buộc hạ tầng tuyến cơ sở được xét.

## 19. Định nghĩa hoàn thành (Definition of Done)

Digital health architecture đạt chuẩn khi định vị sản phẩm trong hệ sinh thái, thiết kế tích hợp với hạ tầng hiện có, nêu giá trị lâm sàng đo được, và tính bảo mật/tuân thủ từ thiết kế.

## 20. Câu hỏi phản tư

Sản phẩm của tôi tích hợp hay tạo ốc đảo? Giá trị lâm sàng thực là gì và đo thế nào? CNTT có chấp nhận kiến trúc này không? Tôi đã tính bảo mật/tuân thủ từ đầu chưa?

## 21. Cạm bẫy quyết định

**Say mê công nghệ** quên giá trị lâm sàng. **Xem nhẹ tích hợp.** Đối trọng: định vị theo luồng lâm sàng, thiết kế tích hợp, và kiểm định giá trị bằng bằng chứng.

## 22. Nguồn dữ liệu động cần xác minh

Chính sách chuyển đổi số y tế, mức số hóa cơ sở, chuẩn liên thông áp dụng — là dữ liệu động. Tra văn bản chính thức và khảo sát hạ tầng thực tế; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md) và [AI tools](../../resources/ai-tool-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Interoperability:** khả năng liên thông. **Data silo:** ốc đảo dữ liệu. **Point solution/platform:** giải pháp điểm/nền tảng. **CMIO:** giám đốc thông tin y khoa. **Architecture:** kiến trúc hệ thống.

## 25. Tóm tắt và bước tiếp theo

Y tế số tạo giá trị khi tích hợp vào hệ sinh thái và cải thiện quyết định/kết cục thật, không phải vì công nghệ mới. Tiếp theo sang **[chương 32 — Khám chữa bệnh từ xa](../32-telemedicine/README.md)** cho một mảnh cụ thể của hệ sinh thái.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Giá trị lâm sàng phải chứng minh bằng bằng chứng; luồng dữ liệu bệnh nhân cần cơ sở pháp lý và bảo mật; chính sách số hóa là dữ liệu động.
