# 53. Kiến trúc phần mềm y tế

Nền tảng tư duy thiết kế hệ thống phần mềm y tế: từ monolith đến microservices, từ API đến tuân thủ chuẩn dữ liệu y tế.

## 1. Giới thiệu

Kiến trúc phần mềm là bộ khung quyết định một sản phẩm HealthTech có thể mở rộng, bảo trì và tuân thủ quy định trong bao lâu. Với các sản phẩm y tế, kiến trúc không chỉ phục vụ tốc độ phát triển mà còn phải đáp ứng các yêu cầu đặc thù: bảo mật dữ liệu bệnh nhân (PHI/PII), khả năng tích hợp với hệ thống bệnh viện (HIS, LIS, PACS), và tuân thủ các chuẩn trao đổi dữ liệu như HL7 FHIR. Theo các báo cáo ngành ước tính, phần lớn startup HealthTech thất bại không phải vì thiếu vốn mà vì kiến trúc không chịu được tải khi mở rộng hoặc không thể tích hợp với hệ sinh thái y tế hiện có.

Với bác sĩ khởi nghiệp, hiểu kiến trúc không có nghĩa là tự viết code, mà là có đủ ngôn ngữ chung để đối thoại với CTO, đánh giá đề xuất kỹ thuật, và ra quyết định đầu tư đúng thời điểm — xây monolith đơn giản trước hay đầu tư microservices ngay từ đầu.

## 2. Tại sao bác sĩ cần học

1. Tránh bị "kỹ thuật hóa" và phụ thuộc hoàn toàn vào đối tác công nghệ khi đàm phán hợp đồng hoặc gọi vốn.
2. Ra quyết định đúng về thời điểm tái cấu trúc (refactor) hệ thống trước khi nó trở thành nợ kỹ thuật quá lớn.
3. Đánh giá được rủi ro bảo mật và tuân thủ ngay từ giai đoạn thiết kế, tránh vi phạm quy định bảo vệ dữ liệu y tế.
4. Giao tiếp hiệu quả với đội kỹ thuật để ưu tiên đúng tính năng theo giá trị lâm sàng, không chỉ theo độ khó kỹ thuật.

## 3. Kiến thức nền

- **Monolith vs Microservices**: monolith dễ triển khai ban đầu, microservices linh hoạt khi scale nhưng tăng độ phức tạp vận hành.
- **API-first design**: thiết kế API (REST, GraphQL) trước khi viết giao diện, giúp tích hợp dễ dàng với bên thứ ba (EHR, thiết bị IoT y tế).
- **HL7 FHIR**: chuẩn trao đổi dữ liệu lâm sàng phổ biến nhất hiện nay, nền tảng cho interoperability.
- **Domain-Driven Design (DDD)**: chia hệ thống theo miền nghiệp vụ (đặt lịch, hồ sơ bệnh án, thanh toán) thay vì theo lớp kỹ thuật.
- **Event-driven architecture**: xử lý các luồng sự kiện thời gian thực (cảnh báo sinh hiệu, kết quả xét nghiệm).
- **Layered architecture**: tách biệt tầng trình bày, nghiệp vụ, dữ liệu để dễ bảo trì.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Chọn microservices quá sớm khi chưa có traffic | Tốn chi phí vận hành, chậm ra sản phẩm | Bắt đầu với "modular monolith", tách dần khi cần |
| Không thiết kế API chuẩn hóa ngay từ đầu | Khó tích hợp với HIS/EHR sau này | Áp dụng chuẩn FHIR/REST từ giai đoạn MVP |
| Bỏ qua thiết kế bảo mật dữ liệu bệnh nhân | Vi phạm quy định, mất niềm tin người dùng | Threat modeling và mã hóa dữ liệu ngay từ thiết kế |
| Không có tài liệu kiến trúc (architecture decision record) | Đội ngũ mới khó hiểu hệ thống, lặp lại sai lầm | Duy trì ADR cho mọi quyết định lớn |
| Phụ thuộc hoàn toàn vào một nhà cung cấp (vendor lock-in) | Khó chuyển đổi khi chi phí tăng | Thiết kế theo hướng trừu tượng hóa dịch vụ |

## 5. Roadmap học (6 tuần)

- **Tuần 1**: Khái niệm cơ bản về kiến trúc phần mềm, client-server, REST API.
- **Tuần 2**: Monolith vs microservices, khi nào chọn cái nào.
- **Tuần 3**: HL7 FHIR và interoperability trong y tế.
- **Tuần 4**: Domain-Driven Design áp dụng cho sản phẩm y tế.
- **Tuần 5**: Bảo mật và tuân thủ trong thiết kế kiến trúc (mã hóa, kiểm soát truy cập).
- **Tuần 6**: Thực hành vẽ sơ đồ kiến trúc cho một ý tưởng sản phẩm cụ thể.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Designing Data-Intensive Applications | Martin Kleppmann | 2017 | Nâng cao | Nền tảng toàn diện về hệ thống dữ liệu phân tán | CTO, kỹ sư hệ thống |
| Clean Architecture | Robert C. Martin | 2017 | Trung bình | Nguyên tắc thiết kế phần mềm bền vững | Founder kỹ thuật |
| Building Microservices | Sam Newman | 2021 | Trung bình | Hướng dẫn thực tế xây dựng microservices | CTO giai đoạn scale |
| Domain-Driven Design | Eric Evans | 2003 | Nâng cao | Kinh điển về thiết kế theo miền nghiệp vụ | Kiến trúc sư phần mềm |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nghiên cứu về kiến trúc hệ thống EHR có khả năng mở rộng | Tra cứu PubMed từ khóa: "EHR system architecture scalability" | — | Tham khảo mô hình thiết kế hệ thống bệnh án điện tử |
| Đánh giá interoperability FHIR trong bệnh viện | Tra cứu PubMed từ khóa: "HL7 FHIR interoperability hospital" | — | Hiểu thực tiễn triển khai FHIR |
| Kiến trúc microservices trong hệ thống y tế | Tra cứu Google Scholar từ khóa: "microservices architecture healthcare systems" | — | So sánh ưu nhược điểm khi áp dụng cho y tế |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| HL7 FHIR Implementation Guide | HL7 International | Cập nhật liên tục | Chuẩn kỹ thuật chính thức |
| ONC Health IT Certification Criteria | ONC (Hoa Kỳ) | Cập nhật liên tục | Yêu cầu chứng nhận hệ thống y tế điện tử |
| ISO/IEC 25010 Software Quality Model | ISO | 2011 | Khung đánh giá chất lượng kiến trúc phần mềm |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| martinfowler.com | Blog kiến trúc phần mềm hàng đầu | Miễn phí |
| hl7.org/fhir | Trang chủ chuẩn FHIR | Miễn phí, có tài liệu kỹ thuật |
| microservices.io | Tài nguyên về microservices patterns | Miễn phí |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| ByteByteGo | Alex Xu | Hệ thống phân tán, kiến trúc |
| Software Architecture Weekly | Cộng đồng độc lập | Tổng hợp xu hướng kiến trúc |
| The Pragmatic Engineer | Gergely Orosz | Kỹ thuật phần mềm thực chiến |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| Software Engineering Daily | Nhiều host | Spotify, Apple Podcasts |
| Software Architecture Radio | Nhiều host | Website riêng, Spotify |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| ByteByteGo | Video minh họa kiến trúc hệ thống dễ hiểu |
| Fireship | Video ngắn về công nghệ và kiến trúc phần mềm |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| Software Architecture Foundations | edX/Coursera | 4-6 tuần | Trả phí (ước tính vài triệu VNĐ) |
| Grokking the System Design Interview | Educative | Tự học | Trả phí |
| Introduction to HL7 FHIR | HL7 hoặc các nền tảng e-learning y tế | 1-2 tuần | Có gói miễn phí và trả phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| hapifhir/hapi-fhir | Thư viện FHIR mã nguồn mở phổ biến | Dùng cho Java |
| system-design-primer | Tài liệu học thiết kế hệ thống | Rất phổ biến, tiếng Anh |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| GitHub Copilot | Trợ lý viết code AI | Tăng tốc phát triển, sinh sơ đồ kiến trúc |
| Claude / ChatGPT | Trợ lý phân tích, tư vấn kiến trúc | Thảo luận trade-off thiết kế |
| Eraser.io (AI diagram) | Vẽ sơ đồ kiến trúc bằng AI | Tài liệu hóa hệ thống nhanh |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| OpenMRS | MPL 2.0 | Hệ thống hồ sơ bệnh án mã nguồn mở |
| HAPI FHIR | Apache 2.0 | Máy chủ và thư viện FHIR |
| OpenEMR | GPL v3 | Phần mềm quản lý phòng khám mã nguồn mở |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| HL7 FHIR Community Chat (chat.fhir.org) | Cộng đồng thảo luận kỹ thuật FHIR |
| InfoQ Software Architecture | Cộng đồng chia sẻ kiến thức kiến trúc phần mềm |

## 18. Case study nổi bật

**Epic Systems**: Xuất phát từ một công ty nhỏ, Epic xây dựng kiến trúc hệ thống EHR module hóa cao, cho phép tùy biến sâu theo từng bệnh viện lớn. Bài học: đầu tư sớm vào khả năng cấu hình linh hoạt giúp giữ chân khách hàng doanh nghiệp lớn.

**Practo (Ấn Độ)**: Ban đầu là monolith đơn giản cho đặt lịch khám, sau đó tái cấu trúc dần thành các dịch vụ độc lập (đặt lịch, tư vấn từ xa, dược phẩm) khi mở rộng sang nhiều quốc gia. Bài học: không cần microservices ngay từ đầu, tái cấu trúc theo nhu cầu thực tế tăng trưởng.

**Doximity**: Nền tảng mạng xã hội cho bác sĩ tại Mỹ, xây dựng kiến trúc ưu tiên bảo mật và xác thực danh tính bác sĩ chặt chẽ ngay từ đầu — yếu tố then chốt tạo niềm tin trong cộng đồng y khoa.

## 19. Checklist thực hành

- [ ] Vẽ sơ đồ kiến trúc tổng thể cho ý tưởng sản phẩm của bạn
- [ ] Xác định các miền nghiệp vụ chính (bounded context)
- [ ] Lựa chọn mô hình triển khai ban đầu (monolith hay modular)
- [ ] Thiết kế API cơ bản cho các chức năng cốt lõi
- [ ] Tìm hiểu chuẩn FHIR liên quan đến sản phẩm của bạn
- [ ] Lập danh sách các bên thứ ba cần tích hợp (HIS, thiết bị, cổng thanh toán)
- [ ] Đánh giá rủi ro bảo mật dữ liệu bệnh nhân trong thiết kế
- [ ] Viết tài liệu quyết định kiến trúc (ADR) đầu tiên
- [ ] Tham khảo ý kiến một kỹ sư phần mềm có kinh nghiệm y tế
- [ ] Lập kế hoạch mở rộng hệ thống khi số người dùng tăng 10 lần
- [ ] Xác định điểm nào có thể thuê ngoài (outsource) an toàn

## 20. Project thực hành

1. **Thiết kế kiến trúc cho MVP đặt lịch khám**: mô tả luồng dữ liệu, API, cơ sở dữ liệu; công cụ: draw.io/Eraser; KPI: hoàn thành sơ đồ và review với 1 kỹ sư trong 1 tuần.
2. **Prototype tích hợp FHIR đơn giản**: kết nối thử với một FHIR sandbox công khai; công cụ: HAPI FHIR, Postman; KPI: gọi thành công API lấy dữ liệu bệnh nhân mẫu.
3. **Đánh giá kiến trúc sản phẩm hiện có**: nếu đã có sản phẩm, viết báo cáo đánh giá điểm yếu kiến trúc; công cụ: phỏng vấn đội kỹ thuật; KPI: danh sách 5 rủi ro kiến trúc ưu tiên xử lý.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu |
|---|---|
| Thời gian phản hồi API trung bình | Dưới 300ms cho các endpoint chính |
| Tỷ lệ uptime hệ thống | Trên 99.5% |
| Số lượng ADR (architecture decision record) đã viết | Ít nhất 5 bản trong 6 tháng đầu |
| Thời gian onboarding kỹ sư mới hiểu hệ thống | Dưới 2 tuần |

## 22. Tài nguyên miễn phí

- Tài liệu chính thức HL7 FHIR (hl7.org/fhir)
- Blog martinfowler.com
- Repo system-design-primer trên GitHub
- Cộng đồng chat.fhir.org

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Grokking the System Design Interview | Vài triệu VNĐ | Tư duy hệ thống bài bản |
| Tư vấn kiến trúc từ chuyên gia độc lập | Theo giờ, thương lượng | Đánh giá nhanh rủi ro kiến trúc thực tế |
| Khóa học HL7 FHIR chuyên sâu | Vài triệu đến chục triệu VNĐ | Kiến thức tích hợp chuẩn y tế bài bản |

## 24. Những tài liệu bắt buộc đọc

1. Tài liệu chính thức HL7 FHIR Implementation Guide
2. Clean Architecture — Robert C. Martin
3. Building Microservices — Sam Newman
4. ONC Health IT Certification Criteria (tổng quan)
5. Ít nhất 2 case study kiến trúc từ các công ty HealthTech thành công

## 25. Lộ trình ưu tiên đọc

1. Bắt đầu với khái niệm cơ bản trên martinfowler.com
2. Đọc Clean Architecture để nắm nguyên tắc thiết kế
3. Tìm hiểu HL7 FHIR qua tài liệu chính thức
4. Đọc Building Microservices khi sản phẩm bắt đầu cần mở rộng
5. Tham gia cộng đồng chat.fhir.org để cập nhật thực tiễn
