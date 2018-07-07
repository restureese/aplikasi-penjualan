from Penjualan.login import Ui_FormLogin
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	form = QtWidgets.QMainWindow()
	ui = Ui_FormLogin()
	ui.setupUi(form)
	ui.center(form)
	form.show()
	sys.exit(app.exec_())
