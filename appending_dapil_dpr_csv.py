import get_provinsi
import get_dapil_dpr
from util_logging import *
from Constants import *

message_string = "====== START :: GENERATE DATA DAPIL DPR RI ======"
print (message_string)
pecker(LOG_DAPIL_DPR_DATA, message_string)

total_data_generated = 0

for data in get_provinsi.getData():
	total_data_generated += get_dapil_dpr.generateCSV(str(data["idWilayah"]), data["namaWilayah"], str(data["idPro"]))

message_string = "======  END :: GENERATE DATA DAPIL DPR RI,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_DAPIL_DPR_DATA, message_string)