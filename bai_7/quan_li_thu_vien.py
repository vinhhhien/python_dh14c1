# quan_ly_thu_vien.py

# ---------------------------------------------------------
# BƯỚC 1: KHAI BÁO DỮ LIỆU BAN ĐẦU
# ---------------------------------------------------------
danh_sach_sach = [
    {"ma_sach": "S01", "ten_sach": "Lap trinh Python", "tac_gia": "Nguyen Van A", "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S02", "ten_sach": "Cau truc du lieu", "tac_gia": "Tran Thi B", "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S03", "ten_sach": "Giai thuat ung dung", "tac_gia": "Le Van C", "trang_thai": "Da muon", "nguoi_muon": "Pham Van D"},
]

lich_su_phat = []


# ---------------------------------------------------------
# BƯỚC 2: HÀM TÌM KIẾM & HIỂN THỊ DỮ LIỆU
# ---------------------------------------------------------
def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach
    return None


def hien_thi_danh_sach_sach():
    print("\n" + "=" * 75)
    print(f"{'Ma sach':<10}{'Ten sach':<25}{'Tac gia':<18}{'Trang thai':<12}{'Nguoi muon':<15}")
    print("-" * 75)
    for sach in danh_sach_sach:
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<25}{sach['tac_gia']:<18}"
              f"{sach['trang_thai']:<12}{sach['nguoi_muon']:<15}")
    print("=" * 75)


def xem_sach_co_san():
    ds_co_san = [sach for sach in danh_sach_sach if sach["trang_thai"] == "Co san"]
    if len(ds_co_san) == 0:
        print("-> Hien tai tat ca sach deu da duoc muon.")
        return
    print("\nCAC SACH DANG CO SAN TRONG THU VIEN:")
    for sach in ds_co_san:
        print(f"  {sach['ma_sach']} - {sach['ten_sach']} - Tac gia: {sach['tac_gia']}")


# ---------------------------------------------------------
# BƯỚC 3: HÀM THÊM, MƯỢN, TRẢ SÁCH
# ---------------------------------------------------------
def them_sach(ma_sach, ten_sach, tac_gia):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    })
    print(f"-> Da them sach {ten_sach} ({ma_sach}) thanh cong.")


def muon_sach(ma_sach, nguoi_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return
    if sach["trang_thai"] == "Da muon":
        print(f"-> Sach {ma_sach} dang duoc mượn boi {sach['nguoi_muon']}, khong the mượn.")
        return
    sach["trang_thai"] = "Da muon"
    sach["nguoi_muon"] = nguoi_muon
    print(f"-> Cho doc gia {nguoi_muon} muon sach {sach['ten_sach']} thanh cong.")


def tra_sach(ma_sach, so_ngay_tre):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return
    if sach["trang_thai"] == "Co san":
        print(f"-> Sach {ma_sach} dang o trong kho, khong co ai mượn de tra.")
        return
    
    # Đơn giá phạt: 5.000 VNĐ / ngày trễ
    DON_GIA_PHAT = 5000
    tien_phat = so_ngay_tre * DON_GIA_PHAT
    ten_nguoi_muon = sach["nguoi_muon"]
    
    if tien_phat > 0:
        lich_su_phat.append({
            "ma_sach": ma_sach,
            "ten_sach": sach["ten_sach"],
            "nguoi_muon": ten_nguoi_muon,
            "so_ngay_tre": so_ngay_tre,
            "tien_phat": tien_phat
        })
        print(f"-> Doc gia {ten_nguoi_muon} tra sach {ma_sach} tre {so_ngay_tre} ngay.")
        print(f"-> Tien phat vi pham: {tien_phat:,} VND")
    else:
        print(f"-> Doc gia {ten_nguoi_muon} tra sach {ma_sach} dung han.")
        
    sach["trang_thai"] = "Co san"
    sach["nguoi_muon"] = ""


# ---------------------------------------------------------
# BƯỚC 4: HÀM THỐNG KÊ & HÀM NHẬP SỐ NGUYÊN AN TOÀN (TRY-EXCEPT)
# ---------------------------------------------------------
def thong_ke_phat():
    if len(lich_su_phat) == 0:
        print("-> Chua co ghi nhan vi pham tra tre nao.")
        return
    tong_tien_phat = 0
    print("\nLICH SU THU TIEN PHAT:")
    for ls in lich_su_phat:
        print(f"  {ls['ma_sach']} - {ls['ten_sach']} - Nguoi tra: {ls['nguoi_muon']} "
              f"- Tre: {ls['so_ngay_tre']} ngay - Phat: {ls['tien_phat']:,} VND")
        tong_tien_phat += ls["tien_phat"]
    print(f"\n>>> TONG TIEN PHAT THU DUOC: {tong_tien_phat:,} VND")


def nhap_so_nguyen(loi_nhac):
    """Sử dụng try-except kết hợp while để bắt lỗi nhập dữ liệu không phải số nguyên"""
    while True:
        try:
            val = int(input(loi_nhac))
            if val >= 0:
                return val
            print("-> Gia tri khong duoc am, vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


# ---------------------------------------------------------
# BƯỚC 5: MENU CHÍNH & VÒNG LẶP CHƯƠNG TRÌNH
# ---------------------------------------------------------
def hien_thi_menu():
    print("\n===== QUAN LY THU VIEN MUON / TRA SACH =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang co san")
    print("3. Them sach moi")
    print("4. Muon sach")
    print("5. Tra sach & Tinh tien phat")
    print("6. Thong ke tien phat")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_sach()
        elif lua_chon == "2":
            xem_sach_co_san()
        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi: ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            tac_gia = input("Nhap ten tac gia: ").strip().title()
            them_sach(ma_sach, ten_sach, tac_gia)
        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
            muon_sach(ma_sach, nguoi_muon)
        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay_tre = nhap_so_nguyen("Nhap so ngay tra tre (0 neu dung han): ")
            tra_sach(ma_sach, so_ngay_tre)
        elif lua_chon == "6":
            thong_ke_phat()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()