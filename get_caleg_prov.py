# -*- coding: utf-8 -*-

import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *

def getData(idDapil, idPartai, idPro):
	try:
		context = ssl._create_unverified_context()

		link_url = BASE_URL + "pengajuan-calon/" + idDapil + "/" + idPartai +"/perubahan-dct.json?"

		print("Request Caleg DPRD PROV di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		print(link_url)

		url = urllib.request.urlopen(link_url, context = context)
		data = json.loads(url.read().decode("utf-8","ignore"))
	except Exception as e:
		message_string = "ERROR !!! Request Caleg DPRD PROV di idDapil=({}), idPartai=({}), idPro=({}) -- {}".format(idDapil,idPartai,idPro,str(e))
		print(message_string)
		pecker(LOG_CALEG_PROV_DATA, message_string)
		data = ""
	return data


def generateCSV(idDapil, idPartai, idPro):
	data = getData(idDapil, idPartai, idPro)

	# Generating CSV
	csv_file = 'data_caleg_prov.csv'
	if (idDapil == "1" and idPartai == "1"):
		print("GENERATING CSV Caleg DPRD PROV di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		caleg_dpr_data = open(BASE_LOCAL_PATH + csv_file, 'w')
		status_data = " -GENERATED"
	else :
		print("Appending CSV Caleg DPRD PROV di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		caleg_dpr_data = open(BASE_LOCAL_PATH + csv_file, 'a')
		status_data = " -appended"

	csvwriter = csv.writer(caleg_prov_data)

	count = 0

	headers = set([])

	if not (count != 0 and idDapil != "1" and idPartai != "1"):
		with open(BASE_LOCAL_PATH + csv_file, newline='') as f:
			reader = csv.reader(f)
			for row in reader:
				if count == 0:
					headers = row
					count += 1

	for caleg_prov in data:
		caleg_prov['idPartai'] = int(idPartai)
		caleg_prov['idDapil'] = int(idDapil)
		caleg_prov['idPro'] = int(idPro)
		if count == 0 and idDapil == "1" and idPartai == "1":
			headers = caleg_prov.keys()
			csvwriter.writerow(headers)
			count += 1			

		row_data = []
		for header in headers:
			if header in caleg_prov.keys():
				row_data.append(caleg_prov[header])
			else :
				row_data.append('null')
				message_string = "WARNING !!! - null found on keys=('{}') in idPartai=({}), idPro=({}, idDapil=({})) ".format(header, idPartai, idPro, idDapil)
				print(message_string)
				pecker(LOG_CALEG_PROV_DATA, message_string)
		csvwriter.writerow(row_data)

	caleg_prov_data.close()

	message_string = "––– CSV Daftar Caleg DPRD PROV di Dapil=" + idDapil + " , Partai=" + idPartai +  " {} ({} data) –––".format(status_data, len(data))

	print(message_string)
	pecker(LOG_CALEG_PROV_DATA, message_string)
	return len(data)