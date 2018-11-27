# -*- coding: utf-8 -*-

import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *

def getData(idDapil, idPartai):
	try:
		context = ssl._create_unverified_context()

		link_url = BASE_URL + "pengajuan-calon/" + idDapil + "/" + idPartai +"/perubahan-dct.json?"

		print("Request Caleg DPR RI di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		print(link_url)

		url = urllib.request.urlopen(link_url, context = context)
		data = json.loads(url.read().decode())
	except Exception as e:
		message_string = "ERROR Request Caleg DPR RI di idDapil=({}), idPartai=({}) -- {}".format(idDapil,idPartai,str(e))
		print(message_string)
		pecker(LOG_CALEG_DPR_DATA, message_string)
		data = ""
	return data


def generateCSV(idDapil, idPartai, idPro):
	data = getData(idDapil, idPartai)

	# Generating CSV

	csv_file = 'data_caleg_dpr_ri.csv'
	if (idDapil == "1" and idPartai == "1"):
		print("GENERATING CSV Caleg DPR RI di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		caleg_dpr_data = open(BASE_LOCAL_PATH + csv_file, 'w')
		status_data = " -GENERATED"
	else :
		print("Appending CSV Caleg DPR RI di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		caleg_dpr_data = open(BASE_LOCAL_PATH + csv_file, 'a')
		status_data = " -appended"

	csvwriter = csv.writer(caleg_dpr_data)

	count = 0

	headers = set([])

	if not (count != 0 and idDapil != "1" and idPartai != "1"):
		with open(BASE_LOCAL_PATH + csv_file, newline='') as f:
			reader = csv.reader(f)
			for row in reader:
				if count == 0:
					headers = row
					count += 1

	for caleg_dpr in data:
		caleg_dpr['idPartai'] = int(idPartai)
		caleg_dpr['idDapil'] = int(idDapil)
		caleg_dpr['idPro'] = int(idPro)
		if count == 0 and idDapil == "1" and idPartai == "1":
			headers = caleg_dpr.keys()
			csvwriter.writerow(headers)
			count += 1			

		row_data = []
		for header in headers:
			if header in caleg_dpr.keys():
				row_data.append(caleg_dpr[header])
			else :
				row_data.append('null')
				message_string = "WARNING !!! - null found on keys=('{}') in idPartai=({}), idDapil=({}), idPro=({}) ".format(header, idPartai, idDapil, idPro)
				print(message_string)
				pecker(LOG_CALEG_DPR_DATA, message_string)
		csvwriter.writerow(row_data)

	caleg_dpr_data.close()

	message_string = "––– CSV Daftar Caleg DPR RI di Dapil=" + idDapil + " , Partai=" + idPartai +  " {} ({} data) –––".format(status_data, len(data))

	print(message_string)
	pecker(LOG_CALEG_DPR_DATA, message_string)
	return len(data)