import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *

context = ssl._create_unverified_context()

link_url = BASE_URL + URL_WILAYAH_PROV

print("Request Daftar Provinsi ...")
print(link_url)

try:
	url = urllib.request.urlopen(link_url, context = context)
	data = json.loads(url.read().decode())
# except urllib.error.HTTPError as e:
# 	message_string = 'ERROR request data provinsi --' + e.message
# 	print(message_string)
# 	pecker(LOG_PROVINSI_DATA, message_string)
# 	data = ""
# except urllib.error.URLError as e:
# 	message_string = 'ERROR request data provinsi --' + str(e.reason)
# 	print(message_string)
# 	pecker(LOG_PROVINSI_DATA, message_string)
# 	data = ""
except Exception as e:
	message_string = 'ERROR request data provinsi --' + str(e)
	print(message_string)
	pecker(LOG_PROVINSI_DATA, message_string)
	data = ""

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
	pecker(LOG_PROVINSI_DATA, message_string)

	return