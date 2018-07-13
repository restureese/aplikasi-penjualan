from PyQt5 import QtCore, QtGui, QtWidgets

from models import Barang, JenisBarang
from database import db_session
from jenisbarang import Ui_Dialog

class Ui_DialogBarang(object):
    def setupUi(self, DialogBarang):
        DialogBarang.setObjectName("DialogBarang")
        DialogBarang.resize(424, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogBarang.sizePolicy().hasHeightForWidth())
        DialogBarang.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogBarang.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogBarang)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnTambah = QtWidgets.QPushButton(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTambah.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/Knob-Add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTambah.setIcon(icon1)
        self.btnTambah.setObjectName("btnTambah")
        self.btnTambah.clicked.connect(self.tambahBarang)
        self.horizontalLayout.addWidget(self.btnTambah)
        self.btnEdit = QtWidgets.QPushButton(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEdit.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/Knob-Valid-Green-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout.addWidget(self.btnEdit)
        self.btnHapus = QtWidgets.QPushButton(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnHapus.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/Knob-Remove-Red-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHapus.setIcon(icon3)
        self.btnHapus.setObjectName("btnHapus")
        self.horizontalLayout.addWidget(self.btnHapus)
        self.btnKembali = QtWidgets.QPushButton(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnKembali.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/Knob-Left-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnKembali.setIcon(icon4)
        self.btnKembali.setObjectName("btnKembali")
        self.horizontalLayout.addWidget(self.btnKembali)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnTambahJenisBarang = QtWidgets.QToolButton(DialogBarang)
        self.btnTambahJenisBarang.setIcon(icon1)
        self.btnTambahJenisBarang.setIconSize(QtCore.QSize(24, 24))
        self.btnTambahJenisBarang.setObjectName("btnTambahJenisBarang")
        self.btnTambahJenisBarang.clicked.connect(self.tambahJenisBarang)
        self.gridLayout.addWidget(self.btnTambahJenisBarang, 2, 3, 1, 1)
        self.txtNamaBarang = QtWidgets.QLineEdit(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNamaBarang.setFont(font)
        self.txtNamaBarang.setObjectName("txtNamaBarang")
        self.gridLayout.addWidget(self.txtNamaBarang, 0, 2, 1, 2)
        self.txtSatuan = QtWidgets.QLineEdit(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSatuan.setFont(font)
        self.txtSatuan.setObjectName("txtSatuan")
        self.gridLayout.addWidget(self.txtSatuan, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.txtStok = QtWidgets.QLineEdit(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtStok.setFont(font)
        self.txtStok.setObjectName("txtStok")
        self.gridLayout.addWidget(self.txtStok, 10, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.txtHargaJual = QtWidgets.QLineEdit(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtHargaJual.setFont(font)
        self.txtHargaJual.setObjectName("txtHargaJual")
        self.gridLayout.addWidget(self.txtHargaJual, 8, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 7, 0, 1, 1)
        self.txtHargaBeli = QtWidgets.QLineEdit(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtHargaBeli.setFont(font)
        self.txtHargaBeli.setObjectName("txtHargaBeli")
        self.gridLayout.addWidget(self.txtHargaBeli, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.cbJenisBarang = QtWidgets.QComboBox(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbJenisBarang.setFont(font)
        self.cbJenisBarang.setObjectName("cbJenisBarang")
        self.cbJenisBarang.addItem("-Pilih Jenis Barang -")
        self.gridLayout.addWidget(self.cbJenisBarang, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(DialogBarang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.updateCBJenisBarang()

        self.retranslateUi(DialogBarang)
        QtCore.QMetaObject.connectSlotsByName(DialogBarang)

    def retranslateUi(self, DialogBarang):
        _translate = QtCore.QCoreApplication.translate
        DialogBarang.setWindowTitle(_translate("DialogBarang", "Form Barang"))
        self.btnTambah.setText(_translate("DialogBarang", "Tambah"))
        self.btnEdit.setText(_translate("DialogBarang", "Edit"))
        self.btnHapus.setText(_translate("DialogBarang", "Hapus"))
        self.btnKembali.setText(_translate("DialogBarang", "Kembali"))
        self.btnTambahJenisBarang.setText(_translate("DialogBarang", "..."))
        self.label_3.setText(_translate("DialogBarang", "Satuan"))
        self.label_6.setText(_translate("DialogBarang", "Stok"))
        self.label_2.setText(_translate("DialogBarang", "Jenis Barang"))
        self.label_4.setText(_translate("DialogBarang", "Harga Beli"))
        self.label_5.setText(_translate("DialogBarang", "Harga Jual"))
        self.label.setText(_translate("DialogBarang", "Nama Barang"))

    def tambahJenisBarang(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.ui.setCenter(self.Dialog)
        self.Dialog.show()
        DialogBarang.close()

    def updateCBJenisBarang(self):
        list_jenis_barang = JenisBarang.query.order_by(JenisBarang.nama).all()
        
        for jenis_barang in list_jenis_barang:
            self.cbJenisBarang.addItem(str(jenis_barang))
        

    def tambahBarang(self):
        nama = self.txtNamaBarang.text()
        jenis = JenisBarang.query.filter_by(nama=self.cbJenisBarang.text()).first()
        satuan = self.txtSatuan.text()
        harga_beli = self.txtHargaBeli.text()
        harga_jual = self.txtHargaJual.text()
        stok = self.txtStok.text()
        
        try:
            barang = Barang(nama=nama,jenis_barang=jenis.kode,satuan=satuan,harga_beli=harga_beli,harga_jual=harga_jual,stok=stok)
            db_session.add(barang)
            db_session.commit()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogBarang = QtWidgets.QDialog()
    ui = Ui_DialogBarang()
    ui.setupUi(DialogBarang)
    DialogBarang.show()
    sys.exit(app.exec_())

