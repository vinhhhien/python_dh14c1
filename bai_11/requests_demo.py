
import requests

# =========================================
# BAI 5.1: GOI API GITHUB
# =========================================

print("===== BAI 5.1: THONG TIN GITHUB =====")

try:
    response = requests.get(
        "https://api.github.com/repos/python/cpython",
        timeout=10
    )

    if response.status_code == 200:
        du_lieu = response.json()

        print("Ten repository:", du_lieu["full_name"])
        print("So luot gan sao (stars):",
              du_lieu["stargazers_count"])
        print("Ngon ngu chinh:", du_lieu["language"])
    else:
        print("Goi API that bai, ma loi:",
              response.status_code)

except requests.exceptions.RequestException as e:
    print("Loi ket noi GitHub:", e)


# =========================================
# BAI 5.2: LAY TY GIA USD/VND
# =========================================

print("\n===== BAI 5.2: TY GIA NGOAI TE =====")

try:
    response = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=10
    )

    if response.status_code == 200:
        du_lieu = response.json()

        if du_lieu.get("result") == "success":
            ty_gia_vnd = du_lieu["rates"]["VND"]

            print(f"1 USD = {ty_gia_vnd:,.0f} VND")
        else:
            print("API khong tra ve du lieu thanh cong.")
    else:
        print("Khong lay duoc ty gia, ma loi:",
              response.status_code)

except requests.exceptions.RequestException as e:
    print("Loi ket noi API ty gia:", e)
