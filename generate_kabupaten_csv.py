import get_provinsi
import get_kabupaten
from util_logging import *
from Constants import *

message_string = "====== START :: GENERATE DATA KABUPATEN ======"
print (message_string)
pecker(LOG_KABUPATEN_DATA, message_string)
total_data_generated = 0

for data in get_provinsi.getData():
	total_data_generated += get_kabupaten.generateCSV(str(data["idWilayah"]), data["namaWilayah"])

message_string = "====== END :: GENERATE DATA KABUPATEN,  {} data generated ======".format(str(total_data_generated))
print (message_string)
pecker(LOG_KABUPATEN_DATA, message_string)