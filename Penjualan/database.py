from PyQt5.QtSql import *
from PyQt5.QtWidgets import QMessageBox
class Database(object):

	def db_connect(self):
	    db = QSqlDatabase.addDatabase('QMYSQL')
	    db.setHostName('localhost')
	    db.setDatabaseName('toko')
	    db.setUserName('restu')
	    db.open()
	    if not db.open():
	        # QMessageBox.critical(None, "Cannot open database",
	        #         "Unable to establish a database connection.\n"
	        #         "This example needs SQLite support. Please read the Qt SQL "
	        #         "driver documentation for information how to build it.\n\n"
	        #         "Click Cancel to exit.", QMessageBox.Cancel)
	        print('gagal')
	        return False
	    return True


	def login(self, query):
		sql = QSqlQuery()
		return sql.exec_(query)
		
db = Database()
db.db_connect()
db.open()
username = 'restureese'
passsword = 'masrestu'
query = 'select * from akun where username='+username+' and passsword='+passsword+';'

print(db.login(query))