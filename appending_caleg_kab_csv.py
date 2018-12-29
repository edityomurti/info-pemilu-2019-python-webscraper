import get_dapil_kab
import get_caleg_kab
from util_logging import *
from Constants import *

def byKabupaten(ID_KAB, ID_PARTAI, ID_PRO):
	data_generated_by_dapil = 0
	for dataDapilKab in get_dapil_kab.getData(ID_KAB, 'NULL_appending', ID_PRO, 'NULL_appending'):
		data_generated_by_dapil += byDapil(str(dataDapilKab['id']), ID_PARTAI, ID_PRO)

	return data_generated_by_dapil

def byDapil(ID_DAPIL, ID_PARTAI, ID_PRO):

	data_generated = get_caleg_kab.generateCSV(ID_DAPIL, ID_PARTAI, ID_PRO)
	if data_generated == 0:
		message_string = "WARNING !!! 0 data in idPartai=({}), idPro=({}), idDapil=({}) ".format(ID_PARTAI, ID_PRO, ID_DAPIL)
		print (message_string)
		pecker(LOG_CALEG_KAB_DATA, message_string)

	return data_generated

TYPE_APPEND = input("1 - By idKab\n2 - By dapil\nEnter appending type : ")

if (TYPE_APPEND == '1'):
	print("APPENDING BY KABUPATEN")

	ID_KAB = input("Enter idKab = ")
	ID_PRO = input("Enter idProv = ")
	ID_PARTAI = input("Enter idPartai = ")

	message_string = "====== START :: APPENDING DATA CALEG DPRD KAB ––BY KABUPATEN: idKab={}, idPro={}, idPartai{} =====".format(ID_KAB, ID_PRO, ID_PARTAI)
	print(message_string)
	pecker(LOG_CALEG_KAB_DATA, message_string)

	total_data_generated = byKabupaten(ID_KAB, ID_PARTAI, ID_PRO)

	message_string = "======  END :: APPENDING DATA CALEG DPRD KAB ––BY KABUPATEN: idKab={},  {} data appended ======".format(ID_KAB, str(total_data_generated))
	print(message_string)
	pecker(LOG_CALEG_KAB_DATA, message_string)
elif (TYPE_APPEND == '2') :
	print("APPENDING BY DAPIL")

	ID_DAPIL = input("Enter idDapil = ")
	ID_PARTAI = input("Enter idPartai = ")
	ID_PRO = input("Enter idProv = ")

	message_string = "====== START :: APPENDING DATA CALEG DPRD KAB ––BY DAPIL: idDapil={}, idPro={}, idPartai{} =====".format(ID_DAPIL, ID_PRO, ID_PARTAI)
	print(message_string)
	pecker(LOG_CALEG_KAB_DATA, message_string)

	total_data_generated = byDapil(ID_DAPIL, ID_PARTAI, ID_PRO)

	message_string = "======  END :: APPENDING DATA CALEG DPRD KAB ––BY DAPIL: idDapil={},  {} data appended ======".format(ID_DAPIL, str(total_data_generated))
	print(message_string)
	pecker(LOG_CALEG_KAB_DATA, message_string)
else :
	print("WRONG INPUT, SMARTASS!")





