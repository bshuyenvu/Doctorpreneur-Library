# 46 — Computer Vision y khoa

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Thiết kế hệ thống thị giác có khả năng tổng quát.
> **Sản phẩm của chương:** CV validation matrix.

---

## 1. Tóm tắt điều hành

Computer vision (thị giác máy) phân tích hình ảnh y khoa — X-quang, CT, MRI, nội soi, bệnh phẩm, ảnh da liễu/đáy mắt. Đây là mảng AI y tế nhiều ứng dụng nhất nhưng cũng nhiều báo cáo hiệu năng lạc quan không tái lập được ngoài thực tế. Chìa khóa là khả năng tổng quát: hoạt động ổn định qua thiết bị, cơ sở và quần thể khác nhau. Đầu ra là *CV validation matrix*: ma trận đánh giá hệ thống thị giác qua nhiều chiều biến thiên để lộ giới hạn tổng quát.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu tác vụ CV y khoa và nguồn biến thiên ảnh; (b) nhận diện nguyên nhân kém tổng quát (thiết bị, quần thể, artefact); (c) thiết kế đánh giá đa chiều; (d) phác CV validation matrix.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Mô hình CV thường giòn: đổi máy chụp hay bệnh viện là hiệu năng tụt. Là bác sĩ, bạn hiểu biến thiên lâm sàng thực và nhận ra khi mô hình học artefact thay vì bệnh lý — lợi thế thiết kế đánh giá bắt được giới hạn thật.

## 4. Khái niệm cốt lõi và định nghĩa

**Tác vụ CV:** phân loại, phát hiện (detection), phân vùng (segmentation). **Domain shift:** khác biệt phân phối giữa nguồn dữ liệu. **Artefact:** yếu tố ngoài bệnh lý (dấu, thiết bị, tư thế). **Generalization:** khả năng hoạt động ngoài dữ liệu huấn luyện. **Ground truth:** nhãn chuẩn (do chuyên gia/kết quả khẳng định). **Subgroup performance:** hiệu năng theo nhóm con.

## 5. Khung tư duy nền tảng

Đánh giá qua ma trận nhiều chiều biến thiên: thiết bị/máy chụp, cơ sở, quần thể (tuổi, giới, chủng tộc/tông da), độ nặng bệnh, và điều kiện chụp. Với mỗi ô, đo hiệu năng và so với ground truth chất lượng. Kiểm tra mô hình dựa vào đặc trưng bệnh lý hay artefact (chương 43). Nguyên tắc: hiệu năng trung bình che giấu thất bại nhóm con; validation phải bóc tách theo chiều để lộ giới hạn.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Thiết bị chụp ở tuyến cơ sở đa dạng và có thể khác dữ liệu huấn luyện của mô hình thương mại. Quần thể Việt Nam có thể khác quần thể huấn luyện. Do đó validation trên dữ liệu địa phương (thiết bị, quần thể thực) là bắt buộc trước triển khai — không tin hiệu năng công bố ở nơi khác.

## 7. Các bên liên quan

Bác sĩ chuyên khoa hình ảnh/giải phẫu bệnh (ground truth và đánh giá), kỹ sư CV, và kỹ thuật viên. Ground truth chất lượng và đánh giá chế độ thất bại cần chuyên môn lâm sàng.

## 8. Quy trình từng bước

1. **Xác định tác vụ** và ground truth chuẩn.
2. **Liệt kê chiều biến thiên** (thiết bị, cơ sở, quần thể, độ nặng...).
3. **Thu dữ liệu đánh giá** phủ các chiều (đặc biệt địa phương).
4. **Đo hiệu năng theo từng ô** ma trận.
5. **Kiểm tra artefact/shortcut** và thất bại nhóm con.
6. **Lập CV validation matrix** và kết luận về giới hạn tổng quát.

## 9. Công cụ và template áp dụng

- **CV validation matrix:** chiều biến thiên × hiệu năng × ground truth.
- **Subgroup analysis table.**
- **Artefact/shortcut checklist.**

## 10. Ví dụ minh họa

Mô hình phát hiện bất thường trên X-quang. Validation matrix theo: hãng máy chụp, cơ sở, nhóm tuổi, độ nặng. Nếu hiệu năng tốt ở máy A nhưng tụt ở máy B, đó là domain shift cần xử lý trước triển khai. Kiểm tra mô hình có dựa vào text/marker trên phim không. Ground truth do bác sĩ hình ảnh xác nhận. Số liệu từ dữ liệu thật.

## 11. Sai lầm thường gặp

- **Chỉ báo hiệu năng trung bình**, giấu thất bại nhóm con.
- **Bỏ qua domain shift** (thiết bị/cơ sở).
- **Học artefact** thay vì bệnh lý.
- **Ground truth kém** (một người đọc, không khẳng định).
- **Không validation địa phương.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

CV sai (bỏ sót/dương tính giả) gây hại; thất bại nhóm con gây bất công (chương 48). Cần human oversight và quản lý AI sai (chương 24, 37). Sản phẩm phục vụ chẩn đoán là thiết bị y tế (chương 20) cần bằng chứng validation (chương 47). Dữ liệu hình ảnh cần ẩn danh và bảo mật (chương 40).

## 13. Chỉ số đo lường

Hiệu năng theo từng ô ma trận (không chỉ trung bình), khoảng cách hiệu năng giữa các nhóm/thiết bị (đo độ giòn), tỉ lệ artefact-driven, và hiệu năng địa phương. Ưu tiên tính tổng quát và công bằng.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng công bố trên một dataset **không dự báo hiệu năng tại cơ sở khác**; domain shift là quy luật, không ngoại lệ. Cần validation đa chiều và địa phương (chương 47). Ghi rõ điều kiện (thiết bị, quần thể) và giới hạn tổng quát.

## 15. Tiêu chuẩn và guideline liên quan

Gắn deep learning (chương 43), validation (chương 47), responsible AI (chương 48), hình ảnh/PACS (chương 37), thiết bị y tế (chương 20). Tham chiếu chuẩn báo cáo AI hình ảnh khi áp dụng.

## 16. Liên hệ các chương khác

Ứng dụng của **43**; tích hợp **37**; đánh giá **47**; công bằng **48**; vận hành **50**; thiết bị **20**.

## 17. Bài tập thực hành — CV validation matrix

Lập CV validation matrix cho một mô hình: xác định tác vụ và ground truth, liệt kê chiều biến thiên (thiết bị, cơ sở, quần thể, độ nặng), thiết kế thu dữ liệu phủ các chiều gồm địa phương, đo hiệu năng theo ô, và kiểm tra artefact/shortcut + nhóm con. Kết luận về giới hạn tổng quát. Ghi rõ điều cần validation thực tế.

## 18. Checklist tự đánh giá

- [ ] Đánh giá theo nhiều chiều biến thiên, không chỉ trung bình.
- [ ] Có validation trên thiết bị/quần thể địa phương.
- [ ] Kiểm tra artefact/shortcut learning.
- [ ] Phân tích hiệu năng nhóm con (công bằng).
- [ ] Ground truth chất lượng.

## 19. Định nghĩa hoàn thành (Definition of Done)

CV validation matrix đạt chuẩn khi đánh giá đa chiều gồm địa phương, bóc tách hiệu năng nhóm con, kiểm tra artefact, dùng ground truth chất lượng, và kết luận rõ về giới hạn tổng quát.

## 20. Câu hỏi phản tư

Mô hình của tôi tổng quát qua thiết bị/cơ sở/quần thể nào? Nó dựa vào bệnh lý hay artefact? Nhóm nào bị hiệu năng kém? Tôi đã validation trên dữ liệu địa phương chưa?

## 21. Cạm bẫy quyết định

**Hiệu năng trung bình che thất bại**, **bỏ qua domain shift**. Đối trọng: validation đa chiều, phân tích nhóm con, và kiểm tra artefact.

## 22. Nguồn dữ liệu động cần xác minh

Hiệu năng theo thiết bị/quần thể, đặc điểm dữ liệu địa phương, quy định AI hình ảnh — là dữ liệu động. Validation thực tế và tra nguồn; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md), [Case Studies](../../case-studies/idoven.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Detection/Segmentation:** phát hiện/phân vùng. **Domain shift:** khác biệt phân phối. **Artefact:** yếu tố ngoài bệnh lý. **Generalization:** khả năng tổng quát. **Subgroup performance:** hiệu năng nhóm con.

## 25. Tóm tắt và bước tiếp theo

CV y khoa đáng tin khi được đánh giá đa chiều để lộ giới hạn tổng quát và thất bại nhóm con, với validation địa phương. Tiếp theo sang **[chương 47 — Thẩm định AI y tế](../47-ai-validation/README.md)** cho khung validation đầy đủ.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Hiệu năng CV công bố không dự báo hiệu năng tại cơ sở khác — cần validation đa chiều/địa phương; mô hình có thể học artefact và thất bại nhóm con; giữ human oversight.
