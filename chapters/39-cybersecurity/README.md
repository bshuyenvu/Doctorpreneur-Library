# 39 — An ninh mạng y tế

> **Nhánh 4 — Y tế số và hạ tầng dữ liệu** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Quản trị nguy cơ, mối đe dọa và ứng phó sự cố.
> **Sản phẩm của chương:** Threat model.

---

## 1. Tóm tắt điều hành

Dữ liệu y tế là mục tiêu giá trị cao của tấn công mạng, và sự cố an ninh trong y tế không chỉ mất dữ liệu mà có thể gây gián đoạn chăm sóc — rủi ro an toàn người bệnh. An ninh mạng phải được thiết kế từ đầu (security by design), không vá sau. Đầu ra là *threat model*: mô hình mối đe dọa xác định tài sản cần bảo vệ, kẻ tấn công, đường tấn công, và biện pháp kiểm soát.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu bối cảnh đe dọa đặc thù y tế; (b) áp dụng nguyên tắc security by design; (c) lập threat model cho sản phẩm; (d) phác kế hoạch ứng phó sự cố.

## 3. Vì sao chương này sống còn với Doctorpreneur

Vi phạm an ninh gây hậu quả pháp lý, mất niềm tin, và có thể ngừng vận hành lâm sàng. CNTT bệnh viện (technical buyer) đánh giá kỹ an ninh trước khi mua. Thiết kế an ninh tốt vừa bảo vệ bệnh nhân vừa là lợi thế bán hàng.

## 4. Khái niệm cốt lõi và định nghĩa

**Threat model:** mô hình hóa mối đe dọa và biện pháp. **CIA triad:** bảo mật (confidentiality), toàn vẹn (integrity), sẵn sàng (availability). **Attack surface:** bề mặt tấn công. **Least privilege:** quyền tối thiểu. **Encryption at rest/in transit:** mã hóa lưu trữ/truyền. **Incident response:** ứng phó sự cố.

## 5. Khung tư duy nền tảng

Security by design: tích hợp an ninh vào kiến trúc từ đầu (chương 31). Dùng threat modeling (ví dụ STRIDE) để nhận diện mối đe dọa theo loại. Áp dụng phòng thủ nhiều lớp (defense in depth), least privilege, mã hóa, và giám sát. Nguyên tắc: giả định sẽ bị tấn công — thiết kế để giảm thiệt hại và phục hồi nhanh, không chỉ để ngăn chặn. Trong y tế, thêm trục *an toàn*: sự cố an ninh không được gây mất an toàn lâm sàng.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Tuyến cơ sở thường hạn chế nguồn lực an ninh chuyên trách. Sản phẩm phải giảm gánh nặng an ninh cho bệnh viện (mặc định an toàn, dễ vận hành) và tuân quy định an toàn thông tin/dữ liệu cá nhân hiện hành — **là dữ liệu động, phải tra văn bản còn hiệu lực**. Ưu tiên biện pháp khả thi trong điều kiện hạn chế.

## 7. Các bên liên quan

CNTT/an ninh bệnh viện, nhà cung dịch vụ hạ tầng, và cơ quan quản lý an toàn thông tin. Nội bộ, an ninh là trách nhiệm toàn đội, không chỉ một người; văn hóa an ninh quan trọng như công cụ.

## 8. Quy trình từng bước

1. **Xác định tài sản** cần bảo vệ (dữ liệu, hệ thống, chức năng).
2. **Nhận diện mối đe dọa** (threat modeling theo loại).
3. **Đánh giá bề mặt tấn công** và lỗ hổng.
4. **Thiết kế kiểm soát** (mã hóa, xác thực, phân quyền, giám sát).
5. **Lập kế hoạch ứng phó sự cố** và sao lưu/phục hồi.
6. **Phác threat model** và kế hoạch kiểm thử an ninh định kỳ.

## 9. Công cụ và template áp dụng

- **Threat model:** tài sản · mối đe dọa · đường tấn công · kiểm soát · rủi ro tồn dư.
- **Incident response plan.**
- **Security checklist** (mã hóa, xác thực, least privilege, sao lưu).

## 10. Ví dụ minh họa

Sản phẩm lưu dữ liệu bệnh nhân trên cloud. Threat model: tài sản (dữ liệu bệnh nhân); mối đe dọa (truy cập trái phép, ransomware, rò rỉ); kiểm soát (mã hóa at rest/in transit, xác thực mạnh, least privilege, giám sát, sao lưu tách biệt); ứng phó (quy trình phát hiện–cô lập–thông báo–phục hồi). Bảo đảm sự cố không làm mất an toàn lâm sàng (có phương án dự phòng).

## 11. Sai lầm thường gặp

- **Vá an ninh sau** thay vì thiết kế từ đầu.
- **Không mã hóa** dữ liệu nhạy cảm.
- **Quyền quá rộng** (thiếu least privilege).
- **Không có kế hoạch ứng phó/sao lưu.**
- **Bỏ qua tác động an toàn lâm sàng** của sự cố.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Vi phạm dữ liệu y tế có hậu quả pháp lý và đạo đức nặng; nghĩa vụ thông báo sự cố theo quy định. Sự cố an ninh có thể gây mất an toàn lâm sàng (gián đoạn hệ thống) — phải có phương án duy trì chăm sóc. Bảo vệ dữ liệu bệnh nhân là nghĩa vụ đạo đức, không chỉ tuân thủ.

## 13. Chỉ số đo lường

Độ phủ kiểm soát an ninh, thời gian phát hiện/ứng phó sự cố (MTTD/MTTR), kết quả kiểm thử an ninh (pentest), và độ sẵn sàng sao lưu/phục hồi. Theo dõi lỗ hổng và vá kịp thời.

## 14. Bằng chứng và mức độ tin cậy

Chương nêu **nguyên tắc an ninh**; biện pháp cụ thể phụ thuộc kiến trúc và cần chuyên gia an ninh. Yêu cầu tuân thủ theo quy định là dữ liệu động. Kiểm thử an ninh định kỳ là cách xác minh thực tế, không dựa tuyên bố.

## 15. Tiêu chuẩn và guideline liên quan

Tham chiếu khung an ninh (ví dụ ISO 27001, NIST) và quy định an toàn thông tin/dữ liệu cá nhân trong nước. Gắn privacy (chương 40), kiến trúc (chương 31, 53), DevOps (chương 55). Ưu tiên văn bản pháp luật Việt Nam hiện hành.

## 16. Liên hệ các chương khác

Nền an ninh cho toàn nhánh **31–38**; gắn privacy **40**, kiến trúc **53**, DevOps/cloud **55**; rủi ro **24**.

## 17. Bài tập thực hành — Threat model

Lập threat model cho sản phẩm: xác định tài sản, nhận diện mối đe dọa theo loại, đánh giá bề mặt tấn công, thiết kế kiểm soát (mã hóa, xác thực, least privilege, giám sát), và phác kế hoạch ứng phó sự cố + sao lưu/phục hồi. Nêu cách bảo đảm sự cố không mất an toàn lâm sàng. Ghi rõ điều cần chuyên gia an ninh xác nhận.

## 18. Checklist tự đánh giá

- [ ] An ninh thiết kế từ đầu, không vá sau.
- [ ] Mã hóa at rest/in transit.
- [ ] Least privilege và xác thực mạnh.
- [ ] Kế hoạch ứng phó sự cố và sao lưu/phục hồi.
- [ ] Phương án duy trì an toàn lâm sàng khi sự cố.

## 19. Định nghĩa hoàn thành (Definition of Done)

Threat model đạt chuẩn khi xác định tài sản và mối đe dọa, thiết kế kiểm soát nhiều lớp, có kế hoạch ứng phó/sao lưu, bảo đảm an toàn lâm sàng khi sự cố, và tuân quy định an toàn thông tin đã xác minh.

## 20. Câu hỏi phản tư

Tài sản giá trị nhất của tôi là gì và bảo vệ thế nào? Nếu bị tấn công, tôi giảm thiệt hại và phục hồi ra sao? Sự cố an ninh có làm mất an toàn lâm sàng không? Tôi đã tuân nghĩa vụ thông báo chưa?

## 21. Cạm bẫy quyết định

**An ninh như việc làm sau**, **tin tưởng mặc định**. Đối trọng: security by design, giả định bị tấn công, kiểm thử định kỳ, và chuyên gia an ninh.

## 22. Nguồn dữ liệu động cần xác minh

Quy định an toàn thông tin, nghĩa vụ thông báo sự cố, khung an ninh cập nhật — là dữ liệu động. Tra văn bản chính thức và tham vấn chuyên gia; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md) và [Thư viện SOP](../../resources/sop-library.md). Quy định tra tại nguồn chính thức.

## 24. Thuật ngữ

**CIA triad:** bảo mật–toàn vẹn–sẵn sàng. **Attack surface:** bề mặt tấn công. **Least privilege:** quyền tối thiểu. **Defense in depth:** phòng thủ nhiều lớp. **Incident response:** ứng phó sự cố.

## 25. Tóm tắt và bước tiếp theo

An ninh mạng y tế phải thiết kế từ đầu, phòng thủ nhiều lớp, và bảo đảm sự cố không mất an toàn lâm sàng. Tiếp theo sang **[chương 40 — Quyền riêng tư và quản trị dữ liệu](../40-privacy-governance/README.md)** cho khung pháp lý và đạo đức dữ liệu.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục, không thay tư vấn an ninh chuyên môn. Quy định an toàn thông tin là dữ liệu động — tra văn bản hiện hành; sự cố an ninh không được gây mất an toàn lâm sàng.
