# Mini project: Đăng ký thông tin cá nhân

ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

# Chuẩn hóa họ tên
ho_ten_chuan = " ".join(ho_ten.split()).title()

# Kiểm tra dữ liệu cơ bản
sdt_hop_le = len(sdt) == 10          # đủ 10 ký tự
email_hop_le = "@" in email          # có chứa ký tự @

# In kết quả
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")