import json

class Provinsi:
	def __init__(self, id, idParent, namaWilayah, tingkatWilayah, idPro, idKab, idKec, idKel, namaPro, namaKab, namaKec, namaKel, kodeWilayah):
		self.id = id
		self.idParent = idParent
		self.namaWilayah = namaWilayah
		self.tingkatWilayah = tingkatWilayah
		self.idPro = idPro
		self.idKab = idKab
		self.idKec = idKel
		self.namaKab = namaKab
		self.namaKec = namaKel
		self.kodeWilayah = kodeWilayah