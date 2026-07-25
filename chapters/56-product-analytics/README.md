# 56 — Phân tích sản phẩm

> **Nhánh 6 — Sản phẩm, công nghệ và tổ chức** · Mức ưu tiên: 🟡 Cao
> **Kỹ năng cần đạt:** Xây funnel, cohort và chỉ số giá trị lâm sàng.
> **Sản phẩm của chương:** Product metrics tree.

---

## 1. Tóm tắt điều hành

Phân tích sản phẩm đo cách người dùng thực sự dùng sản phẩm để hướng dẫn quyết định. Cạm bẫy là vanity metrics (số đẹp nhưng vô nghĩa) và — đặc thù y tế — nhầm chỉ số sử dụng với giá trị lâm sàng. Đầu ra là *product metrics tree*: cây chỉ số liên kết từ chỉ số vận hành (sử dụng) tới chỉ số giá trị (kết cục lâm sàng và kinh doanh), giúp biết chỉ số nào thực sự quan trọng.

## 2. Mục tiêu học tập

Bạn sẽ: (a) phân biệt vanity và actionable metrics; (b) xây funnel và phân tích cohort; (c) liên kết chỉ số sử dụng với giá trị lâm sàng/kinh doanh; (d) phác product metrics tree.

## 3. Vì sao chương này quan trọng với Doctorpreneur

Đo sai dẫn tới quyết định sai. Trong y tế, "nhiều lượt dùng" không đồng nghĩa "cải thiện chăm sóc". Metrics tree giúp bạn nối sử dụng với giá trị thật và tránh tự huyễn bằng số đẹp.

## 4. Khái niệm cốt lõi và định nghĩa

**Vanity vs actionable metric:** số đẹp vô dụng vs số dẫn tới hành động. **Funnel:** chuỗi bước chuyển đổi. **Cohort:** nhóm người dùng theo mốc. **North Star metric:** chỉ số dẫn dắt phản ánh giá trị cốt lõi. **Retention:** giữ chân. **Leading/lagging indicator:** chỉ số dẫn/trễ.

## 5. Khung tư duy nền tảng

Xây cây chỉ số từ North Star (giá trị cốt lõi) xuống các chỉ số đầu vào (drivers) mà đội tác động được. Trong y tế, North Star nên gắn giá trị lâm sàng/kết cục, không chỉ engagement. Dùng funnel để tìm điểm rơi, cohort để hiểu retention thật. Nguyên tắc: mỗi chỉ số phải dẫn tới một quyết định; nếu không, bỏ. Phân biệt chỉ số sử dụng (leading) với giá trị lâm sàng (lagging, cần bằng chứng — chương 25–30).

## 6. Bối cảnh y tế Việt Nam và tuyến cơ sở

Đo lường phải tuân bảo mật dữ liệu (chương 40) — không thu thập dữ liệu định danh vượt mục đích. Ở tuyến cơ sở, chỉ số giá trị thực dụng gồm giảm gánh nặng, cải thiện tuân thủ theo dõi, giảm chuyển tuyến — nối được với ngân sách và chất lượng. Giá trị lâm sàng cần bằng chứng, không suy từ chỉ số sử dụng.

## 7. Các bên liên quan

Product/analytics, lâm sàng (định nghĩa giá trị), và bảo mật. Định nghĩa "giá trị" cần đầu vào lâm sàng để chỉ số không lệch sang engagement thuần.

## 8. Quy trình từng bước

1. **Xác định North Star** gắn giá trị lâm sàng/kinh doanh.
2. **Phân rã thành drivers** đội tác động được.
3. **Xây funnel** cho hành trình then chốt.
4. **Thiết lập cohort/retention.**
5. **Nối chỉ số sử dụng với giá trị** (và kế hoạch bằng chứng lâm sàng).
6. **Lập product metrics tree** và bảng theo dõi.

## 9. Công cụ và template áp dụng

- **Product metrics tree:** North Star → drivers → chỉ số vận hành.
- **Funnel + cohort chart.**
- **Bảng vanity vs actionable.**

## 10. Ví dụ minh họa

Công cụ tuân thủ điều trị. North Star: tỉ lệ tuân thủ cải thiện (gắn kết cục). Drivers: kích hoạt, retention, tần suất dùng. Funnel: đăng ký → dùng lần đầu → dùng lặp. Cohort retention theo tuần. Nối "dùng lặp" với "tuân thủ" — nhưng giá trị lâm sàng (cải thiện kết cục) cần bằng chứng riêng (chương 25–30), không suy từ retention.

## 11. Sai lầm thường gặp

- **Vanity metrics** (tổng tải, lượt xem).
- **Nhầm engagement với giá trị lâm sàng.**
- **Chỉ số không dẫn tới quyết định.**
- **Bỏ cohort** (nhìn tổng số che retention kém).
- **Thu thập dữ liệu vượt mục đích** (vi phạm privacy).

## 12. Rủi ro an toàn, pháp lý và đạo đức

Thu thập/dùng dữ liệu hành vi phải tuân privacy (chương 40) — minimization, mục đích rõ, đồng thuận khi cần. Không tối ưu chỉ số theo cách gây hại (ví dụ engagement bằng lo âu — chương 33). Không tuyên bố giá trị lâm sàng dựa chỉ số sử dụng.

## 13. Chỉ số đo lường

Chất lượng đo lường: tỉ lệ chỉ số dẫn tới quyết định, độ nối giữa sử dụng và giá trị, và tính tuân thủ privacy. Chỉ số chính là North Star và drivers, không phải vanity.

## 14. Bằng chứng và mức độ tin cậy

Chỉ số sử dụng là **leading indicator**, không chứng minh giá trị lâm sàng — cái sau cần thiết kế nghiên cứu (chương 25–30). Tương quan không phải nhân quả. Ghi rõ giới hạn và tránh diễn giải quá mức từ dashboard.

## 15. Tiêu chuẩn và guideline liên quan

Gắn product management (chương 51), mHealth engagement (chương 33), privacy (chương 40), bằng chứng lâm sàng (chương 25–30), data engineering (chương 54).

## 16. Liên hệ các chương khác

Cung cấp bằng chứng cho **51** (ưu tiên); gắn **33** (engagement), **40** (privacy), **25–30** (giá trị lâm sàng), **54** (dữ liệu).

## 17. Bài tập thực hành — Product metrics tree

Xây product metrics tree: chọn North Star gắn giá trị lâm sàng/kinh doanh, phân rã thành drivers đội tác động được, xây một funnel và cohort retention, nối chỉ số sử dụng với giá trị (kèm kế hoạch bằng chứng lâm sàng), và loại bỏ vanity metrics. Nêu cách tuân privacy. Ghi rõ giới hạn diễn giải.

## 18. Checklist tự đánh giá

- [ ] North Star gắn giá trị, không engagement thuần.
- [ ] Mỗi chỉ số dẫn tới một quyết định.
- [ ] Có cohort/retention, không chỉ tổng số.
- [ ] Phân biệt chỉ số sử dụng và giá trị lâm sàng.
- [ ] Tuân privacy (minimization, mục đích).

## 19. Định nghĩa hoàn thành (Definition of Done)

Product metrics tree đạt chuẩn khi có North Star gắn giá trị, drivers tác động được, funnel/cohort, phân biệt rõ sử dụng vs giá trị lâm sàng, và tuân privacy.

## 20. Câu hỏi phản tư

Chỉ số của tôi dẫn tới quyết định hay chỉ để khoe? Tôi có nhầm engagement với giá trị lâm sàng không? Retention thật (cohort) thế nào? Tôi có thu thập dữ liệu vượt mục đích không?

## 21. Cạm bẫy quyết định

**Vanity metrics**, **nhầm sử dụng với giá trị**, **tương quan giả nhân quả**. Đối trọng: metrics tree gắn giá trị, cohort thật, và bằng chứng lâm sàng riêng.

## 22. Nguồn dữ liệu động cần xác minh

Benchmark retention/chuyển đổi ngành, quy định dữ liệu — là dữ liệu động. Đo thực tế và tra quy định; benchmark ngành khác không mượn nguyên si.

## 23. Tài nguyên đọc thêm (curation queue)

Xem [Thư viện sách](../../resources/book-library.md), [AI tools](../../resources/ai-tool-library.md). Nguồn chưa xác minh giữ trong hàng chờ curation.

## 24. Thuật ngữ

**Vanity/actionable metric:** số khoe/số hành động. **Funnel:** phễu chuyển đổi. **Cohort:** nhóm theo mốc. **North Star metric:** chỉ số dẫn dắt. **Leading/lagging:** chỉ số dẫn/trễ.

## 25. Tóm tắt và bước tiếp theo

Phân tích sản phẩm tốt nối sử dụng với giá trị qua metrics tree, tránh vanity metrics và không nhầm engagement với giá trị lâm sàng. Tiếp theo sang **[chương 57 — Quản lý dự án HealthTech](../57-project-management/README.md)** để điều phối thực thi.

---

> ⚠️ **Miễn trừ:** Nội dung phục vụ giáo dục. Chỉ số sử dụng không chứng minh giá trị lâm sàng — cần bằng chứng riêng; thu thập dữ liệu hành vi phải tuân privacy và không tối ưu chỉ số gây hại.
