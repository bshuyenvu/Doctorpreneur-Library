# Validation Report

**Generated:** 2026-07-19T04:54:17  
**Repository:** `Doctorpreneur-Library`

## Kết quả

| Kiểm tra | Kết quả |
|---|---|
| File tổng cộng | 103 |
| Markdown files | 97 |
| Chapter folders/README | 66 / 66 |
| Chương có đủ mục 1–25 | 66 / 66 |
| Chương 01–10 ≥2.000 từ | 10 / 10 |
| Word count thấp nhất | 3,297 |
| Word count cao nhất | 6,443 |
| Resource files | 9 / 9 |
| Case-study files | 6 / 6 |
| Community files | 2 / 2 |
| `.nojekyll` rỗng | Đạt |
| Validator | `0 errors, 0 warnings` |
| HTTP smoke test | `200 OK`, title `Doctorpreneur Library` |
| ZIP integrity | `No errors detected` |

## Kiểm tra nội dung kỹ thuật

- `index.html` có Docsify core, search, sidebar collapse, copy code, zoom image, pagination, tabs, dark mode và edit link.
- Giscus được chèn bằng `hook.afterEach` và nạp bằng `hook.doneEach`; placeholder ngăn script chạy khi chưa cấu hình.
- Disqus mẫu được giữ trong comment.
- Sidebar chứa đủ 66 đường dẫn chương.
- Tất cả local Markdown links được validator kiểm tra tồn tại.
- Đường dẫn dùng file tĩnh, không yêu cầu build, PHP hoặc database.

## Chính sách dữ liệu

- DOI chỉ ghi khi có bản ghi đã xác định; các mục chưa xác minh được giữ dưới dạng PubMed curation query.
- Impact Factor, Quartile, GitHub stars, phí, quy mô cộng đồng và lịch hội nghị được đánh dấu là dữ liệu động.
- Case studies có source list và cảnh báo kiểm tra lại trạng thái hiện hành.

## Lệnh kiểm tra lại

```bash
python scripts/validate_repo.py
```
