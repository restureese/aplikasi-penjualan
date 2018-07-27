from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, update
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from random import randint

from Penjualan.database import Base

from sqlalchemy.sql import func



class Akun(Base):
	__tablename__ = 'akun'
	kode = Column(String(12),primary_key=True)
	nama = Column(String(128),nullable=False)
	telepon = Column(String(13),nullable=False)
	username = Column(String(128),nullable=False)
	password = Column(String(255),nullable=False)
	transaksi = relationship("Transaksi")

	def __init__(self,kode, nama, telepon, username, password):
		self.kode = kode
		self.nama = nama
		self.telepon = telepon
		self.username = username
		self.password = generate_password_hash(password)

	def __repr__(self):
		return self.nama

	def check_password(self,password):
		return check_password_hash(self.password,password)

class JenisBarang(Base):
	__tablename__ = 'jenis_barang'
	kode = Column(String(12),primary_key=True)
	nama = Column(String(128), nullable=False)
	barang = relationship("Barang")

	def __init__(self,kode,nama):
		self.kode = kode
		self.nama = nama

	def __repr__(self):
		return self.nama

class Barang(Base):
	__tablename__ = 'barang'
	kode = Column(String(13),primary_key=True)
	nama = Column(String(255),nullable=False)
	jenis_barang = Column(String(12), ForeignKey('jenis_barang.kode'))
	satuan = Column(String(64),nullable=False)
	harga_beli = Column(Integer,nullable=False)
	harga_jual = Column(Integer,nullable=False)
	stok = Column(Integer,nullable=False)
	detail_transaksi = relationship("DetailTransaksi")

	def getKode(self):
		return randint(100000000000,999999999999)

	def __init__(self, nama, jenis_barang, satuan, harga_beli, harga_jual, stok):
		self.kode = self.getKode()
		self.nama = nama
		self.jenis_barang = jenis_barang
		self.satuan = satuan
		self.harga_beli = harga_beli
		self.harga_jual = harga_jual
		self.stok = stok

	def __repr__(self):
		return self.nama

class Transaksi(Base):
	__tablename__ = 'transaksi'
	nota = Column(Integer,primary_key=True, autoincrement=True)
	kasir = Column(String(12),ForeignKey('akun.kode'))
	tanggal = Column(DateTime,default=func.now())
	detail_transaksi = relationship("DetailTransaksi")

	def __init__(self, kasir):
		self.kasir = kasir

	def __repr__(self):
		return self.nota

class DetailTransaksi(Base):
	__tablename__ = 'detail_transaksi'
	id = Column(Integer,primary_key=True, autoincrement=True)
	nota = Column(Integer,ForeignKey('transaksi.nota'))
	barang = Column(String(13), ForeignKey('barang.kode'))
	jumlah = Column(Integer,nullable=False)

	def __init__(self, nota, barang, jumlah):
		self.nota = nota
		self.barang = barang
		self.jumlah = jumlah
		self.minBarang()

	def minBarang(self):
		barang = Barang.query.filter_by(kode=self.barang).first()
		barang.stok = int(barang.stok) - self.jumlah
