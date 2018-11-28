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

		print("Request Caleg DPRD KAB di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		print(link_url)

		url = urllib.request.urlopen(link_url, context = context)
		data = json.loads(url.read().decode("utf-8","ignore"))
	except Exception as e:
		message_string = "ERROR !!! Request Caleg DPRD KAB di idDapil=({}), idPartai=({}), idPro=({}) -- {}".format(idDapil,idPartai,idPro,str(e))
		print(message_string)
		pecker(LOG_CALEG_KAB_DATA, message_string)
		data = ""
	return data


def generateCSV(idDapil, idPartai, idPro):
	data = getData(idDapil, idPartai, idPro)

	# Generating CSV
	csv_file = BASE_LOCAL_PATH + 'data_caleg_kab.csv'
	if (idDapil == "2724" and idPartai == "1"):
		print("GENERATING CSV Caleg DPRD KAB di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		caleg_kab_data = open(csv_file, 'w')
		status_data = " -GENERATED"
	else :
		print("Appending CSV Caleg DPRD KAB di Dapil=" + idDapil + " , Partai=" + idPartai + " ...")
		caleg_kab_data = open(csv_file, 'a')
		status_data = " -appended"

	csvwriter = csv.writer(caleg_kab_data)

	count = 0

	headers = set([])

	if not (count != 0 and idDapil != "2724" and idPartai != "1"):
		with open(csv_file, newline='') as f:
			reader = csv.reader(f)
			for row in reader:
				if count == 0:
					headers = row
					count += 1

	for caleg_kab in data:
		caleg_kab['idPartai'] = int(idPartai)
		caleg_kab['idDapil'] = int(idDapil)
		caleg_kab['idPro'] = int(idPro)
		if len(headers) == 0:
			headers = caleg_kab.keys()
			csvwriter.writerow(headers)
			count += 1	

		row_data = []
		for header in headers:
			if header in caleg_kab.keys():
				row_data.append(caleg_kab[header])
			else :
				row_data.append('null')
				message_string = "WARNING !!! - null found on keys=('{}') in idPartai=({}), idPro=({}, idDapil=({})) ".format(header, idPartai, idPro, idDapil)
				print(message_string)
				pecker(LOG_CALEG_KAB_DATA, message_string)
		csvwriter.writerow(row_data)

	caleg_kab_data.close()

	message_string = "––– CSV Daftar Caleg DPRD KAB di Dapil=" + idDapil + " , Partai=" + idPartai +  " {} ({} data) –––".format(status_data, len(data))

	print(message_string)
	pecker(LOG_CALEG_KAB_DATA, message_string)
	return len(data)