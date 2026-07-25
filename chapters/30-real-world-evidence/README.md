# 30 — Real-world data và real-world evidence

> **Nhánh 3 — Bằng chứng, chất lượng và nghiên cứu** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Thiết kế nghiên cứu dữ liệu thực tế đáng tin cậy.
> **Sản phẩm của chương:** RWE protocol.

---

## 1. Tóm tắt điều hành

Real-world data (RWD) là dữ liệu thu thập trong chăm sóc thường quy (EHR, đăng ký bệnh, thiết bị, yêu cầu thanh toán); real-world evidence (RWE) là bằng chứng rút ra từ phân tích RWD. RWE bổ sung mạnh cho thử nghiệm: rẻ hơn, gần thực hành hơn, và theo dõi dài hạn — nhưng dễ nhiễu và thiên lệch nếu thiết kế cẩu thả. Đầu ra là *RWE protocol*: giao thức nghiên cứu RWD có kỷ luật, nêu nguồn dữ liệu, thiết kế, kiểm soát nhiễu và hạn chế.

## 2. Mục tiêu học tập

Bạn sẽ: (a) phân biệt RWD và RWE; (b) đánh giá chất lượng và tính phù hợp của nguồn RWD; (c) áp dụng thiết kế giảm nhiễu (ví dụ điều chỉnh, matching); (d) phác RWE protocol trung thực về hạn chế.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Ở tuyến cơ sở, RWD từ hệ thống sẵn có là nguồn bằng chứng khả thi và rẻ. Dùng đúng, RWE hỗ trợ đánh giá lâm sàng, kinh tế và hậu kiểm. Dùng sai, nó tạo kết luận nhân quả giả — nguy hiểm khi ảnh hưởng quyết định lâm sàng.

## 4. Khái niệm cốt lõi và định nghĩa

**RWD:** dữ liệu chăm sóc thường quy. **RWE:** bằng chứng từ phân tích RWD. **Fit-for-purpose:** dữ liệu đủ chất lượng/phù hợp cho câu hỏi. **Confounding by indication:** nhiễu do lý do chỉ định. **Điều chỉnh nhiễu:** hồi quy, matching, propensity score. **Target trial emulation:** mô phỏng thử nghiệm giả định để giảm thiên lệch thiết kế.

## 5. Khung tư duy nền tảng

Coi RWE nghiêm như nghiên cứu: câu hỏi rõ, đánh giá dữ liệu fit-for-purpose, thiết kế giảm nhiễu (khung target trial emulation giúp tránh các thiên lệch phổ biến như immortal time bias), phân tích định trước, và phân tích độ nhạy. Nguyên tắc: RWD nhiều không bù được thiết kế yếu; minh bạch nguồn nhiễu và giới hạn nhân quả.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

RWD từ HIS/EHR tuyến cơ sở thường thiếu chuẩn hóa, thiếu biến quan trọng, và chất lượng ghi chép không đều. Đánh giá fit-for-purpose là bước bắt buộc trước khi phân tích. Sử dụng dữ liệu bệnh án cho nghiên cứu phải có cơ sở pháp lý, quản trị dữ liệu và phê duyệt đạo đức (chương 40, 26).

## 7. Các bên liên quan

Quản lý dữ liệu/CNTT, thống kê, lâm sàng, hội đồng đạo đức, và bộ phận bảo mật/pháp chế. Chất lượng RWE phụ thuộc mạnh vào hiểu biết về cách dữ liệu được sinh ra trong thực hành.

## 8. Quy trình từng bước

1. **Phát biểu câu hỏi** và giả thuyết.
2. **Đánh giá nguồn RWD** fit-for-purpose (đầy đủ, chính xác, phù hợp).
3. **Thiết kế** (ưu tiên target trial emulation khi hỏi nhân quả).
4. **Kế hoạch kiểm soát nhiễu** (điều chỉnh/matching/propensity score).
5. **Analysis plan định trước** + độ nhạy (chương 28).
6. **Viết RWE protocol** nêu rõ hạn chế và quản trị dữ liệu/đạo đức.

## 9. Công cụ và template áp dụng

- **RWE protocol:** câu hỏi · nguồn RWD · đánh giá fit-for-purpose · thiết kế · kiểm soát nhiễu · phân tích · hạn chế · đạo đức/dữ liệu.
- **Data quality assessment checklist.**
- **Bảng biến nhiễu và cách điều chỉnh.**

## 10. Ví dụ minh họa

Câu hỏi: công cụ có gắn với cải thiện kết cục trong thực hành không? Dùng RWD từ HIS. Đánh giá fit-for-purpose (có đủ biến kết cục và nhiễu không?), thiết kế theo target trial emulation, điều chỉnh nhiễu bằng propensity score, phân tích độ nhạy. Kết luận nêu rõ là bằng chứng kết hợp (association) có kiểm soát, thận trọng về nhân quả. Số liệu phải từ dữ liệu thật.

## 11. Sai lầm thường gặp

- **Tuyên bố nhân quả từ dữ liệu quan sát.**
- **Bỏ đánh giá fit-for-purpose.**
- **Bỏ qua confounding by indication.**
- **Immortal time bias** và các thiên lệch thời gian.
- **Không phân tích độ nhạy.**

## 12. Rủi ro an toàn, pháp lý và đạo đức

Dùng dữ liệu bệnh nhân cho nghiên cứu cần cơ sở pháp lý, đồng thuận/miễn trừ hợp lệ, ẩn danh phù hợp và phê duyệt đạo đức (chương 40). Không tuyên bố hiệu quả nhân quả vượt điều RWE cho phép, đặc biệt khi ảnh hưởng điều trị. Minh bạch mọi hạn chế.

## 13. Chỉ số đo lường

Chất lượng: đánh giá fit-for-purpose có hệ thống, thiết kế giảm nhiễu, phân tích định trước, và độ nhạy. Tính minh bạch về hạn chế và khả năng khái quát là chỉ số hàng đầu.

## 14. Bằng chứng và mức độ tin cậy

RWE thường cung cấp **bằng chứng kết hợp có kiểm soát**, mạnh hơn quan sát thô nhưng thường yếu hơn RCT về nhân quả. Nêu rõ mức bằng chứng, nguồn nhiễu tồn dư và giới hạn. Không nâng cấp RWE thành khẳng định nhân quả.

## 15. Tiêu chuẩn và guideline liên quan

Tuân chuẩn báo cáo nghiên cứu quan sát/RWD (ví dụ **STROBE**, và các hướng dẫn RECORD/RECORD-PE cho dữ liệu thường quy) và hướng dẫn RWE của cơ quan quản lý khi áp dụng. Gắn phương pháp (chương 28), thống kê (chương 29), data engineering (chương 54), privacy (chương 40).

## 16. Liên hệ các chương khác

Bổ sung bằng chứng cho **25–27**; dùng phương pháp **28–29**; phụ thuộc hạ tầng dữ liệu **35, 54**; quản trị dữ liệu **40**; hậu kiểm sản phẩm **50**.

## 17. Bài tập thực hành — RWE protocol

Viết RWE protocol: câu hỏi, nguồn RWD và đánh giá fit-for-purpose, thiết kế (cân nhắc target trial emulation), kế hoạch kiểm soát nhiễu, analysis plan định trước + độ nhạy, và mục quản trị dữ liệu/đạo đức. Nêu rõ giới hạn nhân quả và điều cần xác minh. Có đầu vào thống kê.

## 18. Checklist tự đánh giá

- [ ] Đánh giá fit-for-purpose nguồn RWD.
- [ ] Thiết kế giảm nhiễu (không tuyên bố nhân quả tùy tiện).
- [ ] Kiểm soát confounding by indication và thiên lệch thời gian.
- [ ] Analysis plan định trước + độ nhạy.
- [ ] Quản trị dữ liệu và phê duyệt đạo đức.

## 19. Định nghĩa hoàn thành (Definition of Done)

RWE protocol đạt chuẩn khi đánh giá dữ liệu fit-for-purpose, chọn thiết kế giảm nhiễu, kiểm soát các thiên lệch đặc thù RWD, định trước phân tích và độ nhạy, tuân quản trị dữ liệu/đạo đức, và nêu rõ giới hạn nhân quả.

## 20. Câu hỏi phản tư

Dữ liệu của tôi có fit-for-purpose cho câu hỏi không? Tôi đã kiểm soát confounding by indication chưa? Kết luận của tôi là kết hợp hay nhân quả — và tôi trình bày đúng chưa? Tôi có cơ sở pháp lý và đạo đức cho dữ liệu không?

## 21. Cạm bẫy quyết định

**Nhầm kết hợp với nhân quả**, **bỏ qua nhiễu tồn dư**, **RWD nhiều nên chủ quan**. Đối trọng: target trial emulation, phân tích độ nhạy, và diễn giải thận trọng.

## 22. Nguồn dữ liệu động cần xác minh

Hướng dẫn RWE của cơ quan quản lý, chuẩn báo cáo RWD, và chất lượng nguồn dữ liệu cụ thể — là dữ liệu động. Tra tại nguồn chính thức; đánh giá chất lượng dữ liệu thực tế, không giả định.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md). Chuẩn báo cáo và hướng dẫn RWE tra tại nguồn chính thức; trích dẫn xác minh theo EDITORIAL_POLICY.

## 24. Thuật ngữ

**RWD/RWE:** dữ liệu/bằng chứng thực tế. **Fit-for-purpose:** phù hợp mục đích. **Propensity score:** điểm xu hướng để cân bằng nhóm. **Target trial emulation:** mô phỏng thử nghiệm giả định. **Confounding by indication:** nhiễu do lý do chỉ định.

## 25. Tóm tắt và bước tiếp theo

RWE bổ sung bằng chứng gần thực hành và dài hạn, nhưng chỉ đáng tin khi thiết kế nghiêm, đánh giá dữ liệu fit-for-purpose và thận trọng về nhân quả. Đây khép nhánh bằng chứng. Tiếp theo sang **[chương 31 — Y tế số nền tảng](../31-digital-health/README.md)** để bước vào nhánh y tế số và hạ tầng dữ liệu.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. RWE thường là bằng chứng kết hợp, không nhân quả; dữ liệu bệnh nhân cần cơ sở pháp lý, quản trị dữ liệu và phê duyệt đạo đức.
