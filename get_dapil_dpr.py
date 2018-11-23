import urllib.request
import json
import ssl
import csv
from Constants import *

def generateCSV(idWilayah, namaWilayah):
	context = ssl._create_unverified_context()

	link_url = BASE_URL + idWilayah + "/dcs-dpr.json?"

	print("Request Daftar DAPIL DPR RI di Provinsi " + namaWilayah + "...")

	url = urllib.request.urlopen(link_url, context = context)
	data = json.loads(url.read().decode())

	# Generating CSV

	if (idWilayah == "1"):
		print("GENERATING CSV DAPIL DPR RI di Provinsi " + namaWilayah + "...")
		dapil_dpr_data = open(BASE_LOCAL_PATH + 'data_dapil_dpr.csv', 'w')
	else :
		print("Appending  CSV DAPIL DPR RI di Provinsi " + namaWilayah + "...")
		dapil_dpr_data = open(BASE_LOCAL_PATH + 'data_dapil_dpr.csv', 'a')

	csvwriter = csv.writer(dapil_dpr_data)

	count = 0

	for dapil_dpr in data:
		if count == 0 and idWilayah == "1":
			header = dapil_dpr.keys()
			csvwriter.writerow(header)
			count += 1

		csvwriter.writerow(dapil_dpr.values())

	dapil_dpr_data.close()

	message_string = "––– CSV Daftar DAPIL DPR RI di Provinsi " + namaWilayah + " created ({} data) –––".format(len(data))

	print(message_string)
	return