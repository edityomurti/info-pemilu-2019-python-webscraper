import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *

def getData(idWilayah, namaWilayah):
	try:
		context = ssl._create_unverified_context()
		link_url = BASE_URL + idWilayah + "/dcs-prov.json?"

		print("Request Daftar DAPIL DPRD PROV di Provinsi " + namaWilayah + "...")
		print(link_url)

		url = urllib.request.urlopen(link_url, context = context)
		data = json.loads(url.read().decode())
	except Exception as e:
		message_string = "ERROR Request idWilayah({}) -- {}".format(idWilayah, str(e))
		print(message_string)
		pecker(LOG_DAPIL_PROV_DATA, message_string)
		data = ""
	return data

def generateCSV(idWilayah, namaWilayah, idPro):
	data = getData(idWilayah, namaWilayah)
	
	# Generating CSV
	csv_file = 'data_dapil_prov.csv'
	if (idWilayah == "1"):
		print("GENERATING CSV DAPIL DPRD PROV di Provinsi " + namaWilayah + "...")
		dapil_dpr_data = open(BASE_LOCAL_PATH + csv_file, 'w')
	else :
		print("Appending  CSV DAPIL DPRD PROV Provinsi " + namaWilayah + "...")
		dapil_dpr_data = open(BASE_LOCAL_PATH + csv_file, 'a')

	csvwriter = csv.writer(dapil_dpr_data)

	count = 0

	for dapil_dpr in data:
		dapil_dpr['idPro'] = idPro
		if count == 0 and idWilayah == "1":
			header = dapil_dpr.keys()
			csvwriter.writerow(header)
			count += 1

		csvwriter.writerow(dapil_dpr.values())

	dapil_dpr_data.close()

	message_string = "––– CSV Daftar DAPIL DPRD PROV di Provinsi " + namaWilayah + " created ({} data) –––".format(len(data))

	print(message_string)
	pecker(LOG_DAPIL_PROV_DATA, message_string)
	return len(data)