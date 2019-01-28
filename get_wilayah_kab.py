import os
import urllib.request
import json
import ssl
import pandas as pd
import csv
from util_logging_wilayah_kab import *

def getData(id, indexOf, totalData):
    is_file_created = False
    message_string = "getting data idKab={}  ({}/{})".format(id, indexOf, totalData)
    
    try:
        context = ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context
        
        url_link = 'https://infopemilu.kpu.go.id/pileg2019/api/dapil/{}/2?_=1546094148666'.format(id)
        print("requesting .. " + url_link)
        
        url = urllib.request.urlopen(url_link, context = context,  timeout=10)
        
        datatowrite = url.read()
        
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(THIS_FOLDER, 'data_wilayah_kab/data_wil_kab_{}.json'.format(id))
        
        with open(file_path, 'wb') as f:
            f.write(datatowrite)
        
        is_file_created = True
        message_string = "–––––– ({}/{}) idKab = {} generated ––––––".format(indexOf, totalData, id)
    except Exception as e:
        message_string = "ERROR !!! failed generating idKab = {} ({}/{}) –– cause : {}".format(id, indexOf, totalData, e)
        is_file_created = False
    
    print(message_string)
    pecker("", message_string)
    return is_file_created

try:
    total_data_generated = 0
    data_generated = 0
    data_error = 0
    
    csv_file = 'data_kabupaten.csv'
    df = pd.read_csv(csv_file)
    
    id_list = df['idWilayah'].tolist()
    
    message_string = "=== START GENERATING WILAYAH DPRD KAB ==="
    
    print(message_string)
    pecker("", message_string)
    
    for i,data in enumerate(id_list):
        if (getData(str(data), str(i+1), str(len(id_list)))):
            data_generated += 1
        else:
            data_error += 1

    total_data_generated = data_generated + data_error
    message_string = "=== END GENERATING WILAYAH DPRD KAB:: generated={}, error={}, total={} data generated, ===".format(data_generated, data_error, total_data_generated)

except Exception as e:
    message_string = "ERROR !!! failed generating WILAYAH DPRD KAB––{}".format(str(e))

print(message_string)
pecker("", message_string)


