import ssl
import urllib.request
import pandas as pd
import csv
import socket
from Constants import *
from util_logging import *

def getImage(id, indexOf, totalData):
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
		message_string = "–––– creating image Caleg DPRD PROV idCaleg={} created –––– ({}/{})".format(id, indexOf, totalData)
		is_image_created = True
	except Exception as e:
		message_string = "ERROR !!! Requesting IMAGE Caleg DPRD KAB ({}/{}) idCaleg={}–– {}".format(indexOf, totalData, id, str(e))
		is_image_created = False

	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)
	return is_image_created

total_data_generated = 0
data_generated = 0
data_error = 0

message_string = "=== START GENERATING IMAGE OF CALEG DPRD PROV ==="
print(message_string)
pecker(LOG_IMAGE_CALEG, message_string)

csv_file = 'data_caleg_kab.csv'

try:
	df = pd.read_csv(csv_file)
	id_list = df['id'].tolist()
	for i,data in enumerate(id_list):
		if (getImage(str(data), str(i+1), str(len(id_list)))):
			data_generated += 1
		else:
			data_error +=1
	total_data_generated = data_generated + data_error
	message_string = "=== END GENERATING IMAGE OF CALEG DPRD KAB:: generated={}, error={}, total={} data generated, ===".format(data_generated, data_error, total_data_generated)
except Exception as e:
	message_string = "ERROR !!! failed generating Caleg DPD KAB image ––{}".format(str(e))

print(message_string)
pecker(LOG_IMAGE_CALEG, message_string)