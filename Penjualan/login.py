from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import *
import sys

from Penjualan.models import Akun
from Penjualan.mainprogram import Ui_MainWindow

class Ui_FormLogin(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.FormLogin = QtWidgets.QMainWindow()
        self.setupUi(self.FormLogin)
        self.setCenter(self.FormLogin)

    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(400, 314)
        self.centralwidget = QtWidgets.QWidget(FormLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 111, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 70, 211, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.verticalLayout_2.addWidget(self.txtUsername)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.txtPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        self.verticalLayout_2.addWidget(self.txtPassword)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 170, 211, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.on_click)
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnClose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        FormLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        FormLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormLogin)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('Form Login')
        FormLogin.setStatusBar(self.statusbar)
        



        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Aplikasi Penjualan"))
        self.label.setText(_translate("FormLogin", "Username"))
        self.label_2.setText(_translate("FormLogin", "Password"))
        self.btnLogin.setText(_translate("FormLogin", "Login"))
        self.btnClose.setText(_translate("FormLogin", "Close"))
        self.label_3.setText(_translate("FormLogin", "LOGIN ADMINISTRATOR"))

    def run(self):
        self.FormLogin.show()
        sys.exit(self.app.exec())

    def setCenter(self,FormLogin):
        qr = FormLogin.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        FormLogin.move(qr.topLeft())

    #@pyqtSlot()
    def on_click(self,form):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        user = Akun.query.filter_by(username=username).first()
        print(user)
        if user is None or not user.check_password(password=password):
            QMessageBox.critical(None, "Login Gagal","Username atau password salah !",QMessageBox.Cancel)
        else:
            form = QtWidgets.QMainWindow()
            main = Ui_MainWindow()
            main.run()
            # self.ui.setupUi(self.form)
            # self.ui.setCenter(self.form)
            
            # self.form.show()