# ==========================================
# HOẠT ĐỘNG 1: HÀM CƠ BẢN
# ==========================================

def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Tối ưu vòng lặp kiểm tra tới sqrt(n)
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    if n <= 0:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# Gọi thử các hàm Hoạt động 1 với ít nhất 3 bộ dữ liệu
print("--- KẾT QUẢ HOẠT ĐỘNG 1 ---")
print("USCLN (24, 36):", uscln(24, 36))
print("USCLN (17, 13):", uscln(17, 13))
print("USCLN (100, 75):", uscln(100, 75))

print("BSCNN (4, 6):", bscnn(4, 6))
print("BSCNN (5, 7):", bscnn(5, 7))
print("BSCNN (12, 18):", bscnn(12, 18))

print("Số nguyên tố (29):", kiem_tra_nguyen_to(29))
print("Số nguyên tố (4):", kiem_tra_nguyen_to(4))
print("Số nguyên tố (1):", kiem_tra_nguyen_to(1))

print("Số hoàn thiện (28):", kiem_tra_so_hoan_thien(28))
print("Số hoàn thiện (6):", kiem_tra_so_hoan_thien(6))
print("Số hoàn thiện (12):", kiem_tra_so_hoan_thien(12))

# Bài tập 1.2
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return

def chia_lay_thuong_du(a, b):
    return a // b, a % b

in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")


# ==========================================
# HOẠT ĐỘNG 2: THAM SỐ MẶC ĐỊNH & TỪ KHÓA
# ==========================================

def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")

print("\n--- KẾT QUẢ HOẠT ĐỘNG 2 ---")
gioi_thieu("An")  # Dùng mặc định
gioi_thieu("Binh", 20)  # Ghi đè tuổi
gioi_thieu("Chi", lop="CNTT01")  # Dùng tham số từ khóa
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)  # Đảo thứ tự tham số từ khóa


# ==========================================
# HOẠT ĐỘNG 3: THAM SỐ LINH HOẠT (*args & **kwargs)
# ==========================================

def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

print("\n--- KẾT QUẢ HOẠT ĐỘNG 3 ---")
print("Tổng 1:", tinh_tong(1, 2, 3))
print("Tổng 2:", tinh_tong(5, 10, 15, 20, 25))
print("Tổng rỗng:", tinh_tong())

in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")