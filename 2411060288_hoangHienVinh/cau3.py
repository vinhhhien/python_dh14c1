
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

THU_MUC = Path(__file__).resolve().parent
FILE_SACH = THU_MUC / "sach.csv"
FILE_BIEU_DO = THU_MUC / "bieudo.png"
FILE_CANH_BAO = THU_MUC / "canh_bao_sach.csv"

CAC_COT = ["MaSach", "TenSach", "Gia", "SoLuong"]

def doc_sach(duong_dan=FILE_SACH):
    """Đọc file CSV và trả về list[dict] các cuốn sách."""
    danh_sach = []
    with open(duong_dan, "r", encoding="utf-8-sig", newline="") as file:
        for dong in csv.DictReader(file):
            danh_sach.append(
                {
                    "MaSach": dong["MaSach"].strip(),
                    "TenSach": dong["TenSach"].strip(),
                    "Gia": int(dong["Gia"]),
                    "SoLuong": int(dong["SoLuong"]),
                }
            )
    return danh_sach

def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f}".replace(",", ".") + "đ"


def in_thong_ke(danh_sach):
    tong_dau_sach = len(danh_sach)
    gia_trung_binh = sum(s["Gia"] for s in danh_sach) / tong_dau_sach
    sach_gia_cao_nhat = max(danh_sach, key=lambda s: s["Gia"])

    print("=" * 55)
    print("THỐNG KÊ KHO SÁCH")
    print("=" * 55)
    print(f"Tổng số đầu sách      : {tong_dau_sach}")
    print(f"Giá trung bình        : {dinh_dang_tien(gia_trung_binh)}")
    print(
        "Sách có giá cao nhất  : "
        f"{sach_gia_cao_nhat['TenSach']} "
        f"({sach_gia_cao_nhat['MaSach']}) - "
        f"{dinh_dang_tien(sach_gia_cao_nhat['Gia'])}"
    )
    print("=" * 55)

def ve_bieu_do(danh_sach, duong_dan=FILE_BIEU_DO):
    ten_sach = [s["TenSach"] for s in danh_sach]
    so_luong = [s["SoLuong"] for s in danh_sach]

    fig, ax = plt.subplots(figsize=(10, 6))
    cot = ax.bar(ten_sach, so_luong, color="#2e86c1", width=0.6)

    ax.set_title("Số lượng tồn kho của từng cuốn sách", fontsize=14, fontweight="bold")
    ax.set_xlabel("Tên sách", fontsize=11)
    ax.set_ylabel("Số lượng tồn kho", fontsize=11)
    ax.set_ylim(0, max(so_luong) * 1.15)
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)

    ax.bar_label(cot, padding=3, fontsize=10)

    plt.setp(ax.get_xticklabels(), rotation=20, ha="right", fontsize=9)
    fig.tight_layout()
    fig.savefig(duong_dan, dpi=150)
    plt.close(fig)

    print(f"\nĐã lưu biểu đồ vào file: {duong_dan.name}")

def loc_sach_sap_het(danh_sach, nguong=10):
    return [s for s in danh_sach if s["SoLuong"] < nguong]


def ghi_canh_bao(danh_sach_canh_bao, duong_dan=FILE_CANH_BAO):
    with open(duong_dan, "w", encoding="utf-8-sig", newline="") as file:
        ghi = csv.DictWriter(file, fieldnames=CAC_COT)
        ghi.writeheader()
        ghi.writerows(danh_sach_canh_bao)


def main():
    danh_sach = doc_sach()
    print(f"Đã đọc {len(danh_sach)} cuốn sách từ file {FILE_SACH.name}.\n")

    in_thong_ke(danh_sach)

    ve_bieu_do(danh_sach)
    danh_sach_canh_bao = loc_sach_sap_het(danh_sach)
    print(f"\nSÁCH SẮP HẾT (Số lượng < 10): {len(danh_sach_canh_bao)} cuốn")
    for sach in danh_sach_canh_bao:
        print(
            f"  {sach['MaSach']} - {sach['TenSach']} - SL: {sach['SoLuong']}"
        )

    ghi_canh_bao(danh_sach_canh_bao)
    print(f"Đã ghi danh sách cảnh báo vào file: {FILE_CANH_BAO.name}")


if __name__ == "__main__":
    main()
