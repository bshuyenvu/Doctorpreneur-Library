# 47 — Thẩm định AI y tế

> **Nhánh 5 — AI trong y tế** · Mức ưu tiên: 🔴 Sống còn
> **Kỹ năng cần đạt:** Xây khung validation nội bộ, ngoại bộ và tiền cứu.
> **Sản phẩm của chương:** Kế hoạch thẩm định AI (AI validation plan).

---

## 1. Tóm tắt điều hành

Một mô hình AI công bố độ chính xác cao trên bài báo hoặc bản demo chưa chứng minh được gì về an toàn khi dùng thật. Thẩm định (validation) là chuỗi bằng chứng tăng dần: *nội bộ* (kiểm tra trên dữ liệu giữ lại cùng nguồn), *ngoại bộ* (kiểm tra trên dữ liệu khác nguồn/địa điểm/thời gian), và *tiền cứu* (theo dõi mô hình chạy song song trong quy trình thật trước khi để nó ảnh hưởng quyết định lâm sàng). Bỏ qua bất kỳ bước nào đều để lại rủi ro chưa được phát hiện. Đầu ra là *kế hoạch thẩm định AI*: tài liệu xác định mô hình sẽ được kiểm chứng ở từng mức nào, với dữ liệu gì, ngưỡng chấp nhận gì, trước khi được tin dùng.

## 2. Mục tiêu học tập

Bạn sẽ: (a) phân biệt validation nội bộ, ngoại bộ và tiền cứu; (b) hiểu vì sao mỗi mức không thể thay thế mức khác; (c) thiết kế thử nghiệm âm thầm (silent trial) trước triển khai; (d) lập kế hoạch thẩm định AI tương xứng mức rủi ro.

## 3. Vì sao chương này sống còn với Doctorpreneur

Rất nhiều sản phẩm AI y tế thất bại không phải vì mô hình kém mà vì triển khai sau khi chỉ mới qua validation nội bộ — hiệu năng sụp đổ khi gặp dữ liệu thật. Hiểu đúng chuỗi bằng chứng này giúp bạn tránh triển khai non, tránh mất niềm tin của bác sĩ và bệnh viện, và đáp ứng được yêu cầu ngày càng chặt của cơ quan quản lý và nhà đầu tư.

## 4. Khái niệm cốt lõi và định nghĩa

**Validation nội bộ:** kiểm tra trên dữ liệu giữ lại (hold-out) hoặc cross-validation cùng nguồn huấn luyện. **Validation ngoại bộ:** kiểm tra trên dữ liệu khác nguồn, địa điểm hoặc thời gian thu thập. **Validation tiền cứu (prospective):** chạy mô hình thời gian thực trong quy trình thật, thường ở chế độ "âm thầm" (silent/shadow) trước khi ảnh hưởng quyết định. **Hiệu chỉnh (calibration):** mức khớp giữa xác suất mô hình dự báo và tần suất thực tế. **Khả năng tổng quát (generalizability):** mức mô hình giữ được hiệu năng ở bối cảnh mới.

## 5. Khung tư duy nền tảng

Coi validation là chuỗi bằng chứng, không phải một bước duy nhất: nội bộ chỉ chứng minh mô hình học được mẫu hình trong chính dữ liệu đó — chưa nói gì về nơi khác; ngoại bộ chứng minh mức tổng quát hóa sang bối cảnh mới; tiền cứu chứng minh mô hình hoạt động đúng trong quy trình thật, thời gian thực, trước khi được phép ảnh hưởng quyết định lâm sàng. Mức bằng chứng cần đạt phải tương xứng mức rủi ro: một công cụ hỗ trợ tham khảo cần ít bằng chứng hơn một công cụ ảnh hưởng trực tiếp quyết định điều trị. Nguyên tắc: không để mô hình ảnh hưởng quyết định lâm sàng thật cho tới khi đã qua đủ các mức tương xứng rủi ro của nó.

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Việt Nam thiếu dữ liệu đa trung tâm công khai và hợp tác liên viện cho validation ngoại bộ còn hạn chế — đây là điểm nghẽn thực tế cần lên kế hoạch sớm (tìm đối tác bệnh viện thứ hai, thỏa thuận chia sẻ dữ liệu). Với các mô hình AI "nhập khẩu" huấn luyện trên dữ liệu nước ngoài, validation ngoại bộ trên dân số và thiết bị Việt Nam là bắt buộc trước khi tin dùng, vì khác biệt dịch tễ, thiết bị và quy trình chụp/khám có thể làm hiệu năng thay đổi đáng kể.

## 7. Các bên liên quan

Nhóm nghiên cứu/thống kê y sinh (chương 28–29) thiết kế thử nghiệm, bác sĩ đối tác ở địa điểm ngoại bộ, khoa học dữ liệu, và cơ quan quản lý khi sản phẩm là thiết bị y tế. Validation ngoại bộ và tiền cứu đòi hỏi hợp tác thực sự với ít nhất một địa điểm độc lập, không thể tự làm một mình.

## 8. Quy trình từng bước

1. **Validation nội bộ:** hold-out hoặc cross-validation, đo hiệu năng và calibration.
2. **Validation ngoại bộ:** kiểm tra trên dữ liệu khác nguồn/địa điểm/thời gian, so sánh độ lệch hiệu năng.
3. **Thiết kế thử nghiệm tiền cứu (silent trial):** chạy song song trong quy trình thật, chưa ảnh hưởng quyết định.
4. **Xác định ngưỡng chấp nhận** theo mức rủi ro lâm sàng của use case.
5. **Ghi nhận giới hạn và phạm vi áp dụng** (generalizability) rõ ràng.
6. **Lập kế hoạch thẩm định AI** đầy đủ ba mức và tiêu chí go/no-go.

## 9. Công cụ và template áp dụng

- **Kế hoạch thẩm định AI:** mức validation · nguồn dữ liệu · thước đo · ngưỡng chấp nhận · giới hạn phạm vi.
- **Giao thức thử nghiệm âm thầm (silent trial protocol).**
- **Biểu đồ hiệu chỉnh (calibration plot)** và bảng so sánh nội bộ–ngoại bộ.

## 10. Ví dụ minh họa

Mô hình dự báo nguy cơ trở nặng. Validation nội bộ tại bệnh viện A cho AUC tốt và calibration khớp. Validation ngoại bộ tại bệnh viện B cho thấy AUC giảm và calibration lệch — cần hiệu chỉnh lại ngưỡng hoặc bổ sung dữ liệu huấn luyện đa dạng hơn. Trước khi dùng ảnh hưởng quyết định thật, mô hình chạy tiền cứu âm thầm ba tháng tại bệnh viện B, so sánh dự báo với kết cục thực tế, chỉ được "bật" ảnh hưởng quyết định sau khi đạt ngưỡng đã định trước.

## 11. Sai lầm thường gặp

- **Dừng lại ở validation nội bộ** rồi công bố sẵn sàng triển khai.
- **Suy rộng hiệu năng từ nghiên cứu/quốc gia khác** sang bối cảnh của mình mà không kiểm tra lại.
- **Bỏ qua calibration**, chỉ nhìn AUC.
- **Rút ngắn hoặc bỏ qua thử nghiệm tiền cứu** vì áp lực thời gian ra mắt.
- **Không định nghĩa ngưỡng chấp nhận trước** khi xem kết quả (dễ tự biện minh sau).

## 12. Rủi ro an toàn, pháp lý và đạo đức

Triển khai thiếu validation ngoại bộ và tiền cứu có thể gây hại lâm sàng thầm lặng — mô hình sai nhưng không ai phát hiện kịp thời. Nhiều khung pháp lý về thiết bị y tế (chương 19–22) yêu cầu bằng chứng đánh giá lâm sàng (chương 25) trước khi lưu hành sản phẩm AI có ảnh hưởng chẩn đoán/điều trị. Thiếu validation phù hợp cũng là rủi ro trách nhiệm pháp lý trực tiếp cho founder.

## 13. Chỉ số đo lường

Hiệu năng và calibration ở từng mức (nội bộ/ngoại bộ/tiền cứu), độ lệch hiệu năng giữa nội bộ và ngoại bộ, và kết quả thử nghiệm âm thầm so với ngưỡng đã định trước khi bắt đầu. Độ lệch lớn giữa các mức là tín hiệu cần điều tra trước khi tiếp tục.

## 14. Bằng chứng và mức độ tin cậy

Số liệu hiệu năng công bố trên bài báo hoặc tài liệu của nhà cung cấp **không thay thế** validation nội bộ, ngoại bộ và tiền cứu tại chính bối cảnh triển khai của bạn. Luôn yêu cầu dữ liệu chi tiết theo phân nhóm và theo mức validation, không chỉ một chỉ số tổng đã được chọn lọc.

## 15. Tiêu chuẩn và guideline liên quan

Gắn đánh giá lâm sàng (chương 25), phương pháp nghiên cứu và thống kê y sinh (chương 28–29), real-world evidence (chương 30), quản lý rủi ro (chương 24), quy định thiết bị y tế (chương 19–22), và tái validation trong MLOps (chương 50).

## 16. Liên hệ các chương khác

Nền tảng bằng chứng cho toàn nhánh AI ứng dụng lâm sàng **41–46, 48–50**; gắn nghiên cứu **25, 28–30**; rủi ro **24**; quy định **19–22**.

## 17. Bài tập thực hành — Kế hoạch thẩm định AI

Lập kế hoạch thẩm định AI cho một use case: thiết kế validation nội bộ (dữ liệu, thước đo), validation ngoại bộ (tìm nguồn dữ liệu/đối tác khác), thiết kế thử nghiệm tiền cứu âm thầm với ngưỡng go/no-go định trước, và nêu rõ giới hạn phạm vi áp dụng dự kiến. Ghi rõ mức rủi ro lâm sàng và mức bằng chứng cần tương xứng.

## 18. Checklist tự đánh giá

- [ ] Có kế hoạch cho cả ba mức: nội bộ, ngoại bộ, tiền cứu.
- [ ] Đã xác định nguồn dữ liệu ngoại bộ độc lập thực sự.
- [ ] Calibration được đánh giá, không chỉ AUC/độ chính xác.
- [ ] Ngưỡng chấp nhận được định trước khi xem kết quả.
- [ ] Chưa để mô hình ảnh hưởng quyết định thật trước khi đạt đủ mức bằng chứng.

## 19. Định nghĩa hoàn thành (Definition of Done)

Kế hoạch thẩm định AI đạt chuẩn khi có đủ ba mức validation với nguồn dữ liệu và ngưỡng rõ ràng, đánh giá calibration, thiết kế thử nghiệm tiền cứu trước khi ảnh hưởng quyết định thật, và mức bằng chứng tương xứng rủi ro lâm sàng của use case.

## 20. Câu hỏi phản tư

Tôi đã có validation ngoại bộ thực sự chưa, hay chỉ dừng ở nội bộ? Tôi có đối tác dữ liệu độc lập cho kiểm tra ngoại bộ không? Mô hình đã được thử nghiệm tiền cứu âm thầm trước khi ảnh hưởng quyết định thật chưa? Ngưỡng chấp nhận của tôi có được định trước khi xem kết quả không?

## 21. Cạm bẫy quyết định

**Dừng ở validation nội bộ**, **tin benchmark ngoại nhập chưa kiểm chứng**, **bỏ qua thử nghiệm tiền cứu vì áp lực ra mắt**. Đối trọng: chuỗi bằng chứng đầy đủ, đối tác dữ liệu độc lập, và ngưỡng go/no-go định trước.

## 22. Nguồn dữ liệu động cần xác minh

Yêu cầu validation theo quy định thiết bị y tế/AI hiện hành, và tính sẵn có đối tác dữ liệu ngoại bộ tại Việt Nam — là dữ liệu động, thay đổi theo thời gian. Tra văn bản chính thức và xác nhận thực tế; ghi ngày kiểm tra.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện bài báo](../../resources/paper-library.md) và [Thư viện SOP](../../resources/sop-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Internal/external/prospective validation:** validation nội bộ/ngoại bộ/tiền cứu. **Calibration:** hiệu chỉnh xác suất. **Silent trial:** thử nghiệm âm thầm. **Generalizability:** khả năng tổng quát hóa.

## 25. Tóm tắt và bước tiếp theo

AI y tế chỉ đáng tin khi đã qua đủ chuỗi bằng chứng — nội bộ, ngoại bộ và tiền cứu — tương xứng mức rủi ro lâm sàng; hiệu năng công bố không bao giờ là đủ một mình. Tiếp theo sang **[chương 48 — AI có trách nhiệm](../48-responsible-ai/README.md)** để xây khung quản trị công bằng, minh bạch và trách nhiệm giải trình.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục, không thay tư vấn thống kê y sinh hoặc pháp lý thiết bị y tế chuyên môn. Không để mô hình AI ảnh hưởng quyết định lâm sàng thật trước khi hoàn tất validation tương xứng mức rủi ro; yêu cầu validation là dữ liệu động — tra quy định hiện hành.
