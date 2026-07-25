# 41 — AI trong chăm sóc sức khỏe

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Đánh giá use case, dữ liệu, rủi ro và giá trị AI.
> **Sản phẩm của chương:** AI use-case card.

---

## 1. Tóm tắt điều hành

AI y tế đầy hứa hẹn nhưng cũng đầy thất bại: nhiều mô hình hiệu năng cao trong phòng thí nghiệm nhưng vô dụng hoặc nguy hiểm trên lâm sàng. Chương này cung cấp khung đánh giá một use case AI *trước khi* xây: vấn đề có phù hợp AI không, dữ liệu có sẵn và đủ chất lượng không, rủi ro thế nào, và giá trị lâm sàng thực là gì. Đầu ra là *AI use-case card*: thẻ tóm tắt đánh giá một ứng dụng AI theo các tiêu chí then chốt.

## 2. Mục tiêu học tập

Bạn sẽ: (a) phân biệt bài toán phù hợp/không phù hợp AI; (b) đánh giá tính sẵn có và chất lượng dữ liệu; (c) đánh giá rủi ro theo mức ảnh hưởng lâm sàng; (d) phác AI use-case card gắn giá trị và human oversight.

## 3. Vì sao chương này sống còn với Doctorpreneur

Sai ở khâu chọn use case dẫn tới lãng phí lớn và rủi ro an toàn. Là bác sĩ, bạn đánh giá được giá trị lâm sàng và rủi ro thực — lợi thế để chọn use case AI đáng làm thay vì chạy theo hype.

## 4. Khái niệm cốt lõi và định nghĩa

**Use case AI:** ứng dụng cụ thể của AI cho một bài toán. **Predictive/diagnostic/generative:** các loại AI theo chức năng. **Ground truth:** nhãn tham chiếu đúng. **Data drift:** dữ liệu thay đổi theo thời gian. **Automation bias:** tin AI quá mức. **Human-in-the-loop:** con người trong vòng quyết định.

## 5. Khung tư duy nền tảng

Đánh giá use case theo bốn trục: (1) *phù hợp* — bài toán có mẫu hình học được và AI vượt phương án đơn giản không? (2) *dữ liệu* — có đủ dữ liệu chất lượng, đại diện, có ground truth đáng tin? (3) *rủi ro* — sai thì hậu quả lâm sàng thế nào, cần oversight gì? (4) *giá trị* — cải thiện quyết định/kết cục/hiệu quả thật, đo được? Nguyên tắc: nếu một giải pháp đơn giản (quy tắc, thống kê) giải được thì đừng dùng AI; AI chỉ đáng khi tạo giá trị vượt chi phí và rủi ro.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Dữ liệu địa phương và ground truth chất lượng là ràng buộc lớn. Mô hình huấn luyện trên quần thể khác có thể kém hiệu năng tại Việt Nam (chương 47). Ở tuyến cơ sở, use case giá trị cao thường là hỗ trợ (triage, sàng lọc, nhắc) với oversight, không phải thay thế bác sĩ. Đánh giá tính sẵn có dữ liệu thực tế trước khi cam kết.

## 7. Các bên liên quan

Bác sĩ lâm sàng (đánh giá giá trị/rủi ro), khoa học dữ liệu, người quản lý dữ liệu, và người bệnh. Đánh giá use case cần đầu vào lâm sàng và kỹ thuật cùng lúc — thiếu một bên dễ chọn sai.

## 8. Quy trình từng bước

1. **Phát biểu bài toán** và phương án không-AI để so sánh.
2. **Đánh giá tính phù hợp AI** (có mẫu hình học được không?).
3. **Đánh giá dữ liệu** (sẵn có, chất lượng, đại diện, ground truth).
4. **Đánh giá rủi ro** theo ảnh hưởng lâm sàng và oversight cần.
5. **Xác định giá trị** và cách đo.
6. **Điền AI use-case card** và quyết định go/no-go.

## 9. Công cụ và template áp dụng

- **AI use-case card:** bài toán · loại AI · dữ liệu/ground truth · rủi ro · oversight · giá trị · quyết định.
- **Bảng so sánh AI vs phương án đơn giản.**
- **Data readiness checklist.**

## 10. Ví dụ minh họa

Ý tưởng: AI dự báo nguy cơ trở nặng. Use-case card: bài toán rõ; phương án đơn giản (thang điểm lâm sàng) là baseline; dữ liệu — cần đủ ca có ground truth kết cục, đại diện quần thể; rủi ro — sai dẫn tới bỏ sót/báo động thừa, cần oversight; giá trị — hỗ trợ ưu tiên, đo bằng kết cục. Nếu dữ liệu không đủ hoặc thang điểm sẵn có đủ tốt, quyết định no-go hoặc dùng baseline.

## 11. Sai lầm thường gặp

- **Dùng AI cho bài toán giải được bằng quy tắc/thống kê.**
- **Bỏ qua tính sẵn có/chất lượng dữ liệu.**
- **Ground truth kém tin cậy.**
- **Không đánh giá rủi ro lâm sàng.**
- **Chạy theo hype**, thiếu giá trị đo được.

## 12. Rủi ro an toàn, pháp lý và đạo đức

AI sai ảnh hưởng quyết định lâm sàng gây hại; mức oversight phải tương xứng rủi ro (chương 24, 47, 48). AI phục vụ quyết định lâm sàng có thể là thiết bị y tế (chương 19–20). Dữ liệu huấn luyện cần cơ sở pháp lý (chương 40). Không triển khai AI khi chưa validation phù hợp; cảnh giác thiên lệch dữ liệu gây bất công (chương 48).

## 13. Chỉ số đo lường

Ở khâu đánh giá: độ phù hợp use case, mức sẵn sàng dữ liệu, mức rủi ro và oversight, và giá trị dự kiến đo được. Sau triển khai: hiệu năng thực, ảnh hưởng quyết định/kết cục, và giám sát drift (chương 50).

## 14. Bằng chứng và mức độ tin cậy

Hiệu năng hứa hẹn của AI **không tự chứng minh giá trị lâm sàng** — cần validation (chương 47) và đánh giá tác động (chương 25–30). Chương nêu khung đánh giá; kết luận về một use case cụ thể cần dữ liệu thật. Không tin số hiệu năng thiếu bối cảnh.

## 15. Tiêu chuẩn và guideline liên quan

Gắn ML (chương 42), validation (chương 47), responsible AI (chương 48), MLOps (chương 50), thiết bị y tế (chương 19–20), dữ liệu (chương 40). Tham chiếu hướng dẫn AI y tế của cơ quan quản lý khi áp dụng.

## 16. Liên hệ các chương khác

Cửa vào nhánh AI **42–50**; dùng workflow **07**, dữ liệu **35–36, 40, 54**; validation **47**; đạo đức **48**; giá trị lâm sàng **25**.

## 17. Bài tập thực hành — AI use-case card

Điền AI use-case card cho một ý tưởng: bài toán và baseline không-AI, đánh giá tính phù hợp, đánh giá dữ liệu/ground truth, đánh giá rủi ro và oversight cần, giá trị và cách đo, và quyết định go/no-go. Ghi rõ giả định về dữ liệu và điều cần xác minh.

## 18. Checklist tự đánh giá

- [ ] Đã so sánh với phương án đơn giản không-AI.
- [ ] Dữ liệu đủ, chất lượng, đại diện; ground truth tin cậy.
- [ ] Rủi ro lâm sàng và oversight được đánh giá.
- [ ] Giá trị đo được, không chạy theo hype.
- [ ] Cơ sở pháp lý dữ liệu và thiên lệch được xét.

## 19. Định nghĩa hoàn thành (Definition of Done)

AI use-case card đạt chuẩn khi so sánh với baseline không-AI, đánh giá dữ liệu/ground truth, đánh giá rủi ro và oversight, xác định giá trị đo được, và ra quyết định go/no-go có căn cứ.

## 20. Câu hỏi phản tư

Bài toán này có cần AI, hay quy tắc/thống kê là đủ? Tôi có đủ dữ liệu chất lượng và ground truth không? Sai thì hại lâm sàng thế nào và tôi kiểm soát ra sao? Giá trị thực đo được là gì?

## 21. Cạm bẫy quyết định

**AI hype**, **bỏ qua dữ liệu**, **automation bias**. Đối trọng: so sánh baseline, data readiness nghiêm, và oversight tương xứng rủi ro.

## 22. Nguồn dữ liệu động cần xác minh

Tính sẵn có/chất lượng dữ liệu địa phương, hiệu năng mô hình theo bối cảnh, quy định AI y tế — là dữ liệu động. Đánh giá thực tế và tra nguồn chính thức; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md), [AI tools](../../resources/ai-tool-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Ground truth:** nhãn tham chiếu đúng. **Data drift:** trôi dữ liệu. **Automation bias:** tin AI quá mức. **Human-in-the-loop:** người trong vòng quyết định. **Baseline:** phương án nền để so sánh.

## 25. Tóm tắt và bước tiếp theo

AI đáng làm khi bài toán phù hợp, dữ liệu đủ chất lượng, rủi ro kiểm soát được và giá trị đo được — không phải vì AI đang thời thượng. Tiếp theo sang **[chương 42 — Machine Learning cho bác sĩ](../42-machine-learning/README.md)** để hiểu pipeline và giới hạn mô hình.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Hiệu năng AI không tự chứng minh giá trị lâm sàng; AI chạm quyết định lâm sàng cần validation, oversight và có thể chịu quản lý thiết bị y tế; dữ liệu cần cơ sở pháp lý.
