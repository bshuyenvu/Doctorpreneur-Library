# 46. Computer Vision y khoa

Ứng dụng thị giác máy tính (computer vision) trong chẩn đoán hình ảnh y khoa — từ X-quang, CT, MRI đến bệnh lý số hóa (digital pathology).

## 1. Giới thiệu

Computer vision (CV) y khoa là lĩnh vực AI tập trung phân tích hình ảnh y tế — X-quang, CT, MRI, siêu âm, ảnh nội soi, ảnh mô bệnh học số hóa, ảnh da liễu và ảnh đáy mắt — để hỗ trợ phát hiện, phân loại và định lượng tổn thương. Đây là một trong những lĩnh vực AI y tế trưởng thành nhất về mặt quy định: nhiều sản phẩm CV đã được FDA cấp phép lưu hành (ví dụ các hệ thống phát hiện bệnh võng mạc đái tháo đường, phát hiện đột quỵ trên CT, phát hiện nốt phổi trên X-quang ngực).

Theo các báo cáo ngành ước tính, thị trường AI chẩn đoán hình ảnh y tế toàn cầu đang tăng trưởng với tốc độ hai chữ số mỗi năm, được thúc đẩy bởi tình trạng thiếu hụt bác sĩ chẩn đoán hình ảnh và nhu cầu tăng độ chính xác, giảm thời gian đọc phim (đây là số liệu minh họa, cần tự tra cứu báo cáo thị trường cập nhật để có con số chính xác). Các công ty tiêu biểu gồm Aidoc, Viz.ai, PathAI, Paige, IDx (nay là Digital Diagnostics) — nhiều công ty trong số này do bác sĩ hoặc nhóm liên ngành bác sĩ-kỹ sư sáng lập.

Đối với bác sĩ khởi nghiệp, CV y khoa là mảng có rào cản kỹ thuật cao nhưng cũng có giá trị lâm sàng rõ ràng và dễ đo lường (độ nhạy, độ đặc hiệu so với chuyên gia), khiến việc gọi vốn và xin phê duyệt quy định có lộ trình tương đối rõ ràng hơn so với các mảng AI y tế khác.

## 2. Tại sao bác sĩ cần học

- **Lĩnh vực AI y tế đã được kiểm chứng lâm sàng nhiều nhất**: Hiểu CV giúp bác sĩ founder học hỏi từ các case đã thành công để tránh sai lầm lặp lại.
- **Đòi hỏi hiểu biết lâm sàng sâu để thiết kế đúng bài toán**: Chọn sai tiêu chí gán nhãn (labeling) hoặc bỏ sót ca biên (edge case) là nguyên nhân phổ biến khiến mô hình CV thất bại khi triển khai thực tế.
- **Cơ hội hợp tác với khoa chẩn đoán hình ảnh, giải phẫu bệnh**: Bác sĩ hiểu quy trình đọc phim/đọc lam có lợi thế lớn khi thiết kế workflow tích hợp AI.
- **Quy trình phê duyệt quy định tương đối rõ ràng**: FDA và các cơ quan quản lý đã có nhiều tiền lệ (predicate devices) cho phần mềm CV chẩn đoán hình ảnh, giúp con đường thương mại hóa dễ hình dung hơn.

## 3. Kiến thức nền

- **Convolutional Neural Network (CNN)**: kiến trúc mạng nơ-ron tích chập, nền tảng truyền thống của CV.
- **Vision Transformer (ViT)**: kiến trúc dựa trên Transformer áp dụng cho ảnh, ngày càng phổ biến trong CV y khoa hiện đại.
- **Segmentation vs. Classification vs. Detection**: phân biệt bài toán phân vùng tổn thương, phân loại ảnh, và phát hiện vị trí đối tượng.
- **Digital pathology / whole-slide imaging**: số hóa lam mô bệnh học độ phân giải cực cao để phân tích bằng AI.
- **Ground truth labeling**: quy trình gán nhãn chuẩn (thường bởi nhiều chuyên gia) làm cơ sở huấn luyện và đánh giá mô hình.
- **Domain shift**: hiện tượng mô hình giảm hiệu suất khi áp dụng trên dữ liệu từ máy chụp/quy trình khác với dữ liệu huấn luyện.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Huấn luyện trên dữ liệu từ một loại máy/một trung tâm | Mô hình thất bại khi dùng ở nơi khác (domain shift) | Thu thập dữ liệu đa trung tâm, đa thiết bị |
| Gán nhãn bởi một chuyên gia duy nhất | Nhãn không đáng tin cậy, mô hình học sai | Dùng nhiều chuyên gia gán nhãn độc lập, đo độ đồng thuận |
| Đánh giá mô hình chỉ bằng độ chính xác tổng thể | Bỏ sót vấn đề mất cân bằng lớp (class imbalance) | Dùng độ nhạy, độ đặc hiệu, AUC, PPV/NPV theo tỷ lệ bệnh thực tế |
| Không kiểm tra hiệu suất trên nhóm dân số đa dạng | Thiên lệch chẩn đoán cho một số nhóm bệnh nhân | Đánh giá công bằng (fairness) trên nhiều nhóm nhân khẩu học |
| Bỏ qua tích hợp workflow (PACS, RIS) | Sản phẩm tốt về kỹ thuật nhưng không được dùng thực tế | Thiết kế tích hợp ngay từ đầu với hệ thống hiện có |

## 5. Roadmap học (6 tuần)

- **Tuần 1**: Ôn tập cơ bản về CNN, các kiến trúc phổ biến (ResNet, U-Net).
- **Tuần 2**: Tìm hiểu bài toán phân loại vs. phân vùng vs. phát hiện trong ảnh y khoa.
- **Tuần 3**: Nghiên cứu quy trình gán nhãn và đánh giá mô hình CV y khoa (độ nhạy/đặc hiệu, AUC).
- **Tuần 4**: Tìm hiểu các sản phẩm CV y khoa đã được FDA cấp phép — phân tích use case và bằng chứng lâm sàng.
- **Tuần 5**: Học về digital pathology và các thách thức đặc thù (ảnh độ phân giải siêu cao).
- **Tuần 6**: Thực hành với bộ dữ liệu ảnh y khoa công khai (ví dụ NIH Chest X-ray) để xây mô hình phân loại đơn giản.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Deep Learning for Medical Image Analysis | S. Kevin Zhou và cộng sự | 2017 (có bản cập nhật) | Kỹ thuật | Tổng quan học thuật về CV y khoa | Người muốn hiểu sâu kỹ thuật |
| Deep Medicine | Eric Topol | 2019 | Trung cấp | Có chương riêng về AI trong chẩn đoán hình ảnh | Bác sĩ founder muốn tầm nhìn tổng thể |
| Artificial Intelligence in Radiology | Erik Ranschaert và cộng sự | 2019 | Trung cấp | Chuyên sâu ứng dụng AI trong chẩn đoán hình ảnh | Bác sĩ chẩn đoán hình ảnh muốn khởi nghiệp |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Hiệu quả AI phát hiện bệnh võng mạc đái tháo đường | Tra cứu PubMed từ khóa "AI diabetic retinopathy screening validation" | Cập nhật liên tục | Bằng chứng lâm sàng cho một trong các sản phẩm CV y tế thành công đầu tiên được FDA duyệt |
| So sánh hiệu suất AI và bác sĩ chẩn đoán hình ảnh trong phát hiện ung thư vú | Tra cứu PubMed từ khóa "AI mammography breast cancer detection accuracy" | Cập nhật liên tục | Đánh giá độ tin cậy AI so với chuyên gia |
| Thách thức domain shift trong AI chẩn đoán hình ảnh đa trung tâm | Tra cứu PubMed/arXiv từ khóa "domain shift medical imaging AI generalization" | Cập nhật liên tục | Hiểu rủi ro khi triển khai đa trung tâm |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| FDA List of AI/ML-Enabled Medical Devices | FDA (Hoa Kỳ) | Cập nhật liên tục | Danh sách sản phẩm CV y tế đã được cấp phép |
| ACR AI-LAB / ACR Data Science Institute Guidance | American College of Radiology | Cập nhật liên tục | Hướng dẫn triển khai AI trong chẩn đoán hình ảnh |
| CLAIM (Checklist for AI in Medical Imaging) | Radiology (RSNA) | 2020 | Chuẩn báo cáo nghiên cứu AI chẩn đoán hình ảnh |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| Papers with Code (Medical Imaging) | Tổng hợp nghiên cứu và mã nguồn CV y khoa | Miễn phí |
| RSNA AI website | Tài nguyên AI chẩn đoán hình ảnh từ hiệp hội chuyên ngành | Miễn phí |
| Grand Challenge | Nền tảng tổ chức thi và chia sẻ bộ dữ liệu CV y khoa | Miễn phí |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| Radiology AI Newsletter (RSNA) | RSNA | AI chẩn đoán hình ảnh |
| The Batch | DeepLearning.AI | AI nói chung, có tin CV y tế |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| AI in Medicine Podcast | Nhiều host khách mời chuyên ngành | Spotify/Apple Podcasts |
| Radiology Firing Line Podcast | ACR | Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| RSNA Learning Center | Video giáo dục AI chẩn đoán hình ảnh |
| Aidoc / Viz.ai official channels | Giới thiệu sản phẩm và case study thực tế |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| AI for Medical Diagnosis | DeepLearning.AI (Coursera) | ~4 tuần | Trả phí |
| Deep Learning for Healthcare Imaging | Các đại học đối tác trên Coursera/edX | ~4-6 tuần | Trả phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| MONAI (Project MONAI) | Framework deep learning chuyên cho ảnh y khoa | Open-source, được NVIDIA và cộng đồng hỗ trợ |
| torchxrayvision | Thư viện phân tích X-quang ngực bằng deep learning | Open-source |
| nnU-Net | Framework phân vùng ảnh y khoa tự động cấu hình | Open-source, hiệu suất cao trong nhiều benchmark |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Aidoc | Nền tảng AI phát hiện bất thường trên CT khẩn cấp | Hỗ trợ ưu tiên đọc phim cấp cứu |
| Viz.ai | AI phát hiện đột quỵ trên CT, kích hoạt quy trình khẩn | Rút ngắn thời gian can thiệp đột quỵ |
| PathAI | Nền tảng AI hỗ trợ chẩn đoán giải phẫu bệnh | Tăng độ chính xác chẩn đoán mô bệnh học |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| MONAI | Apache 2.0 | Bộ công cụ deep learning cho ảnh y khoa |
| nnU-Net | Apache 2.0 | Framework phân vùng ảnh y khoa tự động |
| OpenSlide | LGPL | Thư viện đọc ảnh whole-slide cho digital pathology |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| RSNA (Radiological Society of North America) | Hiệp hội chuyên ngành chẩn đoán hình ảnh, có mảng AI mạnh |
| MICCAI Society | Cộng đồng học thuật hàng đầu về CV y khoa |
| Digital Pathology Association | Cộng đồng chuyên về bệnh lý số hóa và AI |

## 18. Case study nổi bật

**IDx-DR (nay là Digital Diagnostics)**: Do bác sĩ nhãn khoa Michael Abramoff sáng lập, là hệ thống AI đầu tiên được FDA cấp phép hoạt động hoàn toàn tự động (không cần bác sĩ đọc lại) để tầm soát bệnh võng mạc đái tháo đường. Bài học: xây dựng bằng chứng lâm sàng vững chắc và quy trình phê duyệt bài bản ngay từ đầu là chìa khóa cho sản phẩm CV y tế đột phá.

**Viz.ai**: Nền tảng AI phát hiện đột quỵ trên CT, tự động cảnh báo bác sĩ can thiệp mạch để rút ngắn thời gian "door-to-needle". Công ty được thành lập bởi một bác sĩ thần kinh can thiệp, minh chứng cho việc hiểu sâu quy trình cấp cứu lâm sàng giúp thiết kế sản phẩm có tác động thực chất đến kết cục bệnh nhân.

## 19. Checklist thực hành

- [ ] Hiểu sự khác biệt giữa classification, segmentation, detection
- [ ] Nắm quy trình gán nhãn chuẩn và đo độ đồng thuận giữa chuyên gia
- [ ] Hiểu cách đánh giá mô hình CV y khoa (độ nhạy, độ đặc hiệu, AUC)
- [ ] Tìm hiểu ít nhất 3 sản phẩm CV y tế đã được FDA cấp phép
- [ ] Thực hành với bộ dữ liệu ảnh y khoa công khai
- [ ] Hiểu khái niệm domain shift và cách giảm thiểu
- [ ] Thiết kế quy trình tích hợp AI vào workflow PACS/RIS
- [ ] Tìm hiểu chuẩn báo cáo CLAIM cho nghiên cứu AI chẩn đoán hình ảnh
- [ ] Xác định use case lâm sàng cụ thể có giá trị đo lường rõ ràng

## 20. Project thực hành

1. **Mô hình phân loại X-quang ngực cơ bản**: Dùng bộ dữ liệu công khai (ví dụ NIH ChestX-ray14) để huấn luyện mô hình phân loại bất thường. Công cụ: MONAI/PyTorch. KPI: AUC trên tập kiểm định.
2. **Công cụ phân vùng tổn thương trên ảnh MRI/CT giả lập**: Xây dựng pipeline segmentation cơ bản. Công cụ: nnU-Net. KPI: chỉ số Dice score.
3. **Prototype tích hợp cảnh báo AI vào quy trình đọc phim**: Thiết kế giao diện hiển thị kết quả AI bên cạnh phim gốc cho bác sĩ. Công cụ: DICOM viewer mã nguồn mở. KPI: thời gian đọc phim, mức độ hài lòng của bác sĩ thử nghiệm.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu tham khảo |
|---|---|
| AUC mô hình phân loại | > 0.90 trên tập kiểm định độc lập |
| Độ nhạy/độ đặc hiệu | Phù hợp với ngưỡng lâm sàng chấp nhận được cho use case cụ thể |
| Dice score (bài toán phân vùng) | > 0.80 tùy loại tổn thương |
| Thời gian xử lý mỗi ca | Đủ nhanh để tích hợp vào workflow lâm sàng thực tế (thường dưới vài phút) |

## 22. Tài nguyên miễn phí

- Bộ dữ liệu công khai: NIH ChestX-ray14, CheXpert, MIMIC-CXR (cần đăng ký)
- Framework MONAI và tài liệu hướng dẫn miễn phí
- Grand Challenge — nền tảng thi và chia sẻ nghiên cứu CV y khoa miễn phí

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| AI for Medical Diagnosis (Coursera) | ~50 USD/tháng (ước tính) | Kiến thức nền tảng có chứng chỉ |
| GPU cloud computing (AWS/GCP/Azure) | Theo giờ sử dụng | Hạ tầng huấn luyện mô hình CV quy mô lớn |
| Tư vấn quy định FDA/SaMD chuyên biệt | Thay đổi theo đơn vị tư vấn | Rút ngắn thời gian và giảm rủi ro xin phê duyệt |

## 24. Những tài liệu bắt buộc đọc

1. FDA List of AI/ML-Enabled Medical Devices
2. CLAIM checklist (Radiology/RSNA)
3. ACR AI-LAB Guidance
4. Deep Medicine (chương về chẩn đoán hình ảnh)
5. Ít nhất 2 bài báo mới nhất về validation AI chẩn đoán hình ảnh (tự tra cứu PubMed)

## 25. Lộ trình ưu tiên đọc

1. Deep Medicine — tầm nhìn tổng thể về AI chẩn đoán hình ảnh
2. CLAIM checklist — hiểu chuẩn báo cáo nghiên cứu
3. FDA List of AI/ML-Enabled Medical Devices — hiểu bối cảnh sản phẩm đã được duyệt
4. ACR AI-LAB Guidance — hiểu khung triển khai thực tế
5. Các bài báo nghiên cứu mới nhất về sản phẩm CV y tế cùng lĩnh vực quan tâm
