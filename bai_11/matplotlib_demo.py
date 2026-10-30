
import pandas as pd
import matplotlib.pyplot as plt

# =========================================
# BAI 3.1: BIEU DO COT
# =========================================

# Doc du lieu tu file CSV
df = pd.read_csv("diem_sinh_vien.csv")

# Tinh diem trung binh theo mon hoc
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

# Tao bieu do cot
plt.figure(figsize=(6, 4))

plt.bar(
    diem_trung_binh_mon.index,
    diem_trung_binh_mon.values,
    color="skyblue"
)

plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")

# Luu bieu do thanh anh PNG
plt.savefig("bieu_do_cot.png")

# Hien thi bieu do
plt.show()


# =========================================
# BAI 3.2: BIEU DO DUONG
# =========================================

# Du lieu diem qua 3 lan kiem tra
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

# Tao bieu do duong
plt.figure(figsize=(6, 4))

plt.plot(
    lan_kiem_tra,
    diem_qua_cac_lan,
    marker="o",
    color="green"
)

plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")

plt.xticks(lan_kiem_tra)

# Luu bieu do thanh anh PNG
plt.savefig("bieu_do_duong.png")

# Hien thi bieu do
plt.show()
