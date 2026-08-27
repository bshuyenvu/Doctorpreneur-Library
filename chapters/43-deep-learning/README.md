# 43. Deep Learning y khoa

Deep Learning (học sâu) — nhánh Machine Learning dựa trên mạng nơ-ron nhiều lớp — là công nghệ đứng sau các đột phá ấn tượng nhất trong chẩn đoán hình ảnh y khoa và các mô hình ngôn ngữ lớn ứng dụng lâm sàng.

## 1. Giới thiệu

Deep Learning sử dụng mạng nơ-ron nhân tạo nhiều lớp (deep neural networks) để tự động học các đặc trưng phức tạp từ dữ liệu thô — ảnh, tín hiệu, văn bản — mà không cần con người thiết kế thủ công đặc trưng đầu vào như ML truyền thống. Trong y khoa, deep learning đã đạt hiệu năng ngang hoặc vượt bác sĩ chuyên khoa trong một số bài toán hẹp và được kiểm chứng kỹ (phát hiện bệnh võng mạc tiểu đường từ ảnh đáy mắt, phát hiện ung thư da từ ảnh da liễu, phát hiện nốt phổi từ CT), đồng thời là nền tảng của các mô hình ngôn ngữ lớn (LLM) đang được thử nghiệm cho tóm tắt bệnh án và hỗ trợ chẩn đoán. Theo các báo cáo ngành ước tính, phần lớn các thiết bị AI/ML y tế được FDA cấp phép gần đây thuộc nhóm hình ảnh học (radiology), phản ánh mức độ trưởng thành của deep learning trong lĩnh vực này — số liệu cụ thể nên tra cứu từ danh sách FDA AI/ML-Enabled Medical Devices vì cập nhật liên tục.

Đối với bác sĩ-founder, deep learning là công nghệ có tiềm năng lớn nhưng cũng đòi hỏi lượng dữ liệu, hạ tầng tính toán và chuyên môn kỹ thuật đáng kể hơn nhiều so với ML truyền thống. Hiểu được deep learning phù hợp cho bài toán nào (dữ liệu phi cấu trúc: ảnh, tín hiệu, văn bản) và khi nào ML truyền thống đã đủ (dữ liệu bảng có cấu trúc) giúp founder tránh lãng phí nguồn lực xây dựng công nghệ phức tạp không cần thiết.

Chương này là phần tiếp nối chương 42 (Machine Learning cho bác sĩ), tập trung sâu vào deep learning và các ứng dụng đặc thù y khoa.

## 2. Tại sao bác sĩ cần học

- Deep learning là công nghệ nền của phần lớn sản phẩm AI chẩn đoán hình ảnh — founder trong mảng radiology/pathology/dermatology cần hiểu sâu để đánh giá đối tác công nghệ.
- Hiểu về nhu cầu dữ liệu khổng lồ của deep learning giúp founder lập kế hoạch thu thập dữ liệu thực tế thay vì đánh giá thấp độ khó.
- Là nền tảng để hiểu các mô hình ngôn ngữ lớn (LLM) — công nghệ đang định hình lại cách bác sĩ tương tác với hồ sơ bệnh án và tài liệu y khoa.
- Founder cần phân biệt được deep learning "thật" (được huấn luyện và kiểm chứng kỹ) với các sản phẩm gắn mác AI thiếu minh chứng khoa học.

## 3. Kiến thức nền

Khái niệm cốt lõi: neural network — mạng nơ-ron nhân tạo, các lớp nút tính toán mô phỏng đơn giản hóa nơ-ron sinh học; CNN (Convolutional Neural Network) — kiến trúc chuyên xử lý ảnh, nền tảng của hầu hết mô hình chẩn đoán hình ảnh y khoa; transformer — kiến trúc hiện đại đứng sau các LLM (GPT, Claude, Gemini), ngày càng được dùng cho cả ảnh và tín hiệu y khoa; transfer learning — tận dụng mô hình đã huấn luyện trên dữ liệu lớn (không nhất thiết y tế) rồi tinh chỉnh cho bài toán y khoa với ít dữ liệu hơn — kỹ thuật quan trọng vì dữ liệu y tế thường khan hiếm; end-to-end learning — mô hình học trực tiếp từ dữ liệu thô đến kết quả, không qua bước trích xuất đặc trưng thủ công; GPU/compute requirement — nhu cầu tính toán lớn, ảnh hưởng trực tiếp đến chi phí phát triển; large language model (LLM) — mô hình ngôn ngữ lớn dựa trên transformer, ứng dụng trong tóm tắt bệnh án, trợ lý lâm sàng; hallucination — hiện tượng LLM tạo ra thông tin sai nhưng nghe có vẻ hợp lý, rủi ro đặc biệt nghiêm trọng trong ngữ cảnh y khoa.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Dùng deep learning cho bài toán dữ liệu bảng đơn giản | Phức tạp hóa không cần thiết, tốn tài nguyên vô ích | Đánh giá ML truyền thống trước, chỉ dùng deep learning khi thực sự cần (ảnh, tín hiệu, văn bản) |
| Đánh giá thấp lượng dữ liệu cần để huấn luyện mô hình tốt | Mô hình overfitting, hiệu năng kém khi triển khai | Lập kế hoạch thu thập dữ liệu thực tế hoặc dùng transfer learning |
| Tin tưởng đầu ra của LLM y khoa mà không kiểm chứng | Rủi ro hallucination dẫn đến sai sót lâm sàng nghiêm trọng | Luôn có bác sĩ xác minh, không dùng LLM cho quyết định lâm sàng trực tiếp không giám sát |
| Không kiểm tra khả năng tổng quát hóa trên thiết bị/máy quét khác | Mô hình chẩn đoán hình ảnh thất bại khi đổi máy chụp/protocol | Huấn luyện và kiểm định trên dữ liệu đa nguồn, đa thiết bị |
| Bỏ qua chi phí hạ tầng tính toán khi lập ngân sách | Vượt ngân sách nghiêm trọng trong giai đoạn phát triển | Ước tính chi phí GPU/cloud compute ngay từ giai đoạn lập kế hoạch |
| Không có chiến lược giải thích kết quả cho bác sĩ sử dụng | Thiếu niềm tin lâm sàng, khó được chấp nhận | Dùng kỹ thuật trực quan hóa (heatmap, saliency map) hỗ trợ diễn giải |

## 5. Roadmap học (6 tuần)

- **Tuần 1:** Ôn lại kiến thức ML nền tảng (chương 42) nếu chưa vững, học khái niệm neural network cơ bản.
- **Tuần 2:** Tìm hiểu CNN và ứng dụng trong chẩn đoán hình ảnh y khoa qua case study cụ thể.
- **Tuần 3:** Tìm hiểu kiến trúc transformer và cách LLM hoạt động ở mức khái niệm.
- **Tuần 4:** Học về transfer learning và tại sao đây là chiến lược thực dụng cho startup có ít dữ liệu.
- **Tuần 5:** Tìm hiểu về hallucination, giới hạn của LLM trong ngữ cảnh y khoa và các biện pháp giảm thiểu rủi ro (RAG, fine-tuning, guardrails).
- **Tuần 6:** Thực hành thử nghiệm một mô hình deep learning có sẵn (pretrained) trên bài toán y khoa đơn giản qua công cụ no-code/low-code.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Deep Medicine | Eric Topol | 2019 | Cơ bản | Tổng quan deep learning và AI trong y học từ góc nhìn bác sĩ | Mọi bác sĩ-founder |
| Deep Learning for Coders with fastai and PyTorch | Jeremy Howard, Sylvain Gugger | 2020 | Trung bình-Nâng cao | Hướng dẫn thực hành deep learning theo cách tiếp cận từ trên xuống | Founder muốn thực hành trực tiếp |
| The Alignment Problem | Brian Christian | 2020 | Trung bình | Vấn đề an toàn và đạo đức của mô hình AI hiện đại | Founder quan tâm rủi ro AI |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nghiên cứu so sánh hiệu năng deep learning và bác sĩ chuyên khoa trong chẩn đoán hình ảnh | Tra cứu trên PubMed theo từ khóa: "deep learning diagnostic performance radiologist comparison" | Cập nhật hằng năm | Hiểu mức độ trưởng thành thực tế của công nghệ |
| Đánh giá độ tin cậy và hallucination của LLM trong trả lời câu hỏi y khoa | Tra cứu theo từ khóa: "large language model hallucination medical question answering evaluation" | Cập nhật hằng năm | Cơ sở đánh giá rủi ro khi dùng LLM lâm sàng |
| Tổng quan về transfer learning trong hình ảnh y khoa với dữ liệu hạn chế | Tra cứu theo từ khóa: "transfer learning medical imaging limited data review" | Cập nhật hằng năm | Chiến lược thực dụng cho startup thiếu dữ liệu lớn |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Good Machine Learning Practice for Medical Device Development | FDA/Health Canada/MHRA | 2021 | Áp dụng chung cho cả deep learning trong thiết bị y tế |
| Predetermined Change Control Plans for AI/ML-Enabled Devices | FDA | Cập nhật định kỳ | Hướng dẫn quản lý mô hình được cập nhật liên tục sau triển khai |
| CONSORT-AI / SPIRIT-AI | Nhóm nghiên cứu quốc tế | Cập nhật định kỳ | Chuẩn báo cáo thử nghiệm lâm sàng có can thiệp AI |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| FDA AI/ML-Enabled Medical Devices List | Danh sách công khai thiết bị AI/ML đã cấp phép, phần lớn dùng deep learning | Truy cập công khai |
| Papers with Code | Tổng hợp nghiên cứu deep learning kèm mã nguồn, có mục y tế | Truy cập công khai |
| Hugging Face | Nền tảng chia sẻ mô hình deep learning/LLM, có nhiều mô hình y tế | Truy cập công khai, một số mô hình cần xin quyền |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| The Batch | DeepLearning.AI (Andrew Ng) | Tóm tắt tin tức deep learning hằng tuần |
| Import AI | Jack Clark | Phân tích xu hướng AI/deep learning chuyên sâu |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| The TWIML AI Podcast | Sam Charrington | Spotify, Apple Podcasts |
| Practical AI | Daniel Whitenack, Chris Benson | Spotify, Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| Two Minute Papers | Tóm tắt nghiên cứu deep learning mới, dễ tiếp cận |
| DeepLearning.AI | Bài giảng chính thức từ Andrew Ng và cộng sự |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí (ước tính) |
|---|---|---|---|
| Deep Learning Specialization | Coursera (DeepLearning.AI) | 3-4 tháng | Miễn phí xem, trả phí lấy chứng chỉ |
| AI For Medicine Specialization | Coursera (DeepLearning.AI) | 2-3 tháng | Miễn phí xem, trả phí lấy chứng chỉ |
| Practical Deep Learning for Coders | fast.ai | 8-10 tuần tự học | Hoàn toàn miễn phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| PyTorch | Framework deep learning phổ biến nhất trong nghiên cứu | Nền tảng kỹ thuật chính hiện nay |
| fastai | Thư viện deep learning cấp cao, dễ tiếp cận cho người mới | Điểm khởi đầu thực hành tốt |
| MONAI | Framework deep learning chuyên biệt cho hình ảnh y khoa | Dùng riêng cho bài toán radiology/pathology |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Mô hình phân đoạn ảnh y khoa (segmentation) dựa trên deep learning | Tự động khoanh vùng tổn thương/cơ quan trên ảnh | Hỗ trợ lập kế hoạch xạ trị, phẫu thuật |
| LLM y khoa chuyên biệt (medical LLM) | Trả lời câu hỏi, tóm tắt bệnh án dựa trên ngôn ngữ tự nhiên | Hỗ trợ ghi chép, tra cứu thông tin lâm sàng |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| MONAI | Apache 2.0 | Framework deep learning mã nguồn mở chuyên cho hình ảnh y khoa |
| PyTorch | BSD | Framework deep learning nền tảng, cộng đồng lớn nhất |
| Hugging Face Transformers | Apache 2.0 | Thư viện mô hình transformer/LLM mã nguồn mở |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| MICCAI (Medical Image Computing and Computer Assisted Intervention) | Cộng đồng học thuật hàng đầu về deep learning trong hình ảnh y khoa |
| RSNA AI Community | Cộng đồng radiology ứng dụng AI của Hội Điện quang Bắc Mỹ |

## 18. Case study nổi bật

**Mô hình phát hiện bệnh võng mạc tiểu đường từ ảnh đáy mắt (dạng tổng hợp từ tài liệu công bố):** một số mô hình deep learning được phát triển và kiểm chứng qua nhiều năm đã đạt độ chính xác đủ cao để được cấp phép sử dụng tự động (autonomous AI) trong sàng lọc, không cần bác sĩ chuyên khoa xác nhận từng ca — một cột mốc quan trọng cho thấy deep learning có thể đạt tiêu chuẩn lâm sàng khi được kiểm chứng nghiêm ngặt qua thời gian dài. Bài học cho founder: con đường từ mô hình nghiên cứu đến sản phẩm được cấp phép sử dụng tự động đòi hỏi nhiều năm dữ liệu, kiểm chứng đa trung tâm và thử nghiệm lâm sàng nghiêm túc, không phải là kết quả một sớm một chiều.

**Startup ứng dụng LLM để tóm tắt hội thoại bác sĩ-bệnh nhân (ambient documentation):** một số công ty đã xây dựng sản phẩm dùng mô hình ngôn ngữ lớn để tự động ghi chép bệnh án từ cuộc trò chuyện khám bệnh, giảm đáng kể thời gian bác sĩ dành cho giấy tờ. Bài học: giá trị lớn nhất của deep learning/LLM trong giai đoạn hiện tại thường đến từ việc giảm gánh nặng hành chính (administrative burden) hơn là thay thế quyết định lâm sàng trực tiếp — một hướng đi rủi ro thấp hơn nhưng vẫn tạo giá trị lớn.

## 19. Checklist thực hành

- [ ] Xác định rõ bài toán có thực sự cần deep learning hay ML truyền thống đã đủ.
- [ ] Đánh giá tính khả thi về khối lượng dữ liệu cần thiết, cân nhắc transfer learning nếu dữ liệu hạn chế.
- [ ] Ước tính chi phí hạ tầng tính toán (GPU/cloud) cho giai đoạn phát triển và vận hành.
- [ ] Kiểm định mô hình trên dữ liệu đa nguồn/đa thiết bị trước khi triển khai rộng.
- [ ] Nếu dùng LLM, thiết kế cơ chế giảm thiểu hallucination (RAG, kiểm chứng nguồn, giới hạn phạm vi trả lời).
- [ ] Có bác sĩ xác minh mọi đầu ra quan trọng trước khi ảnh hưởng đến quyết định lâm sàng.
- [ ] Trang bị công cụ trực quan hóa (heatmap/saliency map) để tăng khả năng diễn giải cho bác sĩ dùng.
- [ ] Xác định lộ trình quản lý phù hợp nếu mô hình được cập nhật liên tục sau triển khai (predetermined change control).
- [ ] Thiết lập quy trình giám sát hiệu năng và phát hiện model drift định kỳ.
- [ ] Chuẩn bị minh chứng khoa học (nghiên cứu, thử nghiệm) trước khi đưa ra tuyên bố hiệu năng.

## 20. Project thực hành

1. **Thử nghiệm transfer learning trên bài toán phân loại ảnh y khoa đơn giản:** dùng mô hình CNN pretrained, tinh chỉnh trên một bộ dữ liệu ảnh y khoa công khai nhỏ (ví dụ ảnh da liễu từ nguồn mở). Công cụ: Python, PyTorch/fastai, Google Colab. KPI: đạt độ chính xác hợp lý với lượng dữ liệu hạn chế, hiểu rõ quy trình.
2. **Xây dựng demo ứng dụng LLM cho tóm tắt bệnh án giả lập:** thử nghiệm dùng một LLM có sẵn để tóm tắt ghi chú lâm sàng mẫu (dữ liệu giả lập, không dùng dữ liệu bệnh nhân thật), đánh giá độ chính xác và rủi ro hallucination. Công cụ: API LLM công khai, dữ liệu mẫu tự tạo. KPI: xác định được ít nhất 3 trường hợp hallucination hoặc lỗi cần kiểm soát.
3. **Đánh giá một sản phẩm deep learning y tế đã được FDA cấp phép:** đọc tài liệu công khai (FDA summary of safety and effectiveness) của một sản phẩm AI hình ảnh y khoa, phân tích dữ liệu huấn luyện, kiến trúc mô hình, phương pháp validation. Công cụ: FDA AI/ML-Enabled Medical Devices List. KPI: viết được bản phân tích có căn cứ về con đường phát triển sản phẩm.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu giai đoạn đầu |
|---|---|
| Hiệu năng mô hình so với chuẩn vàng lâm sàng/chuyên gia | Đạt ngưỡng đã kiểm định trong nghiên cứu, có so sánh đối chứng |
| Khả năng tổng quát hóa trên dữ liệu ngoài (external validation) | Duy trì hiệu năng chấp nhận được trên ít nhất một nguồn dữ liệu độc lập |
| Tỷ lệ đầu ra LLM cần bác sĩ chỉnh sửa/xác minh lại | Theo dõi và giảm dần, không bao giờ bằng 0 (luôn cần giám sát) |
| Chi phí tính toán trên mỗi lượt suy luận (inference cost) | Tối ưu để đảm bảo mô hình kinh doanh bền vững |

## 22. Tài nguyên miễn phí

- Practical Deep Learning for Coders (fast.ai) — khóa học thực hành hoàn toàn miễn phí.
- FDA AI/ML-Enabled Medical Devices List — dữ liệu công khai.
- MONAI, PyTorch, Hugging Face — framework và mô hình mã nguồn mở.

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Deep Learning Specialization (chứng chỉ) | Vài chục đến vài trăm USD | Kiến thức nền tảng deep learning có chứng nhận |
| Hạ tầng GPU cloud (AWS/GCP/Azure) | Chi phí theo giờ sử dụng, có thể lên đến hàng nghìn USD/tháng | Huấn luyện mô hình quy mô lớn không cần đầu tư phần cứng |
| API LLM thương mại cấp doanh nghiệp | Gói thuê bao theo mức sử dụng | Truy cập mô hình ngôn ngữ mạnh mà không cần tự huấn luyện |

## 24. Những tài liệu bắt buộc đọc

1. Good Machine Learning Practice for Medical Device Development (FDA/Health Canada/MHRA).
2. FDA Predetermined Change Control Plans for AI/ML-Enabled Devices.
3. Deep Medicine (Eric Topol) — các chương về deep learning trong chẩn đoán hình ảnh.
4. Một nghiên cứu tiêu biểu về hiệu năng deep learning so với chuyên gia (tự tra cứu PubMed theo chuyên khoa quan tâm).
5. Một tổng quan về hallucination trong LLM y khoa (tự tra cứu PubMed).

## 25. Lộ trình ưu tiên đọc

1. Deep Medicine (bối cảnh tổng quan, dễ tiếp cận nhất).
2. Nghiên cứu so sánh hiệu năng deep learning và chuyên gia cho lĩnh vực bạn quan tâm.
3. Good Machine Learning Practice (nguyên tắc phát triển an toàn).
4. FDA Predetermined Change Control Plans (khi mô hình cần cập nhật liên tục).
5. Nghiên cứu về hallucination LLM (nếu sản phẩm có thành phần ngôn ngữ tự nhiên).
