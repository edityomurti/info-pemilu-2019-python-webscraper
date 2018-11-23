import urllib.request
import json
import ssl
import csv
from Constants import *

context = ssl._create_unverified_context()

print("Request Daftar Calon Tetap ...")

url = urllib.request.urlopen(BASE_URL + 'pengajuan-calon/82/1/calonDct.json?_=1542910154646', context = context)
data = json.loads(url.read().decode())

pileg_data = open(BASE_LOCAL_PATH + 'data_pileg.csv', 'w')

csvwriter = csv.writer(pileg_data)

count = 0

for pileg in data:
	if count == 0:
		header = pileg.keys()
		csvwriter.writerow(header)
		count += 1

	csvwriter.writerow(pileg.values())

pileg_data.close()

message_string = "––– CSV Daftar Calon Tetap created ({} data) –––".format(len(data))

print(message_string)

def getData():
	return data