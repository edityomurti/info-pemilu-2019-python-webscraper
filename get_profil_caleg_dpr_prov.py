import os
import urllib.request
import ssl
import csv
import pandas as pd
from bs4 import BeautifulSoup
from util_logging import *
from urllib.error import URLError, HTTPError


def getData(indexOf, totalData, idCaleg, idPartai, idDapil, idPro):
	is_success = False
	message_string = "getting data id={} ({}/{})".format(idCaleg, indexOf, totalData)

	try:
		context = ssl._create_unverified_context()
		url = "https://infopemilu.kpu.go.id/pileg2019/pencalonan/calon/{}".format(idCaleg)
		print("requesting {}".format(url))
		url_link = urllib.request.urlopen(url, context = context)
		data = url_link.read().decode("utf8")

		THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

		soup = BeautifulSoup(data, "html.parser")

		listDataRaw = soup.find_all("div", class_=["row no-margin", "row no-margin yellow-one"])

		listData = list()

		for i,item in enumerate(listDataRaw):
			if (i<18):
				listData.append(item)

		
		content = [idCaleg, idPartai, idDapil, idPro]
		contentData = [item.find("div", {'class' : 'col-sm-9'}).text for item in listData]
		content.extend(contentData)

		if (indexOf == '1'):
			headers = ['id', 'idPartai', 'idDapil', 'idPro']
			headersData = [header.find("div", {'class' : 'col-sm-3'}).text for header in listData]
			headers.extend(headersData)
			f = open('data_profil_caleg_prov.csv', 'w')
			writer = csv.writer(f)
			writer.writerow(headers)
			writer.writerow(content)
		else:
			f = open('data_profil_caleg_prov.csv', 'a')
			writer = csv.writer(f)
			writer.writerow(content)

		is_success = True
		message_string = "–––––– ({}/{}) idCaleg = {} generated ––––––".format(indexOf, totalData, idCaleg)
	except HTTPError as e:
		message_string = "ERROR  !!! failed getting idCaleg = {} ({}/{}) - HTTPError cause : {}".format(idCaleg, indexOf, totalData, e)
		is_success = False
	except URLError as e:
		message_string = "ERROR !!! failed getting idCaleg = {} ({}/{}) - URLError cause : {}".format(idCaleg, indexOf, totalData, e)
		is_success = False
	except Exception as e:
		message_string = "ERROR !!! failed getting idCaleg = {} ({}/{}) - cause : {}".format(idCaleg, indexOf, totalData, e)
		is_success = False
	print(message_string)
	pecker("", message_string)
	return is_success


try:
	total_data_generated = 0
	data_generated = 0
	data_error = 0

	csv_file = 'data_caleg_prov.csv'
	df = pd.read_csv(csv_file)

	id_list = df['id'].tolist()
	idPartai_list = df['idPartai'].tolist()
	idDapil_list = df['idDapil'].tolist()
	idPro_list = df['idPro'].tolist()

	message_string = "=== START GENERATING PROFIL CALEG DPRD PROV ==="

	print(message_string)
	pecker("", message_string)

	for i,idCaleg in enumerate(id_list):
		if (getData(str(i+1), str(len(id_list)), str(idCaleg), idPartai_list[i], idDapil_list[i], idPro_list[i])):
			data_generated +1
		else:
			data_error += 1

	total_data_generated = data_generated + data_error
	message_string = "=== END GENERATING PROFIL CALEG DPRD PROV:: generated={}, error={}, total={} data generated ===".format(data_generated, data_error, total_data_generated)

except Exception as e:
	message_string = "ERROR !!! Failed generating profil caleg dprd prov –– {}".format(str(e))

print(message_string)
pecker("", message_string)