# -*- coding: utf-8 -*-

import requests
import json
from Provinsi import *
from bs4 import BeautifulSoup
from Constants import *

print("Request Daftar Provinsi ...")
page = requests.get(BASE_URL + BASE_URL_WILAYAH_PROV)

pageContent = page.content

soup = BeautifulSoup(pageContent, 'html.parser')

print("Generating JSON Daftar Provinsi ...")
outfile = open('data_provinsi.json', 'w')

provinsi_list = []

for item in soup.find(id="provFilter").find_all('option') :
	if (item['value'] != "empty"):
		provinsi = Provinsi(item['value'], item.text)
		provinsi_list.append(provinsi.toJSON())

json.dump(provinsi_list, outfile)

message_string = "––– JSON Daftar Partai created ({} data) –––".format(len(provinsi_list))

print(message_string)
print("json formatting may required")