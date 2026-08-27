# 52. UX/UI cho sản phẩm y tế

Nguyên tắc thiết kế trải nghiệm người dùng (UX) và giao diện (UI) đặc thù cho sản phẩm y tế, nơi sai sót thiết kế có thể gây hậu quả lâm sàng thực sự.

## 1. Giới thiệu

UX/UI trong y tế không chỉ là làm giao diện đẹp — đó là một lĩnh vực an toàn (safety-critical design), nơi một nút bấm đặt sai vị trí hoặc một cảnh báo bị bỏ qua có thể dẫn đến sai sót y khoa. Ngành này kết hợp nguyên tắc thiết kế trải nghiệm người dùng truyền thống với "human factors engineering" — lĩnh vực nghiên cứu tương tác giữa con người và hệ thống trong bối cảnh áp lực cao, thời gian hạn chế, và nhiều gián đoạn (như phòng cấp cứu). Theo các báo cáo ngành ước tính, một tỷ lệ đáng kể sự cố y khoa liên quan đến công nghệ bắt nguồn từ thiết kế giao diện kém chứ không phải lỗi phần mềm thuần túy.

Người dùng của sản phẩm y tế rất đa dạng: bác sĩ, điều dưỡng, kỹ thuật viên, bệnh nhân, người chăm sóc — mỗi nhóm có nhu cầu, trình độ công nghệ và bối cảnh sử dụng khác nhau. Một EHR (hồ sơ bệnh án điện tử) thiết kế tốt cho bác sĩ nội trú có thể hoàn toàn không phù hợp với điều dưỡng làm việc tại giường bệnh. Đây là lý do UX y tế đòi hỏi nghiên cứu người dùng sâu và kiểm thử khả dụng (usability testing) nghiêm ngặt hơn nhiều so với ứng dụng tiêu dùng thông thường.

Đối với bác sĩ khởi nghiệp, UX/UI không phải là công việc "làm đẹp cuối cùng" trước khi ra mắt, mà là một phần cốt lõi của thiết kế sản phẩm ngay từ đầu — quyết định liệu người dùng có thực sự áp dụng công nghệ vào quy trình làm việc hàng ngày hay không, bất kể công nghệ nền tảng có tiên tiến đến đâu.

## 2. Tại sao bác sĩ cần học

- Bác sĩ hiểu rõ nhất bối cảnh sử dụng thực tế (căng thẳng, thiếu thời gian, nhiều gián đoạn) — kiến thức này là đầu vào không thể thay thế cho thiết kế UX an toàn.
- FDA yêu cầu bắt buộc quy trình Human Factors Engineering đối với nhiều loại thiết bị y tế và phần mềm SaMD có tương tác người dùng.
- Thiết kế UX kém là nguyên nhân hàng đầu khiến bác sĩ từ chối sử dụng công nghệ mới (technology rejection), dù công nghệ đó có giá trị lâm sàng thực sự.
- Hiểu UX giúp founder bác sĩ đánh giá và phản biện hiệu quả với đội thiết kế, đảm bảo sản phẩm không chỉ đẹp mà còn an toàn và dễ dùng trong môi trường lâm sàng thực tế.

## 3. Kiến thức nền

- **Usability testing**: kiểm thử khả năng sử dụng thực tế với người dùng thật, phát hiện lỗi thiết kế trước khi ra mắt.
- **Human Factors Engineering (HFE)**: phân tích tương tác người-hệ thống trong điều kiện thực tế, bắt buộc với thiết bị y tế theo FDA.
- **Cognitive load**: tải nhận thức — nguyên tắc thiết kế giảm thiểu gánh nặng xử lý thông tin cho người dùng đang bận rộn.
- **Alert fatigue**: hiện tượng người dùng "lờn" cảnh báo do bị làm phiền quá nhiều, dẫn đến bỏ qua cảnh báo quan trọng.
- **Accessibility (WCAG)**: tiêu chuẩn thiết kế cho người khuyết tật, ngày càng quan trọng với sản phẩm hướng tới bệnh nhân.
- **Design system**: bộ quy tắc và thành phần giao diện nhất quán, giúp mở rộng sản phẩm nhanh và đồng bộ.
- **Heuristic evaluation**: đánh giá giao diện dựa trên các nguyên tắc khả dụng đã được kiểm chứng (ví dụ 10 nguyên tắc Nielsen).

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Thiết kế dựa trên ý kiến một bác sĩ duy nhất | Sản phẩm không phù hợp với đa số người dùng | Kiểm thử với nhiều vai trò và khoa khác nhau |
| Quá nhiều cảnh báo/pop-up | Alert fatigue, người dùng bỏ qua cả cảnh báo quan trọng | Phân loại mức độ ưu tiên cảnh báo, giảm nhiễu |
| Sao chép giao diện ứng dụng tiêu dùng không điều chỉnh | Không phù hợp bối cảnh lâm sàng áp lực cao | Thiết kế riêng cho ngữ cảnh sử dụng thực tế |
| Bỏ qua kiểm thử khả dụng trước khi ra mắt | Lỗi thiết kế gây sai sót sử dụng, rủi ro an toàn | Thực hiện usability testing có ghi nhận theo FDA HFE |
| Thiết kế không đồng nhất giữa các màn hình | Người dùng mất thời gian học lại, tăng lỗi thao tác | Áp dụng design system nhất quán |
| Không tính đến accessibility cho bệnh nhân lớn tuổi/khuyết tật | Loại trừ một nhóm người dùng quan trọng | Tuân thủ chuẩn WCAG, kiểm thử với người dùng đa dạng |

## 5. Roadmap học (6 tuần)

- **Tuần 1**: Học nguyên tắc UX cơ bản (heuristics Nielsen, information architecture).
- **Tuần 2**: Tìm hiểu Human Factors Engineering và yêu cầu FDA liên quan.
- **Tuần 3**: Thực hành phỏng vấn và quan sát người dùng (contextual inquiry) tại môi trường lâm sàng.
- **Tuần 4**: Học cách xây wireframe/prototype bằng công cụ như Figma.
- **Tuần 5**: Thực hành usability testing với 5-8 người dùng mẫu.
- **Tuần 6**: Xây dựng design system cơ bản cho sản phẩm của riêng mình.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Don't Make Me Think | Steve Krug | 2014 | Cơ bản | Nguyên tắc thiết kế trực quan, dễ hiểu | Bác sĩ mới học UX |
| The Design of Everyday Things | Don Norman | 2013 | Cơ bản | Nguyên tắc thiết kế lấy con người làm trung tâm | Mọi founder sản phẩm |
| Design for Care | Peter Jones | 2013 | Trung cấp | Ứng dụng tư duy thiết kế cho hệ thống chăm sóc sức khỏe | Founder HealthTech |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nghiên cứu về alert fatigue trong hệ thống EHR | JAMIA | Tra cứu PubMed từ khóa "alert fatigue electronic health record" | Cơ sở thiết kế cảnh báo hợp lý |
| Nghiên cứu về usability của ứng dụng sức khỏe di động cho bệnh nhân cao tuổi | JMIR mHealth | Tra cứu từ khóa "mobile health usability older adults" | Bài học thiết kế accessibility |
| Nghiên cứu về sai sót do thiết kế giao diện trong hệ thống kê đơn điện tử | BMJ Quality & Safety | Tra cứu từ khóa "usability e-prescribing medication error" | Minh chứng hậu quả lâm sàng của UX kém |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Applying Human Factors and Usability Engineering to Medical Devices | FDA | 2016 | Tài liệu bắt buộc tham khảo cho thiết bị y tế |
| WCAG 2.1/2.2 | W3C | 2018/2023 | Chuẩn accessibility quốc tế |
| EHR Usability Toolkit | HIMSS/ONC | Cập nhật định kỳ | Khung đánh giá khả dụng cho hệ thống EHR |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| Nielsen Norman Group | Nguồn tham khảo UX uy tín hàng đầu | nngroup.com |
| HIMSS UX/Usability | Tài nguyên UX chuyên biệt cho y tế | himss.org |
| A11y Project | Tài nguyên về accessibility | a11yproject.com |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| NN/g Newsletter | Nielsen Norman Group | UX research và best practices |
| UX Design Weekly | Kenny Chen | Tổng hợp bài viết UX |
| Health Design Weekly (hoặc tương đương) | Cộng đồng thiết kế y tế | Thiết kế chuyên biệt ngành y tế |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| UX Podcast | James Royal-Lawson & Per Axbom | Spotify/Apple Podcasts |
| Design Better Podcast | InVision | Spotify/Apple Podcasts |
| Healthcare Design | Cộng đồng thiết kế y tế | Spotify/Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| Nielsen Norman Group | Video nghiên cứu và bài giảng UX chuyên sâu |
| Figma | Hướng dẫn công cụ thiết kế và prototype |
| AJ&Smart | Phương pháp thiết kế sản phẩm (design sprint) |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| UX Research and Design Certificate | Google (Coursera) | 3-6 tháng | Trả phí, có hỗ trợ tài chính |
| Human Factors in Medical Device Design | Tổ chức đào tạo chuyên ngành (ví dụ RAPS) | Vài ngày | Trả phí |
| Figma cơ bản đến nâng cao | Figma Academy | Tự học | Miễn phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| awesome-design-systems | Tổng hợp design system nổi bật | Tham khảo xây dựng design system riêng |
| a11yproject/a11yproject.com | Mã nguồn dự án accessibility | Tài nguyên thực hành accessibility |
| carbon-design-system/carbon | Design system mã nguồn mở của IBM | Tham khảo cấu trúc component |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Figma (với AI plugin) | Công cụ thiết kế và prototype hàng đầu | Thiết kế wireframe, UI, prototype tương tác |
| Maze | Nền tảng usability testing từ xa | Kiểm thử khả dụng nhanh với người dùng thật |
| UserTesting | Nền tảng thu thập phản hồi người dùng qua video | Nghiên cứu người dùng quy mô lớn |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| Carbon Design System | Apache 2.0 | Design system của IBM, tham khảo tốt cho enterprise |
| Material Design (Material UI) | MIT | Bộ component UI phổ biến, dễ tùy biến |
| Penpot | MPL 2.0 | Công cụ thiết kế UI/UX mã nguồn mở thay thế Figma |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| UXPA (User Experience Professionals Association) | Hiệp hội chuyên gia UX toàn cầu |
| Health Experience Design (HXD) Conference | Cộng đồng thiết kế trải nghiệm y tế |
| IxDA (Interaction Design Association) | Cộng đồng thiết kế tương tác quốc tế |

## 18. Case study nổi bật

**MyChart (Epic)**: Cổng thông tin bệnh nhân được sử dụng rộng rãi tại Mỹ, thành công một phần nhờ liên tục cải tiến dựa trên phản hồi người dùng thực tế qua nhiều năm, dù vẫn còn nhiều tranh luận về độ phức tạp giao diện — bài học về tầm quan trọng của lặp lại thiết kế (iterative design) dựa trên dữ liệu sử dụng thực tế.

**Ada Health**: Ứng dụng kiểm tra triệu chứng được thiết kế với giao diện hội thoại (conversational UI) đơn giản, giúp người dùng không chuyên y khoa dễ dàng tương tác — minh họa giá trị của việc giảm tải nhận thức (cognitive load) cho người dùng không phải chuyên gia.

**Bài học chung**: sản phẩm y tế thành công về UX thường trải qua nhiều vòng kiểm thử khả dụng thực tế với đúng nhóm người dùng mục tiêu, thay vì chỉ dựa vào đánh giá nội bộ của đội phát triển.

## 19. Checklist thực hành

- [ ] Xác định rõ các nhóm người dùng chính (bác sĩ, điều dưỡng, bệnh nhân...) và nhu cầu riêng từng nhóm
- [ ] Thực hiện contextual inquiry — quan sát người dùng trong môi trường làm việc thực tế
- [ ] Xây dựng wireframe/prototype trước khi code
- [ ] Thực hiện heuristic evaluation dựa trên 10 nguyên tắc Nielsen
- [ ] Kiểm thử khả dụng với ít nhất 5 người dùng thật mỗi vòng thiết kế lớn
- [ ] Rà soát và giảm thiểu số lượng cảnh báo/pop-up không cần thiết
- [ ] Kiểm tra tuân thủ chuẩn accessibility (WCAG) cơ bản
- [ ] Xây dựng design system nhất quán cho toàn bộ sản phẩm
- [ ] Ghi nhận và phân tích lỗi thao tác của người dùng trong quá trình test
- [ ] Lập tài liệu Human Factors Engineering nếu sản phẩm thuộc diện quản lý FDA
- [ ] Thu thập phản hồi định kỳ sau khi ra mắt để cải tiến liên tục

## 20. Project thực hành

1. **Contextual inquiry tại phòng khám**: Quan sát và ghi chép quy trình làm việc thực tế của 3-5 bác sĩ/điều dưỡng; công cụ: sổ ghi chép, video (có đồng ý); KPI: xác định được 3-5 điểm gây khó khăn (pain point) rõ ràng.
2. **Prototype và usability test**: Xây dựng prototype tương tác bằng Figma và kiểm thử với 5-8 người dùng; công cụ: Figma, Maze; KPI: tỷ lệ hoàn thành tác vụ (task success rate) trên 80%.
3. **Xây dựng design system tối giản**: Tạo bộ component UI cơ bản (màu sắc, typography, button, form) dùng nhất quán toàn sản phẩm; công cụ: Figma; KPI: giảm thời gian thiết kế màn hình mới xuống dưới 1 ngày.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu |
|---|---|
| Tỷ lệ hoàn thành tác vụ (task success rate) trong usability test | Trên 80% |
| Thời gian hoàn thành tác vụ trung bình | Giảm dần qua mỗi vòng thiết kế |
| System Usability Scale (SUS) score | Trên 70 điểm (mức "tốt") |
| Số lỗi thao tác nghiêm trọng phát hiện mỗi vòng test | Giảm dần về 0 trước khi ra mắt |
| Tỷ lệ tuân thủ WCAG cơ bản | 100% các tiêu chí mức AA quan trọng |

## 22. Tài nguyên miễn phí

- Bài viết Nielsen Norman Group (nhiều bài mở miễn phí)
- Tài liệu WCAG 2.1 của W3C
- A11y Project (a11yproject.com)
- Công cụ thiết kế Penpot (mã nguồn mở, miễn phí)

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Figma (gói Professional) | Vài USD/tháng/người dùng | Công cụ thiết kế và prototype chuyên nghiệp |
| UserTesting/Maze (gói trả phí) | Theo mức sử dụng | Thu thập phản hồi người dùng nhanh, có phân tích |
| Google UX Design Certificate | Vài triệu VNĐ (ước tính, tùy khu vực) | Chứng chỉ có cấu trúc, dự án thực hành |

## 24. Những tài liệu bắt buộc đọc

1. FDA — Applying Human Factors and Usability Engineering to Medical Devices
2. The Design of Everyday Things — Don Norman
3. Don't Make Me Think — Steve Krug
4. WCAG 2.1 (các nguyên tắc mức AA)
5. Ít nhất một case study về sự cố y khoa liên quan đến thiết kế giao diện kém (tìm qua PubMed hoặc báo cáo an toàn bệnh nhân)

## 25. Lộ trình ưu tiên đọc

1. Don't Make Me Think (nền tảng dễ tiếp cận nhất)
2. The Design of Everyday Things (tư duy thiết kế lấy con người làm trung tâm)
3. FDA Human Factors and Usability Engineering Guidance (bắt buộc nếu sản phẩm là thiết bị y tế)
4. WCAG 2.1 (áp dụng khi thiết kế cho bệnh nhân đa dạng)
5. Design for Care (mở rộng tư duy sang toàn hệ thống chăm sóc sức khỏe)
