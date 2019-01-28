import ssl
import urllib.request
import pandas as pd
import csv
from Constants import *
from util_logging import *
import socket

def getImage(id, indexOf, totalData, fromIndex, fromTotal):
	is_image_created = False
	context = ssl._create_unverified_context()
	ssl._create_default_https_context = ssl._create_unverified_context
	socket.setdefaulttimeout(60)
	proxy = urllib.request.ProxyHandler({})
	opener = urllib.request.build_opener(proxy)
	opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30')]
	urllib.request.install_opener(opener)

	full_path = BASE_HTML_PATH + "caleg/images/" + id + ".jpg"

	try:
		print(URL_IMAGE_CALEG.format(id))

		urllib.request.urlretrieve(URL_IMAGE_CALEG.format(id), full_path)
		message_string = "–––– creating image Caleg DPRD KAB :: ({}/{}) from ({}/{}) - idCaleg={} created ––––".format(indexOf, totalData, fromIndex, fromTotal, id)
		is_image_created = True
	except Exception as e:
		message_string = "ERROR !!! Requesting IMAGE Caleg DPRD KAB :: ({}/{}) from ({}/{}) - idCaleg={} –– {}".format(indexOf, totalData, fromIndex, fromTotal, id, str(e))
		is_image_created = False

	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)
	return is_image_created

def byIndexOf(indexOf):
	total_data_generated = 0
	data_generated = 0
	data_error = 0

	try:
		INDEX_OF = int(indexOf)
	except Exception as e:
		return print("INVALID INPUT, SMARTASS! ––{}".format(str(e)))
		
	message_string = "===== START :: APPENDING IMAGE OF CALEG DPRD KAB ––BY START FROM INDEX OF={}=====".format(INDEX_OF)
	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)

	csv_file = 'data_caleg_kab.csv'

	try:
		df = pd.read_csv(csv_file)
		id_list = df['id'].tolist()
		for i,data in enumerate(id_list):
			if ((i+1) >= INDEX_OF):
				if (getImage(str(data), str((i + 1) - INDEX_OF + 1), str(len(id_list) - INDEX_OF + 1), str(i + 1), str(len(id_list)))):
					data_generated += 1
				else:
					data_error += 1
		total_data_generated = data_generated + data_error
		message_string = "===== END :: APPENDING IMAGE OF CALEG DPRD KAB ––BY START FROM INDEX OF={}:: generated={}, error={}, appended={} data appended from {} total, =====".format(str(INDEX_OF), data_generated, data_error, total_data_generated, len(id_list))
	except Exception as e:
		message_string = "ERROR !!! failed generating Caleg DPRD KAB ––BY START FROM INDEX OF={} –– {}".format(INDEX_OF, str(e))

	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)

TYPE_APPEND = input("1 - Single id\n 2 - From indexOf\nEnter appending type : ")

if(TYPE_APPEND == '1'):
	total_data_generated = 0
	data_generated = 0
	data_error = 0

	print("APPENDING SINGLE ID")

	ID_CALEG = input("Enter idCaleg")

	message_string = "===== START :: APPENDING IMAGE OF CALEG DPRD KAB ––BY SINGLE ID idCaleg={}=====".format(ID_CALEG)
	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)

	if (getImage(ID_CALEG, '1', '1', 'SINGLE', 'SINGLE')):
		data_generated += 1
	else:
		data_error = 0

	total_data_generated = data_generated + data_error
	message_string = "===== END :: APPENDING IMAGE OF CALEG DPRD KAB ––BY SINGLE ID idCaleg={}:: generated={}, error={}, total={} data appended, =====".format(ID_CALEG, data_generated, data_error, total_data_generated)
	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)
elif (TYPE_APPEND == '2'):
	print ("APPENDING BY INDEXOF")

	INDEX_OF = input("Enter start from index of = ")
	byIndexOf(INDEX_OF)
else:
	print("WRONG INPUT, SMARTASS!")



