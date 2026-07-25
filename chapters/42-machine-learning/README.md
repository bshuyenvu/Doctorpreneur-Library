# 42 — Machine Learning cho bác sĩ

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Hiểu pipeline ML và giới hạn mô hình.
> **Sản phẩm của chương:** Baseline ML notebook plan.

---

## 1. Tóm tắt điều hành

Machine learning học mẫu hình từ dữ liệu để dự báo. Bác sĩ không cần tự lập trình mô hình, nhưng phải hiểu pipeline ML và giới hạn của nó để đánh giá, giám sát và hợp tác hiệu quả với nhóm kỹ thuật — đặc biệt là các bẫy đặc thù y tế (rò rỉ dữ liệu, mất cân bằng lớp, thiên lệch). Đầu ra là *baseline ML notebook plan*: kế hoạch cho một mô hình baseline có kỷ luật, gồm dữ liệu, đặc trưng, đánh giá và các kiểm tra giới hạn.

## 2. Mục tiêu học tập

Bạn sẽ: (a) nắm pipeline ML từ dữ liệu tới đánh giá; (b) hiểu các bẫy đặc thù y tế (data leakage, class imbalance, thiên lệch); (c) chọn thước đo đánh giá phù hợp lâm sàng; (d) phác kế hoạch mô hình baseline.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Không hiểu giới hạn ML dễ bị "con số đẹp" đánh lừa (ví dụ accuracy cao trên lớp mất cân bằng). Hiểu pipeline giúp bạn đặt câu hỏi đúng cho nhóm kỹ thuật và bảo vệ an toàn lâm sàng.

## 4. Khái niệm cốt lõi và định nghĩa

**Pipeline ML:** dữ liệu → tiền xử lý → đặc trưng → huấn luyện → đánh giá → triển khai. **Train/validation/test split:** chia dữ liệu để tránh overfit. **Data leakage:** thông tin tương lai/nhãn lọt vào đặc trưng. **Class imbalance:** lớp hiếm (bệnh) ít mẫu. **Overfitting:** học thuộc dữ liệu huấn luyện, kém tổng quát. **Calibration:** độ khớp xác suất dự báo với thực tế.

## 5. Khung tư duy nền tảng

Luôn bắt đầu bằng baseline đơn giản (quy tắc lâm sàng, hồi quy) để có mốc so sánh — mô hình phức tạp phải vượt baseline mới đáng. Chia dữ liệu nghiêm để tránh rò rỉ; đánh giá bằng thước đo phù hợp lâm sàng (không chỉ accuracy — dùng độ nhạy/đặc hiệu, AUC, calibration theo bối cảnh). Nguyên tắc: nghi ngờ kết quả quá tốt (thường do leakage), và luôn xét hiệu năng trên nhóm nhỏ/hiếm.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Dữ liệu tuyến cơ sở thường nhỏ, mất cân bằng và thiếu chuẩn hóa. Baseline đơn giản và mô hình gọn thường phù hợp hơn mô hình phức tạp cần nhiều dữ liệu. Hiệu năng phải đánh giá trên dữ liệu đại diện địa phương, không mượn từ nghiên cứu quần thể khác.

## 7. Các bên liên quan

Khoa học dữ liệu, bác sĩ (cung cấp ground truth và đánh giá ý nghĩa lâm sàng), quản lý dữ liệu. Bác sĩ tham gia chọn thước đo và diễn giải kết quả — thước đo kỹ thuật thuần dễ lệch giá trị lâm sàng.

## 8. Quy trình từng bước

1. **Xác định bài toán và nhãn** (ground truth) rõ.
2. **Lập baseline đơn giản** làm mốc.
3. **Chuẩn bị dữ liệu** và chia train/val/test tránh leakage.
4. **Chọn đặc trưng và mô hình** phù hợp cỡ dữ liệu.
5. **Đánh giá** bằng thước đo lâm sàng + calibration + hiệu năng nhóm nhỏ.
6. **Lập baseline ML notebook plan** với các kiểm tra giới hạn.

## 9. Công cụ và template áp dụng

- **Baseline ML notebook plan:** bài toán · nhãn · baseline · dữ liệu/split · đặc trưng · thước đo · kiểm tra leakage/imbalance/thiên lệch.
- **Bảng thước đo đánh giá** theo bối cảnh lâm sàng.
- **Checklist bẫy ML y tế.**

## 10. Ví dụ minh họa

Dự báo tái nhập viện. Baseline: thang điểm lâm sàng. ML: kiểm tra rò rỉ (không dùng biến chỉ có sau kết cục), xử lý mất cân bằng, đánh giá bằng AUC + độ nhạy ở ngưỡng vận hành + calibration, và hiệu năng trên nhóm nhỏ. Nếu ML không vượt baseline hoặc không calibrate tốt, chưa nên triển khai. Số liệu phải từ dữ liệu thật.

## 11. Sai lầm thường gặp

- **Không có baseline** để so sánh.
- **Data leakage** tạo hiệu năng ảo.
- **Chỉ dùng accuracy** trên lớp mất cân bằng.
- **Bỏ qua calibration** và hiệu năng nhóm nhỏ.
- **Overfit** do đánh giá trên dữ liệu đã thấy.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Mô hình kém calibrate hoặc thiên lệch dẫn tới quyết định sai và bất công cho nhóm yếu thế (chương 48). Hiệu năng ảo do leakage nguy hiểm khi triển khai. Cần validation độc lập (chương 47), oversight, và giám sát drift (chương 50). Dữ liệu huấn luyện cần cơ sở pháp lý (chương 40).

## 13. Chỉ số đo lường

Thước đo phù hợp lâm sàng (độ nhạy/đặc hiệu tại ngưỡng vận hành, AUC, calibration), hiệu năng trên nhóm con, và mức vượt baseline. Tránh dựa một con số tổng hợp.

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng trên test nội bộ **không đảm bảo hiệu năng thực tế** — cần validation ngoại bộ/tiền cứu (chương 47). Chương nêu nguyên tắc; kết quả cụ thể cần dữ liệu thật và diễn giải thống kê (chương 29). Nghi ngờ kết quả quá tốt.

## 15. Tiêu chuẩn và guideline liên quan

Tham chiếu chuẩn báo cáo mô hình dự báo (ví dụ **TRIPOD**, và mở rộng cho AI), validation (chương 47), thống kê (chương 29), responsible AI (chương 48), MLOps (chương 50).

## 16. Liên hệ các chương khác

Nối **41**; sâu hơn ở **43** (deep learning); đánh giá **47**; thống kê **29**; đạo đức **48**; vận hành **50**.

## 17. Bài tập thực hành — Baseline ML notebook plan

Lập baseline ML notebook plan: xác định bài toán và nhãn, thiết kế baseline đơn giản, kế hoạch chuẩn bị dữ liệu và split tránh leakage, chọn thước đo lâm sàng + calibration + đánh giá nhóm nhỏ, và checklist kiểm tra bẫy (leakage, imbalance, thiên lệch). Ghi rõ giả định dữ liệu và điều cần validation.

## 18. Checklist tự đánh giá

- [ ] Có baseline đơn giản để so sánh.
- [ ] Split dữ liệu tránh data leakage.
- [ ] Thước đo phù hợp lâm sàng, không chỉ accuracy.
- [ ] Đánh giá calibration và hiệu năng nhóm nhỏ.
- [ ] Kiểm tra thiên lệch và tính đại diện.

## 19. Định nghĩa hoàn thành (Definition of Done)

Baseline ML notebook plan đạt chuẩn khi có baseline so sánh, split tránh leakage, thước đo lâm sàng phù hợp gồm calibration, đánh giá nhóm nhỏ, và kiểm tra các bẫy ML y tế.

## 20. Câu hỏi phản tư

Mô hình của tôi có vượt baseline đơn giản không? Kết quả có bị leakage không (quá tốt để tin)? Thước đo có phản ánh giá trị lâm sàng không? Hiệu năng trên nhóm hiếm/yếu thế thế nào?

## 21. Cạm bẫy quyết định

**Con số đẹp lừa dối** (accuracy/leakage), **bỏ qua nhóm nhỏ**. Đối trọng: baseline, split nghiêm, thước đo lâm sàng, và kiểm tra thiên lệch.

## 22. Nguồn dữ liệu động cần xác minh

Hiệu năng mô hình theo bối cảnh, tính đại diện dữ liệu, chuẩn báo cáo AI — là dữ liệu động. Đánh giá thực tế và tra nguồn chính thức; không dùng số quảng cáo.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md), [Open source](../../resources/open-source-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Data leakage:** rò rỉ dữ liệu. **Class imbalance:** mất cân bằng lớp. **Overfitting:** học thuộc, kém tổng quát. **Calibration:** khớp xác suất dự báo. **AUC:** diện tích dưới đường ROC.

## 25. Tóm tắt và bước tiếp theo

Hiểu pipeline và giới hạn ML — baseline, tránh leakage, thước đo lâm sàng, calibration, nhóm nhỏ — giúp đánh giá mô hình trung thực. Tiếp theo sang **[chương 43 — Deep Learning y khoa](../43-deep-learning/README.md)** cho các mô hình phức tạp hơn.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Hiệu năng test nội bộ không đảm bảo thực tế — cần validation độc lập; mô hình thiên lệch/kém calibrate gây rủi ro; dữ liệu cần cơ sở pháp lý.
