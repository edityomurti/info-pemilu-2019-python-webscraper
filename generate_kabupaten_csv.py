import get_provinsi
import get_kabupaten

print ("====== START :: GENERATE DATA KABUPATEN ======")

for data in get_provinsi.getData():
	get_kabupaten.generateCSV(str(data["idWilayah"]), data["namaWilayah"])

print ("======  END :: GENERATE DATA KABUPATEN  ======")