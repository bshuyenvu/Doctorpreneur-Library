# 44 — Generative AI trong y tế

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Thiết kế GenAI có kiểm soát và đánh giá.
> **Sản phẩm của chương:** GenAI guardrail plan.

---

## 1. Tóm tắt điều hành

Generative AI — mô hình ngôn ngữ lớn (LLM) và mô hình sinh — có thể soạn văn bản, tóm tắt, trả lời và hỗ trợ nhiều tác vụ y tế hành chính và giáo dục. Nhưng nó có đặc tính nguy hiểm trong lâm sàng: "ảo giác" (bịa thông tin nghe hợp lý), thiếu ổn định, và khó kiểm soát. Dùng đúng chỗ (hành chính, nháp, giáo dục có kiểm chứng) với guardrails phù hợp là chìa khóa. Đầu ra là *GenAI guardrail plan*: kế hoạch kiểm soát và đánh giá một ứng dụng GenAI theo mức rủi ro.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu năng lực và giới hạn của GenAI (đặc biệt ảo giác); (b) phân loại ứng dụng theo rủi ro (hành chính vs lâm sàng); (c) thiết kế guardrails (kiểm chứng nguồn, human review, giới hạn phạm vi); (d) phác kế hoạch đánh giá đầu ra GenAI.

## 3. Vì sao chương này sống còn với Doctorpreneur

GenAI đang được dùng rộng nhưng rủi ro ảo giác trong y tế nghiêm trọng: một thông tin bịa nghe thuyết phục có thể gây hại. Là bác sĩ, bạn phải thiết kế ranh giới rõ giữa dùng an toàn (có kiểm chứng) và dùng nguy hiểm (tin mù quáng cho quyết định lâm sàng).

## 4. Khái niệm cốt lõi và định nghĩa

**LLM:** mô hình ngôn ngữ lớn. **Ảo giác (hallucination):** đầu ra sai nhưng nghe hợp lý. **Prompt/prompting:** cách ra chỉ dẫn cho mô hình. **RAG (retrieval-augmented generation):** kết hợp truy xuất nguồn để giảm bịa. **Guardrails:** ràng buộc kiểm soát đầu ra. **Human-in-the-loop:** người kiểm chứng trước khi dùng.

## 5. Khung tư duy nền tảng

Phân loại ứng dụng theo rủi ro và thiết kế guardrail tương ứng: (1) *hành chính/nháp* (soạn thư, tóm tắt tài liệu nội bộ) — rủi ro thấp, cần human review; (2) *giáo dục/tra cứu* — cần kiểm chứng nguồn (RAG + trích dẫn xác minh); (3) *chạm quyết định lâm sàng* — rủi ro cao, thường không dùng GenAI tự do; nếu dùng phải có bằng chứng, guardrail mạnh và oversight. Nguyên tắc: không bao giờ tin đầu ra GenAI cho quyết định lâm sàng mà không kiểm chứng; mọi thông tin y khoa từ GenAI phải được người có chuyên môn xác minh.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

GenAI có giá trị cao cho công việc hành chính, soạn thảo văn bản, tóm tắt và hỗ trợ giáo dục — đúng các nhóm việc quá tải ở tuyến cơ sở. Nhưng phải kiểm chứng nội dung y khoa (đặc biệt phác đồ, liều thuốc, guideline — GenAI dễ bịa) và tuân bảo mật dữ liệu (không đưa dữ liệu bệnh nhân định danh vào dịch vụ không kiểm soát — chương 40).

## 7. Các bên liên quan

Người dùng (bác sĩ/nhân viên), người xây ứng dụng, và bộ phận bảo mật/pháp chế. Với ứng dụng chạm nội dung y khoa, chuyên môn lâm sàng phải tham gia thiết kế guardrail và đánh giá.

## 8. Quy trình từng bước

1. **Xác định tác vụ** và phân loại rủi ro.
2. **Quyết định GenAI có phù hợp** (hay cần phương pháp xác định hơn).
3. **Thiết kế guardrails** (RAG/nguồn, giới hạn phạm vi, từ chối ngoài phạm vi).
4. **Bắt buộc human review** cho đầu ra rủi ro.
5. **Thiết kế đánh giá đầu ra** (độ chính xác, ảo giác, an toàn).
6. **Lập GenAI guardrail plan** và giám sát vận hành.

## 9. Công cụ và template áp dụng

- **GenAI guardrail plan:** tác vụ · rủi ro · phù hợp? · guardrails · human review · đánh giá · bảo mật.
- **Bộ test đánh giá đầu ra** (gồm ca dễ ảo giác).
- **Chính sách dữ liệu** cho GenAI (không đưa dữ liệu định danh vào dịch vụ không kiểm soát).

## 10. Ví dụ minh họa

Trợ lý soạn thảo văn bản hành chính. Guardrail plan: dùng cho nháp, human review bắt buộc trước khi ban hành; không nhập dữ liệu bệnh nhân định danh; với nội dung y khoa, yêu cầu trích dẫn nguồn và kiểm chứng. Đánh giá bằng bộ test có ca dễ ảo giác. Không dùng cho quyết định lâm sàng tự do. (Về lựa chọn mô hình/kỹ thuật cụ thể, tham vấn tài liệu cập nhật của nhà cung cấp.)

## 11. Sai lầm thường gặp

- **Tin đầu ra GenAI** cho quyết định lâm sàng.
- **Không kiểm chứng nội dung y khoa** (liều, phác đồ, trích dẫn).
- **Đưa dữ liệu bệnh nhân định danh** vào dịch vụ không kiểm soát.
- **Thiếu human review** cho đầu ra rủi ro.
- **Không đánh giá ảo giác** một cách hệ thống.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Ảo giác trong nội dung y khoa có thể gây hại trực tiếp; mọi thông tin y khoa từ GenAI phải được chuyên môn xác minh. Không đưa dữ liệu bệnh nhân định danh vào dịch vụ bên thứ ba không có cơ sở pháp lý/bảo mật (chương 40). Ứng dụng GenAI chạm quyết định lâm sàng có thể là thiết bị y tế (chương 19–20) và cần bằng chứng. Minh bạch với người dùng rằng nội dung do AI sinh và cần kiểm chứng.

## 13. Chỉ số đo lường

Tỉ lệ ảo giác/sai trên bộ test, tỉ lệ đầu ra được người dùng sửa, độ phủ trích dẫn kiểm chứng được, và tuân thủ chính sách dữ liệu. Theo dõi trong vận hành vì hành vi mô hình có thể đổi.

## 14. Bằng chứng và mức độ tin cậy

GenAI **không phải nguồn bằng chứng y khoa**; đầu ra phải kiểm chứng tại nguồn chính thức. Hiệu năng phụ thuộc mô hình, prompt và bối cảnh, thay đổi theo thời gian. Đánh giá phải có hệ thống và cập nhật; không giả định độ tin cậy ổn định.

## 15. Tiêu chuẩn và guideline liên quan

Gắn responsible AI (chương 48), validation (chương 47), privacy (chương 40), thiết bị y tế nếu chạm lâm sàng (chương 19–20). Tham chiếu hướng dẫn về AI/LLM trong y tế của cơ quan quản lý và nhà cung cấp mô hình khi áp dụng.

## 16. Liên hệ các chương khác

Nối **41**; NLP lâm sàng **45**; đánh giá **47**; đạo đức **48**; dữ liệu **40**; ứng dụng nội dung/đào tạo **63**.

## 17. Bài tập thực hành — GenAI guardrail plan

Chọn một tác vụ và lập GenAI guardrail plan: phân loại rủi ro, quyết định GenAI có phù hợp, thiết kế guardrails (nguồn/RAG, giới hạn phạm vi, human review), chính sách dữ liệu (bảo mật), và bộ test đánh giá đầu ra gồm ca dễ ảo giác. Nêu ranh giới dùng an toàn vs không dùng. Ghi rõ điều cần kiểm chứng.

## 18. Checklist tự đánh giá

- [ ] Ứng dụng được phân loại theo rủi ro.
- [ ] Không dùng GenAI tự do cho quyết định lâm sàng.
- [ ] Guardrails và human review cho đầu ra rủi ro.
- [ ] Chính sách dữ liệu bảo mật (không định danh vào dịch vụ không kiểm soát).
- [ ] Đánh giá ảo giác có hệ thống.

## 19. Định nghĩa hoàn thành (Definition of Done)

GenAI guardrail plan đạt chuẩn khi phân loại rủi ro, giới hạn phạm vi dùng an toàn, có guardrails + human review, chính sách dữ liệu bảo mật, và bộ test đánh giá ảo giác/an toàn.

## 20. Câu hỏi phản tư

Tác vụ này có chấp nhận được rủi ro ảo giác không? Nội dung y khoa có được kiểm chứng không? Tôi có đưa dữ liệu bệnh nhân định danh vào đâu không an toàn không? Người dùng có biết cần kiểm chứng đầu ra không?

## 21. Cạm bẫy quyết định

**Tin đầu ra thuyết phục** (ảo giác), **tiện lợi lấn an toàn**. Đối trọng: human review bắt buộc, kiểm chứng nguồn, và giới hạn phạm vi rõ.

## 22. Nguồn dữ liệu động cần xác minh

Năng lực/giới hạn mô hình, hướng dẫn dùng an toàn, quy định AI/dữ liệu — thay đổi nhanh, là dữ liệu động. Tra tài liệu nhà cung cấp và văn bản chính thức cập nhật; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [AI tools](../../resources/ai-tool-library.md), [Prompt](../../resources/prompt-library.md), [Thư viện bài báo](../../resources/paper-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**LLM:** mô hình ngôn ngữ lớn. **Hallucination:** ảo giác/bịa. **RAG:** sinh có truy xuất nguồn. **Guardrails:** ràng buộc kiểm soát. **Prompt:** chỉ dẫn cho mô hình.

## 25. Tóm tắt và bước tiếp theo

GenAI giá trị cao cho việc hành chính/nháp/giáo dục có kiểm chứng, nhưng nguy hiểm nếu tin mù quáng cho quyết định lâm sàng; guardrails và human review là bắt buộc. Tiếp theo sang **[chương 45 — NLP lâm sàng](../45-nlp-clinical/README.md)** cho xử lý văn bản y khoa.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. GenAI không phải nguồn bằng chứng y khoa và có thể ảo giác — mọi nội dung y khoa phải kiểm chứng; không đưa dữ liệu bệnh nhân định danh vào dịch vụ không kiểm soát; không dùng tự do cho quyết định lâm sàng.
