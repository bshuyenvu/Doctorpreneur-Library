# 30. Real-world data và real-world evidence

Chương này giới thiệu cách dữ liệu thực hành lâm sàng thường ngày (Real-World Data - RWD) được chuyển hóa thành bằng chứng thực tế (Real-World Evidence - RWE) phục vụ nghiên cứu, quản lý sản phẩm và ra quyết định trong HealthTech.

## 1. Giới thiệu

Real-World Data (RWD) là dữ liệu về tình trạng sức khỏe bệnh nhân được thu thập ngoài môi trường thử nghiệm lâm sàng ngẫu nhiên có đối chứng (RCT) - ví dụ hồ sơ bệnh án điện tử (EHR), dữ liệu bảo hiểm y tế, sổ đăng ký bệnh (registry), dữ liệu từ thiết bị đeo, hoặc ứng dụng sức khỏe di động. Khi RWD được phân tích một cách có phương pháp để rút ra kết luận về hiệu quả, an toàn hoặc giá trị của một can thiệp y tế, kết quả đó gọi là Real-World Evidence (RWE).

Theo các báo cáo ngành ước tính, thị trường phân tích RWE toàn cầu có thể đạt quy mô hàng tỷ USD trong vòng vài năm tới, với tốc độ tăng trưởng hai chữ số mỗi năm - đây là số liệu minh họa, người đọc nên tự tra cứu các báo cáo thị trường cập nhật (ví dụ Grand View Research, IQVIA) để có con số chính xác tại thời điểm tham khảo. Các cơ quan quản lý lớn như FDA (Hoa Kỳ) và EMA (châu Âu) đã ban hành khung hướng dẫn chính thức cho phép RWE hỗ trợ hồ sơ phê duyệt thuốc, mở rộng chỉ định, và giám sát hậu mãi (post-market surveillance).

Đối với bác sĩ khởi nghiệp HealthTech, RWD/RWE không chỉ là công cụ nghiên cứu học thuật mà còn là tài sản chiến lược: dữ liệu sử dụng thực tế sản phẩm chính là RWD, và việc phân tích nó một cách nghiêm túc giúp startup chứng minh giá trị lâm sàng, thuyết phục nhà đầu tư và cơ quan bảo hiểm.

## 2. Tại sao bác sĩ cần học

- Hiểu RWE giúp bác sĩ đánh giá đúng chất lượng bằng chứng khi sản phẩm HealthTech quảng bá "đã được chứng minh hiệu quả trong thực tế".
- RWD là nguồn dữ liệu huấn luyện và đánh giá quan trọng cho các sản phẩm AI y tế - biết cách thu thập, làm sạch dữ liệu đúng chuẩn giúp tránh sai lệch (bias) nghiêm trọng.
- Nhiều cơ quan quản lý và bảo hiểm y tế ngày càng yêu cầu bằng chứng RWE để chi trả (reimbursement) cho sản phẩm số hoặc thiết bị y tế mới.
- Founder có nền tảng RWE có lợi thế khi gọi vốn, vì nhà đầu tư đánh giá cao khả năng chứng minh outcome bằng dữ liệu thực tế thay vì chỉ dựa vào thử nghiệm nhỏ lẻ.

## 3. Kiến thức nền

Một số khái niệm cốt lõi: nguồn RWD (EHR, claims data, registry, patient-reported outcomes, dữ liệu thiết bị đeo); thiết kế nghiên cứu quan sát (cohort, case-control, cross-sectional); các phương pháp kiểm soát nhiễu (confounding) như propensity score matching; khung đánh giá chất lượng dữ liệu (tính đầy đủ, chính xác, nhất quán); và phân biệt RWE với RCT về mức độ bằng chứng theo thang GRADE. Founder cũng cần nắm khái niệm "fit-for-purpose" - dữ liệu phải phù hợp với câu hỏi nghiên cứu cụ thể, không phải RWD nào cũng dùng được cho mọi mục đích.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Dùng RWD chưa làm sạch để huấn luyện AI | Mô hình sai lệch, dự đoán sai | Áp dụng quy trình data governance nghiêm ngặt |
| Nhầm tương quan với nhân quả | Kết luận sai về hiệu quả sản phẩm | Dùng phương pháp kiểm soát nhiễu, tham vấn biostatistician |
| Bỏ qua tính đại diện của mẫu dữ liệu | Kết quả không khái quát hóa được | Kiểm tra phân bố nhân khẩu học, địa lý |
| Không tuân thủ quy định bảo mật dữ liệu | Rủi ro pháp lý, mất niềm tin | Ẩn danh hóa, tuân thủ HIPAA/GDPR/Luật khám chữa bệnh VN |
| Công bố RWE thổi phồng như RCT | Mất uy tín khoa học | Trình bày rõ giới hạn thiết kế nghiên cứu |

## 5. Roadmap học (6 tuần)

- Tuần 1-2: Nắm khái niệm RWD/RWE, đọc hướng dẫn FDA về RWE.
- Tuần 3: Học các nguồn dữ liệu phổ biến tại Việt Nam (BHYT, HIS, EMR).
- Tuần 4: Thực hành thiết kế nghiên cứu quan sát cơ bản.
- Tuần 5: Học công cụ thống kê xử lý nhiễu (propensity score, R hoặc Python).
- Tuần 6: Áp dụng vào một case study thực tế của sản phẩm/startup.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt | Ai nên đọc |
|---|---|---|---|---|---|
| Real-World Evidence in Drug Development | Harry Guess et al. | tham khảo bản mới nhất | Trung cấp | Tổng quan phương pháp RWE trong dược | Bác sĩ, nhà nghiên cứu |
| Causal Inference: The Mixtape | Scott Cunningham | tham khảo bản mới nhất | Nâng cao | Nền tảng suy luận nhân quả | Data scientist y tế |
| The Book of Why | Judea Pearl | 2018 | Trung cấp | Tư duy nhân quả hiện đại | Founder AI y tế |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nghiên cứu về khung sử dụng RWE trong phê duyệt thuốc | tra cứu trên PubMed từ khóa "real-world evidence regulatory framework" | cập nhật | Hiểu chuẩn mực quản lý |
| Nghiên cứu về chất lượng dữ liệu EHR cho RWE | tra cứu PubMed từ khóa "EHR data quality real-world evidence" | cập nhật | Áp dụng vào chọn nguồn dữ liệu |
| Nghiên cứu ứng dụng RWE trong đánh giá thiết bị y tế | tra cứu PubMed từ khóa "real-world evidence medical device" | cập nhật | Case tham khảo cho HealthTech |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Framework for FDA's Real-World Evidence Program | FDA | 2018 (cập nhật định kỳ) | Khung chính thức, nên đọc bản mới nhất |
| Guideline on registry-based studies | EMA | cập nhật định kỳ | Áp dụng cho thị trường châu Âu |
| Hướng dẫn quản lý dữ liệu y tế điện tử | Bộ Y tế Việt Nam | cập nhật định kỳ | Tham chiếu pháp lý trong nước |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| FDA.gov - RWE section | Trang chính thức về khung RWE | Truy cập tự do |
| ClinicalTrials.gov | Cơ sở dữ liệu thử nghiệm lâm sàng và registry | Truy cập tự do |
| ISPOR.org | Tổ chức nghiên cứu kết quả và kinh tế y tế | Một số tài liệu cần thành viên |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| STAT Health Tech | STAT News | Tin tức HealthTech, RWE |
| Nature Medicine Briefing | Nature | Nghiên cứu y sinh học mới |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| The Evidence Base | ISPOR-liên kết | Spotify/Apple Podcasts |
| Health Tech Deals | Digital Health cộng đồng | Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| ISPOR channel | Video hội thảo về RWE và kinh tế y tế |
| StatQuest | Giải thích thống kê nền tảng dễ hiểu |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| Real-World Evidence in Healthcare | Coursera (các đại học đối tác) | 4-6 tuần | Miễn phí audit/trả phí chứng chỉ |
| Causal Inference course | edX | 6-8 tuần | Miễn phí audit/trả phí chứng chỉ |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| OHDSI/OMOP-CDM | Chuẩn hóa dữ liệu y tế quan sát | Cộng đồng lớn, tài liệu đầy đủ |
| tidyverse/dplyr | Công cụ xử lý dữ liệu R | Hữu ích cho phân tích RWD |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| OHDSI ATLAS | Nền tảng phân tích dữ liệu quan sát chuẩn OMOP | Thiết kế nghiên cứu RWE |
| Python lifelines | Thư viện phân tích sống còn (survival analysis) | Nghiên cứu outcome dài hạn |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| OMOP Common Data Model | Apache 2.0 | Chuẩn dữ liệu quan sát dùng toàn cầu |
| OHDSI HADES | Apache 2.0 | Bộ công cụ phân tích dịch tễ dược |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| OHDSI (Observational Health Data Sciences and Informatics) | Cộng đồng nghiên cứu dữ liệu quan sát lớn nhất thế giới |
| ISPOR | Hiệp hội nghiên cứu kết quả và kinh tế y tế |

## 18. Case study nổi bật

**Flatiron Health**: Công ty được thành lập bởi các kỹ sư công nghệ, xây dựng nền tảng dữ liệu ung thư thực tế từ hồ sơ bệnh án điện tử của hàng trăm phòng khám ung bướu tại Mỹ. Dữ liệu RWE của Flatiron sau đó được các hãng dược sử dụng để hỗ trợ hồ sơ phê duyệt thuốc và được Roche mua lại với giá trị lớn. Bài học: chất lượng và khả năng chuẩn hóa dữ liệu là tài sản cốt lõi.

**Aetion**: Nền tảng phần mềm giúp các công ty dược và cơ quan quản lý phân tích RWE nhanh và minh bạch hơn, hợp tác trực tiếp với FDA trong một số chương trình thí điểm. Bài học: xây dựng công cụ phân tích chuẩn hóa, có thể tái sử dụng, tạo lợi thế cạnh tranh bền vững.

## 19. Checklist thực hành

- [ ] Xác định rõ câu hỏi nghiên cứu trước khi chọn nguồn RWD
- [ ] Đánh giá tính đầy đủ và chất lượng dữ liệu nguồn
- [ ] Thiết lập quy trình ẩn danh hóa dữ liệu bệnh nhân
- [ ] Lựa chọn thiết kế nghiên cứu quan sát phù hợp
- [ ] Áp dụng phương pháp kiểm soát nhiễu (nếu cần)
- [ ] Tuân thủ quy định pháp lý về dữ liệu y tế tại Việt Nam
- [ ] Ghi rõ giới hạn của nghiên cứu khi công bố kết quả
- [ ] Tham vấn chuyên gia thống kê sinh học
- [ ] Xây dựng pipeline lưu trữ và cập nhật dữ liệu liên tục
- [ ] Kiểm tra khả năng khái quát hóa kết quả cho quần thể mục tiêu

## 20. Project thực hành

1. **Dashboard theo dõi outcome bệnh nhân**: Xây dựng dashboard tổng hợp dữ liệu sử dụng thực tế từ một ứng dụng sức khỏe, dùng công cụ BI (Power BI/Metabase); KPI: tỷ lệ giữ chân bệnh nhân, cải thiện chỉ số lâm sàng theo thời gian.
2. **Nghiên cứu quan sát nhỏ**: Thiết kế một nghiên cứu cohort hồi cứu dựa trên dữ liệu phòng khám hợp tác; công cụ: R/Python, OHDSI ATLAS; KPI: chất lượng dữ liệu, khả năng tái lập kết quả.
3. **Pipeline chuẩn hóa dữ liệu OMOP**: Chuyển đổi dữ liệu EHR mẫu sang chuẩn OMOP CDM; công cụ: OHDSI tools; KPI: tỷ lệ trường dữ liệu ánh xạ thành công.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu tham khảo |
|---|---|
| Tỷ lệ dữ liệu đầy đủ (completeness) | trên 90% |
| Thời gian chuẩn hóa dữ liệu | rút ngắn theo từng chu kỳ |
| Số nghiên cứu RWE hoàn thành/năm | tùy quy mô tổ chức |

## 22. Tài nguyên miễn phí

- Tài liệu hướng dẫn FDA RWE Framework (bản PDF công khai)
- Khóa học OHDSI cơ bản trên trang chính thức
- Bộ dữ liệu mẫu synthetic từ Synthea

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Nền tảng phân tích Aetion | theo hợp đồng doanh nghiệp | Phân tích RWE chuẩn hóa, nhanh |
| Khóa học chứng chỉ ISPOR | vài trăm USD (ước tính) | Chứng chỉ chuyên môn được công nhận |

## 24. Những tài liệu bắt buộc đọc

1. FDA Framework for RWE Program
2. Hướng dẫn OMOP Common Data Model
3. Một bài tổng quan hệ thống về phương pháp kiểm soát nhiễu trong nghiên cứu quan sát
4. Quy định pháp lý Việt Nam về dữ liệu y tế điện tử
5. Case study Flatiron Health (tự tra cứu tài liệu công khai)

## 25. Lộ trình ưu tiên đọc

1. FDA Framework for RWE Program
2. Tài liệu nhập môn OHDSI/OMOP CDM
3. Sách hoặc khóa học nền tảng về suy luận nhân quả
4. Case study Flatiron Health và Aetion
5. Quy định pháp lý dữ liệu y tế Việt Nam hiện hành
