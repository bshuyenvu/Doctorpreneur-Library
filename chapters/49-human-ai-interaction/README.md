# 49. Tương tác người–AI

Tương tác người-AI (Human-AI Interaction) quyết định liệu một công cụ AI y tế có thực sự được bác sĩ và bệnh nhân tin dùng, hay bị bỏ xó dù thuật toán chính xác đến đâu.

## 1. Giới thiệu

Human-AI Interaction (HAI) là lĩnh vực nghiên cứu cách con người và hệ thống AI phối hợp, tin tưởng lẫn nhau và ra quyết định cùng nhau — nằm ở giao điểm giữa thiết kế trải nghiệm người dùng (UX), tâm lý học nhận thức và kỹ thuật AI. Trong y tế, đây là mảng thường bị đánh giá thấp: nhiều sản phẩm AI có độ chính xác thuật toán ấn tượng trên giấy nhưng thất bại khi triển khai thực tế vì bác sĩ không tin tưởng, không hiểu cách dùng, hoặc cảm thấy bị "qua mặt" trong quy trình ra quyết định. Theo các báo cáo ngành ước tính, một tỷ lệ đáng kể các dự án AI y tế thất bại không phải vì thuật toán kém mà vì vấn đề triển khai và chấp nhận của người dùng cuối — con số cụ thể dao động lớn giữa các khảo sát nên founder cần tự tra cứu các báo cáo về AI adoption trong y tế (ví dụ từ Gartner, KLAS Research) để có số liệu cập nhật.

Đối với bác sĩ-founder, HAI là lợi thế cạnh tranh tự nhiên: chỉ người từng đứng trong phòng khám mới hiểu được sự khác biệt giữa "công cụ hữu ích" và "công cụ gây phiền toái", giữa mức độ tự động hóa phù hợp và mức độ khiến bác sĩ cảm thấy mất kiểm soát. Thiết kế tương tác người-AI tốt trong y tế còn liên quan trực tiếp đến an toàn bệnh nhân: một giao diện gây hiểu lầm về độ tin cậy của AI có thể dẫn đến automation bias (tin tưởng mù quáng vào máy) hoặc ngược lại, alert fatigue khiến bác sĩ bỏ qua cảnh báo đúng.

Chương này giúp bác sĩ-founder nắm được nguyên lý thiết kế tương tác người-AI, đặc biệt trong bối cảnh lâm sàng có rủi ro cao.

## 2. Tại sao bác sĩ cần học

- Bác sĩ-founder hiểu trực tiếp tâm lý và quy trình làm việc của người dùng cuối (đồng nghiệp bác sĩ) — lợi thế lớn khi thiết kế tương tác AI phù hợp.
- Automation bias (tin tưởng quá mức vào AI) và algorithm aversion (từ chối AI dù đúng) đều là rủi ro lâm sàng thực sự — hiểu để thiết kế cân bằng.
- Trải nghiệm tương tác kém là nguyên nhân hàng đầu khiến sản phẩm AI y tế tốt về mặt kỹ thuật vẫn thất bại thương mại.
- Thiết kế đúng mức độ minh bạch và giải thích (explainability) giúp founder xây dựng niềm tin với cả bác sĩ, bệnh nhân và cơ quan quản lý.

## 3. Kiến thức nền

Khái niệm cốt lõi: automation bias — xu hướng con người tin tưởng quá mức vào gợi ý tự động, kể cả khi sai; algorithm aversion — xu hướng ngược lại, từ chối tin tưởng AI dù nó đúng hơn con người; trust calibration — hiệu chỉnh mức độ tin tưởng của người dùng khớp với độ tin cậy thực của hệ thống, không quá cao cũng không quá thấp; human-in-the-loop vs human-on-the-loop — mức độ con người tham gia trực tiếp vào từng quyết định so với chỉ giám sát tổng thể; explainable AI (XAI) — thiết kế để AI giải thích được lý do đưa ra kết quả, tăng khả năng kiểm chứng; cognitive load — gánh nặng nhận thức mà giao diện AI đặt lên người dùng, cần tối thiểu hóa trong môi trường lâm sàng áp lực cao; mental model — mô hình tinh thần người dùng hình thành về cách AI hoạt động, ảnh hưởng trực tiếp đến cách họ dùng công cụ; friction design — thiết kế có chủ đích điểm "chậm lại" trong quy trình để buộc con người xác nhận trước quyết định quan trọng.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Thiết kế giao diện AI quá tự tin, không thể hiện độ bất định (uncertainty) | Automation bias, bác sĩ tin tưởng mù quáng vào gợi ý sai | Hiển thị độ tin cậy/khoảng bất định của mỗi dự đoán |
| Yêu cầu quá nhiều thao tác xác nhận cho mọi gợi ý AI | Cognitive load cao, bác sĩ bỏ qua hoặc click xác nhận không đọc | Chỉ yêu cầu xác nhận chủ động cho các gợi ý rủi ro cao |
| Không giải thích lý do AI đưa ra gợi ý | Algorithm aversion, bác sĩ từ chối sử dụng dù hệ thống đúng | Bổ sung lớp giải thích đơn giản, phù hợp ngữ cảnh lâm sàng |
| Thiết kế không thay đổi theo mức độ kinh nghiệm người dùng | Bác sĩ mới và bác sĩ kỳ cựu cần mức hỗ trợ khác nhau nhưng nhận cùng một giao diện | Cá nhân hóa mức độ chi tiết/tự động hóa theo vai trò và kinh nghiệm |
| Không kiểm thử tương tác thực tế trước khi triển khai rộng | Vấn đề UX chỉ lộ ra khi đã triển khai, khó sửa | Thực hiện usability testing với bác sĩ thật từ giai đoạn thiết kế sớm |
| Bỏ qua sự khác biệt văn hóa/thói quen làm việc giữa các cơ sở y tế | Sản phẩm hoạt động tốt ở nơi thử nghiệm nhưng thất bại khi mở rộng | Thích nghi thiết kế tương tác theo từng bối cảnh triển khai cụ thể |

## 5. Roadmap học (6 tuần)

- **Tuần 1:** Tìm hiểu khái niệm automation bias, algorithm aversion qua các nghiên cứu kinh điển trong tâm lý học quyết định.
- **Tuần 2:** Học nguyên lý thiết kế explainable AI (XAI) và các kỹ thuật giải thích phổ biến.
- **Tuần 3:** Nghiên cứu case study về UX của các sản phẩm CDS/AI y tế thành công và thất bại.
- **Tuần 4:** Tìm hiểu về trust calibration và cách đo lường mức độ tin tưởng phù hợp của người dùng.
- **Tuần 5:** Thực hành phỏng vấn/quan sát bác sĩ đồng nghiệp sử dụng một công cụ AI hiện có, ghi nhận điểm ma sát.
- **Tuần 6:** Phác thảo nguyên tắc thiết kế tương tác người-AI cho sản phẩm của bạn.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Thinking, Fast and Slow | Daniel Kahneman | 2011 | Cơ bản | Nền tảng tâm lý học nhận thức về cách con người ra quyết định | Mọi bác sĩ-founder |
| Human Compatible | Stuart Russell | 2019 | Trung bình | Tư duy về thiết kế AI an toàn, phối hợp được với con người | Founder quan tâm thiết kế AI có trách nhiệm |
| Designing for Trust | (nhiều tác giả, tìm theo chủ đề UX/AI trust) | — | Trung bình | Nguyên lý thiết kế UX xây dựng niềm tin người dùng với hệ thống tự động | Founder/nhà thiết kế sản phẩm AI |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nghiên cứu về automation bias trong quyết định lâm sàng có hỗ trợ AI | Tra cứu trên PubMed theo từ khóa: "automation bias clinical decision support physician" | Cập nhật hằng năm | Cơ sở thiết kế giao diện tránh tin tưởng mù quáng |
| Nghiên cứu về algorithm aversion và các yếu tố ảnh hưởng đến chấp nhận AI của bác sĩ | Tra cứu theo từ khóa: "algorithm aversion physician trust AI adoption" | Cập nhật hằng năm | Hiểu rào cản tâm lý khi triển khai AI lâm sàng |
| Đánh giá hiệu quả của explainable AI trong tăng niềm tin lâm sàng | Tra cứu theo từ khóa: "explainable AI clinician trust interpretability healthcare" | Cập nhật hằng năm | Thiết kế lớp giải thích phù hợp với người dùng y khoa |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Human Factors in Medical Device Design Guidance | FDA | Cập nhật định kỳ | Nguyên tắc thiết kế lấy con người làm trung tâm cho thiết bị y tế |
| Ethics Guidelines for Trustworthy AI | Ủy ban châu Âu (EU) | 2019 | Khung nguyên tắc AI đáng tin cậy, bao gồm yêu cầu về giám sát con người |
| WHO Guidance on Ethics and Governance of AI for Health | WHO | Cập nhật định kỳ | Nguyên tắc đạo đức và quản trị AI y tế toàn cầu |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| FDA Human Factors and Usability Engineering | Tài nguyên hướng dẫn thiết kế lấy con người làm trung tâm | Truy cập công khai |
| Nielsen Norman Group | Nghiên cứu UX hàng đầu, có nhiều bài về thiết kế AI | Truy cập công khai, một số nội dung trả phí |
| ACM CHI Conference proceedings | Kho nghiên cứu học thuật về tương tác người-máy | Truy cập công khai một phần |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| UX Design Weekly | Kenny Chen | Tổng hợp bài viết UX hằng tuần, có chủ đề AI |
| The Batch | DeepLearning.AI | AI nói chung, thường có bài về tương tác người-AI |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| Human-Centered AI (tìm theo từ khóa) | Nhiều host chuyên ngành | Spotify, Apple Podcasts |
| Design Better Podcast | InVision | Spotify, Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| Nielsen Norman Group | Video nghiên cứu UX chuyên sâu, dễ áp dụng |
| Stanford HAI (Human-Centered AI Institute) | Bài giảng và hội thảo về AI lấy con người làm trung tâm |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí (ước tính) |
|---|---|---|---|
| Human-Centered Design for Inclusive Innovation | Coursera (Đại học lớn) | 4-6 tuần | Miễn phí xem, trả phí lấy chứng chỉ |
| Designing AI Products and Services | Nền tảng đào tạo UX chuyên nghiệp | Vài tuần | Trả phí |
| Stanford HAI Executive Education | Stanford HAI | Vài ngày | Trả phí, thường cao |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| interpretml | Thư viện mã nguồn mở hỗ trợ giải thích mô hình ML | Dùng cho lớp explainability trong sản phẩm |
| google/model-card-toolkit | Công cụ tạo "model card" minh bạch hóa thông tin mô hình AI | Tham khảo chuẩn minh bạch mô hình |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Công cụ trực quan hóa độ tin cậy/bất định của mô hình | Hiển thị mức độ chắc chắn của dự đoán AI cho người dùng | Hỗ trợ trust calibration trong giao diện lâm sàng |
| Nền tảng usability testing từ xa | Ghi nhận hành vi người dùng khi tương tác với prototype AI | Kiểm thử thiết kế tương tác trước khi triển khai |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| InterpretML | MIT | Thư viện giải thích mô hình ML mã nguồn mở của Microsoft |
| Model Card Toolkit | Apache 2.0 | Công cụ chuẩn hóa tài liệu minh bạch về mô hình AI |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| ACM CHI Community | Cộng đồng học thuật hàng đầu về tương tác người-máy |
| Stanford HAI | Viện nghiên cứu AI lấy con người làm trung tâm, nhiều tài nguyên mở |

## 18. Case study nổi bật

**Hệ thống cảnh báo lâm sàng bị tắt hàng loạt vì alert fatigue (dạng tổng hợp từ tài liệu công bố):** nhiều bệnh viện triển khai hệ thống CDS với tỷ lệ cảnh báo giả cao đã ghi nhận tỷ lệ bác sĩ tắt hoặc phớt lờ cảnh báo lên đến phần lớn các trường hợp trong một số nghiên cứu công bố, làm mất tác dụng của cả những cảnh báo đúng và quan trọng. Bài học cho founder: thiết kế tương tác không phù hợp có thể vô hiệu hóa hoàn toàn giá trị lâm sàng của một hệ thống AI dù thuật toán bên dưới chính xác.

**Startup AI hình ảnh y khoa thành công nhờ tập trung vào workflow, không chỉ độ chính xác:** một số công ty AI chẩn đoán hình ảnh đã thành công thương mại không chỉ nhờ độ chính xác thuật toán mà nhờ thiết kế tích hợp mượt mà vào workflow đọc phim hiện có của bác sĩ chẩn đoán hình ảnh — không yêu cầu thay đổi thói quen làm việc, chỉ "chèn" gợi ý đúng lúc đúng chỗ. Bài học: mức độ ma sát khi tích hợp vào quy trình làm việc hiện có thường quyết định thành công thương mại nhiều hơn vài phần trăm độ chính xác thuật toán.

## 19. Checklist thực hành

- [ ] Xác định rõ mức độ tự động hóa phù hợp (human-in-the-loop vs human-on-the-loop) cho từng chức năng sản phẩm.
- [ ] Thiết kế hiển thị độ tin cậy/bất định của mỗi gợi ý AI thay vì trình bày như sự thật tuyệt đối.
- [ ] Xây dựng lớp giải thích (explainability) phù hợp với ngữ cảnh và thời gian ra quyết định của bác sĩ.
- [ ] Thực hiện usability testing với bác sĩ thật từ giai đoạn prototype, không đợi đến khi hoàn thiện.
- [ ] Đo lường và hiệu chỉnh mức độ tin tưởng của người dùng (trust calibration) qua thời gian sử dụng.
- [ ] Thiết kế friction có chủ đích cho các quyết định rủi ro cao, giảm friction cho tác vụ thường quy.
- [ ] Thu thập phản hồi định tính (không chỉ định lượng) về trải nghiệm sử dụng.
- [ ] Kiểm tra khả năng thích nghi giao diện với các nhóm người dùng có kinh nghiệm khác nhau.
- [ ] Đánh giá tác động của thiết kế đến cognitive load trong môi trường lâm sàng áp lực cao.
- [ ] Xây dựng cơ chế phản hồi để bác sĩ có thể báo cáo khi AI sai hoặc gây hiểu lầm.

## 20. Project thực hành

1. **Usability testing một công cụ AI y tế hiện có:** quan sát 3-5 bác sĩ đồng nghiệp sử dụng một sản phẩm CDS/AI, ghi nhận điểm ma sát và phản ứng cảm xúc. Công cụ: kịch bản nhiệm vụ mẫu, ghi hình màn hình (có sự đồng ý). KPI: xác định được ít nhất 3 điểm ma sát cụ thể có thể cải thiện.
2. **Thiết kế prototype giao diện hiển thị độ bất định:** vẽ wireframe cho một tính năng AI, thử nghiệm 2-3 cách hiển thị độ tin cậy khác nhau (số phần trăm, thang màu, ngôn ngữ tự nhiên). Công cụ: Figma hoặc giấy/bút. KPI: thu thập phản hồi từ ít nhất 5 bác sĩ về cách hiểu và ưu tiên.
3. **Xây dựng bộ nguyên tắc thiết kế tương tác người-AI cho sản phẩm của bạn:** tổng hợp thành tài liệu ngắn gọn dựa trên nghiên cứu và thực hành ở trên. Công cụ: tài liệu văn bản, có thể tham khảo mẫu "AI design guidelines" của các công ty công nghệ lớn. KPI: hoàn thành tài liệu 1-2 trang có thể chia sẻ với đội ngũ thiết kế/kỹ thuật.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu giai đoạn đầu |
|---|---|
| Tỷ lệ chấp nhận gợi ý AI phù hợp (không quá cao gây automation bias, không quá thấp gây algorithm aversion) | Theo dõi và hiệu chỉnh liên tục, có ngưỡng mục tiêu rõ ràng |
| Điểm hài lòng người dùng (usability score, ví dụ SUS) | Đạt mức "tốt" trở lên theo thang đo chuẩn |
| Thời gian học sử dụng thành thạo (time to proficiency) | Càng ngắn càng tốt, có mục tiêu cụ thể theo loại người dùng |
| Tỷ lệ báo cáo sự cố/hiểu lầm liên quan đến giao diện AI | Giảm dần theo thời gian nhờ cải tiến thiết kế |

## 22. Tài nguyên miễn phí

- FDA Human Factors and Usability Engineering — tài liệu hướng dẫn công khai.
- Nielsen Norman Group — nhiều bài viết UX miễn phí, có chủ đề AI.
- WHO Guidance on Ethics and Governance of AI for Health — tài liệu công khai.

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Dịch vụ usability testing chuyên nghiệp | Vài nghìn USD tùy phạm vi | Đánh giá độc lập, phát hiện vấn đề UX sớm |
| Stanford HAI Executive Education | Học phí cao, thường vài nghìn USD | Kiến thức chuyên sâu và mạng lưới quan hệ chất lượng cao |
| Nền tảng thiết kế/prototype chuyên nghiệp (Figma nâng cao, v.v.) | Gói thuê bao hằng tháng | Tăng tốc quá trình thiết kế và kiểm thử prototype |

## 24. Những tài liệu bắt buộc đọc

1. FDA Human Factors and Usability Engineering Guidance.
2. WHO Guidance on Ethics and Governance of AI for Health.
3. Thinking, Fast and Slow (Daniel Kahneman) — chương về heuristics và bias liên quan quyết định.
4. Một nghiên cứu tiêu biểu về automation bias trong CDS (tự tra cứu PubMed).
5. Ethics Guidelines for Trustworthy AI (Ủy ban châu Âu) — phần về giám sát con người (human oversight).

## 25. Lộ trình ưu tiên đọc

1. Thinking, Fast and Slow (nền tảng tâm lý học quyết định, dễ tiếp cận).
2. FDA Human Factors and Usability Engineering Guidance (nguyên tắc thiết kế thực dụng).
3. Nghiên cứu về automation bias và algorithm aversion (hiểu rủi ro hai chiều).
4. WHO Guidance on Ethics and Governance of AI for Health (khung đạo đức tổng thể).
5. Ethics Guidelines for Trustworthy AI của EU (khi sản phẩm hướng đến thị trường quốc tế).
