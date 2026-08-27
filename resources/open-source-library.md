# 🧩 Thư viện mã nguồn mở

Danh sách hơn 50 dự án mã nguồn mở liên quan đến dữ liệu y tế, khả năng liên thông (interoperability) và AI trong y học, phân theo nhóm chức năng. Đây là các dự án có thật và được biết đến rộng rãi trong cộng đồng tương ứng; giấy phép, mức độ hoạt động và số liệu (sao GitHub, phiên bản mới nhất...) thay đổi liên tục nên **hãy tự tra cứu trực tiếp tại repository chính thức trước khi sử dụng hoặc trích dẫn**.

> Gợi ý sử dụng: với dữ liệu bệnh nhân thật, luôn tự kiểm tra lại giấy phép sử dụng và mức độ tuân thủ pháp lý (HIPAA/GDPR) của từng dự án — mã nguồn mở không đồng nghĩa với đã được chứng nhận an toàn cho production.

## 1. Hệ thống thông tin y tế & hồ sơ bệnh án điện tử

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 01 | OpenMRS | MPL 2.0 / OpenMRS PL | Nền tảng hồ sơ bệnh án điện tử mã nguồn mở phổ biến nhất tại các nước thu nhập thấp/trung bình. |
| 02 | OpenEMR | GPL v3 | Hệ thống EHR/quản lý phòng khám mã nguồn mở được chứng nhận ONC tại Mỹ. |
| 03 | GNU Health | GPL v3 | Hệ thống thông tin y tế và bệnh viện mã nguồn mở tích hợp cả quản lý và hồ sơ lâm sàng. |
| 04 | Bahmni | AGPL v3 | Hệ thống EMR mã nguồn mở dành cho bệnh viện, xây dựng trên nền OpenMRS. |
| 05 | DHIS2 | BSD 3-Clause | Nền tảng quản lý thông tin y tế cộng đồng được WHO và nhiều quốc gia sử dụng rộng rãi. |
| 06 | Medical-Objects / HAPI HL7v2 | Apache 2.0 | Thư viện xử lý thông điệp HL7 v2 mã nguồn mở phổ biến trong tích hợp hệ thống bệnh viện. |
| 07 | OpenClinica | LGPL | Nền tảng quản lý dữ liệu thử nghiệm lâm sàng (EDC) mã nguồn mở. |
| 08 | REDCap (không hoàn toàn mở, học thuật) | Giấy phép riêng cho tổ chức phi lợi nhuận, tự tra cứu tại project-redcap.org | Nền tảng thu thập dữ liệu nghiên cứu lâm sàng được sử dụng rộng rãi trong học thuật. |

## 2. Chuẩn hóa dữ liệu, FHIR & khả năng liên thông

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 09 | HAPI FHIR | Apache 2.0 | Thư viện Java mã nguồn mở triển khai đầy đủ chuẩn HL7 FHIR, dùng rộng rãi để xây server FHIR. |
| 10 | Microsoft FHIR Server (FHIR Server for Azure) | MIT | Máy chủ FHIR mã nguồn mở của Microsoft, triển khai được trên Azure. |
| 11 | Google FHIR (google-fhir) | Apache 2.0 | Thư viện và công cụ mã nguồn mở của Google hỗ trợ xử lý dữ liệu FHIR ở quy mô lớn. |
| 12 | Firely .NET SDK | BSD 3-Clause | Bộ SDK .NET mã nguồn mở phổ biến để làm việc với FHIR. |
| 13 | Synthea | Apache 2.0 | Công cụ mã nguồn mở tạo dữ liệu bệnh nhân giả lập (synthetic) thực tế để test hệ thống mà không vi phạm quyền riêng tư. |
| 14 | Mirth Connect (NextGen Connect) | MPL 1.1 | Engine tích hợp (interface engine) mã nguồn mở phổ biến để kết nối HL7 v2/FHIR giữa các hệ thống y tế. |
| 15 | IHE Gazelle | Giấy phép hỗn hợp theo module, tự tra cứu tại gazelle.ihe.net | Bộ công cụ kiểm thử tuân thủ chuẩn liên thông IHE (Integrating the Healthcare Enterprise). |
| 16 | SNOMED CT International Edition (thuật ngữ, không phải phần mềm) | Cấp phép theo SNOMED International, tự tra cứu | Hệ thống thuật ngữ lâm sàng chuẩn hóa toàn cầu — nền tảng để mã hóa dữ liệu lâm sàng có cấu trúc. |
| 17 | LOINC | Cấp phép sử dụng miễn phí có đăng ký, tự tra cứu tại loinc.org | Chuẩn mã hóa quốc tế cho xét nghiệm và quan sát lâm sàng. |

## 3. Mô hình dữ liệu chung & nghiên cứu quan sát

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 18 | OHDSI / OMOP Common Data Model | Apache 2.0 | Mô hình dữ liệu chung (Common Data Model) cho phép nghiên cứu quan sát trên nhiều nguồn dữ liệu khác nhau. |
| 19 | ATLAS (OHDSI) | Apache 2.0 | Công cụ web mã nguồn mở để thiết kế và phân tích nghiên cứu trên dữ liệu OMOP. |
| 20 | Achilles (OHDSI) | Apache 2.0 | Công cụ mã nguồn mở đánh giá chất lượng và mô tả đặc điểm dữ liệu OMOP CDM. |
| 21 | i2b2/tranSMART | GPL v3 | Nền tảng mã nguồn mở tích hợp dữ liệu lâm sàng và nghiên cứu chuyển dịch (translational research). |
| 22 | PCORnet Common Data Model | Giấy phép mở theo PCORnet, tự tra cứu | Mô hình dữ liệu chung cho mạng lưới nghiên cứu hướng đến kết quả do bệnh nhân báo cáo tại Mỹ. |

## 4. AI/Machine Learning nền tảng & y sinh

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 23 | scikit-learn | BSD 3-Clause | Thư viện machine learning cổ điển phổ biến nhất trong Python, nền tảng cho hầu hết dự án ML. |
| 24 | TensorFlow | Apache 2.0 | Framework deep learning mã nguồn mở của Google, dùng rộng rãi trong nghiên cứu AI y tế. |
| 25 | PyTorch | BSD 3-Clause (BSD-style) | Framework deep learning mã nguồn mở của Meta, phổ biến nhất trong nghiên cứu AI hiện nay. |
| 26 | MONAI | Apache 2.0 | Framework mã nguồn mở dựa trên PyTorch chuyên biệt cho hình ảnh y khoa, do NVIDIA/King's College London khởi xướng. |
| 27 | Hugging Face Transformers | Apache 2.0 | Thư viện mã nguồn mở cung cấp hàng nghìn mô hình ngôn ngữ/AI pretrained, bao gồm nhiều mô hình y sinh. |
| 28 | BioBERT | Apache 2.0 | Mô hình ngôn ngữ pretrained chuyên biệt cho văn bản y sinh, dựa trên kiến trúc BERT. |
| 29 | ClinicalBERT | Giấy phép theo repository cụ thể, tự tra cứu trên GitHub | Mô hình ngôn ngữ pretrained trên ghi chú lâm sàng (MIMIC-III), dùng cho NLP lâm sàng. |
| 30 | scispaCy | MIT | Thư viện NLP mã nguồn mở chuyên biệt cho văn bản khoa học và y sinh, xây trên nền spaCy. |
| 31 | MedCAT | Elastic License 2.0 / MIT (tùy phiên bản, tự kiểm tra) | Công cụ trích xuất khái niệm y khoa có cấu trúc từ văn bản lâm sàng phi cấu trúc (NLP). |
| 32 | cTAKES (Apache) | Apache 2.0 | Hệ thống trích xuất thông tin lâm sàng mã nguồn mở của Apache, chuyên xử lý ghi chú y khoa. |
| 33 | RDKit | BSD 3-Clause | Bộ công cụ mã nguồn mở cho tin học hóa học (cheminformatics), dùng trong nghiên cứu phát triển thuốc. |
| 34 | DeepChem | MIT | Thư viện mã nguồn mở ứng dụng deep learning vào hóa học, sinh học và khám phá thuốc. |
| 35 | AlphaFold (mã nguồn + trọng số mô hình) | Apache 2.0 (mã nguồn); giấy phép riêng cho trọng số mô hình, tự kiểm tra | Mô hình AI dự đoán cấu trúc protein của DeepMind, công khai mã nguồn cho nghiên cứu. |
| 36 | ESM (Evolutionary Scale Modeling, Meta) | MIT | Bộ mô hình ngôn ngữ protein mã nguồn mở của Meta AI cho nghiên cứu sinh học cấu trúc. |

## 5. Hình ảnh y khoa & xử lý tín hiệu sinh học

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 37 | 3D Slicer | BSD-style (Slicer License) | Nền tảng mã nguồn mở hàng đầu để xử lý, phân tích và trực quan hóa hình ảnh y khoa 3D. |
| 38 | ITK (Insight Toolkit) | Apache 2.0 | Thư viện mã nguồn mở nền tảng cho xử lý và phân tích hình ảnh y khoa đa chiều. |
| 39 | VTK (Visualization Toolkit) | BSD 3-Clause | Thư viện mã nguồn mở trực quan hóa dữ liệu khoa học 3D, được dùng rộng rãi cùng ITK. |
| 40 | OHIF Viewer | MIT | Trình xem hình ảnh y khoa (DICOM) mã nguồn mở chạy trên nền web, phổ biến trong nghiên cứu. |
| 41 | dcm4che | Apache 2.0 / MPL 2.0 (tùy module) | Bộ công cụ Java mã nguồn mở xử lý chuẩn DICOM, nền tảng cho nhiều hệ thống PACS. |
| 42 | Orthanc | GPL v3 (bản lõi); có bản thương mại | Máy chủ PACS/DICOM nhẹ, mã nguồn mở, dễ triển khai cho nghiên cứu và phòng khám nhỏ. |
| 43 | pydicom | MIT | Thư viện Python mã nguồn mở đọc/ghi/xử lý file DICOM, phổ biến trong nghiên cứu AI hình ảnh y khoa. |
| 44 | NiBabel | MIT | Thư viện Python mã nguồn mở đọc/ghi định dạng ảnh thần kinh học (NIfTI, v.v.). |
| 45 | FreeSurfer | Giấy phép phi thương mại riêng, tự tra cứu tại surfer.nmr.mgh.harvard.edu | Bộ công cụ phân tích hình ảnh MRI não mã nguồn mở dùng rộng rãi trong nghiên cứu thần kinh học. |
| 46 | NeuroKit2 | MIT | Thư viện Python mã nguồn mở xử lý tín hiệu sinh học (ECG, EDA, EEG...) cho nghiên cứu sinh lý học. |
| 47 | WFDB (PhysioNet) | BSD-style (tùy ngôn ngữ triển khai) | Bộ công cụ mã nguồn mở đọc/ghi tín hiệu sinh lý học, gắn liền với kho dữ liệu PhysioNet. |

## 6. Dữ liệu mở & bộ dữ liệu nghiên cứu

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 48 | MIMIC-III / MIMIC-IV (PhysioNet) | PhysioNet Credentialed Health Data License, tự tra cứu | Bộ dữ liệu ICU lớn được sử dụng rộng rãi nhất trong nghiên cứu AI y tế học thuật (cần xin quyền truy cập). |
| 49 | PhysioNet (nền tảng dữ liệu) | Giấy phép theo từng bộ dữ liệu, tự tra cứu tại physionet.org | Kho lưu trữ dữ liệu sinh lý học và tín hiệu y sinh mở lớn nhất cho nghiên cứu. |
| 50 | UK Biobank (dữ liệu, không phải mã nguồn) | Giấy phép truy cập có kiểm soát, tự tra cứu tại ukbiobank.ac.uk | Kho dữ liệu gen và sức khỏe quy mô lớn của Anh, phục vụ nghiên cứu y sinh (cần đăng ký truy cập). |
| 51 | Synthea | Apache 2.0 | (Xem thêm mục 1) Công cụ tạo dữ liệu bệnh nhân tổng hợp thực tế, an toàn để chia sẻ và thử nghiệm công khai. |
| 52 | OpenNeuro | CC0 (theo từng bộ dữ liệu) | Nền tảng chia sẻ dữ liệu hình ảnh thần kinh học mở, phục vụ nghiên cứu tái lập (reproducibility). |

## 7. Bảo mật, quyền riêng tư & hạ tầng

| Số | Dự án | Giấy phép (ước tính, tự kiểm tra lại) | Mô tả |
|---|---|---|---|
| 53 | Keycloak | Apache 2.0 | Nền tảng quản lý danh tính và truy cập (IAM) mã nguồn mở, dùng để triển khai xác thực cho hệ thống y tế. |
| 54 | HashiCorp Vault | BSL 1.1 (từ 2023, không còn hoàn toàn mã nguồn mở — tự kiểm tra) | Công cụ quản lý bí mật (secrets) và mã hóa, thường dùng để bảo vệ dữ liệu nhạy cảm trong hạ tầng y tế. |
| 55 | Presidio (Microsoft) | MIT | Công cụ mã nguồn mở phát hiện và ẩn danh hóa (de-identify) thông tin định danh cá nhân (PII/PHI) trong văn bản. |
| 56 | Apache Kafka | Apache 2.0 | Nền tảng streaming dữ liệu mã nguồn mở, thường dùng làm xương sống tích hợp dữ liệu thời gian thực cho hệ thống y tế lớn. |
| 57 | Apache Airflow | Apache 2.0 | Công cụ điều phối pipeline dữ liệu mã nguồn mở, phổ biến trong xử lý dữ liệu lâm sàng theo lô. |

---

**Lưu ý về độ chính xác:** giấy phép ghi trong bảng là **ước tính** dựa trên hiểu biết chung về từng dự án tại thời điểm biên soạn — một số dự án có nhiều module với giấy phép khác nhau, hoặc đã đổi mô hình cấp phép theo thời gian (ví dụ chuyển từ mã nguồn mở hoàn toàn sang "open core"/business source license). Trước khi sử dụng trong sản phẩm thương mại — đặc biệt là sản phẩm xử lý dữ liệu bệnh nhân — hãy tự kiểm tra file LICENSE trong repository chính thức trên GitHub/GitLab và tham khảo ý kiến pháp lý nếu cần.
