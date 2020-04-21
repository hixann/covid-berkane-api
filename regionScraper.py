from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import re

url = 'http://provberkane.com/covid19/public/page4'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

now = datetime.now().strftime("%d/%m/%Y %H:%M")
regions_en = [ "Ahfir",  "Ain Reggada",  "Berkane",  "Boughriba",  "Fezouane",  "Laatamna", ]
regions_ar = [ "أحفير",  "عين الركادة",  "بركان",  "بوغريبة",  "فزوان",  "لعثامنة", ]
cases =  [ 6,  3,  12,  14,  2,  2, ]

perRegion = []

for region_en, region_ar, case in zip(regions_en, regions_ar, cases):
    provinceBerkane = {
        "region_en": region_en,
        "region_ar": region_ar,
        "cases": case
            }
    perRegion.append(provinceBerkane)

print(perRegion)

with open('regionData.json', 'w') as outfile:
    json.dump(perRegion, outfile, default=str)
