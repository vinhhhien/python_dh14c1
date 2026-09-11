import math

# ========== HOẠT ĐỘNG 3: NUMBER ==========

# Bài 3.1: Các kiểu số và chuyển đổi
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))   # 15.0
print(int(so_thuc))       # 4 (cắt phần thập phân)

# Bài 3.2: Hàm built-in xử lý số
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))                 # 7
print(round(b))               # 3
print(round(b, 2))            # 2.68
print(pow(c, 2))              # 289
print(c ** 2)                 # 289
print(divmod(c, d))           # (3, 2)

# Bài 3.3: Giải phương trình bậc hai (delta dương)
a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

# ========== HOẠT ĐỘNG 4: STRING ==========

# Bài 4.1: Indexing và slicing
cau = "Lap trinh Python rat thu vi"
print(cau[0])          # L
print(cau[-1])         # i
print(cau[4:10])       # trinh
print(cau[:8])         # Lap trin
print(cau[11:])        # Python rat thu vi
print(cau[::-1])       # đảo ngược chuỗi

# Kiểm tra palindrome
print("La palindrome?", cau == cau[::-1])   # False

# Bài 4.2: Tính bất biến
ten = "Nam"
# ten[0] = "T"   # TypeError
ten_moi = "T" + ten[1:]
print(ten_moi)   # Tam

# Bài 4.3: Các phương thức xử lý chuỗi
cau2 = "  Toi dang HOC Python rat vui  "
print(cau2.strip())
print(cau2.strip().upper())
print(cau2.strip().lower())
print(cau2.strip().replace("HOC", "hoc"))
print(cau2.strip().split())
print(len(cau2.strip().split()))
print(cau2.count("o"))
print(cau2.find("Python"))
print(cau2.strip().startswith("Toi"))
print(cau2.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

# Bài 4.4: Chuẩn hóa họ tên
ho_ten_tho = "   hoang hien vinh   "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach)   