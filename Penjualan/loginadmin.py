import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

from Penjualan.models import Akun
from Penjualan.database import db_session

from Penjualan.mainprogram import Ui_MainWindow

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Ui_DialogLogin(object):
    def __init__(self):
        self.DialogLogin = QtWidgets.QDialog()
        self.setupUi(self.DialogLogin)
        self.setCenter(self.DialogLogin)

    def setupUi(self, DialogLogin):
        DialogLogin.setObjectName("DialogLogin")
        DialogLogin.resize(332, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogLogin.sizePolicy().hasHeightForWidth())
        DialogLogin.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogLogin.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DialogLogin)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPassword.setFont(font)
        self.txtPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.txtPassword, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        self.txtUsername = QtWidgets.QLineEdit(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.txtUsername.setFocus()
        self.gridLayout.addWidget(self.txtUsername, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.login)
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnCancel = QtWidgets.QPushButton(DialogLogin)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(self.close)
        self.horizontalLayout.addWidget(self.btnCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)

    def retranslateUi(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "Form Login"))
        self.label.setText(_translate("DialogLogin", "Username"))
        self.label_2.setText(_translate("DialogLogin", "Password"))
        self.label_3.setText(_translate("DialogLogin", "LOGIN ADMINISTRATOR"))
        self.btnLogin.setText(_translate("DialogLogin", "Login"))
        self.btnCancel.setText(_translate("DialogLogin", "Batal"))

    def run(self):
        self.DialogLogin.exec()
        # sys.exit(self.app.exec())

    def setCenter(self,FormLogin):
        qr = FormLogin.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        FormLogin.move(qr.topLeft())

    def login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        user = Akun.query.filter_by(username=username).first()

        if user is None or not user.check_password(password=password):
            QMessageBox.critical(None, "Login Gagal","Username atau password salah !",QMessageBox.Cancel)
        else:
            form = QtWidgets.QMainWindow()
            main = Ui_MainWindow()
            main.run()
            self.DialogLogin.hide()

    def close(self):
        self.DialogLogin.close()