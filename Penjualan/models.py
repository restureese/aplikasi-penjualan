from sqlalchemy import Column, Integer, String
from Penjualan.database import Base



class User(Base):
	__tablename__ = 'users'
	username = Column(String(128),primary_key=True)
	password = Column(String(255))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return self.username

	def check_password(self,password):
		return self.password is password
