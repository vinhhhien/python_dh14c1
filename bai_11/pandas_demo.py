
import pandas as pd

# ==================================
# BAI 2.1: DOC CSV VA XEM TONG QUAN
# ==================================

df = pd.read_csv("diem_sinh_vien.csv")

print("===== BAI 2.1: DOC DU LIEU CSV =====")

print("\n5 dong dau tien:")
print(df.head())

print("\nSo dong, so cot:")
print(df.shape)

print("\nDanh sach ten cot:")
print(df.columns.tolist())


# ==================================
# BAI 2.2: THONG KE THEO MON HOC
# ==================================

print("\n===== BAI 2.2: THONG KE DIEM =====")

diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

print("\nDiem trung binh theo mon:")
print(diem_trung_binh_mon)

print("\nDiem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())


# ==================================
# BAI 2.3: TINH DTB TUNG SINH VIEN
# ==================================

print("\n===== BAI 2.3: LOC SINH VIEN =====")

diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)

print("\nDiem trung binh tung sinh vien:")
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)

print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)
