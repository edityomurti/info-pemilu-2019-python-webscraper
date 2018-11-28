import get_provinsi
import get_kabupaten
import get_dapil_kab
from util_logging import *
from Constants import *

message_string = "====== START :: GENERATE DATA DAPIL DPRD KAB ======"
print(message_string)
pecker(LOG_DAPIL_KAB_DATA, message_string)

total_data_generated = 0

for dataProv in get_provinsi.getData():
	for dataKab in get_kabupaten.getData(str(dataProv['idWilayah']), dataProv['namaWilayah'] ):
		data_generated = get_dapil_kab.generateCSV(str(dataKab['idWilayah']), dataKab['namaWilayah'], str(dataProv['idWilayah']), dataProv['namaWilayah'])
		if data_generated == 0:
			message_string = "WARNING !!! 0 data in idKab=({}), idPro=({})".format(str(dataKab['idWilayah']), str(dataProv['idWilayah']))
			print(message_string)
			pecker(LOG_DAPIL_KAB_DATA, message_string)
		total_data_generated += data_generated

message_string = "======  END :: GENERATE DATA DAPIL DPRD KAB,  {} data generated ======".format(str(total_data_generated))
print(message_string)
pecker(LOG_DAPIL_KAB_DATA, message_string)