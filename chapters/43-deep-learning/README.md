# 43 — Deep Learning y khoa

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Hiểu kiến trúc, dữ liệu và lỗi thường gặp.
> **Sản phẩm của chương:** Deep-learning evaluation plan.

---

## 1. Tóm tắt điều hành

Deep learning (mạng nơ-ron nhiều lớp) mạnh với dữ liệu phi cấu trúc — hình ảnh, tín hiệu, văn bản — và đứng sau nhiều tiến bộ AI y tế. Nhưng nó "đói" dữ liệu, khó diễn giải, và dễ thất bại theo cách khó phát hiện (shortcut learning, kém tổng quát ngoài phân phối). Chương này giúp bác sĩ hiểu đủ để đánh giá và giám sát, không để bị "hộp đen" đánh lừa. Đầu ra là *deep-learning evaluation plan*: kế hoạch đánh giá một mô hình deep learning nhấn tính tổng quát và các chế độ thất bại.

## 2. Mục tiêu học tập

Bạn sẽ: (a) nắm khái niệm kiến trúc deep learning và nhu cầu dữ liệu; (b) hiểu các chế độ thất bại (shortcut learning, out-of-distribution, adversarial); (c) thiết kế đánh giá tính tổng quát; (d) phác evaluation plan gắn an toàn lâm sàng.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Deep learning dễ tạo hiệu năng ấn tượng nhưng giòn: học "đường tắt" giả (ví dụ nhận diện thiết bị chụp thay vì bệnh lý). Hiểu điều này giúp bạn đòi bằng chứng tổng quát thực và tránh triển khai mô hình nguy hiểm.

## 4. Khái niệm cốt lõi và định nghĩa

**Mạng nơ-ron sâu:** mô hình nhiều lớp học biểu diễn. **CNN/Transformer:** kiến trúc phổ biến cho ảnh/chuỗi. **Shortcut learning:** học đặc trưng giả tương quan. **Out-of-distribution (OOD):** dữ liệu khác phân phối huấn luyện. **Adversarial example:** đầu vào nhiễu đánh lừa mô hình. **Explainability:** khả năng giải thích quyết định.

## 5. Khung tư duy nền tảng

Nhấn *tính tổng quát* và *chế độ thất bại* hơn hiệu năng trung bình: đánh giá trên dữ liệu ngoại bộ (cơ sở/thiết bị khác), kiểm tra shortcut learning (mô hình dựa vào gì?), và hành vi OOD. Dùng công cụ giải thích (ví dụ bản đồ nổi bật) thận trọng — chúng gợi ý, không chứng minh. Nguyên tắc: deep learning cần validation ngoại bộ nghiêm ngặt hơn (chương 47) vì dễ giòn; luôn có human oversight.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Dữ liệu đủ lớn và đa dạng để huấn luyện deep learning là ràng buộc lớn ở tuyến cơ sở. Mô hình tiền huấn luyện/chuyển giao (transfer learning) có thể giúp, nhưng phải validation trên dữ liệu địa phương vì khác biệt thiết bị/quần thể gây kém tổng quát. Cân nhắc chi phí hạ tầng tính toán.

## 7. Các bên liên quan

Khoa học dữ liệu/ML engineer, bác sĩ chuyên khoa (đánh giá ý nghĩa và chế độ thất bại lâm sàng), và QA. Đánh giá chế độ thất bại cần chuyên môn lâm sàng để nhận ra "đường tắt" nguy hiểm.

## 8. Quy trình từng bước

1. **Xác định bài toán** và vì sao cần deep learning (vs ML đơn giản).
2. **Đánh giá dữ liệu** (đủ lớn, đa dạng, đại diện).
3. **Thiết kế đánh giá tổng quát** (validation ngoại bộ).
4. **Kiểm tra chế độ thất bại** (shortcut, OOD, nhóm nhỏ).
5. **Dùng explainability** thận trọng để hiểu quyết định.
6. **Lập evaluation plan** với oversight và giám sát.

## 9. Công cụ và template áp dụng

- **Deep-learning evaluation plan:** dữ liệu · validation ngoại bộ · kiểm tra shortcut/OOD · nhóm nhỏ · explainability · oversight.
- **Failure mode checklist.**
- **Bảng so sánh với ML đơn giản/baseline.**

## 10. Ví dụ minh họa

Mô hình phân loại ảnh da liễu. Evaluation plan: validation trên ảnh từ thiết bị/cơ sở khác; kiểm tra shortcut (mô hình có dựa vào dấu bút/thước trên ảnh không?); hiệu năng trên các tông da khác nhau (thiên lệch); explainability để soi vùng mô hình chú ý. Nếu mô hình dựa artefact thay vì tổn thương, không triển khai. Số liệu phải từ dữ liệu thật.

## 11. Sai lầm thường gặp

- **Chỉ đánh giá nội bộ**, bỏ validation ngoại bộ.
- **Bỏ qua shortcut learning.**
- **Không kiểm OOD** và nhóm nhỏ (thiên lệch).
- **Tin explainability như bằng chứng.**
- **Dùng deep learning khi ML đơn giản đủ.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Mô hình giòn hoặc học đường tắt thất bại nguy hiểm và khó phát hiện. Thiên lệch theo nhóm (ví dụ tông da, giới) gây bất công (chương 48). Tính "hộp đen" đòi human oversight mạnh và validation nghiêm (chương 47). Sản phẩm chạm chẩn đoán chịu quản lý thiết bị y tế (chương 20).

## 13. Chỉ số đo lường

Hiệu năng trên validation ngoại bộ, khoảng cách nội bộ–ngoại bộ (đo độ giòn), hiệu năng nhóm con, và kết quả kiểm tra chế độ thất bại. Ưu tiên tính tổng quát và an toàn hơn hiệu năng đỉnh.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng nội bộ của deep learning **đặc biệt dễ lạc quan** do khả năng ghi nhớ và shortcut. Cần validation ngoại bộ/tiền cứu (chương 47). Explainability là công cụ hỗ trợ, không phải chứng minh nhân quả. Ghi rõ giới hạn và điều kiện.

## 15. Tiêu chuẩn và guideline liên quan

Gắn validation (chương 47), responsible AI (chương 48), MLOps (chương 50), thiết bị y tế (chương 20), computer vision (chương 46). Tham chiếu chuẩn báo cáo AI y tế và Good Machine Learning Practice khi áp dụng.

## 16. Liên hệ các chương khác

Nối **42**; ứng dụng ở **45–46** (NLP, computer vision); đánh giá **47**; đạo đức **48**; vận hành **50**; hình ảnh **37**.

## 17. Bài tập thực hành — Deep-learning evaluation plan

Lập evaluation plan cho một mô hình: biện minh vì sao cần deep learning, đánh giá dữ liệu, thiết kế validation ngoại bộ, kiểm tra chế độ thất bại (shortcut/OOD/nhóm nhỏ), dùng explainability thận trọng, và oversight. Ghi rõ giới hạn và điều cần validation thực tế.

## 18. Checklist tự đánh giá

- [ ] Biện minh deep learning vs ML đơn giản.
- [ ] Có validation ngoại bộ.
- [ ] Kiểm tra shortcut learning và OOD.
- [ ] Đánh giá thiên lệch nhóm con.
- [ ] Human oversight và giám sát.

## 19. Định nghĩa hoàn thành (Definition of Done)

Deep-learning evaluation plan đạt chuẩn khi có validation ngoại bộ, kiểm tra chế độ thất bại và thiên lệch, dùng explainability thận trọng, và gắn oversight + giám sát vòng đời.

## 20. Câu hỏi phản tư

Mô hình của tôi dựa vào đặc trưng thật hay đường tắt? Nó tổng quát sang cơ sở/thiết bị khác không? Nó có thiên lệch nhóm nào không? Tôi có human oversight đủ mạnh chưa?

## 21. Cạm bẫy quyết định

**Tin hiệu năng nội bộ**, **shortcut learning ẩn**, **hộp đen**. Đối trọng: validation ngoại bộ, kiểm tra chế độ thất bại, và oversight lâm sàng.

## 22. Nguồn dữ liệu động cần xác minh

Hiệu năng tổng quát theo cơ sở, kiến trúc/kỹ thuật cập nhật, hướng dẫn AI y tế — là dữ liệu động. Validation thực tế và tra nguồn chính thức; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md), [Open source](../../resources/open-source-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**CNN/Transformer:** kiến trúc mạng. **Shortcut learning:** học đặc trưng giả. **OOD:** ngoài phân phối. **Adversarial example:** đầu vào đánh lừa. **Explainability:** khả năng giải thích.

## 25. Tóm tắt và bước tiếp theo

Deep learning mạnh nhưng giòn; đánh giá phải nhấn tính tổng quát, chế độ thất bại và thiên lệch, với validation ngoại bộ và oversight. Tiếp theo sang **[chương 44 — Generative AI trong y tế](../44-generative-ai/README.md)** cho lớp mô hình sinh.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Hiệu năng nội bộ deep learning dễ lạc quan — cần validation ngoại bộ; mô hình có thể học đường tắt và thiên lệch; giữ human oversight.
