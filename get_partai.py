import urllib.request
import json
import ssl
import csv
from Constants import *
from util_logging import *


def getData():
	context = ssl._create_unverified_context()

	print("Request Daftar Partai ...")

	try:
		url = urllib.request.urlopen(BASE_URL + 'allparpol.json?', context = context)
		data = json.loads(url.read().decode())
	except Exception as e:
		message_string = "ERROR request daftar partai --" + str(e)
		pecker(LOG_PARTAI_DATA, message_string)
		data = ""

	return data

def generateCSV():
	data = getData()
	print("Generating CSV Daftar Partai ...")
	partai_data = open(BASE_LOCAL_PATH + 'data_partai.csv', 'w')

	csvwriter = csv.writer(partai_data)

	count = 0

	for partai in data:
		if count == 0:
			header = partai.keys()
			csvwriter.writerow(header)
			count += 1

		csvwriter.writerow(partai.values())

	partai_data.close()

	message_string = "––– CSV Daftar Partai created ({} data) –––".format(len(data))

	print(message_string)
	pecker(LOG_PARTAI_DATA, message_string)
	return