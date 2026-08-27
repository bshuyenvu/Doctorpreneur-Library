# 29. Thống kê y học cho startup

Nền tảng thống kê y sinh cần thiết để bác sĩ founder thiết kế nghiên cứu, đánh giá bằng chứng lâm sàng và trình bày dữ liệu thuyết phục với nhà đầu tư và cơ quan quản lý.

## 1. Giới thiệu

Thống kê y học (biostatistics) là nền tảng để đánh giá bằng chứng khoa học, thiết kế thử nghiệm lâm sàng, và diễn giải kết quả nghiên cứu một cách chính xác — kỹ năng vốn quen thuộc với bác sĩ qua đào tạo y khoa, nhưng cần được nâng cấp và ứng dụng theo cách khác khi chuyển sang vai trò founder HealthTech. Theo các khảo sát trong giới đầu tư y tế số ước tính, phần lớn nhà đầu tư chuyên về digital health/AI y tế đánh giá rất kỹ chất lượng thiết kế nghiên cứu và bằng chứng thống kê trước khi rót vốn cho các sản phẩm có yếu tố lâm sàng — đây là quan sát định tính phổ biến, không phải số liệu khảo sát chính xác đã kiểm chứng.

Đối với một startup, thống kê y học không chỉ phục vụ việc công bố khoa học mà còn là công cụ thiết yếu để: thiết kế thử nghiệm lâm sàng cho sản phẩm (đặc biệt là thiết bị y tế/AI chẩn đoán), đánh giá hiệu quả thực tế qua dữ liệu real-world evidence, và tránh các sai lầm thống kê phổ biến khi trình bày kết quả cho nhà đầu tư hoặc cơ quan quản lý (dẫn đến mất niềm tin nếu bị phát hiện diễn giải sai).

Chương này cung cấp khung kiến thức thống kê thực hành, tập trung vào những gì founder cần biết để thiết kế nghiên cứu chứng minh giá trị sản phẩm, tránh các cạm bẫy thống kê phổ biến, và giao tiếp hiệu quả với đội ngũ khoa học dữ liệu/thống kê chuyên nghiệp.

## 2. Tại sao bác sĩ cần học

1. Bác sĩ có nền tảng thống kê y học từ đào tạo lâm sàng, nhưng cần chuyển hóa sang tư duy thống kê ứng dụng cho sản phẩm công nghệ (ví dụ: đánh giá hiệu năng thuật toán AI).
2. Hiểu thống kê đúng giúp tránh các tuyên bố quá mức về hiệu quả sản phẩm — rủi ro pháp lý và uy tín nghiêm trọng trong ngành y tế.
3. Nhà đầu tư và cơ quan quản lý (FDA, Bộ Y tế) đòi hỏi bằng chứng thống kê chặt chẽ để phê duyệt hoặc đầu tư vào sản phẩm có yếu tố lâm sàng.
4. Founder hiểu thống kê có thể giao tiếp hiệu quả hơn với đội ngũ data science, tránh bị "qua mặt" bởi các con số được trình bày sai lệch.

## 3. Kiến thức nền

- **Sensitivity, specificity, PPV, NPV**: các chỉ số đánh giá độ chính xác chẩn đoán, cốt lõi khi đánh giá thuật toán AI/công cụ sàng lọc.
- **AUC-ROC**: diện tích dưới đường cong ROC, thước đo tổng quát khả năng phân biệt của mô hình dự đoán/chẩn đoán.
- **Statistical significance vs. clinical significance**: p-value nhỏ không đồng nghĩa với ý nghĩa lâm sàng thực tế — cạm bẫy phổ biến khi trình bày kết quả.
- **Sample size & power analysis**: tính toán cỡ mẫu cần thiết để nghiên cứu có đủ sức mạnh thống kê phát hiện hiệu ứng thực sự.
- **Bias & confounding**: các loại sai lệch (selection bias, confounding) có thể làm sai lệch kết luận nếu không kiểm soát trong thiết kế nghiên cứu.
- **Real-world evidence (RWE)**: bằng chứng từ dữ liệu thực tế lâm sàng (ngoài thử nghiệm ngẫu nhiên có đối chứng - RCT), ngày càng được FDA công nhận trong đánh giá sản phẩm số.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Nhầm lẫn ý nghĩa thống kê với ý nghĩa lâm sàng | Tuyên bố hiệu quả sản phẩm quá mức, gây hiểu lầm nhà đầu tư/khách hàng | Luôn báo cáo kèm effect size và khoảng tin cậy, không chỉ p-value |
| Cỡ mẫu quá nhỏ khi thử nghiệm sản phẩm | Kết quả không đủ tin cậy để khái quát hóa | Thực hiện power analysis trước khi thu thập dữ liệu |
| Bỏ qua yếu tố gây nhiễu (confounder) | Kết luận sai về nguyên nhân-kết quả | Thiết kế nghiên cứu có nhóm đối chứng phù hợp, kiểm soát biến gây nhiễu |
| Chỉ báo cáo độ chính xác (accuracy) mà bỏ qua sensitivity/specificity | Đánh giá sai hiệu năng thuật toán trên dữ liệu mất cân bằng | Luôn báo cáo đầy đủ bộ chỉ số phù hợp bài toán lâm sàng |
| Trình bày dữ liệu chọn lọc có lợi (cherry-picking) | Mất niềm tin nghiêm trọng khi bị phát hiện, rủi ro pháp lý | Báo cáo minh bạch toàn bộ kết quả, kể cả kết quả không thuận lợi |

## 5. Roadmap học (6 tuần)

- **Tuần 1**: Ôn lại các khái niệm thống kê y học cơ bản (sensitivity, specificity, p-value, khoảng tin cậy).
- **Tuần 2**: Học sâu về AUC-ROC và các chỉ số đánh giá mô hình dự đoán/AI chẩn đoán.
- **Tuần 3**: Học power analysis và cách tính cỡ mẫu cho thử nghiệm sản phẩm.
- **Tuần 4**: Tìm hiểu về bias, confounding và cách thiết kế nghiên cứu tránh sai lệch.
- **Tuần 5**: Thực hành phân tích một bộ dữ liệu mẫu (ví dụ dữ liệu công khai từ Kaggle/PhysioNet) bằng Python/R.
- **Tuần 6**: Xây dựng báo cáo thống kê mẫu cho sản phẩm của bạn, tham vấn chuyên gia thống kê nếu có thể.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Medical Statistics at a Glance | Aviva Petrie, Caroline Sabin | 2019 (ấn bản gần đây) | Cơ bản | Tổng quan trực quan, dễ hiểu về thống kê y học | Bác sĩ founder mới bắt đầu ôn lại thống kê |
| Clinical Prediction Models | Ewout Steyerberg | 2019 (ấn bản gần đây) | Nâng cao | Hướng dẫn xây dựng và đánh giá mô hình dự đoán lâm sàng | Founder xây sản phẩm AI/thuật toán dự đoán |
| How to Read a Paper | Trisha Greenhalgh | 2019 (ấn bản gần đây) | Cơ bản | Kỹ năng đọc và đánh giá phản biện nghiên cứu y học | Founder cần đánh giá bằng chứng khoa học nhanh |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Hướng dẫn báo cáo nghiên cứu mô hình dự đoán (TRIPOD statement) | BMJ | Gần đây | Tra cứu PubMed từ khóa "TRIPOD statement prediction model reporting" |
| Nghiên cứu về real-world evidence trong đánh giá phần mềm y tế | npj Digital Medicine | Gần đây | Tra cứu từ khóa "real-world evidence digital health FDA npj" |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| TRIPOD Statement | Nhóm nghiên cứu quốc tế (công bố trên BMJ/Annals of Internal Medicine) | 2015 (gốc), cập nhật thảo luận liên tục | Chuẩn báo cáo mô hình dự đoán lâm sàng, quan trọng cho sản phẩm AI |
| FDA Guidance on Real-World Evidence | U.S. FDA | Cập nhật định kỳ | Hướng dẫn chính thức về sử dụng RWE trong đánh giá sản phẩm |
| STARD Guideline (Standards for Reporting Diagnostic Accuracy) | Nhóm nghiên cứu quốc tế | Cập nhật định kỳ | Chuẩn báo cáo độ chính xác chẩn đoán, tra cứu trên equator-network.org |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| EQUATOR Network | Tổng hợp các chuẩn báo cáo nghiên cứu y học (TRIPOD, STARD, CONSORT...) | Miễn phí |
| PubMed | Cơ sở dữ liệu nghiên cứu y học lớn nhất | Miễn phí |
| Khan Academy Statistics | Học thống kê cơ bản miễn phí | Miễn phí |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| npj Digital Medicine Alerts | Nature | Cập nhật nghiên cứu digital health mới |
| Data Elixir | Lon Riesberg | Khoa học dữ liệu, thống kê ứng dụng |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| Effective Statistician | Alexander Schacht | Spotify/Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| StatQuest with Josh Starmer | Giải thích thống kê và machine learning dễ hiểu, trực quan |
| 3Blue1Brown | Trực quan hóa toán học và xác suất thống kê nền tảng |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| Biostatistics in Public Health | Coursera (Johns Hopkins University) | 4-6 tuần/khóa (chuỗi nhiều khóa) | Miễn phí (trả phí lấy chứng chỉ) |
| Statistics for Genomic Data Science | Coursera (Johns Hopkins) | 4-5 tuần | Miễn phí (trả phí lấy chứng chỉ) |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| awesome-biostatistics | Danh sách tổng hợp tài nguyên thống kê y sinh | Tìm kiếm trên GitHub theo từ khóa |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| R/RStudio | Ngôn ngữ và môi trường thống kê chuyên dụng | Phân tích thống kê y học chuyên sâu |
| Python (scipy, statsmodels, scikit-learn) | Thư viện phân tích thống kê và machine learning | Xây dựng và đánh giá mô hình dự đoán lâm sàng |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| PhysioNet | Mở (dữ liệu theo từng bộ, cần đăng ký) | Kho dữ liệu y sinh công khai để thực hành phân tích thống kê |
| scikit-learn | BSD | Thư viện machine learning phổ biến, có công cụ đánh giá mô hình (AUC, ROC...) |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| American Statistical Association (ASA) — Biostatistics Section | Hiệp hội thống kê Mỹ, phân ban thống kê y sinh |
| PyData/R-Ladies Community | Cộng đồng thực hành phân tích dữ liệu bằng Python/R |

## 18. Case study nổi bật

**IDx-DR (thuật toán AI chẩn đoán bệnh võng mạc tiểu đường)**: Là một trong những AI chẩn đoán đầu tiên được FDA cấp phép độc lập (không cần bác sĩ đọc lại), nhờ thiết kế nghiên cứu lâm sàng chặt chẽ với cỡ mẫu đủ lớn và báo cáo đầy đủ sensitivity/specificity theo chuẩn quốc tế. Bài học: bằng chứng thống kê chặt chẽ, minh bạch là điều kiện tiên quyết để đạt phê duyệt AI y tế mức độ cao.

**Sai lầm điển hình về diễn giải quá mức kết quả pilot nhỏ**: Nhiều startup AI y tế từng công bố kết quả ấn tượng từ pilot cỡ mẫu rất nhỏ (vài chục ca) rồi ngoại suy thành tuyên bố hiệu quả tổng quát, sau đó gặp khó khăn khi kết quả không lặp lại được ở quy mô lớn hơn. Bài học: cần thận trọng với power analysis và tránh khái quát hóa vượt quá phạm vi dữ liệu thực tế.

## 19. Checklist thực hành

- [ ] Xác định rõ câu hỏi nghiên cứu/giả thuyết cần kiểm định trước khi thu thập dữ liệu
- [ ] Thực hiện power analysis để tính cỡ mẫu cần thiết
- [ ] Thiết kế nghiên cứu có nhóm đối chứng phù hợp (nếu áp dụng được)
- [ ] Xác định và kiểm soát các biến gây nhiễu tiềm ẩn
- [ ] Báo cáo đầy đủ sensitivity, specificity, PPV, NPV, AUC-ROC khi đánh giá mô hình
- [ ] Luôn kèm khoảng tin cậy (confidence interval) bên cạnh điểm ước tính
- [ ] Tuân theo chuẩn báo cáo phù hợp (TRIPOD cho mô hình dự đoán, STARD cho chẩn đoán)
- [ ] Tránh diễn giải "statistical significance" thành "clinical significance" một cách mặc định
- [ ] Có chuyên gia thống kê/biostatistician rà soát trước khi công bố kết quả chính thức
- [ ] Lưu trữ và công khai (khi phù hợp) toàn bộ quy trình phân tích để đảm bảo minh bạch

## 20. Project thực hành

1. **Phân tích bộ dữ liệu y sinh công khai**: mô tả — tải một bộ dữ liệu từ PhysioNet/Kaggle liên quan lĩnh vực sản phẩm của bạn và thực hành tính sensitivity/specificity/AUC; công cụ — Python (pandas, scikit-learn) hoặc R; KPI — hoàn thành báo cáo phân tích trong 2 tuần.
2. **Thiết kế đề cương nghiên cứu pilot cho sản phẩm**: mô tả — soạn đề cương nghiên cứu (bao gồm power analysis, tiêu chí thu nhận/loại trừ) để đánh giá hiệu quả sản phẩm; công cụ — mẫu đề cương nghiên cứu, phần mềm tính cỡ mẫu (G*Power hoặc tương đương); KPI — đề cương sẵn sàng để hội đồng đạo đức/cố vấn khoa học rà soát.
3. **Xây dashboard theo dõi hiệu năng thuật toán**: mô tả — nếu sản phẩm có thuật toán AI, xây dashboard theo dõi sensitivity/specificity theo thời gian trên dữ liệu thực tế; công cụ — Python/R kết hợp công cụ trực quan hóa (Streamlit, Tableau); KPI — dashboard cập nhật tự động với dữ liệu mẫu trong 3 tuần.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu |
|---|---|
| Cỡ mẫu đạt yêu cầu power analysis (thường power ≥ 80%) | 100% các nghiên cứu chính thức |
| Tỷ lệ báo cáo đầy đủ theo chuẩn TRIPOD/STARD (nếu áp dụng) | 100% khi công bố/nộp hồ sơ quản lý |
| Số nghiên cứu/pilot có chuyên gia thống kê rà soát | 100% trước khi công bố chính thức |
| Thời gian hoàn thành phân tích dữ liệu pilot | Trong vòng 4-6 tuần sau khi thu thập xong |

## 22. Tài nguyên miễn phí

- Khóa học Biostatistics in Public Health trên Coursera (Johns Hopkins, có thể học miễn phí)
- Bộ dữ liệu công khai trên PhysioNet để thực hành
- Kênh YouTube StatQuest để học trực quan các khái niệm khó

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Tư vấn biostatistician độc lập | Vài trăm-nghìn USD tùy phạm vi dự án | Thiết kế nghiên cứu và phân tích đạt chuẩn công bố/quản lý |
| Phần mềm thống kê chuyên dụng (SAS, SPSS) | Theo giấy phép hàng năm, chi phí đáng kể | Công cụ phân tích được công nhận rộng rãi trong hồ sơ quản lý |
| G*Power / phần mềm tính cỡ mẫu chuyên dụng | Một số miễn phí, một số trả phí tùy tính năng nâng cao | Tính toán cỡ mẫu chính xác cho nghiên cứu chính thức |

## 24. Những tài liệu bắt buộc đọc

1. Medical Statistics at a Glance — Aviva Petrie, Caroline Sabin
2. TRIPOD Statement — hướng dẫn báo cáo mô hình dự đoán lâm sàng
3. How to Read a Paper — Trisha Greenhalgh
4. FDA Guidance on Real-World Evidence — bản mới nhất trên fda.gov
5. Case study IDx-DR (tìm hiểu qua tài liệu công khai về quá trình FDA clearance)

## 25. Lộ trình ưu tiên đọc

1. Ôn lại Medical Statistics at a Glance để củng cố nền tảng thống kê y học
2. Đọc TRIPOD Statement nếu sản phẩm có yếu tố mô hình dự đoán/AI
3. Đọc How to Read a Paper để rèn kỹ năng đánh giá phản biện nhanh
4. Nghiên cứu case study IDx-DR để hiểu tiêu chuẩn bằng chứng cần đạt cho AI y tế
5. Thực hành ngay project "Phân tích bộ dữ liệu y sinh công khai" để áp dụng kiến thức vào công cụ thực tế
