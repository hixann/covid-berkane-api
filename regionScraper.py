from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import urllib.request
from re import findall
import re

#url = 'http://provberkane.com/covid19/public/'
#response = urllib.request.urlopen(url)
#html = response.read()
#htmlStr = html.decode()

#response = requests.get(url, timeout=5)
#content = BeautifulSoup(response.content, "html.parser")

#r = re.findall(r'[-+]?\d+?\.\d+,[-+]?\d+?\.\d+', htmlStr)
#print(r)

now = datetime.now().strftime("%H:%M %d/%m/%Y")
regions_en = [ "Ahfir",  "Ain Reggada",  "Berkane",  "Boughriba",  "Fezouane",  "Laatamna", ]
regions_ar = [ "أحفير",  "عين الركادة",  "بركان",  "بوغريبة",  "فزوان",  "لعثامنة", ]
cases =  [ 1,  3,  27,  3,  2,  1, ]
recovered =  [ 1,  0,  6,  0,  0,  0, ]
deaths =  [ 0,  0,  1,  1,  0,  0, ]

perRegion = [
        {
            "Date": now,
        }
        ]

for region_en, region_ar, case, recover, death in zip(regions_en, regions_ar, cases, recovered, deaths):
    provinceBerkane = {
        "region_en": region_en,
        "region_ar": region_ar,
        "confirmed": case,
        "recovered": recover,
        "dead": death
            }
    perRegion.append(provinceBerkane)

print(perRegion)

with open('regionData.json', 'w') as outfile:
    json.dump(perRegion, outfile, default=str)
