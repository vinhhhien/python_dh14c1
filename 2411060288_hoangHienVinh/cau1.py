
import sys

# Tránh lỗi UnicodeEncodeError khi in tiếng Việt trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": gia,
        "SoLuong": soluong,
    }
    danh_sach.append(sach)
    return sach


def tim_kiem_theo_ten(danh_sach, tu_khoa):
    tu_khoa = tu_khoa.strip().lower()
    if not tu_khoa:
        return []
    return [sach for sach in danh_sach if tu_khoa in sach["TenSach"].lower()]


def tong_gia_tri_kho_sach(danh_sach):
    return sum(sach["Gia"] * sach["SoLuong"] for sach in danh_sach)

def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f}".replace(",", ".") + "đ"


def in_danh_sach(danh_sach):
    if not danh_sach:
        print("  (Danh sách trống)")
        return

    print(f"  {'Mã sách':<10}{'Tên sách':<36}{'Giá':>12}{'Số lượng':>11}")
    print("  " + "-" * 68)
    for sach in danh_sach:
        print(
            f"  {sach['MaSach']:<10}"
            f"{sach['TenSach']:<36}"
            f"{dinh_dang_tien(sach['Gia']):>12}"
            f"{sach['SoLuong']:>11}"
        )


def nhap_chuoi(thong_bao):
    while True:
        gia_tri = input(thong_bao).strip()
        if gia_tri:
            return gia_tri
        print("  -> Giá trị không được để trống, vui lòng nhập lại!")


def nhap_so(thong_bao, la_so_nguyen=False):
    """Nhập một số hợp lệ, không âm. Trả về int hoặc float."""
    while True:
        gia_tri = input(thong_bao).strip()
        try:
            so = int(gia_tri) if la_so_nguyen else float(gia_tri)
        except ValueError:
            print("  -> Giá trị nhập vào không phải là số, vui lòng nhập lại!")
            continue
        if so < 0:
            print("  -> Giá trị phải lớn hơn hoặc bằng 0, vui lòng nhập lại!")
            continue
        return int(so) if la_so_nguyen else so


def hien_thi_menu():
    print("\n" + "=" * 45)
    print("      QUẢN LÝ SÁCH THƯ VIỆN")
    print("=" * 45)
    print("  1. Thêm sách")
    print("  2. Tìm kiếm theo tên")
    print("  3. Xem tổng giá trị kho sách")
    print("  4. Thoát chương trình")
    print("=" * 45)


def chuc_nang_them_sach(danh_sach):
    print("\n--- 1. THÊM SÁCH ---")
    ma = nhap_chuoi("  Mã sách   : ")
    ten = nhap_chuoi("  Tên sách  : ")
    gia = nhap_so("  Giá       : ")
    so_luong = nhap_so("  Số lượng  : ", la_so_nguyen=True)

    sach = them_sach(danh_sach, ma, ten, gia, so_luong)
    print(
        f"  => Đã thêm: {sach['MaSach']} - {sach['TenSach']}"
        f" - {dinh_dang_tien(sach['Gia'])} - SL: {sach['SoLuong']}"
    )


def chuc_nang_tim_kiem(danh_sach):
    print("\n--- 2. TÌM KIẾM THEO TÊN ---")
    tu_khoa = input("  Nhập từ khóa cần tìm: ").strip()

    ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
    if not ket_qua:
        print("  => Không tìm thấy sách nào phù hợp.")
        return

    print(f"  => Tìm thấy {len(ket_qua)} cuốn sách:")
    in_danh_sach(ket_qua)


def chuc_nang_tong_gia_tri(danh_sach):
    print("\n--- 3. TỔNG GIÁ TRỊ KHO SÁCH ---")
    print(f"  Số đầu sách          : {len(danh_sach)}")
    print(f"  Tổng giá trị kho sách: {dinh_dang_tien(tong_gia_tri_kho_sach(danh_sach))}")


def tao_du_lieu_mau():
    """Dữ liệu mẫu dùng để kiểm thử."""
    danh_sach = []
    them_sach(danh_sach, "S001", "Lập trình Python cơ bản", 95000, 40)
    them_sach(danh_sach, "S002", "Cấu trúc dữ liệu và giải thuật", 120000, 6)
    them_sach(danh_sach, "S003", "Nhập môn trí tuệ nhân tạo", 150000, 25)
    return danh_sach


def main():
    danh_sach = tao_du_lieu_mau()
    print("Đã nạp 3 cuốn sách mẫu. Danh sách hiện tại:")
    in_danh_sach(danh_sach)

    try:
        while True:
            hien_thi_menu()
            lua_chon = input("  Chọn chức năng (1-4): ").strip()

            if lua_chon == "1":
                chuc_nang_them_sach(danh_sach)
            elif lua_chon == "2":
                chuc_nang_tim_kiem(danh_sach)
            elif lua_chon == "3":
                chuc_nang_tong_gia_tri(danh_sach)
            elif lua_chon == "4":
                print("\n  Tạm biệt! Đã thoát chương trình.")
                break
            else:
                print("  -> Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4!")
    except (EOFError, KeyboardInterrupt):
        print("\n  Đã thoát chương trình.")


if __name__ == "__main__":
    main()
