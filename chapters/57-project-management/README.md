# 57. Quản lý dự án HealthTech

Nguyên tắc và công cụ quản lý dự án cho sản phẩm y tế: từ Agile/Scrum đến quản lý rủi ro và tuân thủ.

## 1. Giới thiệu

Quản lý dự án trong HealthTech khác biệt so với các ngành khác vì mỗi tính năng đều có thể ảnh hưởng trực tiếp đến an toàn người bệnh và phải đi qua các bước kiểm định chặt chẽ hơn (validation, kiểm thử lâm sàng nếu cần, tuân thủ quy định). Theo các báo cáo ngành ước tính, phần lớn dự án phần mềm y tế bị trễ tiến độ hoặc vượt ngân sách không phải vì thiếu kỹ thuật mà vì thiếu quy trình quản lý phạm vi, ưu tiên và giao tiếp giữa đội ngũ lâm sàng và đội kỹ thuật.

Với bác sĩ khởi nghiệp, quản lý dự án là kỹ năng cầu nối: người vừa hiểu ngôn ngữ lâm sàng vừa có thể điều phối đội ngũ kỹ thuật, thiết kế và kinh doanh để sản phẩm ra đời đúng thời hạn, đúng phạm vi và đúng chất lượng. Không nắm được các nguyên tắc cơ bản của Agile, quản lý rủi ro và roadmap, founder bác sĩ dễ rơi vào tình trạng phụ thuộc hoàn toàn vào báo cáo một chiều từ đội kỹ thuật.

## 2. Tại sao bác sĩ cần học

1. Kiểm soát được tiến độ và ngân sách phát triển sản phẩm, tránh "burn rate" không kiểm soát.
2. Biết đặt ưu tiên tính năng theo giá trị lâm sàng và giá trị kinh doanh, không chỉ theo độ dễ triển khai.
3. Giao tiếp hiệu quả với đội ngũ đa chức năng (kỹ thuật, thiết kế, pháp lý, y khoa) trong cùng một ngôn ngữ dự án.
4. Quản lý rủi ro đặc thù y tế (an toàn dữ liệu, sai sót lâm sàng do phần mềm) ngay từ giai đoạn lập kế hoạch.

## 3. Kiến thức nền

- **Agile/Scrum**: phát triển theo chu kỳ ngắn (sprint 1-2 tuần), ưu tiên phản hồi nhanh và điều chỉnh liên tục.
- **Kanban**: quản lý luồng công việc liên tục, phù hợp với đội vận hành/hỗ trợ sản phẩm.
- **Product roadmap**: lộ trình tính năng theo quý, gắn với mục tiêu kinh doanh và lâm sàng.
- **RACI matrix**: phân định trách nhiệm rõ ràng (Responsible, Accountable, Consulted, Informed) giữa các bên liên quan.
- **Risk register**: bảng theo dõi rủi ro dự án, đặc biệt rủi ro liên quan an toàn người bệnh và tuân thủ.
- **Definition of Done**: tiêu chí hoàn thành rõ ràng cho mỗi tính năng, bao gồm cả kiểm thử và tài liệu tuân thủ.

## 4. Những sai lầm thường gặp

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Không có product owner rõ ràng | Ưu tiên tính năng mâu thuẫn, đội kỹ thuật mất phương hướng | Chỉ định một người chịu trách nhiệm quyết định cuối cùng |
| Ước lượng thời gian quá lạc quan | Trễ deadline liên tục, mất niềm tin nhà đầu tư | Dùng dữ liệu lịch sử, thêm buffer 20-30% |
| Bỏ qua đánh giá rủi ro tuân thủ ngay từ đầu sprint | Phải làm lại tính năng khi phát hiện vi phạm quy định | Đưa checklist tuân thủ vào Definition of Done |
| Giao tiếp một chiều, không có retrospective | Lặp lại sai lầm giữa các sprint | Duy trì họp retrospective định kỳ, ghi nhận bài học |
| Quản lý quá nhiều dự án song song mà không ưu tiên | Đội ngũ quá tải, chất lượng giảm | Áp dụng WIP limit (giới hạn công việc đang làm) |

## 5. Roadmap học (5 tuần)

- **Tuần 1**: Nguyên tắc Agile/Scrum, vai trò Product Owner và Scrum Master.
- **Tuần 2**: Xây dựng product roadmap và backlog ưu tiên theo giá trị.
- **Tuần 3**: Quản lý rủi ro dự án, đặc biệt rủi ro an toàn và tuân thủ y tế.
- **Tuần 4**: Công cụ quản lý dự án (Jira, Linear, Notion) và thiết lập quy trình cho đội nhỏ.
- **Tuần 5**: Thực hành lập kế hoạch sprint đầu tiên cho một tính năng sản phẩm cụ thể.

## 6. Top sách

| Tên | Tác giả | Năm | Mức độ | Tóm tắt 1 câu | Ai nên đọc |
|---|---|---|---|---|---|
| Scrum: The Art of Doing Twice the Work in Half the Time | Jeff Sutherland | 2014 | Cơ bản | Nguồn gốc và triết lý Scrum | Founder mới bắt đầu |
| Inspired | Marty Cagan | 2017 | Trung bình | Tư duy sản phẩm hiện đại | Product owner |
| The Lean Startup | Eric Ries | 2011 | Cơ bản | Xây dựng sản phẩm qua vòng lặp học nhanh | Founder giai đoạn sớm |

## 7. Top bài báo/nghiên cứu

| Tiêu đề | Nguồn/Tạp chí | Năm | Ý nghĩa ứng dụng |
|---|---|---|---|
| Nguyên nhân thất bại dự án phần mềm y tế | Tra cứu PubMed từ khóa: "health information system project failure causes" | — | Nhận diện rủi ro thường gặp |
| Áp dụng Agile trong phát triển phần mềm y tế | Tra cứu Google Scholar từ khóa: "agile methodology healthcare software development" | — | So sánh hiệu quả với mô hình truyền thống |

## 8. Top guideline / white paper

| Tên | Tổ chức | Năm | Ghi chú |
|---|---|---|---|
| Scrum Guide | Scrum.org | Cập nhật liên tục | Tài liệu chính thức, miễn phí |
| PMBOK Guide (tổng quan) | Project Management Institute | Cập nhật định kỳ | Khung quản lý dự án truyền thống, tham khảo đối chiếu |

## 9. Top website

| Tên | Mô tả | Ghi chú truy cập |
|---|---|---|
| scrum.org | Tài liệu và chứng chỉ Scrum | Miễn phí phần cơ bản |
| producttalk.org | Blog về product management | Miễn phí |
| atlassian.com/agile | Hướng dẫn Agile thực hành | Miễn phí |

## 10. Top newsletter

| Tên | Tác giả/tổ chức | Chủ đề |
|---|---|---|
| Lenny's Newsletter | Lenny Rachitsky | Product management, growth |
| The Product Compass | Paweł Huryn | Chiến lược sản phẩm |

## 11. Top podcast

| Tên | Host | Nền tảng |
|---|---|---|
| Product Thinking | Melissa Perri | Spotify, Apple Podcasts |
| This is Product Management | Mind the Product | Spotify |

## 12. Top kênh YouTube

| Tên | Mô tả |
|---|---|
| Atlassian | Video hướng dẫn Agile, Jira thực hành |
| Product School | Nội dung đào tạo product management |

## 13. Top khóa học

| Tên | Nền tảng/Tổ chức | Thời lượng ước tính | Chi phí |
|---|---|---|---|
| Agile with Atlassian Jira | Coursera | 3-4 tuần | Miễn phí/trả phí có chứng chỉ |
| Certified ScrumMaster (CSM) | Scrum Alliance | 2 ngày | Trả phí (vài triệu VNĐ) |
| Digital Product Management | Coursera/Google | 4-6 tuần | Trả phí |

## 14. Top GitHub repo

| Tên | Mô tả | Ghi chú |
|---|---|---|
| awesome-project-management | Danh sách tài nguyên quản lý dự án | Tổng hợp công cụ, template |
| open-source-templates (Notion/Jira export) | Mẫu quản lý dự án chia sẻ cộng đồng | Tùy nguồn, cần kiểm tra license |

## 15. Top AI Tools

| Tên | Mô tả | Ứng dụng |
|---|---|---|
| Notion AI | Hỗ trợ viết tài liệu, tóm tắt cuộc họp | Quản lý backlog, ghi chú dự án |
| Linear | Công cụ quản lý issue hiện đại, tích hợp AI gợi ý ưu tiên | Theo dõi sprint, roadmap |
| ClickUp AI | Tự động tóm tắt tiến độ dự án | Báo cáo nhanh cho nhà đầu tư |

## 16. Top Open-source projects

| Tên | License | Mô tả |
|---|---|---|
| Taiga | MPL 2.0 | Công cụ quản lý dự án Agile mã nguồn mở |
| OpenProject | GPL v3 | Nền tảng quản lý dự án doanh nghiệp mã nguồn mở |

## 17. Cộng đồng quốc tế liên quan

| Tên | Mô tả |
|---|---|
| Mind the Product community | Cộng đồng product manager toàn cầu |
| Scrum Alliance community | Cộng đồng thực hành Agile/Scrum |

## 18. Case study nổi bật

**Oscar Health**: Trong giai đoạn đầu, đội ngũ áp dụng chu kỳ phát triển ngắn để liên tục điều chỉnh trải nghiệm người dùng bảo hiểm y tế dựa trên phản hồi thực tế, thay vì xây dựng toàn bộ tính năng trước khi ra mắt. Bài học: quản lý dự án linh hoạt giúp sản phẩm bám sát nhu cầu thị trường thay đổi nhanh.

**Một startup đặt lịch khám tại Việt Nam** (ẩn danh, minh họa): founder bác sĩ ban đầu quản lý dự án bằng bảng Excel, dẫn đến mất kiểm soát ưu tiên khi đội mở rộng lên 10 người; sau khi chuyển sang Scrum với sprint 2 tuần và backlog rõ ràng, tốc độ ra tính năng tăng đáng kể. Bài học: quy trình quản lý dự án cần được chuẩn hóa sớm trước khi đội ngũ mở rộng.

## 19. Checklist thực hành

- [ ] Xác định vai trò Product Owner cho dự án của bạn
- [ ] Xây dựng backlog tính năng ưu tiên theo giá trị lâm sàng và kinh doanh
- [ ] Thiết lập chu kỳ sprint 1-2 tuần với mục tiêu rõ ràng
- [ ] Tạo risk register cho các rủi ro an toàn và tuân thủ
- [ ] Chọn công cụ quản lý dự án phù hợp quy mô đội (Notion, Linear, Jira)
- [ ] Thiết lập Definition of Done bao gồm tiêu chí tuân thủ
- [ ] Tổ chức họp retrospective sau mỗi sprint
- [ ] Xây dựng roadmap sản phẩm theo quý
- [ ] Phân định trách nhiệm rõ ràng bằng RACI matrix
- [ ] Đánh giá lại ước lượng thời gian sau mỗi 2-3 sprint

## 20. Project thực hành

1. **Lập backlog và sprint đầu tiên**: chọn một tính năng MVP, chia nhỏ thành task; công cụ: Notion/Linear; KPI: hoàn thành sprint đúng hạn với ít nhất 80% task.
2. **Xây dựng risk register**: liệt kê 10 rủi ro lớn nhất của dự án và kế hoạch giảm thiểu; công cụ: bảng tính; KPI: cập nhật risk register hàng tháng.
3. **Thực hành retrospective**: tổ chức 3 buổi retrospective liên tiếp sau mỗi sprint; công cụ: họp trực tiếp/online; KPI: ít nhất 2 cải tiến quy trình được áp dụng.

## 21. KPI cần đạt

| Chỉ số | Mục tiêu |
|---|---|
| Tỷ lệ hoàn thành sprint đúng kế hoạch | Trên 80% |
| Thời gian trung bình từ ý tưởng đến triển khai tính năng | Dưới 4 tuần cho tính năng nhỏ |
| Số rủi ro được xác định trước khi xảy ra | Tăng dần theo thời gian, mục tiêu trên 70% |
| Tần suất retrospective | Đều đặn sau mỗi sprint |

## 22. Tài nguyên miễn phí

- Scrum Guide chính thức (scrum.org)
- Blog atlassian.com/agile
- Template quản lý dự án miễn phí trên Notion
- Cộng đồng Mind the Product

## 23. Tài nguyên trả phí

| Tên | Chi phí ước tính | Giá trị mang lại |
|---|---|---|
| Certified ScrumMaster (CSM) | Vài triệu đến chục triệu VNĐ | Chứng chỉ và kỹ năng quản lý Agile bài bản |
| Linear/Jira gói trả phí | Vài trăm nghìn VNĐ/người/tháng | Công cụ quản lý dự án chuyên nghiệp |
| Tư vấn quản lý dự án từ chuyên gia | Theo giờ, thương lượng | Thiết lập quy trình nhanh, tránh sai lầm ban đầu |

## 24. Những tài liệu bắt buộc đọc

1. Scrum Guide chính thức
2. Inspired — Marty Cagan
3. The Lean Startup — Eric Ries
4. Tài liệu hướng dẫn RACI matrix (tìm kiếm "RACI matrix template")
5. Ít nhất 1 case study về quản lý dự án HealthTech thất bại và bài học

## 25. Lộ trình ưu tiên đọc

1. Bắt đầu với Scrum Guide để nắm khung Agile cơ bản
2. Đọc The Lean Startup để hiểu tư duy vòng lặp học nhanh
3. Tìm hiểu Inspired để nâng cao tư duy sản phẩm
4. Thực hành thiết lập backlog và sprint đầu tiên
5. Tham gia cộng đồng Mind the Product để cập nhật thực tiễn
