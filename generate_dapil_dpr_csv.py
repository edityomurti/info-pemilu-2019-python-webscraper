import get_provinsi
import get_dapil_dpr

print ("====== START :: GENERATE DATA DAPIL DPR RI ======")

for data in get_provinsi.getData():
	get_dapil_dpr.generateCSV(str(data["idWilayah"]), data["namaWilayah"])

print ("======  END :: GENERATE DATA DAPIL DPR RI  ======")