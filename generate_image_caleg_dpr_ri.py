import ssl
import urllib.request
import pandas as pd
# import csv
from Constants import *
from util_logging import *

def getImage(id):
	is_image_created = False
	context = ssl._create_unverified_context()
	ssl._create_default_https_context = ssl._create_unverified_context

	full_path = BASE_LOCAL_PATH + "caleg/images/" + id + ".jpg"

	message_string = "––– Requesting IMAGE idCaleg={} –––".format(id)
	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)

	try:
		print(URL_IMAGE_CALEG.format(id))
		urllib.request.urlretrieve(URL_IMAGE_CALEG.format(id), full_path)
		message_string = "–––– image idCaleg={} created ––––".format(id)
		is_image_created = True
	except Exception as e:
		message_string = "ERROR !!! Requesting IMAGE idCaleg={} –– {}".format(id, str(e))
		is_image_created = False

	print(message_string)
	pecker(LOG_IMAGE_CALEG, message_string)
	return is_image_created

total_data_generated = 0
message_string = "=== START GENERATING IMAGE OF CALEG DPR RI ==="
print(message_string)
pecker(LOG_IMAGE_CALEG, message_string)

csv_file = 'data_caleg_dpr_ri.csv'

try:
	df = pd.read_csv(csv_file)
	for data in df['id'].tolist():
		if (getImage(data)):
			total_data_generated += 1
	message_string = "=== END GENERATING IMAGE OF CALEG DPR RI, {} data generated ===".format(total_data_generated)
except Exception as e:
	message_string = "ERROR !!! failed generating Caleg DPR RI image ––{}".format(str(e))

print(message_string)
pecker(LOG_IMAGE_CALEG, message_string)



