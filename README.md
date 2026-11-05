# BÁO CÁO PHÂN TÍCH BẢO MẬT: CHUỖI TẤN CÔNG DOMINO TỪ MẬT KHẨU RÒ RỈ

## 1. Cơ chế tấn công Domino (Credential Stuffing)
1. Diễn đàn nhỏ bị lộ database (chứa plaintext/mật khẩu băm yếu `123456`).
2. Hacker dùng bot tự động thử cặp email/password trên các dịch vụ lớn (Gmail, GitHub, Facebook...).
3. Hiệu ứng sụp đổ dây chuyền: Mất Gmail -> Hacker dùng "Quên mật khẩu" để reset mọi tài khoản liên quan.

## 2. So sánh Mật khẩu cảm tính vs Máy tính tạo ra
- Cảm tính: Entropy thấp (10-30 bits), dễ bị Dictionary Attack và Rainbow Table.
- Máy tính tạo: Ngẫu nhiên tuyệt đối, Entropy cao (>80-128 bits), miễn nhiễm tấn công từ điển.

## 3. Tiêu chuẩn AES-256 trong Password Manager
- AES-256 mã hóa cấp quân sự kết hợp Zero-Knowledge.
- Khắc phục hoàn toàn rủi ro bị xem trộm vật lý hoặc dính mã độc InfoStealer quét ghi chú không mã hóa.