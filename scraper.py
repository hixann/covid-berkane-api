from bs4 import BeautifulSoup
from termcolor import colored
from datetime import date
from datetime import datetime
import requests
import json
import re

url = 'http://provberkane.com/covid19/public/page4'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


now = datetime.now().strftime("%d/%m/%Y %H:%M")
excluded = content.select_one("div.panel-success div.panel-body").text
confirmed = content.select_one("div.panel-danger div.panel-body").text
dead = content.select_one("div.panel-default div.panel-body").text
recovered = content.select_one("div.panel-info div.panel-body").text


excluded_processed = re.sub('\s', '', excluded)
confirmed_processed = re.sub('\s', '', confirmed)
dead_processed = re.sub('\s', '', dead)
recovered_processed = re.sub('\s', '', recovered)

covidBerkane = []

covidObject = {
        "Date": now,
        "excluded": excluded_processed,
        "confirmed": confirmed_processed,
        "dead": dead_processed,
        "recovered": recovered_processed
        }

covidBerkane.append(covidObject)

print("COVID-19 situation in Berkane")
print("Date: ", now)
print(colored("Excluded: ", 'blue'), covidBerkane[0]['excluded'])
print(colored("Confirmed: ", 'blue'), covidBerkane[0]['confirmed'])
print(colored("Dead: ", 'red'), covidBerkane[0]['dead'])
print(colored("Recovered: ", 'green'), covidBerkane[0]['recovered'])
#print("Dead: ",covidObject['dead'])
#print("Recovered: ",covidObject['recovered'])

with open('coviData.json', 'w') as outfile:
    json.dump(covidBerkane, outfile, default=str)
