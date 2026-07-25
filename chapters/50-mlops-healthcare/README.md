# 50 — MLOps trong y tế

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Theo dõi drift, versioning và vận hành mô hình.
> **Sản phẩm của chương:** MLOps monitoring plan.

---

## 1. Tóm tắt điều hành

Một mô hình AI validation tốt hôm nay có thể suy giảm ngày mai: dữ liệu đổi (data drift), thực hành đổi (concept drift), thiết bị đổi. MLOps là tập thực hành vận hành mô hình trong sản xuất — versioning, giám sát hiệu năng và drift, tái huấn luyện có kiểm soát, và khả năng khôi phục. Trong y tế, giám sát liên tục là vấn đề an toàn: mô hình suy giảm âm thầm có thể gây hại. Đầu ra là *MLOps monitoring plan*: kế hoạch giám sát và vận hành mô hình suốt vòng đời.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu các loại drift và tác động; (b) thiết kế giám sát hiệu năng và drift trong sản xuất; (c) quản lý version và tái huấn luyện có kiểm soát; (d) phác MLOps monitoring plan gắn an toàn.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Triển khai AI không phải điểm kết thúc mà là bắt đầu trách nhiệm vận hành. Không giám sát, mô hình suy giảm âm thầm gây rủi ro an toàn và trách nhiệm pháp lý. Hiểu MLOps giúp bạn giữ AI an toàn suốt vòng đời, không chỉ lúc ra mắt.

## 4. Khái niệm cốt lõi và định nghĩa

**Data drift:** phân phối đầu vào đổi. **Concept drift:** quan hệ đầu vào–kết cục đổi. **Model versioning:** quản lý phiên bản mô hình/dữ liệu. **Monitoring:** giám sát hiệu năng/drift trong sản xuất. **Retraining:** tái huấn luyện. **Rollback:** khôi phục phiên bản trước. **Shadow deployment:** chạy phiên bản mới song song trước khi thay.

## 5. Khung tư duy nền tảng

Coi mô hình như hệ thống cần giám sát liên tục, không phải artefact tĩnh. Giám sát hai lớp: đầu vào (drift) và đầu ra/hiệu năng (khi có ground truth trễ). Thiết lập ngưỡng cảnh báo, quy trình điều tra, và tái huấn luyện có kiểm soát (với validation lại — chương 47 — trước khi thay). Nguyên tắc: mọi thay đổi mô hình phải qua kiểm soát thay đổi (gắn QMS — chương 23) và validation lại; có khả năng rollback nhanh khi suy giảm.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Ở tuyến cơ sở, nguồn lực giám sát hạn chế; cần thiết kế giám sát khả thi (cảnh báo tự động, quy trình đơn giản). Ground truth để đo hiệu năng thực thường trễ (chờ kết cục) — dùng proxy và drift đầu vào để cảnh báo sớm. Thay đổi thực hành/thiết bị địa phương là nguồn drift cần theo dõi.

## 7. Các bên liên quan

Khoa học dữ liệu/ML engineer, CNTT vận hành, QA/regulatory, và bác sĩ (phát hiện suy giảm qua trải nghiệm). Trách nhiệm giám sát và ứng phó phải rõ (gắn chương 48).

## 8. Quy trình từng bước

1. **Xác định chỉ số giám sát** (drift đầu vào, hiệu năng, proxy).
2. **Thiết lập ngưỡng cảnh báo** và quy trình điều tra.
3. **Quản lý version** mô hình/dữ liệu và kiểm soát thay đổi.
4. **Thiết kế tái huấn luyện + validation lại** (chương 47).
5. **Thiết lập rollback và shadow deployment.**
6. **Lập MLOps monitoring plan** gắn QMS và trách nhiệm.

## 9. Công cụ và template áp dụng

- **MLOps monitoring plan:** chỉ số · ngưỡng · quy trình ứng phó · versioning · tái huấn luyện · rollback · trách nhiệm.
- **Model registry** (version, dữ liệu, validation).
- **Change control log** (gắn QMS).

## 10. Ví dụ minh họa

Mô hình dự báo triển khai. Monitoring plan: giám sát drift đầu vào (đặc trưng bệnh nhân đổi), theo dõi hiệu năng khi ground truth kết cục về, cảnh báo khi vượt ngưỡng; nếu suy giảm, điều tra và tái huấn luyện với validation lại trước khi thay; giữ khả năng rollback. Mọi thay đổi qua change control. Số liệu từ vận hành thật.

## 11. Sai lầm thường gặp

- **Triển khai rồi bỏ mặc** (không giám sát).
- **Không phát hiện drift** cho tới khi gây hại.
- **Tái huấn luyện không validation lại.**
- **Thiếu versioning/rollback.**
- **Thay đổi mô hình ngoài kiểm soát thay đổi.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Mô hình suy giảm không giám sát gây hại âm thầm — rủi ro an toàn và trách nhiệm. Thay đổi mô hình mà không validation lại có thể đưa lỗi mới; trong nhiều khung pháp lý, thay đổi cần kiểm soát và có thể cần đánh giá lại (chương 19–22). Giám sát công bằng liên tục để drift không tạo thiên lệch mới (chương 48).

## 13. Chỉ số đo lường

Độ trễ phát hiện drift/suy giảm, tần suất và kết quả tái huấn luyện, thời gian rollback, và độ ổn định hiệu năng theo thời gian (gồm theo nhóm). Theo dõi cả hiệu năng và công bằng.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng tại thời điểm triển khai **không đảm bảo hiệu năng tương lai** — drift là quy luật. Giám sát cung cấp bằng chứng vận hành liên tục. Ghi rõ giới hạn của proxy khi ground truth trễ; không giả định ổn định.

## 15. Tiêu chuẩn và guideline liên quan

Gắn QMS/kiểm soát thay đổi (chương 23), quản lý rủi ro (chương 24), validation (chương 47), responsible AI (chương 48), DevOps/cloud (chương 55). Tham chiếu hướng dẫn về AI thay đổi liên tục (predetermined change control) của cơ quan quản lý khi áp dụng.

## 16. Liên hệ các chương khác

Vận hành hóa **47**; gắn QMS **23**, rủi ro **24**, công bằng **48**, DevOps **55**; hậu kiểm gắn **20, 22**.

## 17. Bài tập thực hành — MLOps monitoring plan

Lập MLOps monitoring plan: xác định chỉ số giám sát (drift, hiệu năng, proxy), ngưỡng cảnh báo và quy trình ứng phó, versioning và change control, quy trình tái huấn luyện + validation lại, rollback/shadow deployment, và phân bổ trách nhiệm giám sát. Gắn QMS. Ghi rõ giới hạn khi ground truth trễ.

## 18. Checklist tự đánh giá

- [ ] Giám sát drift đầu vào và hiệu năng.
- [ ] Ngưỡng cảnh báo và quy trình ứng phó rõ.
- [ ] Versioning và change control (gắn QMS).
- [ ] Tái huấn luyện có validation lại.
- [ ] Khả năng rollback nhanh.

## 19. Định nghĩa hoàn thành (Definition of Done)

MLOps monitoring plan đạt chuẩn khi giám sát drift và hiệu năng (gồm công bằng), có ngưỡng và ứng phó, quản lý version qua change control, tái huấn luyện với validation lại, và rollback khả thi.

## 20. Câu hỏi phản tư

Tôi phát hiện mô hình suy giảm bằng cách nào và nhanh ra sao? Thay đổi mô hình có qua validation lại và kiểm soát không? Tôi rollback được nhanh không? Drift có tạo thiên lệch mới không?

## 21. Cạm bẫy quyết định

**Triển khai rồi bỏ mặc**, **tái huấn luyện thiếu kiểm soát**. Đối trọng: giám sát liên tục, change control, và validation lại trước khi thay.

## 22. Nguồn dữ liệu động cần xác minh

Hướng dẫn kiểm soát thay đổi AI của cơ quan quản lý, công cụ MLOps, đặc điểm drift địa phương — là dữ liệu động. Tra nguồn chính thức và theo dõi thực tế; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md), [AI tools](../../resources/ai-tool-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Data/concept drift:** trôi dữ liệu/khái niệm. **Versioning:** quản lý phiên bản. **Retraining:** tái huấn luyện. **Rollback:** khôi phục phiên bản. **Shadow deployment:** chạy song song trước khi thay.

## 25. Tóm tắt và bước tiếp theo

MLOps giữ AI an toàn suốt vòng đời qua giám sát drift, versioning, tái huấn luyện có kiểm soát và rollback — triển khai là khởi đầu trách nhiệm, không phải kết thúc. Đây khép nhánh AI. Tiếp theo sang **[chương 51 — Quản lý sản phẩm HealthTech](../51-product-management/README.md)** để bước vào nhánh sản phẩm–tổ chức.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Mô hình suy giảm không giám sát gây hại âm thầm; thay đổi mô hình cần validation lại và kiểm soát thay đổi; giám sát cả công bằng để drift không tạo thiên lệch mới.
