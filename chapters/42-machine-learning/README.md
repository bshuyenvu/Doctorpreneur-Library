# 42. Machine Learning cho bác sĩ

Machine Learning (học máy) là nền tảng toán học và kỹ thuật đứng sau phần lớn các sản phẩm AI y tế hiện đại — hiểu nó giúp bác sĩ-founder đối thoại ngang hàng với đội ngũ kỹ thuật và đánh giá đúng giới hạn của công nghệ.

## 1. Giới thiệu

Machine Learning (ML) là nhánh trí tuệ nhân tạo cho phép hệ thống học các mẫu (pattern) từ dữ liệu thay vì được lập trình luật cứng. Trong y tế, ML đã được ứng dụng rộng rãi: từ dự đoán nguy cơ tái nhập viện, phân loại hình ảnh X-quang, đến tối ưu hóa lịch phẫu thuật. Theo các báo cáo ngành ước tính, số lượng thiết bị y tế được FDA cấp phép có thành phần AI/ML đã tăng nhanh trong những năm gần đây, phần lớn tập trung vào chẩn đoán hình ảnh và cảnh báo lâm sàng — con số cụ thể nên được tra cứu trực tiếp từ danh sách công khai của FDA (AI/ML-Enabled Medical Devices list) vì được cập nhật thường xuyên.

Đối với bác sĩ-founder, hiểu ML không có nghĩa là phải tự viết code mô hình, mà là nắm được các khái niệm nền tảng đủ để: đánh giá liệu một bài toán lâm sàng có phù hợp với ML hay không, phát hiện các dấu hiệu mô hình có vấn đề (overfitting, bias, data leakage), và giao tiếp hiệu quả với data scientist/ML engineer khi xây sản phẩm. Đây cũng là kiến thức nền cần thiết trước khi đi sâu vào Deep Learning (chương 43) — vốn là một nhánh con chuyên biệt của ML.

Chương này trang bị cho bác sĩ bản đồ khái niệm ML thực dụng, tập trung vào ứng dụng y tế thay vì lý thuyết toán học thuần túy.

## 2. Tại sao bác sĩ cần học

- Hiểu ML giúp founder đánh giá đúng liệu ý tưởng sản phẩm có khả thi về mặt kỹ thuật và dữ liệu hay không, trước khi đầu tư nguồn lực.
- Bác sĩ có thể phát hiện các "cờ đỏ" trong tuyên bố hiệu năng mô hình (ví dụ AUC quá cao trên tập dữ liệu nhỏ) — kỹ năng phản biện quan trọng khi đánh giá đối tác/nhà cung cấp công nghệ.
- Giao tiếp hiệu quả với data scientist bằng ngôn ngữ chung giúp rút ngắn thời gian phát triển sản phẩm và giảm hiểu lầm.
- Hiểu về bias và fairness trong ML giúp founder có trách nhiệm đạo đức khi triển khai công nghệ ảnh hưởng đến các nhóm bệnh nhân khác nhau.

## 3. Kiến thức nền

Khái niệm cốt lõi: supervised learning — học có giám sát, mô hình học từ dữ liệu đã gán nhãn (ví dụ: ảnh X-quang có/không có tổn thương); unsupervised learning — học không giám sát, tìm cấu trúc ẩn trong dữ liệu chưa gán nhãn (phân cụm bệnh nhân); overfitting — mô hình học "thuộc lòng" dữ liệu huấn luyện, hoạt động kém trên dữ liệu mới; train/validation/test split — chia dữ liệu để huấn luyện và đánh giá khách quan; AUC-ROC, sensitivity, specificity — các chỉ số đánh giá hiệu năng mô hình phân loại, quen thuộc với bác sĩ vì tương tự đánh giá xét nghiệm chẩn đoán; feature engineering — quá trình chọn/tạo biến đầu vào cho mô hình; data leakage — lỗi khiến thông tin từ tập test "rò rỉ" vào huấn luyện, gây đánh giá sai lệch hiệu năng thực; algorithmic bias — thiên lệch hệ thống khi mô hình học từ dữ liệu không đại diện đầy đủ các nhóm dân số; model drift — hiệu năng mô hình suy giảm theo thời gian khi dữ liệu thực tế thay đổi so với lúc huấn luyện.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Tin vào một chỉ số hiệu năng duy nhất (ví dụ accuracy) mà không xét ngữ cảnh lâm sàng | Bỏ sót vấn đề nghiêm trọng như mất cân bằng lớp dữ liệu | Đánh giá đa chỉ số (sensitivity, specificity, PPV, NPV) phù hợp bài toán |
| Không kiểm tra data leakage giữa tập huấn luyện và kiểm tra | Hiệu năng báo cáo cao giả tạo, thất bại khi triển khai thực tế | Tách dữ liệu nghiêm ngặt theo bệnh nhân, không theo bản ghi |
| Huấn luyện mô hình trên dữ liệu từ một cơ sở y tế duy nhất | Mô hình không tổng quát hóa tốt sang cơ sở khác | Kiểm định trên dữ liệu đa trung tâm trước khi triển khai rộng |
| Bỏ qua đánh giá bias theo nhóm dân số | Kết quả sai lệch, gây hại cho nhóm thiểu số | Phân tích hiệu năng theo từng phân nhóm (giới tính, chủng tộc, độ tuổi) |
| Coi mô hình là "final" sau khi triển khai một lần | Model drift khiến hiệu năng suy giảm âm thầm theo thời gian | Giám sát hiệu năng liên tục, có kế hoạch tái huấn luyện định kỳ |
| Founder không phân biệt được ML thật với "AI washing" trong marketing | Đầu tư sai chỗ, mất niềm tin đối tác/nhà đầu tư | Yêu cầu minh chứng kỹ thuật cụ thể trước khi tin vào tuyên bố "có AI" |

## 5. Roadmap học (6 tuần)

- **Tuần 1:** Học các khái niệm nền tảng (supervised/unsupervised learning, train/test split) qua khóa học nhập môn.
- **Tuần 2:** Tìm hiểu các chỉ số đánh giá mô hình (AUC-ROC, sensitivity, specificity) và cách diễn giải trong ngữ cảnh lâm sàng.
- **Tuần 3:** Thực hành với một bộ dữ liệu y tế công khai đơn giản (ví dụ dự đoán tiểu đường từ Kaggle) dùng công cụ no-code/low-code.
- **Tuần 4:** Học về bias, fairness và các vấn đề đạo đức trong ML y tế qua case study thực tế.
- **Tuần 5:** Tìm hiểu quy trình FDA cho AI/ML-based SaMD và danh sách thiết bị đã được cấp phép.
- **Tuần 6:** Đánh giá một sản phẩm AI y tế hiện có trên thị trường, phân tích điểm mạnh/yếu về mặt dữ liệu và mô hình.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Deep Medicine | Eric Topol | 2019 | Cơ bản | Tổng quan AI/ML trong y học từ góc nhìn bác sĩ | Mọi bác sĩ-founder |
| Machine Learning Yearning | Andrew Ng | 2018 | Trung bình | Chiến lược thực dụng xây dựng hệ thống ML hiệu quả | Founder muốn hiểu quy trình phát triển ML |
| Weapons of Math Destruction | Cathy O'Neil | 2016 | Cơ bản | Cảnh báo về bias và hậu quả xã hội của thuật toán | Mọi bác sĩ-founder quan tâm đạo đức AI |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Đánh giá hiệu năng mô hình ML dự đoán nguy cơ lâm sàng trên dữ liệu đa trung tâm | Tra cứu trên PubMed theo từ khóa: "machine learning clinical prediction model external validation" | Cập nhật hằng năm | Hiểu tầm quan trọng của validation ngoài |
| Nghiên cứu về bias thuật toán trong các mô hình dự đoán y tế | Tra cứu theo từ khóa: "algorithmic bias healthcare machine learning fairness" | Cập nhật hằng năm | Cơ sở đánh giá công bằng khi triển khai sản phẩm |
| Tổng quan hệ thống về ứng dụng ML trong dự đoán biến chứng lâm sàng | Tra cứu theo từ khóa: "machine learning systematic review clinical outcome prediction" | Cập nhật hằng năm | Bức tranh tổng thể về mức độ trưởng thành công nghệ |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Good Machine Learning Practice for Medical Device Development | FDA/Health Canada/MHRA | 2021 | 10 nguyên tắc phát triển ML an toàn cho thiết bị y tế |
| AI/ML-Based SaMD Action Plan | FDA | Cập nhật định kỳ | Định hướng quản lý phần mềm y tế dựa trên AI/ML |
| TRIPOD-AI / PROBAST-AI | Nhóm nghiên cứu quốc tế | Cập nhật định kỳ | Chuẩn báo cáo và đánh giá chất lượng mô hình dự đoán AI trong y khoa |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| FDA AI/ML-Enabled Medical Devices List | Danh sách công khai thiết bị AI/ML đã cấp phép | Truy cập công khai |
| Kaggle | Nền tảng thi đấu và dữ liệu ML, có nhiều bộ dữ liệu y tế | Truy cập công khai, miễn phí |
| Papers with Code | Tổng hợp nghiên cứu ML kèm mã nguồn | Truy cập công khai |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| Import AI | Jack Clark | Tin tức và phân tích xu hướng AI nói chung |
| The Batch | DeepLearning.AI (Andrew Ng) | Tóm tắt tin tức AI/ML hằng tuần, dễ tiếp cận |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| The TWIML AI Podcast | Sam Charrington | Spotify, Apple Podcasts |
| Data Skeptic | Kyle Polich | Spotify, Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| StatQuest with Josh Starmer | Giải thích trực quan các khái niệm thống kê và ML |
| DeepLearning.AI | Bài giảng chính thức từ Andrew Ng và cộng sự |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí (ước tính) |
|---|---|---|---|
| Machine Learning Specialization | Coursera (Andrew Ng/DeepLearning.AI) | 3 tháng | Miễn phí xem, trả phí lấy chứng chỉ |
| AI For Medicine Specialization | Coursera (DeepLearning.AI) | 2-3 tháng | Miễn phí xem, trả phí lấy chứng chỉ |
| Machine Learning for Healthcare | edX (MIT) | 6-10 tuần | Miễn phí xem, trả phí lấy chứng chỉ |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| scikit-learn | Thư viện ML nền tảng cho Python, dễ tiếp cận | Điểm khởi đầu tốt để thực hành |
| MIT-LCP/mimic-code | Bộ công cụ xử lý dữ liệu MIMIC (ICU dataset nổi tiếng) | Dùng cho thực hành ML y tế thực tế |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| AutoML platforms (Google, Azure, DataRobot) | Tự động hóa xây dựng mô hình ML không cần code sâu | Prototyping nhanh cho founder không chuyên kỹ thuật |
| Công cụ giải thích mô hình (SHAP, LIME) | Diễn giải lý do mô hình đưa ra dự đoán | Tăng độ tin cậy và khả năng kiểm chứng lâm sàng |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| scikit-learn | BSD | Thư viện ML cổ điển, nền tảng cho hầu hết bài toán không phải deep learning |
| MIMIC-IV (dữ liệu, cần xin quyền truy cập) | PhysioNet Credentialed | Bộ dữ liệu ICU lớn dùng rộng rãi trong nghiên cứu ML y tế |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| Machine Learning for Healthcare (MLHC) Conference | Cộng đồng học thuật hàng đầu về ML ứng dụng y tế |
| Kaggle Community | Cộng đồng thực hành ML lớn nhất, có nhiều cuộc thi y tế |

## 18. Case study nổi bật

**Mô hình dự đoán tổn thương thận cấp (dạng tổng hợp từ nghiên cứu công bố):** một số nhóm nghiên cứu lớn đã phát triển mô hình ML dự đoán sớm tổn thương thận cấp từ dữ liệu EHR, cho thấy khả năng cảnh báo trước nhiều giờ so với chẩn đoán lâm sàng thông thường trong môi trường nghiên cứu. Bài học cho founder: khoảng cách giữa hiệu năng mô hình trong nghiên cứu và giá trị lâm sàng thực tế (liệu cảnh báo sớm có dẫn đến can thiệp hiệu quả hơn hay không) là câu hỏi riêng biệt cần được kiểm chứng bằng thử nghiệm lâm sàng.

**Startup xây dựng mô hình ML dự đoán nguy cơ tái nhập viện cho bệnh viện:** một số công ty HealthTech tập trung vào bài toán vận hành (tái nhập viện, no-show, phân bổ giường bệnh) thay vì chẩn đoán trực tiếp, nhờ đó tránh được rào cản quản lý FDA nặng nề trong khi vẫn tạo giá trị đo lường được (tiết kiệm chi phí, cải thiện vận hành). Bài học: không phải mọi ứng dụng ML y tế đều cần "chẩn đoán" — bài toán vận hành lâm sàng thường có đường đi đến thị trường ngắn hơn.

## 19. Checklist thực hành

- [ ] Xác định rõ bài toán lâm sàng/vận hành cụ thể mà ML sẽ giải quyết.
- [ ] Đánh giá tính sẵn có và chất lượng dữ liệu cần thiết trước khi cam kết xây mô hình.
- [ ] Hiểu và có thể giải thích các chỉ số đánh giá mô hình (AUC, sensitivity, specificity) phù hợp bài toán.
- [ ] Kiểm tra nguy cơ data leakage trong thiết kế pipeline dữ liệu.
- [ ] Đánh giá hiệu năng mô hình theo từng phân nhóm dân số để phát hiện bias.
- [ ] Xác định mô hình có thuộc diện quản lý SaMD của FDA hay không.
- [ ] Thiết lập cơ chế giám sát model drift sau triển khai.
- [ ] Chuẩn bị lớp giải thích (explainability) phù hợp với người dùng lâm sàng.
- [ ] Kiểm định mô hình trên dữ liệu ngoài (external validation) trước khi mở rộng.
- [ ] Xây dựng tài liệu minh bạch về giới hạn và phạm vi áp dụng của mô hình.

## 20. Project thực hành

1. **Xây dựng mô hình dự đoán đơn giản trên bộ dữ liệu y tế công khai:** ví dụ dự đoán nguy cơ tiểu đường từ dữ liệu Kaggle/UCI. Công cụ: Python, scikit-learn hoặc nền tảng AutoML. KPI: đạt AUC hợp lý và hiểu rõ ý nghĩa từng chỉ số đánh giá.
2. **Đánh giá bias của một mô hình có sẵn:** phân tích hiệu năng mô hình theo nhóm giới tính/độ tuổi trên bộ dữ liệu công khai. Công cụ: Python, thư viện fairness (ví dụ Fairlearn). KPI: xác định được ít nhất một khoảng cách hiệu năng đáng chú ý giữa các nhóm.
3. **Rà soát một sản phẩm AI y tế trên thị trường qua lăng kính ML:** đọc tài liệu công khai (FDA summary, whitepaper) của một sản phẩm AI/ML-SaMD đã được cấp phép, phân tích dữ liệu huấn luyện, phương pháp validation. Công cụ: FDA AI/ML-Enabled Medical Devices List. KPI: viết được bản đánh giá điểm mạnh/yếu có căn cứ.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu giai đoạn đầu |
|---|---|
| AUC-ROC trên tập validation | Vượt ngưỡng chấp nhận được cho bài toán cụ thể, có so sánh với baseline lâm sàng |
| Chênh lệch hiệu năng giữa các phân nhóm dân số | Càng nhỏ càng tốt, có ngưỡng chấp nhận rõ ràng |
| Tỷ lệ mô hình vượt qua external validation | 100% trước khi triển khai lâm sàng |
| Tần suất giám sát/tái đánh giá model drift | Định kỳ, có lịch trình rõ ràng (ví dụ hằng quý) |

## 22. Tài nguyên miễn phí

- Machine Learning Specialization (Coursera, chế độ audit miễn phí).
- FDA AI/ML-Enabled Medical Devices List — dữ liệu công khai.
- Papers with Code — nghiên cứu và mã nguồn mở miễn phí.

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| AI For Medicine Specialization (chứng chỉ) | Vài chục đến vài trăm USD | Kiến thức ứng dụng ML y tế có chứng nhận |
| Quyền truy cập bộ dữ liệu MIMIC-IV (yêu cầu khóa học CITI) | Chi phí thời gian hoàn thành khóa đào tạo đạo đức, miễn phí truy cập dữ liệu | Thực hành trên dữ liệu ICU thực tế, quy mô lớn |
| Nền tảng AutoML thương mại | Gói thuê bao theo mức sử dụng | Rút ngắn thời gian phát triển mô hình prototype |

## 24. Những tài liệu bắt buộc đọc

1. Good Machine Learning Practice for Medical Device Development (FDA/Health Canada/MHRA).
2. FDA AI/ML-Based SaMD Action Plan.
3. Deep Medicine (Eric Topol) — các chương về ML trong lâm sàng.
4. Một tổng quan hệ thống về validation mô hình dự đoán ML y tế (tự tra cứu PubMed).
5. Weapons of Math Destruction — hiểu rủi ro đạo đức của thuật toán trong xã hội.

## 25. Lộ trình ưu tiên đọc

1. Deep Medicine (bối cảnh tổng quan, dễ tiếp cận nhất).
2. Good Machine Learning Practice (nguyên tắc phát triển an toàn).
3. FDA AI/ML-Based SaMD Action Plan (hiểu hướng quản lý).
4. Một nghiên cứu validation ML tiêu biểu cho lĩnh vực bạn quan tâm.
5. Weapons of Math Destruction (khi sản phẩm chuẩn bị triển khai rộng, cần cân nhắc đạo đức).
