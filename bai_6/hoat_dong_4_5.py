# ==========================================
# HOẠT ĐỘNG 4: PHẠM VI BIẾN (LOCAL, GLOBAL)
# ==========================================

so_luot_truy_cap = 0  # Biến global

def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1

def vi_du_bien_local():
    so_luot_truy_cap = 100  # Biến local trùng tên
    print("Ben trong ham, bien local =", so_luot_truy_cap)

print("--- KẾT QUẢ HOẠT ĐỘNG 4 ---")
tang_luot_truy_cap()
tang_luot_truy_cap()
print("So luot truy cap (global):", so_luot_truy_cap)
vi_du_bien_local()
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)


# ==========================================
# HOẠT ĐỘNG 5: HÀM LAMBDA (map, filter, sorted)
# ==========================================

danh_sach_so = [1, 2, 3, 4, 5]

# 5.1 map() với lambda
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))

# 5.2 filter() với lambda
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))

# 5.3 sorted() với lambda
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]

sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)

print("\n--- KẾT QUẢ HOẠT ĐỘNG 5 ---")
print("Bình phương:", binh_phuong)
print("Số chẵn:", so_chan)

print("\nSắp xếp tăng dần theo điểm:")
for sv in sap_xep_theo_diem:
    print(f"  {sv['ten']} - {sv['diem']}")

print("\nSắp xếp giảm dần theo điểm:")
for sv in sap_xep_giam_dan:
    print(f"  {sv['ten']} - {sv['diem']}")