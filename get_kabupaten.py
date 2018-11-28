import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *

def getData(idWilayah, namaWilayah):
	context = ssl._create_unverified_context()

	link_url = BASE_URL + idWilayah + "/wilayah.json?"
	
	print("Request Daftar Kabupaten di Provinsi " + namaWilayah + "...")
	print(link_url)

	try :
		url = urllib.request.urlopen(link_url, context = context)
		data = json.loads(url.read().decode())
	except Exception as e:
		message_string = 'ERROR !!! Request Daftar Kabupaten idWilayah(' + idWilayah + ') -- ' + str(e)
		print(message_string)
		pecker(LOG_DAPIL_DPR_DATA, message_string)
		data = ""

	return data

def generateCSV(idWilayah, namaWilayah):
	data = getData(idWilayah, namaWilayah)

	# Generating CSV
	csv_file = 'data_kabupaten.csv'
	if (idWilayah == "1"):
		message_string = "GENERATING CSV Daftar Kabupaten di Provinsi " + namaWilayah + "..."
		print(message_string)
		kabupaten_data = open(BASE_LOCAL_PATH + csv_file, 'w')
		status_data = " -GENERATED"
	else :
		message_string = "Appending  CSV Daftar Kabupaten di Provinsi " + namaWilayah + "..."
		print(message_string)
		kabupaten_data = open(BASE_LOCAL_PATH + csv_file, 'a')
		status_data = " -appended"

	csvwriter = csv.writer(kabupaten_data)

	count = 0

	for kabupaten in data:
		if count == 0 and idWilayah == "1":
			header = kabupaten.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(kabupaten.values())

	kabupaten_data.close()

	message_string = "––– CSV Daftar Kabupaten di Provinsi " + namaWilayah + " {} ({} data) –––".format(status_data, len(data))

	print(message_string)
	pecker(LOG_KABUPATEN_DATA, message_string)
	return len(data)