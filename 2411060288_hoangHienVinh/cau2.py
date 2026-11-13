import tkinter as tk
from tkinter import ttk, messagebox


class QuanLySachApp:


    def __init__(self, root):
        self.root = root
        self.danh_sach = []
        self.root.title("Quản lý sách thư viện")
        self.root.geometry("780x680")
        self.root.minsize(700, 600)
        self.tao_giao_dien()

    def tao_giao_dien(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TEntry", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10))
        style.configure("TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure(
            "TieuDe.TLabel", font=("Segoe UI", 16, "bold"), foreground="#1f4e79"
        )


        khung_chinh = ttk.Frame(self.root, padding=12)
        khung_chinh.pack(fill="both", expand=True)
        khung_chinh.columnconfigure(0, weight=1)

        tieu_de = ttk.Label(
            khung_chinh,
            text="QUẢN LÝ SÁCH THƯ VIỆN",
            style="TieuDe.TLabel",
            anchor="center",
        )
        tieu_de.grid(row=0, column=0, pady=(0, 10))


        khung_form = ttk.LabelFrame(khung_chinh, text="Thông tin sách", padding=12)
        khung_form.grid(row=1, column=0, sticky="ew")
        khung_form.columnconfigure(1, weight=1)

        self.var_ma = tk.StringVar()
        self.var_ten = tk.StringVar()
        self.var_gia = tk.StringVar()
        self.var_so_luong = tk.StringVar()

        cac_o_nhap = [
            ("Mã sách:", self.var_ma),
            ("Tên sách:", self.var_ten),
            ("Giá:", self.var_gia),
            ("Số lượng:", self.var_so_luong),
        ]

        for hang, (nhan, bien) in enumerate(cac_o_nhap):
            ttk.Label(khung_form, text=nhan).grid(
                row=hang, column=0, sticky="w", padx=(0, 10), pady=5
            )
            o_nhap = ttk.Entry(khung_form, textvariable=bien, font=("Segoe UI", 10))
            o_nhap.grid(row=hang, column=1, sticky="ew", pady=5)
            if hang == 0:
                self.o_ma = o_nhap


        khung_nut = ttk.Frame(khung_form)
        khung_nut.grid(row=4, column=0, columnspan=2, sticky="e", pady=(8, 0))
        self.nut_them = tk.Button(
            khung_nut,
            text="Thêm sách",
            font=("Segoe UI", 10, "bold"),
            bg="#1f6feb",
            fg="white",
            activebackground="#1657b8",
            activeforeground="white",
            padx=18,
            pady=4,
            relief="groove",
            cursor="hand2",
            command=self.them_sach,
        )
        self.nut_them.pack(side="right")

        khung_tim = ttk.LabelFrame(khung_chinh, text="Tìm kiếm theo tên", padding=12)
        khung_tim.grid(row=2, column=0, sticky="ew", pady=10)
        khung_tim.columnconfigure(1, weight=1)

        ttk.Label(khung_tim, text="Từ khóa:").grid(
            row=0, column=0, sticky="w", padx=(0, 10)
        )
        self.var_tu_khoa = tk.StringVar()
        self.o_tu_khoa = ttk.Entry(
            khung_tim, textvariable=self.var_tu_khoa, font=("Segoe UI", 10)
        )
        self.o_tu_khoa.grid(row=0, column=1, sticky="ew")
        self.o_tu_khoa.bind("<Return>", lambda su_kien: self.tim_kiem())

        ttk.Button(khung_tim, text="Tìm kiếm", command=self.tim_kiem).grid(
            row=0, column=2, padx=(10, 0)
        )

        khung_ds = ttk.LabelFrame(
            khung_chinh, text="Danh sách sách", padding=10
        )
        khung_ds.grid(row=3, column=0, sticky="nsew")
        khung_chinh.rowconfigure(3, weight=1)
        khung_ds.rowconfigure(0, weight=1)
        khung_ds.columnconfigure(0, weight=1)

        thanh_cuon = ttk.Scrollbar(khung_ds, orient="vertical")
        self.listbox = tk.Listbox(
            khung_ds,
            font=("Consolas", 11),
            yscrollcommand=thanh_cuon.set,
            activestyle="none",
            selectbackground="#cfe2ff",
            selectforeground="#000000",
        )
        thanh_cuon.config(command=self.listbox.yview)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        thanh_cuon.grid(row=0, column=1, sticky="ns")

        # Dòng trạng thái
        self.var_trang_thai = tk.StringVar(value="Chưa có sách nào trong danh sách.")
        ttk.Label(
            khung_chinh, textvariable=self.var_trang_thai, foreground="#666666"
        ).grid(row=4, column=0, sticky="w", pady=(8, 0))

    @staticmethod
    def dinh_dang_sach(sach):
        """Trả về chuỗi hiển thị: S001 - Tên sách - 95000đ - SL: 40."""
        gia = f"{sach['Gia']:,.0f}".replace(",", ".")
        return (
            f"{sach['MaSach']} - {sach['TenSach']}"
            f" - {gia}đ - SL: {sach['SoLuong']}"
        )

    def xoa_form(self):
        self.var_ma.set("")
        self.var_ten.set("")
        self.var_gia.set("")
        self.var_so_luong.set("")
        self.o_ma.focus_set()

    def them_sach(self):
        """Lấy dữ liệu từ form, kiểm tra hợp lệ rồi thêm vào danh sách."""
        ma = self.var_ma.get().strip()
        ten = self.var_ten.get().strip()
        chuoi_gia = self.var_gia.get().strip()
        chuoi_so_luong = self.var_so_luong.get().strip()

        if not ma:
            messagebox.showerror("Lỗi dữ liệu", "Mã sách không được để trống!")
            self.o_ma.focus_set()
            return

        if not ten:
            messagebox.showerror("Lỗi dữ liệu", "Tên sách không được để trống!")
            return

        try:
            gia = float(chuoi_gia)
        except ValueError:
            messagebox.showerror(
                "Lỗi dữ liệu", "Giá phải là một số hợp lệ (ví dụ: 95000)!"
            )
            return

        if gia < 0:
            messagebox.showerror("Lỗi dữ liệu", "Giá phải lớn hơn hoặc bằng 0!")
            return

        try:
            so_luong = int(chuoi_so_luong)
        except ValueError:
            messagebox.showerror(
                "Lỗi dữ liệu", "Số lượng phải là một số nguyên hợp lệ (ví dụ: 40)!"
            )
            return

        if so_luong < 0:
            messagebox.showerror("Lỗi dữ liệu", "Số lượng phải lớn hơn hoặc bằng 0!")
            return

        sach = {
            "MaSach": ma,
            "TenSach": ten,
            "Gia": gia,
            "SoLuong": so_luong,
        }
        self.danh_sach.append(sach)
        self.listbox.insert(tk.END, self.dinh_dang_sach(sach))
        self.listbox.see(tk.END)

        self.var_trang_thai.set(
            f"Đã thêm sách {ma}. Tổng số sách trong danh sách: {len(self.danh_sach)}."
        )
        self.xoa_form()

    def tim_kiem(self):
        """Lọc sách theo tên, xóa kết quả cũ trước khi hiển thị kết quả mới."""
        tu_khoa = self.var_tu_khoa.get().strip().lower()

        self.listbox.delete(0, tk.END)

        if tu_khoa:
            ket_qua = [
                sach
                for sach in self.danh_sach
                if tu_khoa in sach["TenSach"].lower()
            ]
        else:
            ket_qua = list(self.danh_sach)

        for sach in ket_qua:
            self.listbox.insert(tk.END, self.dinh_dang_sach(sach))

        if not ket_qua:
            self.var_trang_thai.set(
                f"Không tìm thấy sách nào có tên chứa '{self.var_tu_khoa.get().strip()}'."
            )
        else:
            self.var_trang_thai.set(f"Tìm thấy {len(ket_qua)} cuốn sách.")


def main():
    root = tk.Tk()
    QuanLySachApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
