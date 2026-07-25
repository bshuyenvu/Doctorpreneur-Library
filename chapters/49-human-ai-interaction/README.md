# 49 — Tương tác người–AI

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Thiết kế giao diện và phân bổ trách nhiệm phù hợp.
> **Sản phẩm của chương:** Human–AI responsibility map.

---

## 1. Tóm tắt điều hành

Ngay cả một mô hình AI tốt vẫn có thể gây hại nếu tương tác người–AI được thiết kế kém: bác sĩ tin AI quá mức (automation bias) hoặc bỏ qua AI hoàn toàn (algorithm aversion). Thiết kế tốt xác định rõ ai quyết định gì, trình bày khuyến nghị AI kèm độ bất định, và giữ con người ở đúng vị trí trong vòng quyết định. Đầu ra là *human–AI responsibility map*: bản đồ phân bổ vai trò và trách nhiệm giữa AI và con người theo từng quyết định.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu automation bias và algorithm aversion; (b) chọn mức tự động phù hợp rủi ro; (c) thiết kế trình bày khuyến nghị AI (bất định, cơ sở); (d) phác responsibility map.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Là bác sĩ, bạn hiểu quyết định lâm sàng và nơi con người phải giữ quyền — lợi thế thiết kế tương tác an toàn. Phân bổ trách nhiệm sai (AI quyết định điều nó không nên) là nguồn rủi ro lớn kể cả khi mô hình đúng.

## 4. Khái niệm cốt lõi và định nghĩa

**Automation bias:** tin/tuân AI quá mức. **Algorithm aversion:** bỏ qua/không tin AI. **Levels of automation:** mức tự động từ gợi ý tới tự quyết. **Human-in/on-the-loop:** người trong/giám sát vòng quyết định. **Calibration of trust:** tin AI đúng mức theo độ tin cậy. **Explanation:** giải thích khuyến nghị.

## 5. Khung tư duy nền tảng

Chọn mức tự động theo rủi ro: quyết định rủi ro cao giữ human-in-the-loop (AI gợi ý, người quyết); rủi ro thấp có thể human-on-the-loop (AI hành động, người giám sát). Thiết kế để *hiệu chỉnh niềm tin*: trình bày độ bất định, cơ sở khuyến nghị, và trường hợp AI không nên tin. Nguyên tắc: con người phải giữ quyết định ở nơi hậu quả nghiêm trọng; giao diện phải hỗ trợ phán đoán, không thay thế nó.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Ở tuyến cơ sở thiếu chuyên khoa, cám dỗ để AI "quyết thay" cao — nhưng đây là nơi rủi ro automation bias lớn nhất. Thiết kế phải giữ bác sĩ ở vị trí quyết định, đồng thời hỗ trợ hiệu quả (không tăng gánh nặng). Đào tạo người dùng về giới hạn AI là phần của thiết kế.

## 7. Các bên liên quan

Bác sĩ/điều dưỡng (người dùng), người thiết kế UX, và người bệnh (chịu hậu quả quyết định). Thiết kế tương tác cần thử với người dùng thực (chương 52) để đo automation bias/aversion.

## 8. Quy trình từng bước

1. **Liệt kê quyết định** AI tham gia và mức rủi ro.
2. **Chọn mức tự động** phù hợp từng quyết định.
3. **Phân bổ trách nhiệm** (ai quyết, ai giám sát, ai chịu trách nhiệm).
4. **Thiết kế trình bày khuyến nghị** (bất định, cơ sở, cảnh báo).
5. **Thiết kế cơ chế override** và phản hồi.
6. **Lập responsibility map** và kế hoạch đo automation bias.

## 9. Công cụ và template áp dụng

- **Human–AI responsibility map:** quyết định · mức tự động · vai người/AI · trách nhiệm · override.
- **Bảng trình bày khuyến nghị** (độ bất định, cơ sở).
- **Kế hoạch đo automation bias/aversion.**

## 10. Ví dụ minh họa

AI gợi ý chẩn đoán phân biệt. Responsibility map: AI đề xuất danh sách kèm độ tin cậy và cơ sở; bác sĩ quyết định (human-in-the-loop); hiển thị cảnh báo khi AI ngoài phạm vi tin cậy; bác sĩ override dễ dàng và phản hồi được ghi lại. Đo xem bác sĩ có tin mù quáng hay bỏ qua AI. Không để AI tự chốt chẩn đoán.

## 11. Sai lầm thường gặp

- **Mức tự động quá cao** cho quyết định rủi ro.
- **Không trình bày độ bất định.**
- **Trách nhiệm mờ** khi AI–người bất đồng.
- **Bỏ qua automation bias/aversion** khi thiết kế.
- **Override khó** khiến người dùng chịu theo AI.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Automation bias có thể khiến bác sĩ theo AI sai — rủi ro an toàn nghiêm trọng; thiết kế phải chống lại. Trách nhiệm pháp lý/đạo đức khi AI sai phải rõ (gắn chương 48). Con người phải giữ quyết định và trách nhiệm ở nơi hậu quả nghiêm trọng. Người bệnh có quyền biết vai trò của AI trong quyết định.

## 13. Chỉ số đo lường

Tỉ lệ tuân/override khuyến nghị AI, độ hiệu chỉnh niềm tin (tin đúng theo độ tin cậy), sai sót do automation bias/aversion, và tác động tới quyết định/kết cục. Đo với người dùng thực.

## 14. Bằng chứng và mức độ tin cậy

Hiệu quả tương tác phụ thuộc thiết kế và người dùng cụ thể — cần thử nghiệm với người dùng thực (chương 52), không suy từ trực giác. Automation bias là hiện tượng có thật cần đo. Ghi rõ giới hạn thiết kế và nhóm người dùng.

## 15. Tiêu chuẩn và guideline liên quan

Gắn responsible AI (chương 48), UX (chương 52), CDS five rights (chương 38), quản lý rủi ro (chương 24), yếu tố con người trong thiết bị y tế. Tham chiếu hướng dẫn human factors khi áp dụng.

## 16. Liên hệ các chương khác

Gắn **48** (trách nhiệm), **38** (CDS), **52** (UX), **24** (rủi ro), **37** (đọc hình ảnh). Bổ trợ triển khai **50**.

## 17. Bài tập thực hành — Human–AI responsibility map

Lập responsibility map cho một hệ AI: liệt kê quyết định và rủi ro, chọn mức tự động, phân bổ vai và trách nhiệm (quyết/giám sát/chịu trách nhiệm), thiết kế trình bày khuyến nghị (bất định, cơ sở, cảnh báo), cơ chế override, và kế hoạch đo automation bias với người dùng thực. Ghi rõ giả định cần kiểm.

## 18. Checklist tự đánh giá

- [ ] Mức tự động phù hợp rủi ro từng quyết định.
- [ ] Con người giữ quyết định ở nơi hậu quả nghiêm trọng.
- [ ] Trình bày độ bất định và cơ sở khuyến nghị.
- [ ] Override dễ, có ghi phản hồi.
- [ ] Kế hoạch đo automation bias/aversion.

## 19. Định nghĩa hoàn thành (Definition of Done)

Responsibility map đạt chuẩn khi phân bổ mức tự động theo rủi ro, giữ con người ở quyết định nghiêm trọng, trình bày bất định/cơ sở, cho override dễ, và có kế hoạch đo automation bias với người dùng thực.

## 20. Câu hỏi phản tư

Con người có giữ quyết định ở nơi cần không? Giao diện của tôi có chống automation bias không? Bác sĩ override được dễ không? Ai chịu trách nhiệm khi AI và người bất đồng?

## 21. Cạm bẫy quyết định

**Tự động hóa quá mức**, **giấu bất định**, **override khó**. Đối trọng: mức tự động theo rủi ro, trình bày bất định, và thử với người dùng thực.

## 22. Nguồn dữ liệu động cần xác minh

Bằng chứng về automation bias trong bối cảnh, hướng dẫn human factors — là dữ liệu động/ngữ cảnh. Đo với người dùng thực và tra nguồn; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Automation bias:** tin AI quá mức. **Algorithm aversion:** bỏ qua AI. **Levels of automation:** mức tự động. **Human-in/on-the-loop:** người trong/giám sát vòng. **Calibration of trust:** hiệu chỉnh niềm tin.

## 25. Tóm tắt và bước tiếp theo

Tương tác người–AI tốt giữ con người ở đúng vị trí quyết định, trình bày bất định, và chống automation bias — để AI hỗ trợ thay vì thay thế phán đoán. Tiếp theo sang **[chương 50 — MLOps trong y tế](../50-mlops-healthcare/README.md)** cho vận hành và giám sát mô hình.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Con người phải giữ quyết định ở nơi hậu quả nghiêm trọng; thiết kế phải chống automation bias; người bệnh có quyền biết vai trò của AI.
