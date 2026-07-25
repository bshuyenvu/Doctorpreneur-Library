# Thư viện SOP

> Khung quy trình chuẩn (SOP) cho HealthTech. Đây là **mẫu cấu trúc** để tùy biến theo bối cảnh và tuân thủ quy định hiện hành — không phải SOP ban hành. Với sản phẩm là thiết bị y tế, SOP nằm trong hệ thống quản lý chất lượng (chương 23).

## Cấu trúc SOP chuẩn

Mỗi SOP nên có: mã số & phiên bản · ngày hiệu lực · phạm vi · người chịu trách nhiệm · các bước · điểm kiểm soát · hồ sơ lưu · tài liệu tham chiếu · lịch sử thay đổi.

## SOP-01 — Onboarding cơ sở mới (triển khai — chương 64)

1. Khảo sát hạ tầng và HIS của cơ sở.
2. Lập integration map (chương 35) và kế hoạch bảo mật.
3. Cấu hình và kiểm thử tích hợp.
4. Đào tạo người dùng theo curriculum (chương 63).
5. Kiểm thử chấp nhận với tiêu chí định trước.
6. Go-live có giám sát; ghi hồ sơ.
**Điểm kiểm soát:** không go-live nếu kiểm thử an toàn/tích hợp chưa đạt.

## SOP-02 — Quản lý thay đổi (change control — chương 23, 50, 55)

1. Đề xuất thay đổi kèm đánh giá tác động (gồm an toàn/rủi ро).
2. Phê duyệt theo cấp phù hợp mức rủi ро.
3. Kiểm thử và (nếu chạm chức năng lâm sàng) validation lại (chương 47).
4. Triển khai có thể rollback; ghi hồ sơ.
**Điểm kiểm soát:** thay đổi chạm quyết định lâm sàng bắt buộc validation lại.

## SOP-03 — Ứng phó sự cố (an toàn/an ninh — chương 39, 24)

1. Phát hiện và phân loại mức nghiêm trọng.
2. Cô lập và giảm thiểu; bảo đảm không mất an toàn lâm sàng (có dự phòng).
3. Thông báo theo nghĩa vụ quy định.
4. Khắc phục và phục hồi.
5. Phân tích nguyên nhân gốc và CAPA; cập nhật risk file.
**Điểm kiểm soát:** sự cố ảnh hưởng an toàn người bệnh phải có phương án duy trì chăm sóc.

## SOP-04 — Quản trị dữ liệu bệnh nhân (chương 40)

1. Xác định cơ sở pháp lý và mục đích cho mỗi luồng dữ liệu.
2. Áp data minimization và phân quyền.
3. Ẩn danh/giả danh khi dùng ngoài chăm sóc trực tiếp.
4. Xử lý yêu cầu quyền chủ thể dữ liệu.
5. Rà soát định kỳ và ghi hồ sơ xử lý.
**Điểm kiểm soát:** không dùng dữ liệu cho AI/nghiên cứu khi thiếu cơ sở pháp lý/phê duyệt.

## SOP-05 — Giám sát mô hình AI (MLOps — chương 50)

1. Giám sát drift đầu vào và hiệu năng (gồm công bằng).
2. Cảnh báo khi vượt ngưỡng; điều tra.
3. Tái huấn luyện có validation lại và change control.
4. Rollback khi suy giảm.
**Điểm kiểm soát:** không thay mô hình khi chưa validation lại.

---

> ⚠️ Đây là khung mẫu, không phải SOP ban hành. Tùy biến theo quy định hiện hành và bối cảnh cơ sở; với thiết bị y tế, đặt trong QMS. Bổ sung/sửa qua pull request.
