import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

from Penjualan.models import JenisBarang
from Penjualan.database import db_session

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Ui_Dialog(object):

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.setCenter(self.Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtKode = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtKode.setFont(font)
        self.txtKode.setObjectName("txtKode")
        self.gridLayout.addWidget(self.txtKode, 0, 1, 1, 1)
        self.txtNama = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNama.setFont(font)
        self.txtNama.setObjectName("txtNama")
        self.gridLayout.addWidget(self.txtNama, 1, 1, 1, 3)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.btnSimpan = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSimpan.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Knob-Add-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSimpan.setIcon(icon1)
        self.btnSimpan.setObjectName("btnSimpan")
        self.btnSimpan.clicked.connect(self.simpan)
        self.gridLayout.addWidget(self.btnSimpan, 0, 5, 1, 1)
        self.btnKembali = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnKembali.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Knob-Left-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnKembali.setIcon(icon2)
        self.btnKembali.setObjectName("btnKembali")
        self.btnKembali.clicked.connect(self.kembali)
        self.gridLayout.addWidget(self.btnKembali, 1, 5, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Form Jenis Barang"))
        self.label_2.setText(_translate("Dialog", "Nama"))
        self.label.setText(_translate("Dialog", "Kode"))
        self.btnSimpan.setText(_translate("Dialog", "Simpan"))
        self.btnKembali.setText(_translate("Dialog", "Kembali"))

    def setCenter(self,Form):
        qr = Form.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        Form.move(qr.topLeft())

    def simpan(self):
        from Penjualan.barang import Ui_DialogBarang
        kode = self.txtKode.text()
        nama = self.txtNama.text()
        formbarang = Ui_DialogBarang()
        try:
            jenis_barang = JenisBarang(kode=kode,nama=nama)
            db_session.add(jenis_barang)
            db_session.commit()
            self.Dialog.close()
        except Exception as e:
            print(e)

    def run(self):
        self.Dialog.exec()

    def kembali(self):
        self.Dialog.close()