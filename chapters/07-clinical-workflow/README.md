# 07 — Phân tích quy trình lâm sàng

> **Nhánh 1 — Nền tảng Doctorpreneur** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Lập bản đồ workflow và phát hiện điểm nghẽn.
> **Sản phẩm của chương:** Workflow map.

---

## 1. Tóm tắt điều hành

Giải pháp y tế tốt trên giấy vẫn thất bại nếu phá vỡ luồng công việc thật. Đây là một trong những nguyên nhân bị đánh giá thấp nhất khiến HealthTech bị bỏ dùng: sản phẩm giải đúng vấn đề nhưng thêm một bước, một cú click, một màn hình vào một quy trình đã quá tải — và người dùng lặng lẽ quay lại cách cũ. Phân tích quy trình lâm sàng là kỹ năng lập bản đồ các bước, tác nhân, thông tin và điểm chuyển giao trong một quy trình chăm sóc, để phát hiện điểm nghẽn, bước thừa và nguy cơ sai sót — và để đặt giải pháp vào đúng chỗ trong luồng.

Nguyên tắc trung tâm: bạn không thể cải thiện thứ chưa vẽ ra được, và bạn không thể vẽ đúng nếu chỉ đọc quy trình văn bản. Đầu ra là *workflow map* — bản đồ trạng thái hiện tại (current-state) dựa trên *quan sát thực tế* (work-as-done), làm nền cho mọi can thiệp và cho việc xác định điểm chèn giải pháp ít gây gián đoạn nhất.

## 2. Mục tiêu học tập

Bạn sẽ: (a) lập bản đồ current-state với tác nhân, bước, thời gian và điểm chuyển giao; (b) phát hiện điểm nghẽn, lãng phí và điểm dễ sai; (c) phân biệt quy trình được kê khai (work-as-imagined) với quy trình thực tế (work-as-done); (d) xác định điểm chèn giải pháp ít gây gián đoạn nhất và không tăng gánh nặng.

## 3. Vì sao chương này sống còn với Doctorpreneur

Nguyên nhân phổ biến khiến HealthTech bị bỏ dùng là "alert fatigue" và tăng gánh nặng thao tác — cả hai đều là lỗi *workflow*, không phải lỗi ý tưởng. Là bác sĩ, bạn có lợi thế hiếm: bạn *sống* trong workflow thật và thấy được khoảng cách giữa quy trình văn bản và thực tế mà founder ngoài ngành không thấy. Nhưng lợi thế này kèm bẫy: bạn quen luồng đến mức "mù" với các bước thừa mà người mới sẽ thấy ngay. Phân tích có phương pháp giúp bạn thiết kế giải pháp *giảm* bước thay vì *thêm* bước, và chèn đúng điểm để được chấp nhận — cầu nối giữa insight người dùng (chương 05) và thiết kế sản phẩm khả thi (chương 51–52).

## 4. Khái niệm cốt lõi và định nghĩa

**Current-state map:** bản đồ quy trình đang diễn ra thực tế. **Future-state map:** quy trình mong muốn sau can thiệp. **Điểm nghẽn (bottleneck):** bước giới hạn thông lượng của toàn luồng — cải thiện chỗ khác không giúp nếu nghẽn còn. **Điểm chuyển giao (handoff):** nơi trách nhiệm/thông tin chuyển giữa các tác nhân — nguồn sai sót lớn nhất trong hệ thống y tế. **Work-as-imagined vs work-as-done:** quy trình kê khai (SOP, sơ đồ chính thức) vs quy trình thực tế người ta làm. **Lãng phí (waste):** bước không tạo giá trị (chờ, làm lại, di chuyển thừa, nhập liệu trùng). **Swimlane:** làn phân theo tác nhân trong sơ đồ.

## 5. Khung tư duy nền tảng

Kết hợp hai lăng kính:
- **Lean:** loại bỏ lãng phí (chờ đợi, làm lại, di chuyển thừa, nhập trùng), tôn trọng người làm (họ biết luồng thật). Đo thời gian và số bước để định lượng lãng phí.
- **Kỹ thuật an toàn hệ thống:** điểm chuyển giao và biến thiên là nơi sai sót nảy sinh; một số bước "chậm" thực ra là *hàng rào an toàn* không được loại bỏ.

Nguyên tắc cốt lõi: luôn lập bản đồ **work-as-done bằng quan sát trực tiếp**, không chỉ dựa vào quy trình văn bản. Khoảng cách giữa work-as-imagined và work-as-done là nơi cả vấn đề *và* giải pháp thực sự nằm — nếu bạn thiết kế cho quy trình trên giấy, sản phẩm sẽ không khớp thực tế.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Tuyến cơ sở nhiều quy trình phụ thuộc giấy tờ, chữ ký và luân chuyển vật lý, tạo nhiều điểm nghẽn và chuyển giao. BHYT thêm các bước xác nhận thủ tục. Bản đồ hóa các luồng này thường lộ ra "quả treo thấp": bước thừa có thể bỏ mà không cần công nghệ — đôi khi giải pháp giá trị nhất là *bỏ một bước*, không phải *thêm một hệ thống*.

Đặc thù quan trọng: work-as-done ở tuyến cơ sở thường lệch xa work-as-imagined vì nhân viên tự chế "lối tắt" để xoay xở với thiếu nguồn lực. Những lối tắt này vừa là dấu hiệu vấn đề (quy trình chính thức không khả thi) vừa là nguồn hiểu biết quý (người làm đã tìm ra cách hiệu quả hơn). Quan sát và tôn trọng chúng thay vì áp quy trình lý thuyết.

## 7. Các bên liên quan

Mỗi tác nhân trong luồng — bác sĩ, điều dưỡng, dược, xét nghiệm, hành chính, BHYT — có mục tiêu và ràng buộc riêng. Bản đồ phải thể hiện swimlane theo tác nhân để thấy chuyển giao và mâu thuẫn động lực. Cảnh báo trung tâm: **tránh tối ưu cục bộ gây hại toàn cục** — giải pháp làm bác sĩ nhanh hơn nhưng đẩy gánh nặng sang điều dưỡng có thể tăng tổng lãng phí và bị điều dưỡng (người bị ảnh hưởng vận hành) từ chối. Luôn hỏi: giải pháp này đẩy công việc đi đâu?

## 8. Quy trình từng bước

1. **Chọn phạm vi** quy trình (điểm đầu–điểm cuối rõ ràng) — đừng vẽ cả bệnh viện.
2. **Quan sát work-as-done**, không chỉ đọc SOP; đi theo chân người làm (shadowing).
3. **Vẽ swimlane** theo tác nhân, ghi bước, thời gian, thông tin trao đổi, điểm quyết định.
4. **Đánh dấu** điểm nghẽn, lãng phí, điểm dễ sai và chuyển giao.
5. **Định lượng** thời gian/số bước/số chuyển giao để ưu tiên can thiệp.
6. **Phác future-state** và xác định điểm chèn giải pháp ít gián đoạn nhất, kiểm với người làm thật.

## 9. Công cụ và template áp dụng

- **Swimlane workflow map** (vẽ tay hoặc công cụ sơ đồ) — làn theo tác nhân, mũi tên theo luồng.
- **Bảng điểm nghẽn:** bước · loại lãng phí · tác động (thời gian/lỗi) · ý tưởng cải thiện.
- **Handoff register** liệt kê chuyển giao và rủi ro sai sót tại mỗi điểm.
- **Bảng gánh nặng người dùng:** số thao tác, số màn hình, thời gian thêm — để tránh giải pháp tăng việc.

## 10. Ví dụ minh họa

Quy trình trả kết quả xét nghiệm. Bản đồ current-state (dựa quan sát) lộ ra: kết quả in ra → chuyển tay qua nhiều khâu → chờ bác sĩ đọc → rồi mới báo bệnh nhân. Nhiều chuyển giao, độ trễ lớn. Định lượng cho thấy điểm nghẽn *không* phải phòng xét nghiệm (máy nhanh) mà là *bước chuyển giao thủ công và chờ bác sĩ đọc*.

Hàm ý thiết kế: giải pháp đúng nhắm vào chuyển giao (thông báo kết quả tới đúng bác sĩ đúng lúc), không phải tăng tốc máy xét nghiệm (không phải nghẽn). Nếu ai đó đề xuất "mua máy xét nghiệm nhanh hơn", bản đồ cho thấy đó là tối ưu sai chỗ. Đây là giá trị của định lượng workflow: nó chỉ ra nghẽn thật thay vì nghẽn giả định.

## 11. Sai lầm thường gặp

- **Vẽ work-as-imagined** (quy trình văn bản) thay vì thực tế.
- **Bỏ qua điểm chuyển giao** — nơi sai sót thật sự nảy sinh.
- **Tối ưu cục bộ** gây nghẽn hoặc gánh nặng chỗ khác.
- **Thêm bước** cho người dùng đã quá tải — nguyên nhân bị bỏ dùng.
- **Không định lượng** nên không ưu tiên được, hoặc tối ưu sai chỗ.
- **Loại bỏ hàng rào an toàn** vì tưởng là "bước chậm thừa".

## 12. Rủi ro an toàn, pháp lý và đạo đức

Thay đổi workflow lâm sàng có thể tạo nguy cơ mới (bỏ sót, nhầm thông tin, mất bước kiểm tra). Mọi thay đổi phải qua phân tích rủi ro (chương 24) và **giữ điểm kiểm soát an toàn**. Nguyên tắc quan trọng: không loại bỏ một bước chỉ vì nó "chậm" nếu nó là hàng rào an toàn — ví dụ bước đối chiếu định danh bệnh nhân trước thủ thuật chậm nhưng cứu mạng. Phân biệt "lãng phí" (bỏ được) với "an toàn" (giữ lại) đòi hỏi đầu vào lâm sàng. Quan sát thực địa phải bảo mật dữ liệu bệnh nhân (chương 40).

## 13. Chỉ số đo lường

Trước/sau can thiệp: thời gian chu trình (cycle time), số bước, số chuyển giao, tỉ lệ sai sót/làm lại, thời gian chờ. Thêm chỉ số **gánh nặng người dùng** (số thao tác, số lần chuyển màn hình, thời gian thêm) để tránh giải pháp làm tăng việc — một sản phẩm giảm thời gian tổng nhưng tăng số click của bác sĩ vẫn có thể bị bỏ. Ưu tiên đo lường có thể truy vết hơn cảm nhận.

## 14. Bằng chứng và mức độ tin cậy

Bản đồ workflow là **mô tả hệ thống**, độ tin cậy phụ thuộc chất lượng quan sát — một bản đồ dựa SOP thay vì quan sát là bản đồ sai. Số đo thời gian nội bộ là dữ liệu ngữ cảnh, không khái quát sang nơi khác (workflow bệnh viện A khác B). Tuyên bố "giảm X% thời gian" cần đo lường có phương pháp (đo trước-sau có kiểm soát), không suy diễn từ sơ đồ — sơ đồ cho thấy *tiềm năng* giảm, không phải *kết quả* giảm.

## 15. Tiêu chuẩn và guideline liên quan

Liên hệ nguyên tắc cải tiến chất lượng (PDSA — Plan-Do-Study-Act) và kỹ thuật yếu tố con người (human factors). Khi can thiệp là phần mềm chạm lâm sàng, gắn quản lý rủi ro ISO 14971 (chương 24) và thiết kế CDS đúng điểm (chương 38). Thay đổi quy trình đã ban hành chính thức thuộc nhóm cần phê duyệt (không tự ý đổi).

## 16. Liên hệ các chương khác

Dùng insight từ **05–06** (nhu cầu, prototype); nền cho **08** (giá trị theo từng bước quy trình), **31, 35–36** (tích hợp vào luồng dữ liệu/EHR), **38** (CDS đúng điểm quyết định), **51–52** (product/UX). Rủi ro thay đổi luồng gắn **24**.

## 17. Bài tập thực hành — Workflow map

Chọn một quy trình trong đơn vị bạn, **quan sát work-as-done** (không chỉ đọc SOP), vẽ swimlane current-state với thời gian và điểm chuyển giao, đánh dấu điểm nghẽn và điểm dễ sai, phân biệt bước "lãng phí" (bỏ được) với bước "an toàn" (giữ), định lượng ít nhất một chỉ số, rồi phác future-state cùng điểm chèn giải pháp ít gián đoạn nhất. Kiểm future-state với người làm thật — họ có thấy nó khả thi không? Ghi giả định cần xác minh.

## 18. Checklist tự đánh giá

- [ ] Bản đồ dựa trên quan sát thực, không chỉ SOP.
- [ ] Có swimlane theo tác nhân và điểm chuyển giao.
- [ ] Đã đánh dấu điểm nghẽn, lãng phí, điểm dễ sai.
- [ ] Phân biệt bước lãng phí với hàng rào an toàn.
- [ ] Có ít nhất một chỉ số định lượng.
- [ ] Điểm chèn giải pháp giảm bước, không tăng gánh nặng, không đẩy việc sang người khác.

## 19. Định nghĩa hoàn thành (Definition of Done)

Workflow map đạt chuẩn khi phản ánh work-as-done qua quan sát, thể hiện tác nhân và chuyển giao, định lượng ít nhất một chỉ số, nhận diện điểm nghẽn/điểm dễ sai, phân biệt lãng phí với an toàn, và chỉ ra điểm chèn giải pháp ít gián đoạn nhất được người làm xác nhận khả thi.

## 20. Câu hỏi phản tư

Bản đồ của tôi là quy trình thật (work-as-done) hay quy trình trên giấy? Sai sót thực sự nảy sinh ở đâu — có phải điểm chuyển giao không? Giải pháp của tôi giảm bước hay thêm bước cho người đã quá tải? Nó đẩy công việc sang ai? Tôi có đang loại bỏ một hàng rào an toàn không?

## 21. Cạm bẫy quyết định

**Ảo tưởng quy hoạch:** tin quy trình văn bản là thực tế. **Tối ưu cục bộ** vì chỉ nhìn một tác nhân. **Mù quen thuộc:** bác sĩ quen luồng đến mức không thấy bước thừa. **Nhầm an toàn với lãng phí.** Đối trọng: quan sát đa vai (gồm điều dưỡng, CNTT), định lượng, đầu vào lâm sàng để phân biệt an toàn/lãng phí, và kiểm định future-state với người làm thật.

## 22. Nguồn dữ liệu động cần xác minh

Số đo thời gian/tần suất phải từ đo thực tế tại chính cơ sở; không mượn số từ nghiên cứu bối cảnh khác. Ghi ngày đo và điều kiện (giờ cao điểm khác thấp điểm). Ước lượng chưa đo giữ là giả định; tuyên bố cải thiện cần đo trước-sau có phương pháp.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện SOP](../../resources/sop-library.md) và [Thư viện template](../../resources/template-library.md) cho mẫu workflow map. Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Swimlane:** làn theo tác nhân trong sơ đồ. **Bottleneck:** điểm nghẽn (giới hạn thông lượng). **Handoff:** chuyển giao trách nhiệm/thông tin. **PDSA:** Plan–Do–Study–Act. **Work-as-done/imagined:** quy trình thực tế/kê khai. **Cycle time:** thời gian chu trình. **Waste:** bước không tạo giá trị.

## 25. Tóm tắt và bước tiếp theo

Không thể cải thiện luồng chưa vẽ ra được, và không thể vẽ đúng nếu chỉ đọc quy trình văn bản. Giải pháp được chấp nhận là giải pháp giảm bước, chèn đúng điểm, giữ hàng rào an toàn, và không đẩy gánh nặng sang người khác. Tiếp theo sang **[chương 08 — Tuyên bố giá trị HealthTech](../08-value-proposition/README.md)** để chuyển hiểu biết quy trình thành giá trị cho từng bên.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Thay đổi workflow lâm sàng cần phân tích rủi ro và giữ hàng rào an toàn; không loại bỏ bước kiểm tra an toàn vì lý do tốc độ; quan sát thực địa phải bảo mật dữ liệu bệnh nhân; thay đổi quy trình đã ban hành cần phê duyệt.
