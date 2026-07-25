# 07 — Phân tích quy trình lâm sàng

> **Nhánh 1 — Nền tảng Doctorpreneur** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Lập bản đồ workflow và phát hiện điểm nghẽn.
> **Sản phẩm của chương:** Workflow map.

---

## 1. Tóm tắt điều hành

Giải pháp y tế tốt trên giấy vẫn thất bại nếu phá vỡ luồng công việc thật. Phân tích quy trình lâm sàng là kỹ năng lập bản đồ các bước, tác nhân, thông tin và điểm chuyển giao trong một quy trình chăm sóc, để phát hiện điểm nghẽn, bước thừa và nguy cơ sai sót. Đầu ra là *workflow map* — bản đồ trạng thái hiện tại (current-state) làm nền cho mọi can thiệp: bạn không thể cải thiện thứ chưa vẽ ra được.

## 2. Mục tiêu học tập

Bạn sẽ: (a) lập bản đồ current-state với tác nhân, bước, thời gian và điểm chuyển giao; (b) phát hiện điểm nghẽn, lãng phí và điểm dễ sai; (c) phân biệt quy trình được kê khai với quy trình thực tế; (d) xác định điểm chèn giải pháp ít gây gián đoạn nhất.

## 3. Vì sao chương này sống còn với Doctorpreneur

Nguyên nhân phổ biến khiến HealthTech bị bỏ dùng là "alert fatigue" và tăng gánh nặng thao tác. Hiểu workflow giúp bạn thiết kế giải pháp *giảm* bước thay vì *thêm* bước, và chèn đúng điểm trong luồng để được chấp nhận. Đây là cầu nối giữa insight người dùng và thiết kế sản phẩm khả thi.

## 4. Khái niệm cốt lõi và định nghĩa

**Current-state map:** bản đồ quy trình đang diễn ra. **Future-state map:** quy trình mong muốn sau can thiệp. **Điểm nghẽn (bottleneck):** bước giới hạn thông lượng. **Điểm chuyển giao (handoff):** nơi trách nhiệm/thông tin chuyển giữa các tác nhân — nguồn sai sót lớn. **Work-as-imagined vs work-as-done:** quy trình kê khai vs thực tế.

## 5. Khung tư duy nền tảng

Kết hợp lăng kính Lean (loại bỏ lãng phí, tôn trọng người làm) và kỹ thuật an toàn hệ thống (điểm chuyển giao và biến thiên là nơi sai sót nảy sinh). Luôn lập bản đồ *work-as-done* bằng quan sát trực tiếp, không chỉ dựa vào quy trình văn bản. Đo thời gian và số bước để định lượng lãng phí.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Tuyến cơ sở nhiều quy trình phụ thuộc giấy tờ, chữ ký và luân chuyển vật lý, tạo điểm nghẽn và chuyển giao nhiều. BHYT thêm các bước xác nhận thủ tục. Bản đồ hóa các luồng này thường lộ ra "quả treo thấp": bước thừa có thể bỏ mà không cần công nghệ.

## 7. Các bên liên quan

Mỗi tác nhân trong luồng — bác sĩ, điều dưỡng, dược, xét nghiệm, hành chính, BHYT — có mục tiêu và ràng buộc riêng. Bản đồ phải thể hiện swimlane theo tác nhân để thấy chuyển giao và mâu thuẫn động lực, tránh tối ưu cục bộ gây hại toàn cục.

## 8. Quy trình từng bước

1. **Chọn phạm vi** quy trình (điểm đầu–điểm cuối rõ ràng).
2. **Quan sát work-as-done**, không chỉ đọc SOP.
3. **Vẽ swimlane** theo tác nhân, ghi bước, thời gian, thông tin, quyết định.
4. **Đánh dấu điểm nghẽn, lãng phí, điểm dễ sai và chuyển giao.**
5. **Định lượng** thời gian/số bước để ưu tiên.
6. **Phác future-state** và điểm chèn giải pháp ít gián đoạn nhất.

## 9. Công cụ và template áp dụng

- **Swimlane workflow map** (vẽ tay hoặc công cụ sơ đồ).
- **Bảng điểm nghẽn:** bước · loại lãng phí · tác động · ý tưởng cải thiện.
- **Handoff register** liệt kê chuyển giao và rủi ро.

## 10. Ví dụ minh họa

Quy trình trả kết quả xét nghiệm: bản đồ current-state lộ ra kết quả in ra, chuyển tay, chờ bác sĩ đọc, rồi mới báo bệnh nhân — nhiều chuyển giao, độ trễ lớn. Điểm nghẽn không phải phòng xét nghiệm mà là bước chuyển giao thủ công. Giải pháp đúng nhắm vào chuyển giao, không phải tăng tốc máy xét nghiệm.

## 11. Sai lầm thường gặp

- **Vẽ work-as-imagined** thay vì thực tế.
- **Bỏ qua điểm chuyển giao** — nơi sai sót thật sự.
- **Tối ưu cục bộ** gây nghẽn chỗ khác.
- **Thêm bước** cho người dùng đã quá tải.
- **Không định lượng** nên không ưu tiên được.

## 12. Rủi ro an toàn, pháp lý và đạo đức

Thay đổi workflow lâm sàng có thể tạo nguy cơ mới (bỏ sót, nhầm thông tin). Mọi thay đổi phải qua phân tích rủi ro (chương 24) và giữ điểm kiểm soát an toàn. Không loại bỏ bước kiểm tra chỉ vì nó "chậm" nếu nó là hàng rào an toàn. Quan sát thực địa phải bảo mật dữ liệu bệnh nhân.

## 13. Chỉ số đo lường

Trước/sau can thiệp: thời gian chu trình, số bước, số chuyển giao, tỉ lệ sai sót/làm lại, thời gian chờ. Thêm chỉ số gánh nặng người dùng (số thao tác, số lần chuyển màn hình) để tránh giải pháp làm tăng việc.

## 14. Bằng chứng và mức độ tin cậy

Bản đồ workflow là **mô tả hệ thống**, độ tin cậy phụ thuộc chất lượng quan sát. Số đo thời gian nội bộ là dữ liệu ngữ cảnh, không khái quát sang nơi khác. Tuyên bố "giảm X% thời gian" cần đo lường có phương pháp, không suy diễn từ sơ đồ.

## 15. Tiêu chuẩn và guideline liên quan

Liên hệ nguyên tắc cải tiến chất lượng (PDSA) và kỹ thuật yếu tố con người. Khi can thiệp là phần mềm chạm lâm sàng, gắn quản lý rủi ro ISO 14971 (chương 24) và thiết kế CDS (chương 38).

## 16. Liên hệ các chương khác

Dùng insight từ **05–06**; nền cho **08** (giá trị theo từng bước quy trình), **35–36** (tích hợp EHR/FHIR vào luồng), **38** (CDS đúng điểm), **51–52** (product/UX).

## 17. Bài tập thực hành — Workflow map

Chọn một quy trình trong đơn vị bạn, quan sát work-as-done, vẽ swimlane current-state với thời gian và chuyển giao, đánh dấu điểm nghẽn và điểm dễ sai, định lượng ít nhất một chỉ số, rồi phác future-state cùng điểm chèn giải pháp ít gián đoạn nhất. Ghi giả định cần xác minh.

## 18. Checklist tự đánh giá

- [ ] Bản đồ dựa trên quan sát thực, không chỉ SOP.
- [ ] Có swimlane theo tác nhân và điểm chuyển giao.
- [ ] Đã đánh dấu điểm nghẽn, lãng phí, điểm dễ sai.
- [ ] Có ít nhất một chỉ số định lượng.
- [ ] Điểm chèn giải pháp giảm bước, không tăng gánh nặng.

## 19. Định nghĩa hoàn thành (Definition of Done)

Workflow map đạt chuẩn khi phản ánh work-as-done qua quan sát, thể hiện tác nhân và chuyển giao, định lượng ít nhất một chỉ số, nhận diện điểm nghẽn/điểm dễ sai, và chỉ ra điểm chèn giải pháp ít gián đoạn nhất.

## 20. Câu hỏi phản tư

Bản đồ của tôi là quy trình thật hay quy trình trên giấy? Sai sót thực sự nảy sinh ở đâu? Giải pháp của tôi giảm bước hay thêm bước cho người đã quá tải? Tôi có đang loại bỏ một hàng rào an toàn không?

## 21. Cạm bẫy quyết định

**Ảo tưởng quy hoạch:** tin quy trình văn bản là thực tế. **Tối ưu cục bộ** vì chỉ nhìn một tác nhân. Đối trọng: quan sát đa vai, đo lường, và kiểm định future-state với người làm thật.

## 22. Nguồn dữ liệu động cần xác minh

Số đo thời gian/tần suất phải từ đo thực tế; không mượn số từ nghiên cứu bối cảnh khác. Ghi ngày đo và điều kiện. Ước lượng chưa đo giữ là giả định.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện SOP](../../resources/sop-library.md) và [Thư viện template](../../resources/template-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Swimlane:** làn theo tác nhân trong sơ đồ. **Bottleneck:** điểm nghẽn. **Handoff:** chuyển giao. **PDSA:** Plan–Do–Study–Act. **Work-as-done:** quy trình thực tế.

## 25. Tóm tắt và bước tiếp theo

Không thể cải thiện luồng chưa vẽ ra được; và giải pháp được chấp nhận là giải pháp giảm bước, chèn đúng điểm, giữ hàng rào an toàn. Tiếp theo sang **[chương 08 — Tuyên bố giá trị HealthTech](../08-value-proposition/README.md)** để chuyển hiểu biết quy trình thành giá trị cho từng bên.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Thay đổi workflow lâm sàng cần phân tích rủi ro và giữ hàng rào an toàn; quan sát thực địa phải bảo mật dữ liệu bệnh nhân.
