import get_provinsi
import get_partai
import get_dapil_dpr
import get_caleg_dpr
from Constants import *
from util_logging import *

# CHANGE THIS PARAMETER
ID_DAPIL = "31"
ID_PARTAI = "12"
ID_PRO = "26141"

message_string = "====== START :: APPENDING DATA CALEG DPR RI ======"
print (message_string)
pecker(LOG_CALEG_DPR_DATA, message_string)

total_data_generated = 0

data_generated = get_caleg_dpr.generateCSV(ID_DAPIL, ID_PARTAI, ID_PRO)
if data_generated == 0:
	message_string = "WARNING !!! 0 data in idPartai=({}), idPro=({}), idDapil=({}) ".format(ID_PARTAI, ID_PRO, ID_DAPIL)
	print (message_string)
	pecker(LOG_CALEG_DPR_DATA, message_string)
total_data_generated += data_generated


message_string = "======  END :: APPENDING DATA CALEG DPR RI,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_CALEG_DPR_DATA, message_string)