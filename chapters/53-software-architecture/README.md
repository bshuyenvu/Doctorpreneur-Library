# 53 — Kiến trúc phần mềm y tế

> **Nhánh 6 — Sản phẩm, công nghệ và tổ chức** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Chọn kiến trúc an toàn, mở rộng và bảo trì.
> **Sản phẩm của chương:** Architecture decision record.

---

## 1. Tóm tắt điều hành

Kiến trúc phần mềm quyết định hệ thống có an toàn, mở rộng, bảo trì và tích hợp được không — những thuộc tính khó sửa về sau. Trong y tế, kiến trúc còn phải hỗ trợ bảo mật, truy vết, độ sẵn sàng và tuân thủ ngay từ thiết kế. Founder không cần tự thiết kế mọi chi tiết, nhưng phải hiểu đủ để ra và ghi lại các quyết định kiến trúc trọng yếu. Đầu ra là *architecture decision record (ADR)*: bản ghi một quyết định kiến trúc, lý do, đánh đổi và hệ quả.

## 2. Mục tiêu học tập

Bạn sẽ: (a) hiểu các thuộc tính chất lượng kiến trúc (an toàn, mở rộng, bảo trì...); (b) nhận diện đánh đổi kiến trúc trọng yếu; (c) tính bảo mật/truy vết/độ sẵn sàng từ thiết kế; (d) viết ADR.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Quyết định kiến trúc sai (ví dụ ghép chặt, bỏ truy vết) tạo nợ kỹ thuật đắt và rủi ro an toàn/tuân thủ khó sửa. Hiểu kiến trúc giúp bạn đối thoại với kỹ thuật và bảo vệ các thuộc tính quan trọng cho y tế.

## 4. Khái niệm cốt lõi và định nghĩa

**Thuộc tính chất lượng:** an toàn, bảo mật, mở rộng, bảo trì, độ sẵn sàng, khả năng tích hợp. **Coupling/cohesion:** mức phụ thuộc/gắn kết. **ADR:** bản ghi quyết định kiến trúc. **Audit trail:** truy vết. **Availability/resilience:** độ sẵn sàng/khả năng chịu lỗi. **Technical debt:** nợ kỹ thuật.

## 5. Khung tư duy nền tảng

Kiến trúc là chuỗi đánh đổi giữa các thuộc tính chất lượng — không có "đúng nhất", chỉ có phù hợp bối cảnh. Xác định thuộc tính quan trọng nhất cho sản phẩm y tế (thường: an toàn, bảo mật, truy vết, độ sẵn sàng, tích hợp) và thiết kế/đánh đổi có ý thức. Ghi lại quyết định bằng ADR để đội hiểu lý do. Nguyên tắc: tính bảo mật, truy vết và độ sẵn sàng từ thiết kế; ưu tiên đơn giản và khả năng tích hợp (chương 35–36).

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Ràng buộc hạ tầng tuyến cơ sở (mạng, điện, thiết bị) đòi hỏi kiến trúc chịu được gián đoạn (ví dụ hoạt động khi mất mạng, đồng bộ lại sau). Tích hợp HIS đa dạng (chương 35) là yêu cầu kiến trúc trọng yếu. Cân nhắc chi phí vận hành và bảo trì trong điều kiện nguồn lực hạn chế.

## 7. Các bên liên quan

Kỹ sư/kiến trúc sư, bảo mật, vận hành (DevOps — chương 55), và tuân thủ. Founder tham gia quyết định trọng yếu ảnh hưởng an toàn, chi phí và tuân thủ.

## 8. Quy trình từng bước

1. **Xác định thuộc tính chất lượng ưu tiên** cho sản phẩm.
2. **Nhận diện quyết định kiến trúc trọng yếu.**
3. **Đánh giá phương án và đánh đổi.**
4. **Thiết kế bảo mật/truy vết/độ sẵn sàng từ đầu.**
5. **Ra quyết định và ghi ADR** (lý do, đánh đổi, hệ quả).
6. **Rà soát định kỳ** khi bối cảnh đổi.

## 9. Công cụ và template áp dụng

- **ADR template:** bối cảnh · quyết định · phương án · đánh đổi · hệ quả.
- **Bảng thuộc tính chất lượng** (ưu tiên theo sản phẩm).
- **Checklist kiến trúc y tế** (bảo mật, truy vết, sẵn sàng, tích hợp).

## 10. Ví dụ minh họa

Chọn giữa kiến trúc phụ thuộc mạng liên tục và kiến trúc hoạt động offline-first. ADR: bối cảnh (tuyến cơ sở mạng không ổn định); quyết định (offline-first, đồng bộ lại); đánh đổi (phức tạp đồng bộ vs độ sẵn sàng lâm sàng); hệ quả (cần xử lý xung đột dữ liệu, truy vết). Ghi lý do để đội và người sau hiểu.

## 11. Sai lầm thường gặp

- **Bỏ truy vết/bảo mật** khỏi thiết kế ban đầu.
- **Ghép chặt (tight coupling)** khó bảo trì/tích hợp.
- **Tối ưu quá sớm** cho quy mô chưa có.
- **Không ghi ADR** — mất lý do quyết định.
- **Bỏ qua ràng buộc hạ tầng** thực tế.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Kiến trúc thiếu truy vết/bảo mật/độ sẵn sàng gây rủi ro an toàn và tuân thủ (chương 39–40). Hệ thống chạm lâm sàng phải chịu lỗi và có phương án dự phòng để không gián đoạn chăm sóc. Với thiết bị y tế, quyết định kiến trúc là phần của quản lý rủi ro và design control (chương 23–24).

## 13. Chỉ số đo lường

Độ sẵn sàng (uptime), độ trễ, khả năng tích hợp (số hệ thống kết nối), nợ kỹ thuật (đo gián tiếp), và số sự cố liên quan kiến trúc. Theo dõi để hướng dẫn tái cấu trúc.

## 14. Bằng chứng và mức độ tin cậy

Không có kiến trúc "đúng" phổ quát — lựa chọn phụ thuộc bối cảnh và đánh đổi. ADR ghi lại *lý do* để quyết định có thể được đánh giá lại. Nêu rõ giả định (quy mô, hạ tầng) mà quyết định dựa vào; điều chỉnh khi giả định đổi.

## 15. Tiêu chuẩn và guideline liên quan

Gắn bảo mật (chương 39), privacy (chương 40), tích hợp (chương 35–36), DevOps (chương 55), data engineering (chương 54), QMS/design control nếu là thiết bị y tế (chương 23–24).

## 16. Liên hệ các chương khác

Nền kỹ thuật cho **54–55**; tích hợp **35–36**; bảo mật **39–40**; MLOps **50**; rủi ro **24**.

## 17. Bài tập thực hành — Architecture decision record

Viết một ADR cho một quyết định kiến trúc trọng yếu của sản phẩm: nêu bối cảnh và thuộc tính chất lượng ưu tiên, các phương án, đánh đổi, quyết định và hệ quả (gồm bảo mật/truy vết/độ sẵn sàng). Ghi rõ giả định (quy mô, hạ tầng) và điều kiện đánh giá lại.

## 18. Checklist tự đánh giá

- [ ] Xác định thuộc tính chất lượng ưu tiên.
- [ ] Bảo mật/truy vết/độ sẵn sàng thiết kế từ đầu.
- [ ] Đánh đổi được cân nhắc có ý thức.
- [ ] Kiến trúc hỗ trợ tích hợp HIS.
- [ ] Quyết định được ghi ADR với lý do.

## 19. Định nghĩa hoàn thành (Definition of Done)

ADR đạt chuẩn khi nêu bối cảnh và thuộc tính ưu tiên, so sánh phương án và đánh đổi, tính bảo mật/truy vết/độ sẵn sàng, và ghi lý do + giả định để đánh giá lại.

## 20. Câu hỏi phản tư

Thuộc tính chất lượng nào quan trọng nhất cho sản phẩm y tế của tôi? Kiến trúc có chịu được gián đoạn hạ tầng không? Tôi đã tính bảo mật/truy vết từ đầu chưa? Lý do quyết định có được ghi lại không?

## 21. Cạm bẫy quyết định

**Tối ưu quá sớm**, **ghép chặt**, **bỏ truy vết**. Đối trọng: ưu tiên đơn giản và tích hợp, thiết kế bảo mật từ đầu, và ghi ADR.

## 22. Nguồn dữ liệu động cần xác minh

Yêu cầu tích hợp HIS thực tế, ràng buộc hạ tầng, tiêu chuẩn bảo mật — là dữ liệu động. Khảo sát thực tế và tra chuẩn; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Open source](../../resources/open-source-library.md), [Thư viện sách](../../resources/book-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**ADR:** architecture decision record. **Coupling/cohesion:** phụ thuộc/gắn kết. **Audit trail:** truy vết. **Availability/resilience:** độ sẵn sàng/chịu lỗi. **Technical debt:** nợ kỹ thuật.

## 25. Tóm tắt và bước tiếp theo

Kiến trúc là chuỗi đánh đổi có ý thức; trong y tế, tính bảo mật, truy vết, độ sẵn sàng và tích hợp phải thiết kế từ đầu và ghi lại bằng ADR. Tiếp theo sang **[chương 54 — Kỹ thuật dữ liệu y tế](../54-data-engineering/README.md)** cho hạ tầng dữ liệu.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Kiến trúc thiếu bảo mật/truy vết/độ sẵn sàng gây rủi ro an toàn và tuân thủ; hệ thống chạm lâm sàng phải chịu lỗi và có dự phòng.
