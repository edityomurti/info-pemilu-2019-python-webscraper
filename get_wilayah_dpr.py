import urllib.request
import json
import ssl
import pandas as pd
import csv
#from Constants_wilayah import *
from util_logging_wilayah_dpr import *

def getData(id, indexOf, totalData):
    is_file_created = False
    
    context = ssl._create_unverified_context()
    ssl._create_default_https_context = ssl._create_unverified_context
    
    file_path = 'data_wilayah_dpr/data_wil_dpr_{}.json'
    
    try:
        url = urllib.request.urlopen('https://infopemilu.kpu.go.id/pileg2019/api/dapil/{}/0?_=1546094148910'.format(id), context = context)
        datatowrite = url.read()
        
        with open(file_path.format(id), 'wb') as f:
            f.write(datatowrite)
        
        is_file_created = True
        message_string = "–––––– ({}/{}) idProv = {} generated ––––––".format(indexOf, totalData, id)
    except Exception as e:
        message_string = "ERROR !!! failed generating idProv = {} ({}/{})".format(id, indexOf, totalData)
        is_file_created = False

    print(message_string)
    pecker("", message_string)
    return is_file_created

try:
    total_data_generated = 0
    data_generated = 0
    data_error = 0

    message_string = "=== START GENERATING WILAYAH DPR ==="
    print(message_string)
    pecker("", message_string)
    
    csv_file = 'data_provinsi.csv'
    df = pd.read_csv(csv_file)
    
    id_list = df['idWilayah'].tolist()
    for i,data in enumerate(id_list):
        if (getData(str(data))):
            data_generated += 1
        else:
            data_error += 1

    total_data_generated = data_generated + data_error
    message_string = "=== END GENERATING WILAYAH DPR:: generated={}, error={}, total={} data generated, ===".format(data_generated, data_error, total_data_generated)

except Exception as e:
    message_string = "ERROR !!! failed generating WILAYAH DPR ––{}".format(str(e))

print(message_string)
pecker("", message_string)
