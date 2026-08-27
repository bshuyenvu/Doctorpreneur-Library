# 04. Khám phá vấn đề lâm sàng

Chương này hướng dẫn bác sĩ phương pháp có hệ thống để nhận diện, xác thực và ưu tiên hóa các vấn đề lâm sàng/vận hành thực sự đáng để xây dựng sản phẩm giải quyết — trước khi bắt tay vào bất kỳ giải pháp cụ thể nào.

## 1. Giới thiệu

Một trong những sai lầm phổ biến nhất của các nhà sáng lập kỹ thuật lẫn bác sĩ khởi nghiệp là bắt đầu từ giải pháp (solution-first) thay vì từ vấn đề (problem-first). Nhiều dự án HealthTech thất bại không phải vì công nghệ kém mà vì giải quyết một vấn đề không đủ "đau" (painful), không đủ thường xuyên (frequent), hoặc không có người sẵn sàng trả tiền để giải quyết nó. Các khảo sát ngành khởi nghiệp công khai (ví dụ báo cáo "Top reasons startups fail" của CB Insights) thường liệt kê "không có nhu cầu thị trường" là nguyên nhân thất bại phổ biến hàng đầu — đây là số liệu mang tính tổng hợp, cần người đọc tự tra cứu nguồn gốc và số liệu cập nhật, không nên xem là con số tuyệt đối áp dụng cho mọi trường hợp.

Khám phá vấn đề (Problem Discovery) là giai đoạn đầu tiên và quan trọng nhất trong hành trình xây dựng sản phẩm, diễn ra trước cả giai đoạn khám phá khách hàng (Customer Discovery, sẽ được trình bày ở chương 05). Mục tiêu của giai đoạn này là trả lời câu hỏi: "Vấn đề gì đang thực sự tồn tại, ai đang chịu ảnh hưởng, mức độ nghiêm trọng ra sao, và tại sao các giải pháp hiện tại chưa giải quyết triệt để?" — trước khi hỏi "Sản phẩm của tôi nên như thế nào?".

Bác sĩ có một lợi thế hiếm có trong giai đoạn này: họ tiếp xúc trực tiếp và liên tục với vô số điểm nghẽn, sai sót quy trình, và khoảng trống công nghệ trong thực hành lâm sàng hàng ngày — nguồn "vấn đề thô" mà hầu hết founder công nghệ thuần túy không có cơ hội quan sát. Tuy nhiên, chính vì quá quen thuộc với những vấn đề này, bác sĩ cũng dễ mắc phải "lời nguyền của kiến thức" (curse of knowledge) — cho rằng vấn đề hiển nhiên đến mức không cần kiểm chứng lại, hoặc đánh giá sai mức độ nghiêm trọng vì đã quen chịu đựng nó. Chương này cung cấp khung tư duy và công cụ để biến quan sát cá nhân thành bằng chứng có hệ thống.

## 2. Tại sao bác sĩ cần học

1. **Chuyển hóa lợi thế quan sát lâm sàng thành tài sản khởi nghiệp có cấu trúc.** Nếu không có phương pháp, hàng trăm quan sát giá trị trong sự nghiệp y khoa sẽ trôi qua mà không bao giờ trở thành cơ hội kinh doanh cụ thể.

2. **Tránh xây dựng giải pháp cho vấn đề không đủ nghiêm trọng hoặc không đủ phổ biến.** Một vấn đề "khó chịu nhẹ" khác hoàn toàn với một vấn đề "gây thiệt hại nghiêm trọng, xảy ra thường xuyên, và người dùng sẵn sàng trả tiền để giải quyết" — phân biệt được hai loại này quyết định sự sống còn của dự án.

3. **Giảm thiên kiến cá nhân (personal bias) trong nhận diện vấn đề.** Bác sĩ có thể nhầm lẫn giữa vấn đề của riêng chuyên khoa/cơ sở mình với vấn đề mang tính hệ thống rộng hơn; phương pháp khám phá vấn đề có hệ thống giúp kiểm chứng tính phổ quát.

4. **Tạo nền tảng thuyết phục cho nhà đầu tư và đối tác.** Nhà đầu tư nghiêm túc luôn hỏi "Bằng chứng nào cho thấy đây là vấn đề đáng giải quyết?" — khả năng trả lời bằng dữ liệu thực chứng minh năng lực nghiên cứu thị trường của founder.

## 3. Kiến thức nền

- **Problem Space vs. Solution Space**: Phân biệt "không gian vấn đề" (hiểu bản chất, nguyên nhân, tác động của vấn đề) với "không gian giải pháp" (thiết kế cách giải quyết) — kỷ luật ở lại không gian vấn đề đủ lâu trước khi nhảy sang giải pháp là kỹ năng cốt lõi.
- **Jobs to be Done (JTBD)**: Khung lý thuyết của Clayton Christensen coi khách hàng "thuê" một sản phẩm/dịch vụ để hoàn thành một "công việc" cụ thể trong cuộc sống/công việc của họ; giúp nhìn vấn đề từ góc độ động cơ sâu xa thay vì tính năng bề mặt.
- **Pain Point Severity Matrix**: Công cụ đánh giá vấn đề theo hai trục — tần suất xảy ra và mức độ nghiêm trọng/thiệt hại — giúp ưu tiên hóa vấn đề nào đáng theo đuổi.
- **Root Cause Analysis (Phân tích nguyên nhân gốc rễ)**: Kỹ thuật như "5 Whys" hoặc sơ đồ xương cá (Fishbone/Ishikawa) giúp đào sâu từ triệu chứng bề mặt đến nguyên nhân thực sự của vấn đề, tránh xây giải pháp cho triệu chứng.
- **Confirmation Bias & Curse of Knowledge**: Hai thiên kiến nhận thức đặc biệt nguy hiểm với bác sĩ khi khám phá vấn đề — xu hướng tìm kiếm thông tin xác nhận niềm tin sẵn có, và xu hướng cho rằng điều mình biết rõ cũng hiển nhiên với người khác.
- **Problem Validation vs. Problem Assumption**: Phân biệt giả định về vấn đề (chưa kiểm chứng) với vấn đề đã được xác thực bằng bằng chứng thực tế (phỏng vấn, quan sát, dữ liệu).
- **Stakeholder Mapping trong bối cảnh lâm sàng**: Một vấn đề lâm sàng thường liên quan đến nhiều bên (bệnh nhân, bác sĩ, điều dưỡng, quản lý bệnh viện, cơ quan bảo hiểm) — vấn đề có thể "đau" với bên này nhưng không đau với bên có quyền quyết định mua hàng, cần lập bản đồ rõ ràng.
- **Willingness to Pay (Sẵn sàng chi trả)**: Không phải mọi vấn đề đau đều có người sẵn sàng trả tiền để giải quyết — cần phân biệt "vấn đề thú vị về mặt lâm sàng" với "vấn đề có giá trị thương mại".

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Nhảy thẳng vào giải pháp trước khi hiểu rõ vấn đề | Xây sản phẩm không ai cần, lãng phí thời gian và vốn | Dành tối thiểu 2-4 tuần chỉ tập trung khám phá vấn đề, cấm bản thân nghĩ về giải pháp |
| Chỉ dựa vào quan sát cá nhân, không kiểm chứng với người khác | Vấn đề có thể chỉ đặc thù cho một cơ sở/chuyên khoa, không phổ quát | Phỏng vấn tối thiểu 10-15 người ở nhiều bối cảnh khác nhau |
| Nhầm lẫn "vấn đề của tôi" với "vấn đề của thị trường" | Sản phẩm chỉ phù hợp với nhu cầu cá nhân, khó mở rộng quy mô | Kiểm chứng tần suất và mức độ phổ biến của vấn đề trên nhiều đối tượng |
| Đặt câu hỏi dẫn dắt khi phỏng vấn ("Bạn có thấy X là vấn đề không?") | Nhận được câu trả lời "lịch sự nhưng vô ích", dữ liệu sai lệch | Áp dụng kỹ thuật "The Mom Test" — hỏi về hành vi quá khứ cụ thể thay vì ý kiến |
| Bỏ qua vấn đề vì "ai cũng biết rồi, chẳng ai giải quyết được" | Bỏ lỡ cơ hội lớn — nhiều vấn đề "ai cũng biết" chưa được giải quyết vì thiếu công nghệ/mô hình kinh doanh phù hợp trước đây | Đánh giá lại tại sao chưa ai giải quyết — thiếu công nghệ, thiếu động lực kinh tế, hay thiếu người hiểu đúng vấn đề |
| Không phân biệt người bị ảnh hưởng bởi vấn đề và người ra quyết định mua hàng | Xây sản phẩm hay nhưng không bán được vì người trả tiền không "đau" | Lập bản đồ các bên liên quan, xác định rõ ai chịu ảnh hưởng và ai kiểm soát ngân sách |
| Dừng khám phá vấn đề quá sớm vì nôn nóng xây sản phẩm | Bỏ lỡ các insight quan trọng, dẫn đến giả thuyết giá trị yếu | Đặt tiêu chí rõ ràng cho "đủ bằng chứng" trước khi chuyển sang giai đoạn thiết kế giải pháp |
| Chỉ tin vào dữ liệu định lượng hoặc chỉ tin vào cảm nhận định tính | Bức tranh phiến diện về vấn đề, bỏ lỡ chiều sâu hoặc quy mô | Kết hợp cả phỏng vấn định tính và dữ liệu định lượng khi có thể |

## 5. Roadmap học (6 tuần)

- **Tuần 1**: Học các khung lý thuyết Jobs to be Done, Root Cause Analysis; bắt đầu nhật ký ghi chép vấn đề quan sát hàng ngày tại nơi làm việc.
- **Tuần 2**: Áp dụng Pain Point Severity Matrix để đánh giá và xếp hạng 10-15 vấn đề đã ghi nhận theo tần suất và mức độ nghiêm trọng.
- **Tuần 3**: Học kỹ thuật phỏng vấn không dẫn dắt (The Mom Test); thiết kế bộ câu hỏi phỏng vấn cho 3 vấn đề ưu tiên hàng đầu.
- **Tuần 4**: Thực hiện 10-15 buổi phỏng vấn với đồng nghiệp, điều dưỡng, bệnh nhân ở các bối cảnh khác nhau (nếu có thể, đa dạng cơ sở y tế).
- **Tuần 5**: Phân tích dữ liệu phỏng vấn, lập bản đồ các bên liên quan (stakeholder mapping) cho vấn đề được chọn lọc lại còn 1-2 vấn đề ưu tiên.
- **Tuần 6**: Viết "problem statement" (tuyên bố vấn đề) hoàn chỉnh, có bằng chứng hỗ trợ, chuẩn bị chuyển sang giai đoạn Customer Discovery (chương 05).

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| The Mom Test | Rob Fitzpatrick | 2013 | Cơ bản | Kỹ thuật phỏng vấn để tránh câu trả lời sai lệch do lịch sự | Mọi Doctorpreneur trước khi phỏng vấn ai |
| Competing Against Luck (Jobs to be Done) | Clayton Christensen và cộng sự | 2016 | Trung cấp | Giới thiệu khung lý thuyết Jobs to be Done toàn diện | Người muốn hiểu động cơ sâu xa của khách hàng |
| Sprint | Jake Knapp | 2016 | Cơ bản | Quy trình 5 ngày để xác định và kiểm chứng vấn đề/giải pháp | Người cần công cụ khám phá nhanh |
| Continuous Discovery Habits | Teresa Torres | 2021 | Trung cấp | Xây dựng thói quen khám phá vấn đề liên tục, không phải một lần | Product owner/founder muốn duy trì nhịp khám phá |
| Just Enough Research | Erika Hall | 2013 | Cơ bản | Hướng dẫn thực hành nghiên cứu người dùng gọn nhẹ, hiệu quả | Người mới bắt đầu nghiên cứu người dùng |
| Talking to Humans | Giff Constable | 2014 | Cơ bản | Cẩm nang ngắn gọn về phỏng vấn khách hàng thực chiến | Người cần checklist thực hành nhanh |
| The Innovator's Prescription | Clayton Christensen, Jerome Grossman, Jason Hwang | 2008 | Trung cấp | Ứng dụng lý thuyết đổi mới đột phá để nhận diện vấn đề hệ thống y tế | Bác sĩ quan tâm chiến lược hệ thống |
| Thinking, Fast and Slow | Daniel Kahneman | 2011 | Nâng cao | Nền tảng khoa học về thiên kiến nhận thức ảnh hưởng đến nhận diện vấn đề | Người muốn hiểu sâu về bias trong ra quyết định |
| Design Thinking for Health | Bon Ku, Ellen Lupton | 2020 | Trung cấp | Áp dụng tư duy thiết kế để khám phá vấn đề trong bối cảnh y tế | Bác sĩ quan tâm thiết kế trải nghiệm chăm sóc |
| Range | David Epstein | 2019 | Trung cấp | Vai trò của tư duy đa lĩnh vực trong việc nhận diện vấn đề mới | Người muốn mở rộng góc nhìn liên ngành |

## 7. Top bài báo/nghiên cứu

| Tiêu đề (chủ đề) | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Phương pháp nhận diện vấn đề trong cải tiến chất lượng lâm sàng (Quality Improvement) | Tra cứu trên PubMed theo từ khóa: "root cause analysis quality improvement healthcare" | Đa dạng | Khung phương pháp luận nhận diện nguyên nhân gốc rễ vấn đề lâm sàng |
| Jobs to be Done trong thiết kế dịch vụ y tế | Tra cứu trên Google Scholar theo từ khóa: "jobs to be done healthcare service design" | Đa dạng | Ứng dụng JTBD cụ thể cho bối cảnh y tế |
| Sai sót quy trình và điểm nghẽn (bottleneck) trong bệnh viện | Tra cứu trên PubMed theo từ khóa: "hospital workflow bottleneck patient safety" | Đa dạng | Nguồn dữ liệu về vấn đề vận hành phổ biến trong bệnh viện |
| Thiên kiến nhận thức của chuyên gia khi đánh giá vấn đề trong lĩnh vực của mình | Tra cứu trên Google Scholar theo từ khóa: "curse of knowledge expert bias problem framing" | Đa dạng | Hiểu rủi ro thiên kiến khi bác sĩ tự đánh giá vấn đề |
| Phương pháp nghiên cứu định tính trong thiết kế can thiệp y tế số | Tra cứu trên PubMed theo từ khóa: "qualitative research digital health intervention design" | Đa dạng | Kỹ thuật thu thập dữ liệu định tính có hệ thống |
| Gánh nặng hành chính (administrative burden) đối với bác sĩ | Tra cứu trên PubMed theo từ khóa: "physician administrative burden burnout EHR" | Đa dạng | Nguồn vấn đề lớn thường gặp trong thực hành lâm sàng hiện đại |
| Khoảng trống công nghệ trong chăm sóc chuyển tiếp (care transitions) | Tra cứu trên PubMed theo từ khóa: "care transitions technology gap hospital discharge" | Đa dạng | Ví dụ điển hình về vấn đề hệ thống có giá trị thương mại tiềm năng |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Human-Centered Design Toolkit | IDEO.org | Cập nhật định kỳ | Bộ công cụ thiết kế lấy con người làm trung tâm, áp dụng được cho khám phá vấn đề y tế |
| Quality Improvement Essentials Toolkit | Institute for Healthcare Improvement (IHI) | Cập nhật định kỳ | Công cụ phân tích nguyên nhân gốc rễ và cải tiến quy trình lâm sàng |
| Digital Health Trends Report | IQVIA Institute | Cập nhật hàng năm | Bối cảnh các vấn đề y tế đang được công nghệ giải quyết trên toàn cầu |
| State of Digital Health | McKinsey Health Institute | Cập nhật định kỳ | Phân tích các "điểm đau" lớn của hệ thống y tế từ góc nhìn chiến lược |
| Chiến lược chuyển đổi số y tế Việt Nam | Bộ Y tế Việt Nam | Theo giai đoạn ban hành | Xác định các vấn đề ưu tiên quốc gia liên quan chuyển đổi số y tế |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| IDEO.org | Tài nguyên về thiết kế lấy con người làm trung tâm | Miễn phí phần lớn công cụ |
| IHI.org (Institute for Healthcare Improvement) | Công cụ và tài liệu cải tiến chất lượng y tế | Một số tài nguyên miễn phí, có khóa học trả phí |
| Rock Health | Báo cáo, phân tích về các vấn đề digital health | Một phần miễn phí |
| MedCity News | Tin tức về các vấn đề và giải pháp HealthTech | Miễn phí |
| Continuous Discovery Habits (blog Teresa Torres) | Bài viết về thực hành khám phá liên tục | Miễn phí phần lớn |
| STAT News | Tin chuyên sâu về các vấn đề y tế, chính sách | Có nội dung miễn phí và trả phí |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| Lenny's Newsletter | Lenny Rachitsky | Product discovery, nghiên cứu người dùng |
| Rock Health Weekly | Rock Health | Vấn đề và xu hướng digital health |
| Nikhil Krishnan's Out-of-Pocket | Nikhil Krishnan | Phân tích sâu các vấn đề hệ thống y tế Mỹ |
| Product Talk (Teresa Torres) | Teresa Torres | Continuous discovery, nghiên cứu người dùng liên tục |
| The Medical Futurist | Bertalan Meskó | Vấn đề và xu hướng công nghệ y tế tương lai |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| Product Thinking Podcast | Melissa Perri | Apple Podcasts, Spotify |
| The Digital Health Podcast | Dr. Roxie Mooney | Apple Podcasts, Spotify |
| Continuous Discovery Habits Podcast/Talks | Teresa Torres | Apple Podcasts |
| a16z Podcast (mảng Bio/Health) | Andreessen Horowitz | Spotify, YouTube |
| 4x4 Health | Care Excellence Network | Apple Podcasts |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| IDEO U | Video về tư duy thiết kế và khám phá vấn đề |
| Teresa Torres (Product Talk) | Video hướng dẫn continuous discovery |
| Y Combinator | Bài giảng về xác định vấn đề trước khi xây sản phẩm |
| TEDMED | Các bài nói chuyện về vấn đề lớn trong y tế toàn cầu |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí (ước tính) |
|---|---|---|---|
| Human-Centered Design course | IDEO U / Coursera | 4-6 tuần | Trả phí, có bản audit miễn phí ở một số nơi |
| Quality Improvement in Healthcare | IHI Open School | Vài giờ đến vài tuần | Miễn phí cho một số module, phần khác trả phí |
| Customer Discovery for Founders | Y Combinator Startup School | ~10 tuần | Miễn phí |
| Qualitative Research Methods | Coursera/edX (các đại học đối tác) | 4-6 tuần | Trả phí, có audit miễn phí |
| Design Thinking for Innovation | Coursera (Đại học Virginia) | 4 tuần | Trả phí, có audit miễn phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| awesome-design-thinking | Tổng hợp tài nguyên về tư duy thiết kế | Tìm trên GitHub theo từ khóa tương ứng |
| interview-question-templates (nhiều repo) | Mẫu câu hỏi phỏng vấn khách hàng | Tìm theo từ khóa "customer interview template" |
| root-cause-analysis-tools | Công cụ hỗ trợ phân tích nguyên nhân gốc rễ | Tìm theo từ khóa tương ứng trên GitHub |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Claude/ChatGPT | Trợ lý AI tổng quát | Phân tích ghi chú phỏng vấn, tìm mẫu hình (pattern) trong dữ liệu định tính |
| Otter.ai | Ghi âm và chuyển văn bản | Ghi lại chính xác các buổi phỏng vấn khám phá vấn đề |
| Dovetail | Nền tảng phân tích nghiên cứu người dùng có AI hỗ trợ | Mã hóa (coding) và tổng hợp insight từ nhiều phỏng vấn |
| Miro/FigJam AI | Công cụ vẽ sơ đồ tư duy, bản đồ hành trình có AI hỗ trợ | Trực quan hóa bản đồ vấn đề và các bên liên quan |
| Perplexity AI | Tìm kiếm có trích dẫn nguồn | Tra cứu nhanh dữ liệu, nghiên cứu liên quan đến vấn đề |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| Taguette | GPLv3 | Công cụ mã nguồn mở hỗ trợ mã hóa (coding) dữ liệu định tính |
| REDCap (miễn phí cho học thuật/phi lợi nhuận) | Giấy phép riêng, miễn phí trong một số điều kiện | Thu thập dữ liệu khảo sát/nghiên cứu vấn đề lâm sàng |
| n8n | Fair-code license | Tự động hóa quy trình thu thập/tổng hợp dữ liệu khám phá vấn đề |
| Kobo Toolbox | Mã nguồn mở | Thu thập dữ liệu khảo sát thực địa, phù hợp môi trường nguồn lực hạn chế |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| IHI Open School Community | Cộng đồng học viên cải tiến chất lượng y tế toàn cầu |
| Product Talk Community (Teresa Torres) | Cộng đồng thực hành continuous discovery |
| Mind the Product | Cộng đồng product management toàn cầu, có nội dung về discovery |
| StartUp Health | Cộng đồng HealthTech founder |
| Health 2.0 | Cộng đồng đổi mới sáng tạo y tế |

## 18. Case study nổi bật

**1. Cerner/Epic và "alert fatigue"** — Nhiều nghiên cứu và phản ánh thực tế trong ngành ghi nhận hiện tượng bác sĩ bị quá tải bởi cảnh báo (alert) từ hồ sơ bệnh án điện tử, dẫn đến việc bỏ qua cả cảnh báo quan trọng. Đây là ví dụ điển hình về vấn đề bị "ẩn" sau một giải pháp công nghệ được cho là đã giải quyết vấn đề (số hóa hồ sơ bệnh án) nhưng thực chất tạo ra vấn đề mới. Bài học: khám phá vấn đề không dừng lại sau khi triển khai một giải pháp — cần tiếp tục quan sát tác dụng phụ và vấn đề phát sinh.

**2. PatientPing** — Người sáng lập nhận diện một vấn đề rất cụ thể: bác sĩ chăm sóc chính không biết khi nào bệnh nhân của mình nhập viện tại một cơ sở khác, dẫn đến gián đoạn chăm sóc. Vấn đề này được xác thực qua quan sát thực tế và phỏng vấn nhiều bác sĩ trước khi xây dựng giải pháp. Bài học: vấn đề càng cụ thể, càng dễ đo lường mức độ nghiêm trọng và tần suất, càng dễ thuyết phục người mua.

**3. Nurx (chăm sóc sức khỏe sinh sản từ xa)** — Bắt đầu từ quan sát vấn đề tiếp cận (access) — nhiều phụ nữ gặp rào cản về thời gian, chi phí, hoặc sự thoải mái khi tiếp cận dịch vụ tránh thai truyền thống. Đội ngũ sáng lập xác thực vấn đề này qua nghiên cứu hành vi người dùng trước khi xây dựng nền tảng telehealth. Bài học: vấn đề tiếp cận (access) trong y tế thường ẩn chứa cơ hội lớn vì ảnh hưởng đến số đông người dùng.

## 19. Checklist thực hành

- [ ] Ghi chép tối thiểu 20 vấn đề lâm sàng/vận hành quan sát được trong 4 tuần
- [ ] Áp dụng Pain Point Severity Matrix để xếp hạng các vấn đề theo tần suất và mức độ nghiêm trọng
- [ ] Thực hiện Root Cause Analysis (5 Whys hoặc Fishbone) cho ít nhất 3 vấn đề ưu tiên
- [ ] Viết bộ câu hỏi phỏng vấn không dẫn dắt theo nguyên tắc The Mom Test
- [ ] Phỏng vấn tối thiểu 10-15 người liên quan (đa dạng vai trò: bác sĩ, điều dưỡng, bệnh nhân, quản lý)
- [ ] Lập bản đồ các bên liên quan (stakeholder map) cho vấn đề được chọn
- [ ] Xác định rõ ai chịu ảnh hưởng và ai có quyền quyết định ngân sách/mua hàng
- [ ] Đánh giá "willingness to pay" sơ bộ qua phỏng vấn hoặc khảo sát
- [ ] Viết problem statement (tuyên bố vấn đề) có bằng chứng hỗ trợ rõ ràng
- [ ] Kiểm tra chéo với ít nhất 2-3 nguồn dữ liệu khác nhau (phỏng vấn, quan sát, dữ liệu thứ cấp)
- [ ] Loại bỏ ít nhất 50% danh sách vấn đề ban đầu qua quá trình xác thực
- [ ] Chia sẻ problem statement với mentor hoặc đồng nghiệp để nhận phản biện khách quan

## 20. Project thực hành

1. **Dự án "Nhật ký 20 vấn đề"** — Trong 3-4 tuần, ghi chép có hệ thống mọi vấn đề vận hành/lâm sàng bạn quan sát, phân loại theo khoa/quy trình. Công cụ: Notion hoặc bảng tính. KPI: 20 vấn đề được ghi nhận, mỗi vấn đề có ít nhất 1 dòng mô tả tần suất và tác động.

2. **Dự án "10 phỏng vấn không dẫn dắt"** — Thực hiện 10 buổi phỏng vấn theo nguyên tắc The Mom Test về một vấn đề cụ thể đã chọn. Công cụ: Otter.ai ghi âm, mẫu câu hỏi chuẩn bị trước. KPI: tổng hợp thành báo cáo với ít nhất 3 insight quan trọng và trích dẫn cụ thể.

3. **Dự án "Bản đồ vấn đề và các bên liên quan"** — Xây dựng sơ đồ trực quan thể hiện vấn đề, các bên liên quan, và mối quan hệ giữa "người đau" và "người trả tiền". Công cụ: Miro/FigJam. KPI: hoàn thành 1 bản đồ rõ ràng, trình bày được cho mentor hoặc nhóm phản biện.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu |
|---|---|
| Số vấn đề được ghi nhận ban đầu | Tối thiểu 20 vấn đề |
| Số vấn đề còn lại sau xác thực | 1-2 vấn đề ưu tiên hàng đầu |
| Số buổi phỏng vấn thực hiện | Tối thiểu 10-15 buổi |
| Số nguồn dữ liệu chéo kiểm chứng | Tối thiểu 2-3 nguồn |
| Hoàn thành problem statement có bằng chứng | 1 bản hoàn chỉnh |
| Thời gian dành cho giai đoạn khám phá vấn đề | 4-6 tuần |

## 22. Tài nguyên miễn phí

- Bài viết và công cụ miễn phí trên IDEO.org
- Tài liệu và khóa học miễn phí trên IHI Open School
- Video Y Combinator Startup School về xác định vấn đề
- Blog Product Talk của Teresa Torres
- Cộng đồng Mind the Product

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Sách "The Mom Test", "Continuous Discovery Habits" | 15-30 USD/cuốn (ước tính) | Kỹ thuật phỏng vấn và khám phá vấn đề có hệ thống |
| Dovetail (nền tảng phân tích nghiên cứu người dùng) | Vài chục đến vài trăm USD/tháng (ước tính) | Tổng hợp và phân tích insight từ nhiều phỏng vấn hiệu quả hơn |
| Khóa học Human-Centered Design (IDEO U) | Vài trăm USD (ước tính) | Chứng chỉ và phương pháp luận có cấu trúc |
| Dịch vụ nghiên cứu thị trường thuê ngoài | Thay đổi lớn tùy phạm vi | Dữ liệu định lượng quy mô lớn hơn khả năng tự thực hiện |

## 24. Những tài liệu bắt buộc đọc

1. The Mom Test — Rob Fitzpatrick (kỹ thuật phỏng vấn không dẫn dắt)
2. Competing Against Luck — Clayton Christensen và cộng sự (Jobs to be Done)
3. Continuous Discovery Habits — Teresa Torres (thói quen khám phá liên tục)
4. Ít nhất 1 công cụ Root Cause Analysis từ Institute for Healthcare Improvement
5. Ít nhất 1 báo cáo về gánh nặng hành chính/burnout bác sĩ (tự tra cứu PubMed) để hiểu bối cảnh vấn đề hệ thống

## 25. Lộ trình ưu tiên đọc

1. The Mom Test (Rob Fitzpatrick) — chuẩn bị kỹ năng phỏng vấn trước tiên
2. Competing Against Luck (Jobs to be Done) — hiểu động cơ sâu xa của người dùng
3. Công cụ Root Cause Analysis của IHI — học kỹ thuật đào sâu nguyên nhân
4. Continuous Discovery Habits (Teresa Torres) — xây thói quen khám phá liên tục
5. Just Enough Research (Erika Hall) — thực hành nghiên cứu gọn nhẹ
6. The Innovator's Prescription — đặt vấn đề trong bối cảnh chiến lược hệ thống y tế
7. Case study trong mục 18 và tài liệu cộng đồng Mind the Product — học từ thực tiễn
