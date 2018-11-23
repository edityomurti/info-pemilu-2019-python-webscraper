import urllib.request
import json
import ssl
import csv
from Constants import *

context = ssl._create_unverified_context()

print("Request Daftar Partai ...")

url = urllib.request.urlopen(BASE_URL + 'allparpol.json?', context = context)
data = json.loads(url.read().decode())


def getData():
	return data

def generateCSV():
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
	return