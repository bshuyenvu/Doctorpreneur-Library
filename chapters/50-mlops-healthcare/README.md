# 50. MLOps trong y tế

Xây dựng và vận hành hệ thống machine learning (ML) y tế đáng tin cậy, an toàn và tuân thủ quy định trong suốt vòng đời sản phẩm.

## 1. Giới thiệu

MLOps (Machine Learning Operations) là tập hợp thực hành kết hợp giữa phát triển ML, DevOps và quản trị dữ liệu, nhằm đưa mô hình từ notebook nghiên cứu ra sản phẩm vận hành ổn định. Trong y tế, MLOps có thêm lớp phức tạp: dữ liệu bệnh nhân nhạy cảm (PHI), yêu cầu truy vết (traceability) cho cơ quan quản lý (FDA, CE), và hậu quả lâm sàng nghiêm trọng nếu mô hình "drift" (suy giảm hiệu năng theo thời gian) mà không ai phát hiện. Theo các báo cáo ngành ước tính, phần lớn dự án AI y tế thất bại không phải vì mô hình kém mà vì thiếu hạ tầng MLOps để triển khai, giám sát và cập nhật mô hình một cách an toàn.

Khác với phần mềm truyền thống, hệ thống ML y tế có ba "đối tượng" cần versioning đồng thời: mã nguồn, dữ liệu huấn luyện, và bản thân mô hình. Một thay đổi nhỏ trong phân bố dữ liệu đầu vào (ví dụ bệnh viện đổi máy X-quang) có thể làm mô hình sai lệch âm thầm — đây là lý do MLOps y tế đòi hỏi giám sát liên tục (continuous monitoring) chứ không chỉ kiểm định một lần trước khi ra mắt.

Đối với bác sĩ khởi nghiệp HealthTech, hiểu MLOps không có nghĩa là tự code pipeline, mà là biết đặt câu hỏi đúng với đội kỹ thuật: mô hình được retrain khi nào, ai chịu trách nhiệm khi hiệu năng giảm, và làm sao chứng minh với FDA rằng một bản cập nhật mô hình vẫn an toàn như bản đã được phê duyệt.

## 2. Tại sao bác sĩ cần học

- Bác sĩ là người hiểu rõ nhất "model drift lâm sàng" nghĩa là gì — khi nào một sai lệch thống kê thực sự nguy hiểm cho bệnh nhân.
- Cơ quan quản lý (FDA với khung Predetermined Change Control Plan) yêu cầu người có chuyên môn lâm sàng tham gia thiết kế quy trình giám sát mô hình sau khi ra mắt.
- Founder bác sĩ cần đánh giá được rủi ro vận hành AI khi gọi vốn hoặc đàm phán hợp đồng với bệnh viện, tránh cam kết những gì đội kỹ thuật chưa thể đảm bảo.
- Hiểu MLOps giúp bác sĩ thiết kế quy trình phản hồi lâm sàng (clinician feedback loop) hiệu quả, biến bác sĩ sử dụng thành nguồn dữ liệu cải tiến mô hình liên tục.

## 3. Kiến thức nền

- **Model versioning**: quản lý phiên bản mô hình song song với dữ liệu và mã nguồn (công cụ: MLflow, DVC, Weights & Biases).
- **CI/CD/CT**: continuous integration, continuous deployment, và continuous training — tự động hóa việc kiểm thử và triển khai lại mô hình.
- **Data drift & concept drift**: sự thay đổi phân bố dữ liệu đầu vào hoặc mối quan hệ giữa đầu vào-đầu ra theo thời gian.
- **Model monitoring**: theo dõi độ chính xác, độ trễ (latency), và các chỉ số công bằng (fairness) theo thời gian thực.
- **Feature store**: kho lưu trữ đặc trưng (feature) dùng chung giữa huấn luyện và suy luận (inference), tránh lệch train-serving.
- **Shadow deployment & canary release**: triển khai mô hình mới song song với mô hình cũ để so sánh trước khi thay thế hoàn toàn.
- **Human-in-the-loop**: quy trình có bác sĩ xác nhận/ghi đè kết quả AI, vừa đảm bảo an toàn vừa tạo dữ liệu huấn luyện mới.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Không giám sát mô hình sau triển khai | Model drift không phát hiện, sai lệch chẩn đoán âm thầm | Thiết lập dashboard giám sát hiệu năng theo thời gian thực |
| Retrain mô hình mà không kiểm định lại lâm sàng | Vi phạm quy định FDA, mất niềm tin bác sĩ | Áp dụng quy trình change control có phê duyệt |
| Thiếu version control cho dữ liệu | Không tái lập được kết quả, khó debug | Dùng công cụ như DVC, lưu snapshot dữ liệu |
| Bỏ qua fairness theo nhóm dân số | Mô hình phân biệt đối xử, rủi ro pháp lý | Đánh giá hiệu năng theo phân nhóm (giới, tuổi, chủng tộc) |
| Triển khai trực tiếp không qua shadow mode | Sự cố ảnh hưởng bệnh nhân thật ngay lập tức | Chạy song song, so sánh trước khi go-live |
| Không có kế hoạch rollback | Sự cố kéo dài, không thể quay lại phiên bản an toàn | Thiết kế cơ chế rollback tự động |

## 5. Roadmap học (6 tuần)

- **Tuần 1-2**: Nắm khái niệm MLOps cơ bản, phân biệt với DevOps; học qua khóa "MLOps Fundamentals" hoặc tài liệu Google Cloud.
- **Tuần 3**: Tìm hiểu công cụ versioning (MLflow, DVC) qua thực hành trên dataset y tế công khai.
- **Tuần 4**: Học về model monitoring và drift detection (Evidently AI, WhyLabs).
- **Tuần 5**: Nghiên cứu khung quy định FDA về Predetermined Change Control Plan cho AI/ML SaMD.
- **Tuần 6**: Thực hành thiết kế một pipeline MLOps đơn giản end-to-end cho một use case lâm sàng cụ thể.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Designing Machine Learning Systems | Chip Huyen | 2022 | Trung cấp | Tư duy hệ thống ML end-to-end thực chiến | Founder kỹ thuật |
| Introducing MLOps | Treveil et al. | 2020 | Cơ bản | Tổng quan MLOps cho doanh nghiệp | Bác sĩ mới tìm hiểu |
| Machine Learning Design Patterns | Lakshmanan et al. | 2020 | Trung cấp | Mẫu thiết kế phổ biến trong ML production | Kỹ sư ML |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nghiên cứu về dataset shift ảnh hưởng mô hình AI chẩn đoán hình ảnh | Nature Medicine | Tra cứu trên PubMed từ khóa "dataset shift medical imaging AI" | Minh chứng tầm quan trọng của giám sát drift |
| Nghiên cứu về suy giảm hiệu năng mô hình sepsis prediction theo thời gian | JAMIA | Tra cứu PubMed từ khóa "clinical AI model degradation temporal" | Case điển hình cần MLOps trong lâm sàng |
| Khung Predetermined Change Control Plan cho AI/ML SaMD | FDA | 2023-2024 | Cơ sở pháp lý cho retrain mô hình đã phê duyệt |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Good Machine Learning Practice (GMLP) | FDA/Health Canada/MHRA | 2021 | 10 nguyên tắc thiết kế ML y tế |
| AI/ML-Based SaMD Action Plan | FDA | 2021 | Định hướng quản lý vòng đời AI y tế |
| Predetermined Change Control Plan Guidance | FDA | 2024 | Hướng dẫn chi tiết về retrain/cập nhật mô hình |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| MLOps Community | Cộng đồng thực hành MLOps toàn cầu | mlops.community, miễn phí tham gia |
| Made With ML | Tài liệu MLOps thực chiến | madewithml.com |
| FDA Digital Health Center of Excellence | Trang chính thức về AI/ML y tế | fda.gov |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| The Batch | DeepLearning.AI | Tin tức AI ứng dụng |
| MLOps Newsletter | MLOps Community | Thực hành MLOps |
| Import AI | Jack Clark | Xu hướng AI nói chung |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| MLOps.community Podcast | Demetrios Brinkmann | Spotify/Apple Podcasts |
| The TWIML AI Podcast | Sam Charrington | Spotify/Apple Podcasts |
| Practical AI | Chris Benson & Daniel Whitenack | Spotify/Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| MLOps Community | Video hội thảo và phỏng vấn chuyên gia |
| Weights & Biases | Hướng dẫn thực hành monitoring mô hình |
| Google Cloud Tech | Bài giảng MLOps trên nền tảng cloud |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| MLOps Specialization | DeepLearning.AI (Coursera) | 4 tuần | Trả phí (~ có hỗ trợ học bổng) |
| Made With ML Course | Made With ML | Tự học, ~20 giờ | Miễn phí |
| MLOps Zoomcamp | DataTalksClub | 8-9 tuần | Miễn phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| mlflow/mlflow | Nền tảng quản lý vòng đời ML | Open-source, phổ biến nhất |
| iterative/dvc | Version control cho dữ liệu và mô hình | Tích hợp tốt với Git |
| evidentlyai/evidently | Giám sát drift và chất lượng dữ liệu | Có dashboard trực quan |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Weights & Biases | Theo dõi thí nghiệm và mô hình | Quản lý vòng đời training |
| Arize AI | Giám sát mô hình production | Phát hiện drift, đánh giá công bằng |
| Seldon Core | Triển khai mô hình trên Kubernetes | Serving mô hình quy mô lớn |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| Kubeflow | Apache 2.0 | Nền tảng ML trên Kubernetes |
| Feast | Apache 2.0 | Feature store mã nguồn mở |
| Great Expectations | Apache 2.0 | Kiểm định chất lượng dữ liệu tự động |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| MLOps Community (Slack) | Hàng chục nghìn thành viên thực hành MLOps |
| Health AI Partnership | Liên minh nghiên cứu triển khai AI y tế có trách nhiệm |
| DrivenData | Cộng đồng thi đấu và dự án ML vì lợi ích xã hội, bao gồm y tế |

## 18. Case study nổi bật

**Epic Sepsis Model**: Một mô hình dự báo nhiễm khuẩn huyết được triển khai rộng rãi tại Mỹ nhưng sau đó bị phát hiện hiệu năng thực tế thấp hơn nhiều so với công bố khi kiểm định độc lập trên dữ liệu thực tế đa trung tâm — bài học kinh điển về tầm quan trọng của giám sát hiệu năng sau triển khai và kiểm định độc lập ngoài dữ liệu huấn luyện.

**Google DeepMind Streams (AKI)**: Ứng dụng cảnh báo tổn thương thận cấp cho thấy giá trị của việc có quy trình phản hồi lâm sàng chặt chẽ, nhưng cũng bộc lộ thách thức về tích hợp workflow và duy trì hiệu năng khi mở rộng sang bệnh viện khác.

**Bài học chung**: mô hình AI y tế xuất sắc trong nghiên cứu vẫn có thể thất bại khi triển khai thực tế nếu thiếu quy trình MLOps giám sát drift, phản hồi lâm sàng và cập nhật mô hình có kiểm soát.

## 19. Checklist thực hành

- [ ] Xác định các chỉ số hiệu năng lâm sàng cần giám sát liên tục
- [ ] Thiết lập version control cho dữ liệu, mã nguồn và mô hình
- [ ] Xây dựng pipeline CI/CD cho việc kiểm thử mô hình tự động
- [ ] Triển khai dashboard giám sát drift theo thời gian thực
- [ ] Thiết kế quy trình human-in-the-loop cho bác sĩ xác nhận kết quả
- [ ] Lập kế hoạch retrain định kỳ và tiêu chí kích hoạt retrain
- [ ] Xây dựng cơ chế rollback khi phát hiện sự cố
- [ ] Đánh giá công bằng (fairness) theo các phân nhóm bệnh nhân
- [ ] Ghi log đầy đủ cho mục đích kiểm toán và truy vết
- [ ] Chuẩn bị tài liệu Predetermined Change Control Plan nếu áp dụng FDA
- [ ] Thử nghiệm shadow deployment trước khi go-live
- [ ] Đào tạo đội ngũ lâm sàng về cách báo cáo bất thường của mô hình

## 20. Project thực hành

1. **Dashboard giám sát drift**: Xây dựng dashboard theo dõi phân bố dữ liệu đầu vào của một mô hình chẩn đoán mẫu; công cụ Evidently AI; KPI: phát hiện drift trong vòng 24 giờ.
2. **Pipeline CI/CT tối giản**: Thiết lập pipeline tự động retrain khi có dữ liệu mới đạt ngưỡng; công cụ MLflow + GitHub Actions; KPI: thời gian từ phát hiện drift đến triển khai lại dưới 1 tuần.
3. **Vòng phản hồi lâm sàng**: Thiết kế giao diện đơn giản để bác sĩ xác nhận/sửa kết quả AI, lưu lại làm dữ liệu huấn luyện; KPI: tỷ lệ phản hồi trên 30% số ca sử dụng.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu |
|---|---|
| Thời gian phát hiện model drift | Dưới 48 giờ |
| Tỷ lệ uptime hệ thống suy luận | Trên 99.5% |
| Độ trễ suy luận (inference latency) | Phù hợp workflow lâm sàng (thường dưới vài giây) |
| Tần suất retrain có kiểm soát | Theo lịch hoặc theo ngưỡng drift đã định nghĩa |
| Tỷ lệ phản hồi từ bác sĩ sử dụng | Trên 20-30% số lượt sử dụng |

## 22. Tài nguyên miễn phí

- Tài liệu Made With ML (madewithml.com)
- Khóa MLOps Zoomcamp của DataTalksClub trên GitHub
- Tài liệu FDA Digital Health Center of Excellence
- Blog kỹ thuật của Evidently AI và Arize AI

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| MLOps Specialization (Coursera) | ~2-3 triệu VNĐ (ước tính, tùy khu vực) | Chứng chỉ có cấu trúc, bài tập thực hành |
| Weights & Biases (gói team) | Theo mức sử dụng, có gói miễn phí giới hạn | Theo dõi thí nghiệm chuyên nghiệp |
| Tư vấn triển khai MLOps từ đối tác cloud | Thay đổi theo dự án | Triển khai nhanh, giảm rủi ro kỹ thuật |

## 24. Những tài liệu bắt buộc đọc

1. FDA Good Machine Learning Practice (GMLP) — 10 nguyên tắc
2. FDA AI/ML-Based SaMD Action Plan
3. Predetermined Change Control Plan Guidance của FDA
4. Chương liên quan trong "Designing Machine Learning Systems" của Chip Huyen về monitoring
5. Case study Epic Sepsis Model (tìm đọc các phân tích độc lập đã công bố)

## 25. Lộ trình ưu tiên đọc

1. FDA AI/ML-Based SaMD Action Plan (nắm bối cảnh quy định trước tiên)
2. Good Machine Learning Practice (GMLP)
3. Introducing MLOps (nền tảng khái niệm)
4. Designing Machine Learning Systems — chương monitoring và drift
5. Predetermined Change Control Plan Guidance (áp dụng thực tế khi sản phẩm gần ra mắt)
