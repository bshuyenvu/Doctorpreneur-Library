# Hướng dẫn đóng góp

- **Repository chính thức:** https://github.com/bshuyenvu/Doctorpreneur-Library
- **Website:** https://bshuyenvu.github.io/Doctorpreneur-Library
- **Tạo issue:** https://github.com/bshuyenvu/Doctorpreneur-Library/issues/new/choose


## Nguyên tắc

1. Mỗi pull request giải quyết một mục tiêu rõ ràng.
2. Nguồn y khoa ưu tiên guideline, cơ quan quản lý, bài báo bình duyệt và trang chính thức.
3. Không bịa DOI, PMID, Impact Factor, số người dùng, vốn gọi được hoặc trạng thái phê duyệt.
4. Với dữ liệu động, ghi ngày kiểm tra.
5. Không đưa thông tin nhận diện bệnh nhân hoặc lời khuyên điều trị cá nhân.

## Quy trình

```bash
git checkout -b docs/ten-thay-doi
# chỉnh sửa
python scripts/validate_repo.py
git add .
git commit -m "docs: mô tả thay đổi"
git push origin docs/ten-thay-doi
```

Tạo pull request tại `https://github.com/bshuyenvu/Doctorpreneur-Library/pulls`, mô tả lý do, nguồn và ảnh hưởng đến các chương liên quan.
