import get_provinsi
import get_partai
import get_dapil_dpr
import get_caleg_dpr
from Constants import *
from util_logging import *

message_string = "====== START :: GENERATE DATA CALEG DPR RI ======"
print (message_string)
pecker(LOG_CALEG_DPR_DATA, message_string)

total_data_generated = 0

for dataPartai in get_partai.getData():
	for dataProv in get_provinsi.getData():
		for dataDapilDpr in get_dapil_dpr.getData(str(dataProv["idWilayah"]), dataProv["namaWilayah"]):
			data_generated = get_caleg_dpr.generateCSV(str(dataDapilDpr["id"]), str(dataPartai["id"]), str(dataProv["idPro"]))
			if data_generated == 0:
				message_string = "WARNING !!! 0 data in idPartai=({}), idPro=({}), idDapil=({}) ".format(str(dataDapilDpr["id"]), str(dataPartai["id"]), str(dataProv["idPro"]))
				print (message_string)
				pecker(LOG_CALEG_DPR_DATA, message_string)
			total_data_generated += data_generated

message_string = "======  END :: GENERATE DATA CALEG DPR RI,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_CALEG_DPR_DATA, message_string)