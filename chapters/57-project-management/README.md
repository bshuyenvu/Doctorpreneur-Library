# 57 — Quản lý dự án HealthTech

> **Nhánh 6 — Sản phẩm, công nghệ và tổ chức** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Quản lý phạm vi, rủi ro, tiến độ và stakeholder.
> **Sản phẩm của chương:** Project RAID log.

---

## 1. Tóm tắt điều hành

Quản lý dự án biến kế hoạch thành thực thi có kiểm soát: quản lý phạm vi, tiến độ, rủi ro và các bên liên quan. Trong HealthTech, dự án thường có nhiều phụ thuộc (kỹ thuật, lâm sàng, tuân thủ, tích hợp) và bên liên quan, nên rủi ro phối hợp cao. Đầu ra là *project RAID log*: nhật ký theo dõi Risks (rủi ro), Assumptions (giả định), Issues (vấn đề), Dependencies (phụ thuộc) — công cụ giữ dự án không trật bánh.

## 2. Mục tiêu học tập

Bạn sẽ: (a) quản lý phạm vi và chống scope creep; (b) nhận diện và theo dõi rủi ro/phụ thuộc; (c) quản lý bên liên quan; (d) duy trì RAID log.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Dự án HealthTech thất bại thường vì phụ thuộc bị bỏ sót (tích hợp HIS, phê duyệt tuân thủ) và scope creep. RAID log giúp phát hiện sớm và xử lý, giữ dự án đi đúng hướng với nguồn lực giới hạn.

## 4. Khái niệm cốt lõi và định nghĩa

**Scope:** phạm vi công việc. **Scope creep:** phạm vi phình ngoài kiểm soát. **RAID:** risks, assumptions, issues, dependencies. **Milestone:** cột mốc. **Critical path:** đường găng (chuỗi quyết định tiến độ). **Stakeholder management:** quản lý bên liên quan.

## 5. Khung tư duy nền tảng

Quản lý dự án là quản lý rủi ro và phụ thuộc chủ động, không phải chỉ theo dõi tiến độ. Dùng RAID log để làm hiện các ẩn số: rủi ro (điều có thể sai), giả định (điều đang cho là đúng), vấn đề (điều đang sai), phụ thuộc (điều chờ bên khác). Với y tế, phụ thuộc tuân thủ và tích hợp thường là đường găng. Nguyên tắc: quản lý phạm vi chặt (thay đổi qua kiểm soát), làm hiện và xử lý rủi ro/phụ thuộc sớm.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Phụ thuộc vào nhà cung HIS, phê duyệt nội bộ bệnh viện, và chu kỳ ngân sách thường là rủi ro tiến độ lớn ở tuyến cơ sở. Kế hoạch phải tính các phụ thuộc bên ngoài này và có phương án dự phòng. Nguồn lực hạn chế đòi hỏi phạm vi thực tế.

## 7. Các bên liên quan

Đội dự án (kỹ thuật, lâm sàng, sản phẩm), lãnh đạo, và bên ngoài (nhà cung HIS, cơ quan). Quản lý kỳ vọng và giao tiếp với bên liên quan là phần cốt lõi.

## 8. Quy trình từng bước

1. **Xác định phạm vi** và tiêu chí hoàn thành.
2. **Lập kế hoạch** với milestone và đường găng.
3. **Khởi tạo RAID log** (rủi ro, giả định, vấn đề, phụ thuộc).
4. **Quản lý bên liên quan** và giao tiếp định kỳ.
5. **Theo dõi và cập nhật RAID** thường xuyên; xử lý sớm.
6. **Kiểm soát thay đổi phạm vi** qua quy trình.

## 9. Công cụ và template áp dụng

- **RAID log:** hạng mục · loại · mức · chủ sở hữu · hành động · trạng thái.
- **Milestone plan / đường găng.**
- **Stakeholder map** (ảnh hưởng/quan tâm).

## 10. Ví dụ minh họa

Dự án triển khai công cụ tại bệnh viện. RAID log: rủi ro (nhà cung HIS chậm mở API); giả định (bệnh viện có ngân sách quý này); vấn đề (thiếu nhân sự CNTT phối hợp); phụ thuộc (phê duyệt tuân thủ dữ liệu). Mỗi mục có chủ sở hữu và hành động. Phụ thuộc HIS nằm trên đường găng — cần xử lý sớm để không trễ toàn dự án.

## 11. Sai lầm thường gặp

- **Scope creep** không kiểm soát.
- **Bỏ sót phụ thuộc** (tích hợp, tuân thủ).
- **RAID log lập rồi bỏ** (không cập nhật).
- **Quản lý bên liên quan kém** (kỳ vọng lệch).
- **Không có đường găng rõ.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Áp lực tiến độ không được đẩy tới cắt bước an toàn/tuân thủ (validation, đánh giá rủi ro). Phụ thuộc tuân thủ (thiết bị y tế, dữ liệu) phải được tôn trọng, không "làm tắt". Giao tiếp trung thực về rủi ro/tiến độ với bên liên quan là nghĩa vụ.

## 13. Chỉ số đo lường

Độ lệch tiến độ/ngân sách so kế hoạch, số rủi ro/vấn đề mở và thời gian xử lý, độ ổn định phạm vi (số thay đổi), và mức hài lòng bên liên quan. Theo dõi để điều chỉnh sớm.

## 14. Bằng chứng và mức độ tin cậy

Kế hoạch dự án là **ước lượng dưới bất định**; RAID log làm hiện bất định thay vì giả định chắc chắn. Ước lượng tiến độ/nguồn lực có sai số — ghi rõ giả định và cập nhật. Không cam kết cứng khi phụ thuộc bên ngoài chưa chắc.

## 15. Tiêu chuẩn và guideline liên quan

Tham chiếu thực hành quản lý dự án (agile/waterfall tùy bối cảnh). Gắn product management (chương 51), QMS/kiểm soát thay đổi (chương 23) cho thiết bị y tế, đội ngũ (chương 58).

## 16. Liên hệ các chương khác

Thực thi hóa **51**; gắn QMS **23**, đội ngũ **58**, tích hợp **35**; rủi ro sản phẩm **24**.

## 17. Bài tập thực hành — Project RAID log

Lập RAID log cho một dự án: liệt kê rủi ro, giả định, vấn đề, phụ thuộc với mức, chủ sở hữu và hành động; lập milestone plan và xác định đường găng (chú ý phụ thuộc tuân thủ/tích hợp); và stakeholder map. Nêu quy trình kiểm soát thay đổi phạm vi. Ghi rõ giả định cần kiểm.

## 18. Checklist tự đánh giá

- [ ] Phạm vi và tiêu chí hoàn thành rõ.
- [ ] RAID log đầy đủ và được cập nhật.
- [ ] Phụ thuộc tuân thủ/tích hợp được nhận diện.
- [ ] Đường găng xác định.
- [ ] Bên liên quan được quản lý kỳ vọng.

## 19. Định nghĩa hoàn thành (Definition of Done)

RAID log đạt chuẩn khi làm hiện rủi ro/giả định/vấn đề/phụ thuộc với chủ sở hữu và hành động, gắn milestone và đường găng, và được cập nhật để xử lý sớm.

## 20. Câu hỏi phản tư

Phụ thuộc nào có thể làm trễ toàn dự án — tôi xử lý sớm chưa? Phạm vi có đang phình không? Rủi ro của tôi có chủ sở hữu và hành động không? Bên liên quan có kỳ vọng đúng không?

## 21. Cạm bẫy quyết định

**Scope creep**, **bỏ sót phụ thuộc**, **lạc quan tiến độ**. Đối trọng: kiểm soát thay đổi, RAID cập nhật, và đường găng rõ.

## 22. Nguồn dữ liệu động cần xác minh

Tiến độ phụ thuộc bên ngoài (HIS, phê duyệt), chu kỳ ngân sách — là dữ liệu động. Xác minh với bên liên quan và cập nhật RAID; ghi ngày.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện template](../../resources/template-library.md), [Thư viện SOP](../../resources/sop-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**RAID:** risks–assumptions–issues–dependencies. **Scope creep:** phình phạm vi. **Critical path:** đường găng. **Milestone:** cột mốc. **Stakeholder:** bên liên quan.

## 25. Tóm tắt và bước tiếp theo

Quản lý dự án tốt là quản lý rủi ro và phụ thuộc chủ động qua RAID log, kiểm soát phạm vi, và không cắt bước an toàn vì tiến độ. Tiếp theo sang **[chương 58 — Xây dựng đội ngũ liên ngành](../58-team-building/README.md)** cho con người thực thi.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Áp lực tiến độ không được cắt bước an toàn/tuân thủ; giao tiếp trung thực về rủi ro và tiến độ với bên liên quan.
