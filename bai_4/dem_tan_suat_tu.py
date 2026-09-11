# ============================================================
# HOAT DONG 6: Van dung - Dem tan suat tu trong van ban
# ============================================================

print("=" * 60)
print("DEM TAN SUAT TU TRONG VAN BAN")
print("=" * 60)

doan_van = "python la ngon ngu lap trinh python de hoc python de dung"
danh_sach_tu = doan_van.split()

tan_suat = {}
for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

print("\n--- Tan suat xuat hien cac tu ---")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")

# Giai thich: tan_suat.get(tu, 0) + 1
# - Neu tu da co trong dict: get() tra ve gia tri hien tai (so lan da dem duoc)
#   -> cong them 1 = tang so lan xuat hien
# - Neu tu chua co trong dict: get() tra ve gia tri mac dinh la 0
#   -> 0 + 1 = 1 (lan dau tien xuat hien)
# Cach nay thay the viec phai kiem tra "tu da xuat hien hay chua" bang if/else
