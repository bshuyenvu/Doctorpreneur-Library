# Viz.ai

## Tên công ty

Viz.ai là công ty công nghệ y tế ứng dụng AI trong chẩn đoán hình ảnh cấp cứu, nổi tiếng nhất với thuật toán phát hiện đột quỵ do tắc mạch máu lớn (large vessel occlusion — LVO) từ ảnh CT sọ não, giúp rút ngắn thời gian từ lúc chụp phim đến khi bác sĩ can thiệp mạch (neuro-interventionalist) nhận được cảnh báo. Công ty được thành lập khoảng năm 2016, có trụ sở tại California, Mỹ.

## Founder

Chris Mansi là bác sĩ phẫu thuật thần kinh (neurosurgeon) được đào tạo tại Anh, đồng sáng lập Viz.ai. Câu chuyện khởi nghiệp thường được kể lại là ông từng chứng kiến một bệnh nhân đột quỵ do tắc mạch lớn tử vong vì sự chậm trễ trong quy trình chẩn đoán và chuyển bệnh nhân đến bác sĩ can thiệp mạch phù hợp — mặc dù về mặt kỹ thuật, ca bệnh này có thể cứu được nếu can thiệp kịp thời. Trải nghiệm lâm sàng trực tiếp đó trở thành động lực để ông rời con đường phẫu thuật và xây dựng công cụ công nghệ nhằm giải quyết đúng "khoảng trống thời gian" (time-to-treatment gap) mà chính ông từng bất lực chứng kiến. Đây là ví dụ điển hình của doctorpreneur khởi nghiệp từ một "khoảnh khắc đau đớn lâm sàng" (clinical pain moment) cụ thể, chứ không phải từ phân tích thị trường trừu tượng.

## Vấn đề lâm sàng

Trong đột quỵ do tắc mạch máu lớn, "thời gian là não" (time is brain) — mỗi phút trì hoãn tái thông mạch máu có thể làm mất hàng triệu tế bào thần kinh. Quy trình truyền thống đòi hỏi: kỹ thuật viên chụp CT, bác sĩ chẩn đoán hình ảnh đọc phim (có thể mất nhiều giờ tùy tải công việc và thời điểm trong ngày), sau đó mới thông báo cho bác sĩ can thiệp mạch — người thường không có mặt sẵn tại bệnh viện, đặc biệt tại các cơ sở y tế không phải trung tâm đột quỵ tuyến cuối. Sự chậm trễ này là nguyên nhân chính khiến nhiều bệnh nhân có thể cứu được về mặt lý thuyết lại không được can thiệp kịp thời trong "cửa sổ vàng" điều trị.

## Giải pháp công nghệ

Viz.ai phát triển phần mềm dùng AI/thị giác máy tính phân tích ảnh CT ngay khi được chụp, tự động phát hiện dấu hiệu nghi ngờ tắc mạch máu lớn, và gửi cảnh báo trực tiếp đến điện thoại của bác sĩ can thiệp mạch — song song với, chứ không thay thế, quy trình đọc phim chính thức của bác sĩ chẩn đoán hình ảnh. Về bản chất, sản phẩm không "chẩn đoán thay bác sĩ" mà nén ngắn thời gian từ "ảnh chụp xong" đến "đúng người có chuyên môn biết tin" — một dạng can thiệp vào quy trình điều hành (workflow), không phải can thiệp vào quyết định y khoa cuối cùng. Đây là lựa chọn định vị pháp lý và lâm sàng khôn ngoan: giảm rủi ro trách nhiệm và giúp sản phẩm được các bác sĩ X-quang chấp nhận thay vì xem là mối đe dọa thay thế vai trò của họ.

## Thành tựu

Viz.ai được ghi nhận là một trong những thuật toán AI y tế đầu tiên được FDA Mỹ trao quyết định "de novo" cho phép lưu hành với chỉ định phát hiện LVO liên quan đến đột quỵ, khoảng năm 2018 — một cột mốc quan trọng cho cả ngành AI chẩn đoán hình ảnh nói chung, mở đường pháp lý cho nhiều sản phẩm AI y tế sau này đi theo con đường 510(k) dựa trên "thiết bị tương đương" (predicate). Công ty sau đó mở rộng nền tảng sang nhiều chỉ định hình ảnh khác (bao gồm cả bệnh lý tim mạch, phổi) và huy động được nhiều vòng gọi vốn lớn từ các quỹ đầu tư mạo hiểm hàng đầu trong lĩnh vực y tế, được nhiều báo cáo ngành xem là một trong những startup AI y tế có giá trị cao nhất thế giới ở giai đoạn phát triển sau này. Con số cụ thể về định giá, tổng vốn huy động hay số bệnh viện triển khai thay đổi theo thời điểm và nên được kiểm tra trên các nguồn tin tài chính công khai cập nhật thay vì trích dẫn như số liệu cố định.

## Bài học cho doctorpreneur

Thứ nhất, một sản phẩm AI y tế thành công không nhất thiết phải "chẩn đoán đúng hơn bác sĩ" — nó có thể tạo ra giá trị lâm sàng to lớn chỉ bằng cách rút ngắn thời gian luân chuyển thông tin đúng đến đúng người trong quy trình đã tồn tại. Đây là bài học quan trọng cho bác sĩ-founder: đôi khi vấn đề lớn nhất không nằm ở độ chính xác thuật toán mà ở logistics và điều phối lâm sàng. Thứ hai, việc định vị sản phẩm như công cụ "hỗ trợ workflow" thay vì "thay thế chẩn đoán" giúp giảm đáng kể rào cản pháp lý (đi theo con đường de novo/510(k) nhẹ hơn PMA) và rào cản tâm lý chấp nhận từ chính đồng nghiệp bác sĩ chẩn đoán hình ảnh — một bài học chiến lược về cách chọn phạm vi (scope) cho sản phẩm AI y tế đầu tiên. Thứ ba, câu chuyện sáng lập gắn với một ca bệnh cụ thể mà founder từng chứng kiến là tài sản truyền thông và gọi vốn mạnh mẽ — bác sĩ-founder nên trân trọng và kể lại rõ ràng "khoảnh khắc vấn đề" của chính mình, vì đó là bằng chứng thuyết phục nhất về insight lâm sàng thật, thứ mà founder không có background y khoa không thể có được.
