import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
)

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May tinh bo tui - PyQt")
        self.resize(300, 400)
        self.khoi_tao_giao_dien()
        
    def khoi_tao_giao_dien(self):
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setStyleSheet("font-size: 24px; padding: 10px; background: #f0f0f0;")
        
        nut_grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]
        
        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("font-size: 18px; padding: 15px;")
            if text == '=':
                btn.clicked.connect(self.tinh_ket_qua)
            elif text == 'C':
                btn.clicked.connect(self.xoa_man_hinh)
            else:
                btn.clicked.connect(lambda checked, t=text: self.them_ky_tu(t))
                
            if text == 'C':
                nut_grid.addWidget(btn, row, col, 1, 4)
            else:
                nut_grid.addWidget(btn, row, col)
                
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.man_hinh)
        layout_chinh.addLayout(nut_grid)
        self.setLayout(layout_chinh)
        
    def them_ky_tu(self, ky_tu):
        hien_tai = self.man_hinh.text()
        self.man_hinh.setText(hien_tai + ky_tu)
        
    def xoa_man_hinh(self):
        self.man_hinh.clear()
        
    def tinh_ket_qua(self):
        try:
            bieu_thuc = self.man_hinh.text()
            ket_qua = str(eval(bieu_thuc))
            self.man_hinh.setText(ket_qua)
        except Exception:
            self.man_hinh.setText("Loi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())