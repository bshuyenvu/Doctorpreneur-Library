# 45 — NLP lâm sàng

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Xử lý văn bản y khoa và đánh giá đầu ra.
> **Sản phẩm của chương:** Clinical NLP test set.

---

## 1. Tóm tắt điều hành

NLP lâm sàng xử lý văn bản y khoa — bệnh án, phiếu, y văn — để trích xuất, phân loại, tóm tắt hoặc mã hóa. Văn bản lâm sàng có đặc thù khó: viết tắt, thuật ngữ, phủ định ("không sốt"), ngữ cảnh thời gian, và tiếng Việt có ít công cụ/tài nguyên hơn tiếng Anh. Chất lượng phụ thuộc đánh giá nghiêm trên dữ liệu đại diện. Đầu ra là *clinical NLP test set*: bộ dữ liệu kiểm thử được xây có kỷ luật để đánh giá một hệ NLP lâm sàng.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu các tác vụ NLP lâm sàng và thách thức đặc thù; (b) nhận diện lỗi nguy hiểm (bỏ phủ định, sai ngữ cảnh); (c) thiết kế bộ test đại diện với ground truth; (d) chọn thước đo đánh giá phù hợp.

## 3. Vì sao chương này quan trọng với Doctorpreneur

NLP lâm sàng sai (ví dụ bỏ qua "không" trong "không đau ngực") tạo trích xuất nguy hiểm. Là bác sĩ, bạn hiểu ngữ cảnh và biết ca nào dễ sai — lợi thế xây bộ test bắt được lỗi thật thay vì chỉ đo trên ca dễ.

## 4. Khái niệm cốt lõi và định nghĩa

**Tác vụ NLP:** trích xuất thực thể (NER), phân loại, tóm tắt, mã hóa (gán ICD...). **Phủ định (negation):** xử lý "không/loại trừ". **Ngữ cảnh (context):** thời gian, người (bệnh nhân vs gia đình), giả định. **Ground truth:** nhãn tham chiếu do chuyên gia gán. **Inter-annotator agreement:** độ đồng thuận giữa người gán nhãn. **F1/precision/recall:** thước đo đánh giá.

## 5. Khung tư duy nền tảng

Chất lượng NLP đánh giá bằng bộ test đại diện, không bằng demo. Xây ground truth với người gán nhãn có chuyên môn và đo độ đồng thuận. Đưa vào bộ test các ca khó và nguy hiểm (phủ định, viết tắt, ngữ cảnh gia đình, thời gian quá khứ). Chọn thước đo theo hậu quả lỗi (ví dụ recall cao cho phát hiện triệu chứng nguy hiểm). Nguyên tắc: lỗi ngữ nghĩa (phủ định, ngữ cảnh) nguy hiểm hơn lỗi bề mặt — bộ test phải bắt được chúng.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Tiếng Việt lâm sàng có ít công cụ/từ điển chuẩn hóa và corpus so với tiếng Anh; viết tắt và pha trộn ngôn ngữ phổ biến. Cần xây tài nguyên và bộ test tiếng Việt riêng, không giả định công cụ tiếng Anh hoạt động tốt. Dữ liệu văn bản lâm sàng chứa thông tin định danh — cần ẩn danh và cơ sở pháp lý (chương 40).

## 7. Các bên liên quan

Bác sĩ/chuyên gia gán nhãn (ground truth), kỹ sư NLP, và quản lý dữ liệu. Ground truth chất lượng cần chuyên môn lâm sàng và quy trình gán nhãn nhất quán.

## 8. Quy trình từng bước

1. **Xác định tác vụ** và định nghĩa nhãn rõ.
2. **Chọn dữ liệu đại diện** (gồm ca khó/nguy hiểm).
3. **Xây ground truth** với hướng dẫn gán nhãn; đo đồng thuận.
4. **Đưa ca thử thách** (phủ định, ngữ cảnh, viết tắt) vào bộ test.
5. **Chọn thước đo** theo hậu quả lỗi.
6. **Lập clinical NLP test set** và quy trình đánh giá.

## 9. Công cụ và template áp dụng

- **Clinical NLP test set:** tác vụ · nhãn · nguồn dữ liệu · ca thử thách · ground truth · thước đo.
- **Hướng dẫn gán nhãn (annotation guideline).**
- **Bảng ca lỗi nguy hiểm** (phủ định, ngữ cảnh...).

## 10. Ví dụ minh họa

Trích xuất triệu chứng từ bệnh án. Test set: gồm ca "không đau ngực", "tiền sử gia đình đột quỵ" (không phải bệnh nhân), "đau ngực cách đây 3 tháng" (thời gian). Nếu hệ NLP gán "đau ngực" cho ca phủ định/gia đình/quá khứ, đó là lỗi nguy hiểm. Ground truth do bác sĩ gán; đo recall cho triệu chứng nguy hiểm. Số liệu từ dữ liệu thật.

## 11. Sai lầm thường gặp

- **Đánh giá trên ca dễ**, bỏ ca thử thách.
- **Bỏ xử lý phủ định/ngữ cảnh.**
- **Ground truth không nhất quán** (không đo đồng thuận).
- **Dùng công cụ tiếng Anh** cho tiếng Việt không hiệu chỉnh.
- **Thước đo không khớp hậu quả lỗi.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Trích xuất sai (bỏ phủ định, nhầm ngữ cảnh) có thể dẫn tới thông tin lâm sàng sai và quyết định sai — cần human oversight cho ứng dụng rủi ro. Văn bản lâm sàng cần ẩn danh và cơ sở pháp lý (chương 40). Ứng dụng chạm quyết định lâm sàng chịu quản lý thiết bị y tế (chương 19–20).

## 13. Chỉ số đo lường

Precision/recall/F1 theo nhãn, hiệu năng trên ca thử thách (phủ định, ngữ cảnh), độ đồng thuận ground truth, và hiệu năng trên tiếng Việt thực tế. Ưu tiên recall cho phát hiện thông tin nguy hiểm.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng demo **không đại diện thực tế**; chỉ bộ test đại diện với ca khó mới đáng tin. Hiệu năng trên corpus khác/tiếng khác không chuyển sang tiếng Việt lâm sàng. Ghi rõ giới hạn dữ liệu và ca chưa bao phủ.

## 15. Tiêu chuẩn và guideline liên quan

Gắn ML/deep learning (chương 42–43), GenAI nếu dùng LLM (chương 44), validation (chương 47), responsible AI (chương 48), dữ liệu (chương 40). Bộ mã (ICD/SNOMED) cho tác vụ mã hóa (chương 36).

## 16. Liên hệ các chương khác

Nối **43–44**; đánh giá **47**; đạo đức **48**; dữ liệu **40**; mã hóa gắn **36**; ứng dụng tài liệu **63**.

## 17. Bài tập thực hành — Clinical NLP test set

Xây clinical NLP test set cho một tác vụ: định nghĩa nhãn, chọn dữ liệu đại diện gồm ca thử thách (phủ định, ngữ cảnh gia đình/thời gian, viết tắt), xây ground truth với hướng dẫn gán nhãn và đo đồng thuận, và chọn thước đo theo hậu quả lỗi. Nêu ràng buộc tiếng Việt và bảo mật. Ghi rõ ca chưa bao phủ.

## 18. Checklist tự đánh giá

- [ ] Bộ test gồm ca khó/nguy hiểm.
- [ ] Xử lý phủ định và ngữ cảnh được đánh giá.
- [ ] Ground truth nhất quán (đo đồng thuận).
- [ ] Đánh giá trên tiếng Việt thực tế.
- [ ] Thước đo khớp hậu quả lỗi.

## 19. Định nghĩa hoàn thành (Definition of Done)

Clinical NLP test set đạt chuẩn khi đại diện gồm ca thử thách, ground truth nhất quán có đo đồng thuận, đánh giá phủ định/ngữ cảnh, thước đo phù hợp hậu quả, và xét đặc thù tiếng Việt + bảo mật.

## 20. Câu hỏi phản tư

Bộ test của tôi có ca phủ định/ngữ cảnh nguy hiểm không? Ground truth có nhất quán không? Hệ NLP có xử lý được tiếng Việt lâm sàng thực không? Thước đo có phản ánh hậu quả lỗi không?

## 21. Cạm bẫy quyết định

**Demo đẹp trên ca dễ**, **bỏ phủ định/ngữ cảnh**. Đối trọng: bộ test đại diện có ca khó, ground truth chất lượng, và human oversight.

## 22. Nguồn dữ liệu động cần xác minh

Công cụ/tài nguyên NLP tiếng Việt, hiệu năng theo corpus, quy định dữ liệu — là dữ liệu động. Đánh giá thực tế và tra nguồn; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md), [Thư viện bài báo](../../resources/paper-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**NER:** trích xuất thực thể. **Negation:** phủ định. **Inter-annotator agreement:** đồng thuận gán nhãn. **F1/precision/recall:** thước đo. **Ground truth:** nhãn tham chiếu.

## 25. Tóm tắt và bước tiếp theo

NLP lâm sàng đáng tin khi được đánh giá trên bộ test đại diện bắt được lỗi ngữ nghĩa nguy hiểm (phủ định, ngữ cảnh), đặc biệt cho tiếng Việt. Tiếp theo sang **[chương 46 — Computer Vision y khoa](../46-computer-vision/README.md)** cho dữ liệu hình ảnh.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Lỗi phủ định/ngữ cảnh trong NLP lâm sàng nguy hiểm — cần bộ test đại diện và oversight; văn bản lâm sàng cần ẩn danh và cơ sở pháp lý.
