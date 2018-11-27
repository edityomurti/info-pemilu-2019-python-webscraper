import get_provinsi
import get_dapil_prov
from util_logging import *
from Constants import *

message_string = "====== START :: GENERATE DATA DAPIL DPRD PROV ======"
print (message_string)
pecker(LOG_DAPIL_DPR_DATA, message_string)

total_data_generated = 0

for data in get_provinsi.getData():
	total_data_generated += get_dapil_prov.generateCSV(str(data["idWilayah"]), data["namaWilayah"], str(data["idPro"]))

message_string = "======  END :: GENERATE DATA DAPIL DPD PROV ,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_DAPIL_DPR_DATA, message_string)