

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


from Penjualan.database import db_session
from Penjualan.models import Barang, Transaksi, DetailTransaksi
class Ui_Transaksi(object):

    def __init__(self):
        self.Transaksi = QtWidgets.QMainWindow()
        self.setupUi(self.Transaksi)
        self.setCenter(self.Transaksi)
        self.txtNamaAdmin.setText("ARG")

    def setupUi(self, Transaksi):
        Transaksi.setObjectName("Transaksi")
        Transaksi.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Transaksi.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Transaksi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 9, 1, 1)
        self.txtJumlahBarang = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtJumlahBarang.setFont(font)
        self.txtJumlahBarang.setObjectName("txtJumlahBarang")
        # self.txtJumlahBarang.keyPressEvent = self.keyPressJumlahBarang
        self.txtJumlahBarang.returnPressed.connect(self.tambahBarang)
        self.gridLayout.addWidget(self.txtJumlahBarang, 4, 7, 1, 1)
        self.txtHargaBarang = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtHargaBarang.setFont(font)
        self.txtHargaBarang.setObjectName("txtHargaBarang")
        self.txtHargaBarang.setEnabled(False)
        self.gridLayout.addWidget(self.txtHargaBarang, 1, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.txtUangKembali = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtUangKembali.setFont(font)
        self.txtUangKembali.setObjectName("txtUangKembali")
        self.txtUangKembali.setEnabled(False)
        self.gridLayout.addWidget(self.txtUangKembali, 9, 11, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 5, 1, 1)
        self.lblTotal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblTotal.setFont(font)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout.addWidget(self.lblTotal, 8, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 7, 7, 1, 1)
        self.txtNamaBarang = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNamaBarang.setFont(font)
        self.txtNamaBarang.setObjectName("txtNamaBarang")
        self.txtNamaBarang.setEnabled(False)
        self.gridLayout.addWidget(self.txtNamaBarang, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.txtUangDiterima = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtUangDiterima.setFont(font)
        self.txtUangDiterima.setObjectName("txtUangDiterima")
        self.txtUangDiterima.returnPressed.connect(self.bayar)
        self.gridLayout.addWidget(self.txtUangDiterima, 8, 11, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 10, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 7, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 8, 12, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 738, 274))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableBarang = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableBarang.setObjectName("tableBarang")
        self.tableBarang.setColumnCount(5)
        self.tableBarang.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableBarang.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableBarang.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableBarang.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableBarang.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableBarang.setHorizontalHeaderItem(4, item)
        header = self.tableBarang.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.gridLayout_2.addWidget(self.tableBarang, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 6, 1, 1, 11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 6, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 5, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 2, 1, 1)
        self.txtKodeBarang = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtKodeBarang.setFont(font)
        self.txtKodeBarang.setObjectName("txtKodeBarang")
        # valid = QtGui.QIntValidator(100000000,999999999)
        # self.txtKodeBarang.setValidator(valid)
        self.txtKodeBarang.setFocus()
        # self.txtKodeBarang.keyPressEvent = self.keyPressKodeBarang
        self.txtKodeBarang.returnPressed.connect(self.tampilBarang)
        self.gridLayout.addWidget(self.txtKodeBarang, 1, 3, 1, 1)
        self.txtNamaAdmin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtNamaAdmin.setFont(font)
        self.txtNamaAdmin.setObjectName("txtNamaAdmin")
        self.gridLayout.addWidget(self.txtNamaAdmin, 1, 11, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 12, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 8, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 10, 1, 1)
        Transaksi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Transaksi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        Transaksi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Transaksi)
        self.statusbar.setObjectName("statusbar")
        Transaksi.setStatusBar(self.statusbar)
        self.actionLogout = QtWidgets.QAction(Transaksi)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/log_out-2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogout.setIcon(icon1)
        self.actionLogout.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionLogout.setObjectName("actionLogout")
        self.menuHome.addAction(self.actionLogout)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(Transaksi)
        QtCore.QMetaObject.connectSlotsByName(Transaksi)

    def retranslateUi(self, Transaksi):
        _translate = QtCore.QCoreApplication.translate
        Transaksi.setWindowTitle(_translate("Transaksi", "Aplikasi Penjualan RESTU REESE"))
        self.label_8.setText(_translate("Transaksi", "Kasir"))
        self.label_3.setText(_translate("Transaksi", "Harga Barang"))
        self.label.setText(_translate("Transaksi", "Kode Barang"))
        self.label_4.setText(_translate("Transaksi", "Jumlah Barang"))
        self.lblTotal.setText(_translate("Transaksi", "Rp. 0,-"))
        self.label_7.setText(_translate("Transaksi", "Uang Kembali"))
        self.label_5.setText(_translate("Transaksi", "Uang Yang Ditema"))
        self.label_2.setText(_translate("Transaksi", "Nama Barang"))
        self.txtNamaAdmin.setText(_translate("Transaksi", "NamaKasir"))
        self.menuHome.setTitle(_translate("Transaksi", "Home"))
        self.actionLogout.setText(_translate("Transaksi", "Logout"))

        item = self.tableBarang.horizontalHeaderItem(0)
        item.setText(_translate("Transaksi", "Kode Barang"))
        item = self.tableBarang.horizontalHeaderItem(1)
        item.setText(_translate("Transaksi", "Nama Barang"))
        item = self.tableBarang.horizontalHeaderItem(2)
        item.setText(_translate("Transaksi", "Harga Barang"))
        item = self.tableBarang.horizontalHeaderItem(3)
        item.setText(_translate("Transaksi", "Jumlah Barang"))
        item = self.tableBarang.horizontalHeaderItem(4)
        item.setText(_translate("Transaksi", "Total"))

    def setCenter(self,FormLogin):
        qr = FormLogin.frameGeometry()

        # center point of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        FormLogin.move(qr.topLeft())

    def run(self):
        self.Transaksi.showMaximized()

    def _tambahbarang(self,kode,nama,harga,jumlah):
        baris = self.tableBarang.rowCount()
        self.tableBarang.setRowCount(baris+1)
        self.tableBarang.setItem(baris,0,QTableWidgetItem(kode))
        self.tableBarang.setItem(baris,1,QTableWidgetItem(nama))
        self.tableBarang.setItem(baris,2,QTableWidgetItem(harga))
        self.tableBarang.setItem(baris,3, QTableWidgetItem(jumlah))
        self.tableBarang.setItem(baris,4,QTableWidgetItem(str(int(harga)*int(jumlah))))

    def hapus(self):
        self.txtKodeBarang.clear()
        self.txtNamaBarang.clear()
        self.txtHargaBarang.clear()
        self.txtJumlahBarang.clear()

    def getTotal(self):

        baris = self.tableBarang.rowCount()
        total = 0

        for i in range(baris):
            total = total + int(self.tableBarang.item(i,4).text())

        return total

    def tambahBarang(self):
        try:
            kode = self.txtKodeBarang.text()
            nama = self.txtNamaBarang.text()
            harga = self.txtHargaBarang.text()
            jumlah = self.txtJumlahBarang.text()

            self._tambahbarang(kode,nama,harga,jumlah)
            self.hapus()
            
            self.txtKodeBarang.setFocus()
            self.lblTotal.setText("Rp. {0}".format(self.getTotal()))
        except Exception as e:
            print(e)

    def tampilBarang(self):
        try:
            barang = Barang.query.filter_by(kode=self.txtKodeBarang.text()).first()
            self.txtNamaBarang.setText(barang.nama)
            self.txtHargaBarang.setText(str(barang.harga_jual))
            self.txtJumlahBarang.setFocus()
        except Exception as e:
            print(e)

    def _tambahTransaksi(self, nota):
        banyakBarang = self.tableBarang.rowCount()

        for barang in range(banyakBarang):
            namaBarang = self.tableBarang.item(barang, 0).text()
            jumlah = int(self.tableBarang.item(barang, 3).text())

            try:
                item = DetailTransaksi(nota,namaBarang,jumlah)
                db_session.add(item)
                db_session.commit()
            except Exception as e:
                db_session.rollback()
                print(e)

    def tambahTransaksi(self):
        
        try:
            kasir = self.txtNamaAdmin.text()
            transaksi = Transaksi(kasir)
            db_session.add(transaksi)
            db_session.commit()
            self._tambahTransaksi(transaksi.nota)
        except Exception as e:
            db_session.rollback()
            print(e)

    def init(self):
        self.tableBarang.clear()
        self.tableBarang.setRowCount(0)
        self.lblTotal.setText("Rp. 0")
        self.txtUangDiterima.setText("")
        self.txtUangKembali.setText("")

    def bayar(self):
        uang = int(self.txtUangDiterima.text())
        total = self.getTotal()

        if uang >= total:
            self.txtUangKembali.setText(str(uang-total))
            self.tambahTransaksi()
            self.init()
            self.txtKodeBarang.setFocus()