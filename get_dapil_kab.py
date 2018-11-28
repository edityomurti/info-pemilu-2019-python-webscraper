import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *

def getData(idKab, namaKab, namaPro):
	try:
		context = ssl._create_unverified_context()
		link_url = BASE_URL + idKab + "/dcs-kab.json?"

		print("Request Daftar DAPIL DPRD KAB di Provinsi " + namaPro + " , Kabupaten " + namaKab + "...")
		print(link_url)

		url = urllib.request.urlopen(link_url, context = context)
		data = json.loads(url.read().decode())
	except Exception as e:
		message_string = "ERROR Request idKab({}) -- {}".format(idKab, str(e))
		print(message_string)
		pecker(LOG_DAPIL_KAB_DATA, message_string)
		data = ""
	return data

def generateCSV(idKab, namaKab, idPro, namaPro):
	data = getData(idKab, namaKab, namaPro)

	# Generating CSV
	csv_file = BASE_LOCAL_PATH + 'data_dapil_kab.csv'
	status_data = ""
	if (idKab == "2"):
		print("GENERATING CSV DAPIL DPRD KAB di Provinsi " + namaPro + " , Kabupaten " + namaKab + "...")
		dapil_kab_data = open(csv_file, 'w')
		status_data = " -GENERATED"
	else :
		print("Appending CSV DAPIL DPRD KAB di Provinsi " + namaPro + " , Kabupaten " + namaKab + "...")
		dapil_kab_data = open(csv_file, 'a')
		status_data = " -appended"

	csvwriter = csv.writer(dapil_kab_data)

	count = 0

	headers = set([])

	if not (count != 0 and idKab != "2"):
		with open(csv_file, newline='') as f:
			reader = csv.reader(f)
			for row in reader:
				if count == 0:
					headers = row
					count += 1

	for dapil_kab in data:
		dapil_kab['idPro'] = idPro
		dapil_kab['idKab'] = idKab
		if count == 0 and idKab == "2":
			headers = dapil_kab.keys()
			csvwriter.writerow(headers)
			count += 1

		row_data = []
		for header in headers:
			if header in dapil_kab.keys():
				row_data.append(dapil_kab[header])
			else :
				row_data.append('null')
				message_string = "WARNING !!! - null found on keys=('{}') in idKab=({}), idPro=({}) ".format(header, idKab, idPro)
				print(message_string)
				pecker(LOG_DAPIL_KAB_DATA, message_string)
		csvwriter.writerow(row_data)

	dapil_kab_data.close()

	message_string = "––– CSV Daftar DAPIL DPRD KAB di Provinsi " + namaPro + " , Kabupaten " + namaKab + " " + status_data + " (" + str(len(data)) + " data) –––"

	print(message_string)
	pecker(LOG_DAPIL_KAB_DATA, message_string)
	return len(data)