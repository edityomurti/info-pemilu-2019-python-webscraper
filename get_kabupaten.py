import urllib.request
import json
import ssl
import csv
from Constants import *

def generateCSV(idWilayah, namaWilayah):
	context = ssl._create_unverified_context()

	link_url = BASE_URL + idWilayah + "/wilayah.json?"

	print("Request Daftar Kabupaten di Provinsi " + namaWilayah + "...")

	url = urllib.request.urlopen(link_url, context = context)
	data = json.loads(url.read().decode())

	# Generating CSV
	
	if (idWilayah == "1"):
		print("Generating CSV Daftar Kabupaten di Provinsi " + namaWilayah + "...")
		kabupaten_data = open(BASE_LOCAL_PATH + 'data_kabupaten.csv', 'w')
	else :
		print("Appending  CSV Daftar Kabupaten di Provinsi " + namaWilayah + "...")
		kabupaten_data = open(BASE_LOCAL_PATH + 'data_kabupaten.csv', 'a')

	csvwriter = csv.writer(kabupaten_data)

	count = 0

	for kabupaten in data:
		if count == 0 and idWilayah == "1":
			header = kabupaten.keys()
			csvwriter.writerow(header)
			count +=1

		csvwriter.writerow(kabupaten.values())

	kabupaten_data.close()

	message_string = "––– CSV Daftar Kabupaten di Provinsi " + namaWilayah + " created ({} data) –––".format(len(data))

	print(message_string)
	return