# 47 — Thẩm định AI y tế

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Xây khung validation nội bộ, ngoại bộ và tiền cứu.
> **Sản phẩm của chương:** AI validation protocol.

---

## 1. Tóm tắt điều hành

Validation là bằng chứng quyết định một mô hình AI có an toàn và hiệu quả để dùng lâm sàng hay không. Nhiều mô hình dừng ở validation nội bộ (trên dữ liệu cùng nguồn) — không đủ, vì hiệu năng thường tụt khi gặp dữ liệu mới. Khung đầy đủ gồm: validation nội bộ, ngoại bộ (dữ liệu độc lập), và tiền cứu (prospective, trong luồng lâm sàng thực). Đầu ra là *AI validation protocol*: giao thức thẩm định nhiều tầng gắn với intended use và rủi ro.

## 2. Mục tiêu học tập

Bạn sẽ: (a) phân biệt validation nội bộ/ngoại bộ/tiền cứu; (b) gắn mức validation với rủi ro và intended use; (c) chọn thước đo và so sánh phù hợp; (d) phác AI validation protocol.

## 3. Vì sao chương này sống còn với Doctorpreneur

Triển khai AI chưa validation đủ là rủi ro an toàn nghiêm trọng và mất uy tín. Validation nghiêm là điều thuyết phục cơ quan quản lý, người mua và bác sĩ. Đây là nơi tư duy bằng chứng lâm sàng của Doctorpreneur tạo giá trị lớn nhất trong AI.

## 4. Khái niệm cốt lõi và định nghĩa

**Validation nội bộ:** trên dữ liệu cùng nguồn (chia ra). **Validation ngoại bộ:** trên dữ liệu độc lập (cơ sở/thời gian/quần thể khác). **Validation tiền cứu:** đánh giá trong sử dụng thực, thời gian thực. **Analytical vs clinical validation:** đúng kỹ thuật vs cải thiện quyết định/kết cục. **Silent trial:** chạy AI song song không ảnh hưởng quyết định để đánh giá. **Calibration/discrimination:** khớp xác suất/phân biệt.

## 5. Khung tư duy nền tảng

Validation theo tầng tương xứng rủi ro: nội bộ (điều kiện tối thiểu) → ngoại bộ (chứng minh tổng quát) → tiền cứu/silent trial (hiệu năng và tác động trong luồng thật) → đánh giá tác động lâm sàng (kết cục, chương 25–26). Với AI rủi ro cao, chỉ validation nội bộ là không đủ. Nguyên tắc: mức bằng chứng phải tương xứng mức rủi ro và tuyên bố; validation trên dữ liệu địa phương là bắt buộc trước triển khai.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Mô hình (kể cả thương mại quốc tế) phải validation ngoại bộ trên dữ liệu Việt Nam/địa phương vì khác biệt thiết bị và quần thể (chương 46). Silent trial tại cơ sở là cách an toàn để đánh giá trước khi cho AI ảnh hưởng quyết định. Nghiên cứu validation cần phê duyệt đạo đức và cơ sở pháp lý dữ liệu.

## 7. Các bên liên quan

Nhóm lâm sàng, thống kê (chương 29), khoa học dữ liệu, hội đồng đạo đức, và QA/regulatory. Validation độc lập (không do chính người phát triển tự đánh giá) tăng độ tin cậy.

## 8. Quy trình từng bước

1. **Xác định intended use, tuyên bố và rủi ro.**
2. **Xác định mức validation cần** (nội bộ/ngoại bộ/tiền cứu).
3. **Thiết kế đánh giá** (dữ liệu độc lập, thước đo, so sánh với chuẩn).
4. **Chạy silent trial/tiền cứu** khi rủi ro cao.
5. **Đánh giá tác động lâm sàng** (kết cục, an toàn).
6. **Lập AI validation protocol** và kế hoạch giám sát sau triển khai (chương 50).

## 9. Công cụ và template áp dụng

- **AI validation protocol:** intended use · mức validation · dữ liệu · thước đo · so sánh · tiêu chí đạt · đạo đức.
- **Bảng ánh xạ rủi ro → mức validation.**
- **Kế hoạch silent trial.**

## 10. Ví dụ minh họa

AI dự báo nguy cơ. Protocol: nội bộ (calibration, discrimination); ngoại bộ (dữ liệu cơ sở khác, quần thể địa phương); silent trial (chạy song song, so dự báo với kết cục thực, không ảnh hưởng quyết định); rồi đánh giá tác động khi tích hợp. Tiêu chí đạt định trước. Phê duyệt đạo đức cho nghiên cứu. Số liệu từ dữ liệu thật.

## 11. Sai lầm thường gặp

- **Dừng ở validation nội bộ.**
- **Không validation trên dữ liệu địa phương.**
- **Chỉ analytical, bỏ clinical validation.**
- **Tiêu chí đạt đặt sau khi thấy kết quả.**
- **Bỏ đánh giá calibration.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Triển khai AI ảnh hưởng quyết định lâm sàng mà chưa validation tương xứng là rủi ro an toàn nghiêm trọng. Nghiên cứu validation trên người/dữ liệu cần phê duyệt đạo đức và cơ sở pháp lý (chương 26, 40). Không tuyên bố hiệu quả vượt mức validation. AI là thiết bị y tế phải đáp ứng yêu cầu bằng chứng của đường pháp lý (chương 19–22).

## 13. Chỉ số đo lường

Hiệu năng ngoại bộ (discrimination, calibration), hiệu năng nhóm con, kết quả silent trial, và tác động lâm sàng (kết cục/an toàn). Mức đạt so tiêu chí định trước.

## 14. Bằng chứng và mức độ tin cậy

Chương phân biệt rõ **các tầng bằng chứng validation** và độ mạnh tương ứng; validation nội bộ là yếu nhất, tiền cứu/tác động là mạnh nhất. Nêu rõ mức validation đã đạt và giới hạn. Không nâng cấp tuyên bố quá mức bằng chứng.

## 15. Tiêu chuẩn và guideline liên quan

Tham chiếu chuẩn báo cáo mô hình dự báo/AI (ví dụ **TRIPOD** và mở rộng AI, **STARD** cho nghiên cứu chẩn đoán), Good Machine Learning Practice, và yêu cầu bằng chứng của đường pháp lý (chương 19–22). Gắn thống kê (chương 29), thử nghiệm (chương 26), MLOps (chương 50).

## 16. Liên hệ các chương khác

Tổng hợp đánh giá của **42–46**; dùng thống kê **29**, thử nghiệm **26**; nền cho **48, 50**; yêu cầu từ **19–22**.

## 17. Bài tập thực hành — AI validation protocol

Lập AI validation protocol: nêu intended use và rủi ro, xác định mức validation cần, thiết kế đánh giá ngoại bộ trên dữ liệu địa phương, kế hoạch silent trial/tiền cứu nếu rủi ro cao, tiêu chí đạt định trước, và mục đạo đức. Gắn kế hoạch giám sát sau triển khai. Ghi rõ giới hạn và điều cần xác minh.

## 18. Checklist tự đánh giá

- [ ] Mức validation tương xứng rủi ro.
- [ ] Có validation ngoại bộ trên dữ liệu địa phương.
- [ ] Có clinical validation, không chỉ analytical.
- [ ] Tiêu chí đạt định trước.
- [ ] Đánh giá calibration và nhóm con.

## 19. Định nghĩa hoàn thành (Definition of Done)

AI validation protocol đạt chuẩn khi gắn mức validation với rủi ro, gồm validation ngoại bộ địa phương và (khi cần) tiền cứu, tiêu chí đạt định trước, đánh giá calibration/nhóm con, và tuân đạo đức nghiên cứu.

## 20. Câu hỏi phản tư

Validation của tôi đủ mạnh cho rủi ro và tuyên bố chưa? Tôi đã kiểm trên dữ liệu địa phương độc lập chưa? Tôi có bằng chứng tác động lâm sàng, không chỉ hiệu năng kỹ thuật? Tiêu chí đạt có định trước không?

## 21. Cạm bẫy quyết định

**Dừng ở nội bộ**, **tiêu chí đặt sau**, **lạc quan tổng quát**. Đối trọng: validation ngoại bộ/tiền cứu, tiêu chí định trước, và đánh giá độc lập.

## 22. Nguồn dữ liệu động cần xác minh

Yêu cầu bằng chứng của đường pháp lý, chuẩn báo cáo AI, hiệu năng theo bối cảnh — là dữ liệu động. Tra nguồn chính thức; validation thực tế, không dựa số công bố.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md). Chuẩn báo cáo tra tại nguồn chính thức; trích dẫn xác minh theo EDITORIAL_POLICY.

## 24. Thuật ngữ

**Validation nội bộ/ngoại bộ/tiền cứu:** các tầng thẩm định. **Silent trial:** chạy song song không ảnh hưởng quyết định. **Discrimination/calibration:** phân biệt/khớp xác suất. **Analytical/clinical validation:** đúng kỹ thuật/giá trị lâm sàng.

## 25. Tóm tắt và bước tiếp theo

Validation nhiều tầng — ngoại bộ địa phương và tiền cứu cho rủi ro cao — là điều kiện để triển khai AI an toàn; mức bằng chứng phải tương xứng rủi ro. Tiếp theo sang **[chương 48 — AI có trách nhiệm](../48-responsible-ai/README.md)** cho công bằng, minh bạch và trách nhiệm.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Validation nội bộ không đủ cho AI rủi ro cao — cần ngoại bộ/tiền cứu và validation địa phương; nghiên cứu cần phê duyệt đạo đức; không tuyên bố vượt mức bằng chứng.
