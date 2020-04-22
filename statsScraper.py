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

now = datetime.now().strftime("%H:%M %d/%m/%Y")

confirmed = 37
recovered = 7
dead = 2

stats = []

latestStats = {
        "Date": now,
        "confirmed": confirmed,
        "recovered": recovered,
        "dead": dead
}

print(latestStats)

stats.append(latestStats)

#print(perRegion)

with open('statsData.json', 'w') as outfile:
    json.dump(stats, outfile, default=str)
