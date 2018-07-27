from Penjualan.transaksi import Ui_Transaksi
from PyQt5 import QtWidgets


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	login = Ui_Transaksi()
	login.run()
	sys.exit(app.exec_())