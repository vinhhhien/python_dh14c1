import time

# ==========================================
# HOẠT ĐỘNG 6: ĐỆ QUY
# ==========================================

# Bài tập 6.1 – Giai thừa
def giai_thua_de_quy(n):
    if n <= 1:
        return 1
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

print("--- BÀI TẬP 6.1: GIAI THỪA ---")
print("Giai thừa đệ quy (5) vs Vòng lặp (5):", giai_thua_de_quy(5), "-", giai_thua_lap(5))


# Bài tập 6.2 – Fibonacci
def fibonacci_de_quy(n):
    if n <= 1:
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

print("\n--- BÀI TẬP 6.2: FIBONACCI ---")
print("10 số Fibonacci đầu tiên:")
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()

# Thử nghiệm kiểm chứng tốc độ thực thi với n = 30
print("\nThử nghiệm tính fibonacci_de_quy(30):")
start_time = time.time()
k_qua = fibonacci_de_quy(30)
end_time = time.time()

print(f"Kết quả Fibo(30) = {k_qua}")
print(f"Thời gian tính toán: {end_time - start_time:.4f} giây")