# 40 — Quyền riêng tư và quản trị dữ liệu

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Thiết lập lawful use, consent và data governance.
> **Sản phẩm của chương:** Data governance charter.

---

## 1. Tóm tắt điều hành

Dữ liệu sức khỏe là dữ liệu cá nhân nhạy cảm, chịu quy định chặt về thu thập, sử dụng, chia sẻ và lưu trữ. Quản trị dữ liệu (data governance) là khung bảo đảm dữ liệu được dùng hợp pháp, có đạo đức và có kiểm soát — không chỉ là tuân thủ mà là nền tảng niềm tin. Đầu ra là *data governance charter*: hiến chương quản trị dữ liệu nêu cơ sở pháp lý sử dụng, đồng thuận, phân quyền, vòng đời dữ liệu và trách nhiệm.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu nguyên tắc bảo vệ dữ liệu cá nhân/sức khỏe; (b) xác định cơ sở pháp lý (lawful basis) và đồng thuận; (c) thiết kế quản trị vòng đời dữ liệu và phân quyền; (d) phác data governance charter.

## 3. Vì sao chương này sống còn với Doctorpreneur

Sử dụng dữ liệu không có cơ sở pháp lý là vi phạm nghiêm trọng và hủy niềm tin. Nhiều hoạt động HealthTech (nghiên cứu, AI, chia sẻ) phụ thuộc nền quản trị dữ liệu vững. Thiết kế đúng từ đầu tránh phải làm lại và rủi ro pháp lý.

## 4. Khái niệm cốt lõi và định nghĩa

**Dữ liệu cá nhân/nhạy cảm:** thông tin định danh, gồm dữ liệu sức khỏe. **Lawful basis:** cơ sở pháp lý cho xử lý dữ liệu. **Đồng thuận (consent):** sự cho phép hợp lệ, có thông tin. **Data minimization:** chỉ thu thập dữ liệu cần thiết. **Purpose limitation:** dùng đúng mục đích đã nêu. **Ẩn danh/giả danh (anonymization/pseudonymization):** giảm khả năng định danh. **Data subject rights:** quyền của chủ thể dữ liệu.

## 5. Khung tư duy nền tảng

Privacy by design: nhúng bảo vệ dữ liệu vào thiết kế. Với mỗi hoạt động dữ liệu, xác định: cơ sở pháp lý là gì, mục đích nào, dữ liệu tối thiểu nào, ai được truy cập, lưu bao lâu, và quyền của chủ thể ra sao. Nguyên tắc: minh bạch với chủ thể dữ liệu, thu thập tối thiểu, dùng đúng mục đích, và trao quyền kiểm soát. Nghiên cứu/AI trên dữ liệu cần cơ sở pháp lý và phê duyệt phù hợp.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Bảo vệ dữ liệu cá nhân ở Việt Nam chịu quy định pháp luật chuyên ngành — **nội dung và yêu cầu thay đổi theo thời gian, phải tra văn bản còn hiệu lực**. Dữ liệu bệnh án chịu quy định về hồ sơ bệnh án và bảo mật thông tin người bệnh. Tuyến cơ sở cần quy trình quản trị dữ liệu khả thi, rõ trách nhiệm, dù nguồn lực hạn chế.

## 7. Các bên liên quan

Chủ thể dữ liệu (bệnh nhân), người kiểm soát/xử lý dữ liệu, CNTT/bảo mật, pháp chế, và hội đồng đạo đức (với nghiên cứu). Vai trò kiểm soát viên/xử lý viên dữ liệu và trách nhiệm phải rõ.

## 8. Quy trình từng bước

1. **Lập bản đồ dữ liệu** (thu thập gì, từ đâu, để làm gì).
2. **Xác định cơ sở pháp lý** và đồng thuận cho từng mục đích.
3. **Áp data minimization và purpose limitation.**
4. **Thiết kế phân quyền, ẩn danh/giả danh, lưu trữ và xóa.**
5. **Xác định quyền chủ thể dữ liệu** và cách đáp ứng.
6. **Phác data governance charter** và trách nhiệm.

## 9. Công cụ và template áp dụng

- **Data governance charter:** phạm vi · cơ sở pháp lý · mục đích · dữ liệu tối thiểu · phân quyền · vòng đời · quyền chủ thể · trách nhiệm.
- **Data flow map** và bản ghi hoạt động xử lý.
- **Consent template** và quy trình rút đồng thuận.

## 10. Ví dụ minh họa

Sản phẩm dùng dữ liệu bệnh nhân cho chăm sóc và (riêng) cho cải tiến AI. Charter phân biệt: chăm sóc trực tiếp (cơ sở pháp lý khám chữa bệnh) và dùng cho AI/nghiên cứu (cần cơ sở pháp lý riêng, đồng thuận/ẩn danh và có thể phê duyệt đạo đức). Purpose limitation ngăn dùng dữ liệu chăm sóc cho mục đích khác không được phép. Cơ sở pháp lý cụ thể phải xác minh.

## 11. Sai lầm thường gặp

- **Dùng dữ liệu không có cơ sở pháp lý.**
- **Purpose creep:** dùng dữ liệu ngoài mục đích đã nêu.
- **Thu thập thừa** (vi phạm minimization).
- **Đồng thuận không hợp lệ** (không đủ thông tin/không tự nguyện).
- **Bỏ qua quyền chủ thể dữ liệu** (truy cập, xóa, rút đồng thuận).

## 12. Rủi ro an toàn, pháp lý và đạo đức

Vi phạm bảo vệ dữ liệu có hậu quả pháp lý nặng và phá hủy niềm tin. Dùng dữ liệu bệnh nhân cho AI/nghiên cứu mà không có cơ sở pháp lý và (khi cần) phê duyệt đạo đức là vi phạm đạo đức nghiêm trọng. Ẩn danh phải đủ mạnh để tránh tái định danh. Minh bạch và tôn trọng quyền tự quyết của người bệnh là nguyên tắc đạo đức cốt lõi.

## 13. Chỉ số đo lường

Độ phủ cơ sở pháp lý cho các hoạt động dữ liệu, tỉ lệ dữ liệu tuân minimization, thời gian đáp ứng quyền chủ thể, và số sự cố quyền riêng tư. Theo dõi tuân thủ vòng đời dữ liệu.

## 14. Bằng chứng và mức độ tin cậy

Chương nêu **nguyên tắc quản trị dữ liệu**, KHÔNG phải tư vấn pháp lý. Yêu cầu cụ thể theo quy định là dữ liệu động, phải tra văn bản còn hiệu lực và tư vấn pháp lý. Phân biệt rõ nguyên tắc chung với nghĩa vụ pháp lý cụ thể (cần xác minh).

## 15. Tiêu chuẩn và guideline liên quan

Tuân quy định bảo vệ dữ liệu cá nhân và bảo mật thông tin người bệnh trong nước; tham chiếu khung quốc tế (ví dụ nguyên tắc GDPR) khi liên quan thị trường tương ứng. Gắn cybersecurity (chương 39), đạo đức nghiên cứu (chương 26), AI có trách nhiệm (chương 48).

## 16. Liên hệ các chương khác

Nền pháp lý–đạo đức dữ liệu cho toàn nhánh **31–39** và AI **41–50**; gắn nghiên cứu **26, 30**; an ninh **39**; responsible AI **48**.

## 17. Bài tập thực hành — Data governance charter

Phác data governance charter: lập data flow map, xác định cơ sở pháp lý và đồng thuận cho từng mục đích, áp minimization/purpose limitation, thiết kế phân quyền/ẩn danh/vòng đời/xóa, và quyền chủ thể dữ liệu cùng trách nhiệm. Đánh dấu điểm bắt buộc tư vấn pháp lý và điều cần xác minh theo văn bản hiện hành.

## 18. Checklist tự đánh giá

- [ ] Mỗi hoạt động dữ liệu có cơ sở pháp lý.
- [ ] Áp data minimization và purpose limitation.
- [ ] Đồng thuận hợp lệ, có thông tin.
- [ ] Phân quyền, ẩn danh và vòng đời dữ liệu rõ.
- [ ] Đáp ứng được quyền chủ thể dữ liệu.

## 19. Định nghĩa hoàn thành (Definition of Done)

Data governance charter đạt chuẩn khi lập bản đồ dữ liệu, gắn cơ sở pháp lý/đồng thuận cho từng mục đích, áp minimization/purpose limitation, thiết kế phân quyền và vòng đời, bảo đảm quyền chủ thể, và chỉ ra điểm cần tư vấn pháp lý.

## 20. Câu hỏi phản tư

Mỗi cách tôi dùng dữ liệu có cơ sở pháp lý không? Tôi có thu thập nhiều hơn cần thiết không? Đồng thuận của tôi có hợp lệ và đủ thông tin không? Người bệnh có thực hiện được quyền của họ không?

## 21. Cạm bẫy quyết định

**Purpose creep**, **thu thập thừa "để dành"**, **đồng thuận hình thức**. Đối trọng: privacy by design, minimization, và tư vấn pháp lý cho cơ sở pháp lý.

## 22. Nguồn dữ liệu động cần xác minh

Quy định bảo vệ dữ liệu cá nhân, bảo mật thông tin người bệnh, yêu cầu đồng thuận — là dữ liệu động. Tra văn bản chính thức và tư vấn pháp lý; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện SOP](../../resources/sop-library.md) và [Thư viện template](../../resources/template-library.md). Văn bản pháp quy tra tại nguồn chính thức; nội dung pháp lý cụ thể cần tư vấn chuyên môn.

## 24. Thuật ngữ

**Lawful basis:** cơ sở pháp lý xử lý. **Consent:** đồng thuận. **Data minimization:** thu thập tối thiểu. **Purpose limitation:** giới hạn mục đích. **Pseudonymization/anonymization:** giả danh/ẩn danh. **Data subject rights:** quyền chủ thể dữ liệu.

## 25. Tóm tắt và bước tiếp theo

Quản trị dữ liệu vững — cơ sở pháp lý rõ, thu thập tối thiểu, dùng đúng mục đích, tôn trọng quyền người bệnh — là nền của niềm tin và mọi hoạt động dữ liệu/AI. Đây khép nhánh y tế số. Tiếp theo sang **[chương 41 — AI trong chăm sóc sức khỏe](../41-ai-healthcare/README.md)** để bước vào nhánh AI.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục, KHÔNG phải tư vấn pháp lý. Quy định bảo vệ dữ liệu là dữ liệu động — tra văn bản còn hiệu lực và tham vấn chuyên gia pháp lý; dùng dữ liệu bệnh nhân cho AI/nghiên cứu cần cơ sở pháp lý và phê duyệt phù hợp.
