# ============================================================
# HOAT DONG 4: Chuyen doi kieu du lieu tuong minh & ngam dinh
# ============================================================

print("=" * 60)
print("HOAT DONG 4: Chuyen doi kieu du lieu")
print("=" * 60)

# --- Bai tap 4.1: Ep kieu tuong minh ---
print("\n--- Bai tap 4.1: Ep kieu tuong minh ---")

chuoi_so = "25"
so = int(chuoi_so)
print(f"int('{chuoi_so}') = {so}, type: {type(so)}")

so_thuc = float("3.14")
print(f"float('3.14') = {so_thuc}, type: {type(so_thuc)}")

danh_sach = list((1, 2, 3))  # tuple -> list
print(f"list((1,2,3)) = {danh_sach}, type: {type(danh_sach)}")

bo_ba = tuple([4, 5, 6])  # list -> tuple
print(f"tuple([4,5,6]) = {bo_ba}, type: {type(bo_ba)}")

tap_hop = set([1, 2, 2, 3, 3, 3])  # list -> set (tu loai bo trung lap)
print(f"set([1,2,2,3,3,3]) = {tap_hop}, type: {type(tap_hop)}")

tu_dien = dict([("a", 1), ("b", 2)])  # list cac tuple -> dict
print(f"dict([('a',1),('b',2)]) = {tu_dien}, type: {type(tu_dien)}")

# --- Bai tap 4.2: Truong hop gay loi khi ep kieu ---
print("\n--- Bai tap 4.2: Truong hop gay loi khi ep kieu ---")

# int("abc") -> gay loi ValueError: invalid literal for int() with base 10: 'abc'
# int("3.14") -> gay loi ValueError: invalid literal for int() with base 10: '3.14'
# Cach dung: ep qua float() truoc
so_hop_le = int(float("3.14"))
print(f"int(float('3.14')) = {so_hop_le} (ep qua float truoc)")

# --- Bai tap 4.3: Chuyen doi ngam dinh ---
print("\n--- Bai tap 4.3: Chuyen doi ngam dinh ---")

ket_qua = 5 + 2.5  # int + float -> Python tu dong chuyen thanh float
print(f"5 + 2.5 = {ket_qua}, type: {type(ket_qua)}")

# Phai ep str() tuong minh, Python KHONG tu dong noi str voi so
ket_qua_2 = "Diem: " + str(8.5)
print(f"'Diem: ' + str(8.5) = {ket_qua_2}")
