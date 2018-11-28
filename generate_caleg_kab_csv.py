import get_provinsi
import get_kabupaten
import get_partai
import get_dapil_kab
import get_caleg_kab
from Constants import *
from util_logging import *

message_string = "====== START :: GENERATE DATA CALEG DPRD KAB ======"
print (message_string)
pecker(LOG_CALEG_KAB_DATA, message_string)

total_data_generated = 0

for dataPartai in get_partai.getData():
	for dataProv in get_provinsi.getData():
		for dataKab in get_kabupaten.getData(str(dataProv["idWilayah"]), dataProv["namaWilayah"]):
			for dataDapilKab in get_dapil_kab.getData(str(dataKab["idWilayah"]), dataKab["namaWilayah"], dataProv["namaWilayah"]):
				data_generated = get_caleg_kab.generateCSV(str(dataDapilKab["id"]), str(dataPartai["id"]), str(dataProv["idPro"]))
				if data_generated == 0:
					message_string = "WARNING !!! 0 data in idPartai=({}), idPro=({}), idKab=({}), idDapil=({}) ".format(str(dataPartai["id"]), str(dataProv["idPro"]), str(dataKab["idWilayah"]), str(dataDapilKab["id"]))
					print (message_string)
					pecker(LOG_CALEG_KAB_DATA, message_string)
				total_data_generated += data_generated

message_string = "======  END :: GENERATE DATA CALEG DPRD KAB,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_CALEG_KAB_DATA, message_string)