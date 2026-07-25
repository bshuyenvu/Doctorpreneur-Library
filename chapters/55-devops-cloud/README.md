# 55 — DevOps và cloud y tế

> **Nhánh 6 — Sản phẩm, công nghệ và tổ chức** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Tự động hóa triển khai, quan sát và khôi phục.
> **Sản phẩm của chương:** Deployment runbook.

---

## 1. Tóm tắt điều hành

DevOps là tập thực hành tự động hóa xây dựng, kiểm thử, triển khai và vận hành phần mềm một cách nhanh, đáng tin và có kiểm soát. Trong y tế, độ tin cậy và khả năng khôi phục là vấn đề an toàn: hệ thống gián đoạn có thể ảnh hưởng chăm sóc. Đầu ra là *deployment runbook*: quy trình triển khai và vận hành có tài liệu, gồm kiểm soát thay đổi, giám sát (observability) và khôi phục.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu CI/CD và kiểm soát thay đổi; (b) thiết kế observability (log, metric, trace); (c) lập kế hoạch khôi phục và rollback; (d) viết deployment runbook.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Triển khai thủ công, thiếu giám sát và không có kế hoạch khôi phục gây sự cố và rủi ro an toàn. DevOps tốt giảm lỗi triển khai, phát hiện sự cố sớm và phục hồi nhanh — bảo vệ cả người bệnh lẫn uy tín.

## 4. Khái niệm cốt lõi và định nghĩa

**CI/CD:** tích hợp/triển khai liên tục. **Infrastructure as code:** hạ tầng bằng mã. **Observability:** khả năng quan sát (log, metric, trace). **Rollback:** khôi phục phiên bản trước. **Change control:** kiểm soát thay đổi. **Disaster recovery:** khôi phục thảm họa. **Uptime/SLA:** độ sẵn sàng/cam kết dịch vụ.

## 5. Khung tư duy nền tảng

Tự động hóa để giảm lỗi con người và tăng khả năng lặp lại; giám sát để phát hiện sự cố trước người dùng; và luôn có đường khôi phục nhanh. Trong y tế, cân bằng tốc độ (DevOps ưa thay đổi nhanh) với kiểm soát thay đổi (an toàn/tuân thủ đòi hỏi truy vết và validation). Nguyên tắc: mọi thay đổi hệ thống chạm lâm sàng phải qua kiểm soát thay đổi, có thể kiểm thử và rollback; độ sẵn sàng và khôi phục là yêu cầu an toàn.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Hạ tầng tuyến cơ sở (mạng, điện) đòi hỏi thiết kế chịu gián đoạn và có phương án khi mất kết nối (gắn chương 53). Lựa chọn cloud/on-premise phụ thuộc quy định lưu trữ dữ liệu y tế (địa điểm dữ liệu) và bảo mật (chương 39–40) — phải xác minh quy định hiện hành. Chi phí vận hành cần khả thi.

## 7. Các bên liên quan

Kỹ sư DevOps/vận hành, phát triển, bảo mật, và CNTT bệnh viện (với on-premise/tích hợp). Trách nhiệm vận hành và ứng phó sự cố phải rõ.

## 8. Quy trình từng bước

1. **Thiết lập CI/CD** với kiểm thử tự động.
2. **Áp kiểm soát thay đổi** (gắn QMS — chương 23) cho hệ thống lâm sàng.
3. **Thiết kế observability** (log, metric, trace, cảnh báo).
4. **Lập kế hoạch rollback và disaster recovery.**
5. **Xác minh quy định** lưu trữ/bảo mật dữ liệu (cloud/on-prem).
6. **Viết deployment runbook** và diễn tập khôi phục.

## 9. Công cụ và template áp dụng

- **Deployment runbook:** quy trình triển khai · kiểm soát thay đổi · kiểm thử · rollback · giám sát · ứng phó sự cố.
- **Observability checklist** (log/metric/trace/alert).
- **Disaster recovery plan** (RTO/RPO).

## 10. Ví dụ minh họa

Triển khai bản cập nhật. Runbook: chạy CI/CD với kiểm thử tự động; qua kiểm soát thay đổi (với validation lại nếu chạm chức năng lâm sàng — chương 47); triển khai theo giai đoạn (canary) với giám sát; nếu lỗi, rollback tự động; ghi log truy vết. Có kế hoạch khôi phục nếu sự cố lớn, bảo đảm không gián đoạn chăm sóc kéo dài.

## 11. Sai lầm thường gặp

- **Triển khai thủ công**, dễ lỗi con người.
- **Thiếu observability** — mù trước sự cố.
- **Không có rollback/khôi phục.**
- **Bỏ kiểm soát thay đổi** cho hệ thống lâm sàng.
- **Bỏ qua quy định địa điểm dữ liệu.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Sự cố hệ thống chạm lâm sàng có thể ảnh hưởng chăm sóc — cần độ sẵn sàng, khôi phục và dự phòng. Thay đổi không kiểm soát có thể đưa lỗi; với thiết bị y tế cần kiểm soát thay đổi và có thể validation/đánh giá lại (chương 20, 23, 47). Lưu trữ dữ liệu y tế chịu quy định (địa điểm, bảo mật — chương 40).

## 13. Chỉ số đo lường

Tần suất triển khai, tỉ lệ triển khai thất bại, thời gian phát hiện/khôi phục sự cố (MTTD/MTTR), uptime, và kết quả diễn tập khôi phục. Cân bằng tốc độ và ổn định.

## 14. Bằng chứng và mức độ tin cậy

Độ tin cậy phải **chứng minh bằng diễn tập và đo lường**, không giả định. Runbook chỉ hữu ích nếu được kiểm thử (diễn tập khôi phục). Ghi rõ giả định về hạ tầng; điều chỉnh theo thực tế vận hành.

## 15. Tiêu chuẩn và guideline liên quan

Gắn QMS/kiểm soát thay đổi (chương 23), bảo mật (chương 39), privacy/địa điểm dữ liệu (chương 40), kiến trúc (chương 53), MLOps (chương 50). Tuân quy định lưu trữ dữ liệu y tế hiện hành.

## 16. Liên hệ các chương khác

Vận hành hóa **53**; gắn QMS **23**, bảo mật **39–40**, MLOps **50**; dữ liệu **54**.

## 17. Bài tập thực hành — Deployment runbook

Viết deployment runbook: quy trình CI/CD và kiểm thử, kiểm soát thay đổi cho hệ thống lâm sàng, observability (log/metric/trace/alert), kế hoạch rollback và disaster recovery (RTO/RPO), và xác minh quy định lưu trữ/bảo mật dữ liệu. Nêu kế hoạch diễn tập khôi phục. Ghi rõ điều cần xác minh.

## 18. Checklist tự đánh giá

- [ ] CI/CD với kiểm thử tự động.
- [ ] Kiểm soát thay đổi cho hệ thống lâm sàng.
- [ ] Observability đủ để phát hiện sự cố sớm.
- [ ] Rollback và disaster recovery có kế hoạch và diễn tập.
- [ ] Quy định địa điểm/bảo mật dữ liệu được xác minh.

## 19. Định nghĩa hoàn thành (Definition of Done)

Deployment runbook đạt chuẩn khi tự động hóa triển khai với kiểm thử, áp kiểm soát thay đổi, có observability và rollback/khôi phục được diễn tập, và tuân quy định lưu trữ/bảo mật dữ liệu.

## 20. Câu hỏi phản tư

Tôi phát hiện sự cố trước hay sau người dùng? Tôi rollback/khôi phục được nhanh không? Thay đổi hệ thống lâm sàng có qua kiểm soát không? Lưu trữ dữ liệu của tôi có tuân quy định địa điểm không?

## 21. Cạm bẫy quyết định

**Tốc độ lấn an toàn**, **mù observability**, **không diễn tập khôi phục**. Đối trọng: kiểm soát thay đổi, giám sát đầy đủ, và diễn tập khôi phục định kỳ.

## 22. Nguồn dữ liệu động cần xác minh

Quy định lưu trữ/địa điểm dữ liệu y tế, tiêu chuẩn bảo mật cloud — là dữ liệu động. Tra văn bản chính thức và tham vấn; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md), [Thư viện SOP](../../resources/sop-library.md). Quy định tra tại nguồn chính thức.

## 24. Thuật ngữ

**CI/CD:** tích hợp/triển khai liên tục. **Observability:** khả năng quan sát. **Rollback:** khôi phục phiên bản. **Disaster recovery:** khôi phục thảm họa. **RTO/RPO:** mục tiêu thời gian/điểm khôi phục.

## 25. Tóm tắt và bước tiếp theo

DevOps trong y tế cân bằng tốc độ và kiểm soát: tự động hóa, giám sát, và khôi phục nhanh là yêu cầu an toàn. Tiếp theo sang **[chương 56 — Phân tích sản phẩm](../56-product-analytics/README.md)** để đo lường giá trị và hành vi.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Sự cố hệ thống chạm lâm sàng có thể ảnh hưởng chăm sóc — cần độ sẵn sàng và khôi phục; thay đổi cần kiểm soát; lưu trữ dữ liệu y tế chịu quy định địa điểm/bảo mật.
