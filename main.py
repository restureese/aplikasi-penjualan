from Penjualan.loginadmin import Ui_DialogLogin
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	login = Ui_DialogLogin()
	login.run()
	sys.exit(app.exec_())
