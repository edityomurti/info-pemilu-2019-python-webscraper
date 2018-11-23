import urllib.request
import json
import ssl
import csv
from Constants import *

context = ssl._create_unverified_context()


link_url = BASE_URL + URL_WILAYAH_PROV

print("Request Daftar Provinsi ...")
print(link_url)

url = urllib.request.urlopen(link_url, context = context)
data = json.loads(url.read().decode())

def getData():
	return data

def generateCSV():
	print("Generating CSV Daftar Provinsi ...")
	provinsi_data = open(BASE_LOCAL_PATH + 'data_provinsi.csv', 'w')

	csvwriter = csv.writer(provinsi_data)

	count = 0

	for provinsi in data:
		if count == 0:
			header = provinsi.keys()
			csvwriter.writerow(header)
			count += 1

		csvwriter.writerow(provinsi.values())

	provinsi_data.close()

	message_string = "––– CSV Daftar Provinsi created ({} data) –––".format(len(data))

	print(message_string)
	return