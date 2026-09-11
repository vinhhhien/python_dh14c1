# ============================================================
# HOAT DONG 1: Dictionary co ban - khai bao, truy xuat, them/sua/xoa
# ============================================================

print("=" * 60)
print("HOAT DONG 1: Dictionary co ban")
print("=" * 60)

# --- Bai tap 1.1: Khai bao & truy xuat ---
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print("\n--- Bai tap 1.1: Khai bao & truy xuat ---")
print(sinh_vien["ho_ten"])          # truy xuat theo khoa
print(sinh_vien.get("diem_tb"))     # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co"))  # get() voi gia tri mac dinh

# Giai thich: sinh_vien["lop"] gay loi KeyError vi "lop" chua ton tai trong dict
# sinh_vien.get("lop", "Chua co") khong loi vi get() tra ve gia tri mac dinh

# --- Bai tap 1.2: Them/sua/xoa ---
print("\n--- Bai tap 1.2: Them/sua/xoa ---")
sinh_vien["lop"] = "CNTT01"        # them khoa moi
sinh_vien["diem_tb"] = 9.0         # sua gia tri khoa da co
print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")  # xoa theo khoa, tra ve gia tri vua xoa
print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"})
print(sinh_vien)

# ============================================================
# HOAT DONG 2: Duyet Dictionary bang for - keys/values/items
# ============================================================

print("\n" + "=" * 60)
print("HOAT DONG 2: Duyet Dictionary bang for")
print("=" * 60)

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

print("\nDuyet theo keys:")
for mon in diem_mon_hoc.keys():
    print(mon)

print("\nDuyet theo values:")
for diem in diem_mon_hoc.values():
    print(diem)

print("\nDuyet theo items:")
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# Tinh diem trung binh
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("\nDiem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

# ============================================================
# HOAT DONG 3: Dictionary comprehension & Set
# ============================================================

print("\n" + "=" * 60)
print("HOAT DONG 3: Dictionary comprehension & Set")
print("=" * 60)

# --- Bai tap 3.1: Dictionary comprehension ---
print("\n--- Bai tap 3.1: Dictionary comprehension ---")
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

# Cong 0.5 diem cho moi mon
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print("Diem cong 0.5:", diem_cong_diem)

# Viet hoa ten mon
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print("Ten mon viet hoa:", ten_mon_viet_hoa)

# --- Bai tap 3.2: So sanh nhanh voi Set ---
print("\n--- Bai tap 3.2: So sanh voi Set ---")
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print("Giao (mon chung):", mon_hoc_ky1 & mon_hoc_ky2)
print("Hop (tat ca mon):", mon_hoc_ky1 | mon_hoc_ky2)
print("Hieu (chi co o ky 1):", mon_hoc_ky1 - mon_hoc_ky2)

# So sanh Set voi Dictionary:
# - Set chi luu gia tri don, khong luu cap khoa-gia tri nhu Dictionary
# - Set khong cho phep phan tu trung lap vi Set su dung implementation hash table
#   va khi them phan ton tai thi no se bi ghi de (khong thay doi)
