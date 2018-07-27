import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

from werkzeug.security import generate_password_hash
from Penjualan.database import db_session
from Penjualan.models import Akun

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Ui_DialogAkun(object):
    def __init__(self):
        self.DialogAkun = QtWidgets.QDialog()
        
        self.setupUi(self.DialogAkun)
        self.setCenter(self.DialogAkun)

    def setupUi(self, DialogAkun):
        DialogAkun.setObjectName("DialogAkun")
        DialogAkun.resize(400, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAkun.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogAkun)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnTambah = QtWidgets.QPushButton(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTambah.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Knob-Add-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTambah.setIcon(icon1)
        self.btnTambah.setObjectName("btnTambah")
        self.btnTambah.clicked.connect(self.tambahAkun)
        self.horizontalLayout.addWidget(self.btnTambah)
        self.btnEdit = QtWidgets.QPushButton(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEdit.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Knob-Valid-Green-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setObjectName("btnEdit")
        self.btnEdit.clicked.connect(self.editAkun)
        self.horizontalLayout.addWidget(self.btnEdit)
        self.btnHapus = QtWidgets.QPushButton(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnHapus.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Knob-Remove-Red-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHapus.setIcon(icon3)
        self.btnHapus.setObjectName("btnHapus")
        self.btnHapus.clicked.connect(self.hapusAkun)
        self.horizontalLayout.addWidget(self.btnHapus)
        self.btnKembali = QtWidgets.QPushButton(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnKembali.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Knob-Left-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnKembali.setIcon(icon4)
        self.btnKembali.setObjectName("btnKembali")
        self.btnKembali.clicked.connect(DialogAkun.close)
        self.horizontalLayout.addWidget(self.btnKembali)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txtNamaLengkap = QtWidgets.QLineEdit(DialogAkun)
        self.txtNamaLengkap.setObjectName("txtNamaLengkap")
        self.gridLayout.addWidget(self.txtNamaLengkap, 2, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.txtTelepon = QtWidgets.QLineEdit(DialogAkun)
        self.txtTelepon.setObjectName("txtTelepon")
        self.gridLayout.addWidget(self.txtTelepon, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.txtUsername = QtWidgets.QLineEdit(DialogAkun)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 6, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(DialogAkun)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout.addWidget(self.txtPassword, 8, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(DialogAkun)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.txtKodeAkun = QtWidgets.QLineEdit(DialogAkun)
        self.txtKodeAkun.setObjectName("txtKodeAkun")
        self.gridLayout.addWidget(self.txtKodeAkun, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)

        self.retranslateUi(DialogAkun)
        QtCore.QMetaObject.connectSlotsByName(DialogAkun)

    def retranslateUi(self, DialogAkun):
        _translate = QtCore.QCoreApplication.translate
        DialogAkun.setWindowTitle(_translate("DialogAkun", "Form Akun"))
        self.btnTambah.setText(_translate("DialogAkun", "Tambah"))
        self.btnEdit.setText(_translate("DialogAkun", "Edit"))
        self.btnHapus.setText(_translate("DialogAkun", "Hapus"))
        self.btnKembali.setText(_translate("DialogAkun", "Kembali"))
        self.label.setText(_translate("DialogAkun", "Kode Akun"))
        self.label_3.setText(_translate("DialogAkun", "Telepon"))
        self.label_4.setText(_translate("DialogAkun", "Username"))
        self.label_2.setText(_translate("DialogAkun", "Nama Lengkap"))
        self.label_5.setText(_translate("DialogAkun", "Password"))

    def run(self):
        self.DialogAkun.exec()
        
    def setCenter(self,Form):
        qr = Form.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        Form.move(qr.topLeft())

    def tambahAkun(self):
        kode = self.txtKodeAkun.text()
        nama = self.txtNamaLengkap.text()
        telepon = self.txtTelepon.text()
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        try:
            akun = Akun(kode=kode, nama=nama, telepon=telepon, username=username, password=password)
            db_session.add(akun)
            db_session.commit()
            self.DialogAkun.close()
        except Exception as e:
            print(e)

    def editAkun(self):
        try:
            akun = Akun.query.filter_by(kode=self.txtKodeAkun.text()).first()
            akun.nama = self.txtNamaLengkap.text()
            akun.telepon = self.txtTelepon.text()
            akun.username = self.txtUsername.text()
            akun.password = generate_password_hash(self.txtPassword.text())
            db_session.commit()
            self.DialogAkun.close()
        except Exception as e:
            print(e)

    def hapusAkun(self):
        try:
            akun = Akun.query.filter_by(kode=self.txtKodeAkun.text()).first()
            db_session.delete(akun)
            db_session.commit()
            self.DialogAkun.close()
        except Exception as e:
            raise e

    def kembali(self):
        self.close()

    def tampilData(self):
        self.btnTambah.setEnabled(False)