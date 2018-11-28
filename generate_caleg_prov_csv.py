import get_provinsi
import get_partai
import get_dapil_prov
import get_caleg_prov
from Constants import *
from util_logging import *

message_string = "====== START :: GENERATE DATA CALEG DPRD PROV ======"
print (message_string)
pecker(LOG_CALEG_PROV_DATA, message_string)

total_data_generated = 0

for dataPartai in get_partai.getData():
	for dataProv in get_provinsi.getData():
		for dataDapilProv in get_dapil_prov.getData(str(dataProv["idWilayah"]), dataProv["namaWilayah"]):
			data_generated = get_caleg_prov.generateCSV(str(dataDapilProv["id"]), str(dataPartai["id"]), str(dataProv["idPro"]))
			if data_generated == 0:
				message_string = "WARNING !!! 0 data in idPartai=({}), idPro=({}), idDapil=({}) ".format(str(dataPartai["id"]) , str(dataProv["idPro"]), str(dataDapilProv["id"]))
				print (message_string)
				pecker(LOG_CALEG_PROV_DATA, message_string)
			total_data_generated += data_generated

message_string = "======  END :: GENERATE DATA CALEG DPRD PROV,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_CALEG_PROV_DATA, message_string)