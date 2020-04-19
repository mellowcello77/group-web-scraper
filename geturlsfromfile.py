import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import csv
from datetime import datetime
import requests
import numpy as np
import random
import lxml

# header presented to server
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
r = requests.get("https://www.spar.co.za/", headers=headers, timeout=5)

html = urlopen("file:///C:/Users/Wesley%20Barnes/Desktop/SPAR%20-%20Store%20Finder.html")

bsObj = BeautifulSoup(html.read());
    for link in bsObj.find_all('a'):
        print(link.get('href'))

links = soup.find_all("a")
print(links)