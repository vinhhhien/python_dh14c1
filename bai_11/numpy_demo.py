
import numpy as np

# 1. Tao danh sach diem bang list Python
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]

# 2. Chuyen list thanh mang NumPy
diem_array = np.array(diem_list)

print("Kieu du lieu list:", type(diem_list))
print("Kieu du lieu NumPy:", type(diem_array))

# 3. Phep toan vector hoa
diem_cong_them = diem_array + 0.5
print("\nDiem sau khi cong 0.5:", diem_cong_them)

# 4. So sanh voi list Python
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("Cong 0.5 bang list:", diem_cong_them_list)

# 5. Thong ke diem
print("\nTrung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

# 6. Tao ma tran NumPy
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])

print("\nMa tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)
