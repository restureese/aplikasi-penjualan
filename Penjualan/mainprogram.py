# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainProgram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 81))
        self.frame_6.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Pothana2000")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(276, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Navilu")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_5.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/log_out-2-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon)
        self.commandLinkButton_5.setIconSize(QtCore.QSize(32, 32))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.horizontalLayout.addWidget(self.commandLinkButton_5)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 4)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(257, 16777215))
        self.frame_3.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Navilu")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("color: rgb(211, 215, 207);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(32, 32))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Navilu")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setStyleSheet("color: rgb(211, 215, 207);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/icon-master-data-management.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon2)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(32, 32))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Navilu")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setStyleSheet("color: rgb(211, 215, 207);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/transaction.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(32, 32))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Navilu")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_4.setFont(font)
        self.commandLinkButton_4.setStyleSheet("\n"
"color: rgb(211, 215, 207);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join(BASE_DIR,"images/Utilities2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon4)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(32, 32))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.verticalLayout.addWidget(self.commandLinkButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 4, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setStyleSheet("background-color: rgb(251, 250, 250);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 130, 531, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.page_4)
        self.widget.setGeometry(QtCore.QRect(10, 90, 521, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.frame_4, 1, 1, 4, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PT RESTU REESE"))
        self.commandLinkButton_5.setText(_translate("MainWindow", " Logout"))
        self.commandLinkButton.setText(_translate("MainWindow", " Dashboard"))
        self.commandLinkButton_2.setText(_translate("MainWindow", " Master"))
        self.commandLinkButton_3.setText(_translate("MainWindow", " Transaksi"))
        self.commandLinkButton_4.setText(_translate("MainWindow", " Akun"))
        self.label_2.setText(_translate("MainWindow", "Dashboard"))
        self.label_3.setText(_translate("MainWindow", "Master"))
        self.label_4.setText(_translate("MainWindow", "Transaksi"))
        self.label_5.setText(_translate("MainWindow", "Akun"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))

    def center(self,Form):
        qr = Form.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        Form.move(qr.topLeft())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.center(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())