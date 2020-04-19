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

# open the file with URL's
f = open('C:/Users/Wesley Barnes/Desktop/urlstoscrape.txt', 'r')

# for every line in the file
for line in f:

    # Get the region from url and store value as variable "region"
    if 'Eastern-Cape' in line:
        region = 'Eastern Cape'
    elif 'Free-State' in line:
        region = 'Free State'
    elif 'Gauteng' in line:
        region = 'Gauteng'
    elif 'KwaZulu-Natal' in line:
        region = 'KwaZulu Natal'
    elif 'Limpopo' in line:
        region = 'Limpopo'
    elif 'Mpumalanga' in line:
        region = 'Mpumalanga'
    elif 'North-West' in line:
        region = 'North West'
    elif 'Northern-Cape' in line:
        region = 'Northern Cape'
    elif 'Western-Cape' in line:
        region = 'Western Cape'
    elif 'Botswana' in line:
        region = 'Botswana'
    elif 'Mozambique' in line:
        region = 'Mozambique'
    elif 'Namibia' in line:
        region = 'Namibia'
    elif 'Swaziland' in line:
        region = 'Swaziland'
    else:
        region = 'Other Region'

    page = urllib.request.urlopen(line)  # open the url
    if r.status_code == 200:
        soup = BeautifulSoup(page, 'html.parser')  # soup fetch content from the page

    # get store type
    try:
        store_type = soup.find('div', {'id': 'StoreType'})
        stype = store_type.text.strip()
    except Exception as e:
        stype = None

    # get store name
    try:
        store_name = soup.find('div', class_='store-header')
        sname = store_name.h1.text.strip()
    except Exception as e:
        sname = None

    # get store address
    try:
        store_address = soup.find('div', {'id': 'store-info'})
        address = store_address.p.text.strip()
    except Exception as e:
        address = None

    # get store tel
    try:
        store_tel = soup.find('a', {'id': 'telephone'})
        tel = store_tel.text.strip()
    except Exception as e:
        tel = None

    # get store email
    try:
        store_email = soup.find('a', {'id': 'mail'})
        email = store_email.text.strip()
    except Exception as e:
        email = None

    #get store coordinates
    try:
        store_coordinates = soup.find('a', {'id': 'maps-directions'})
        coordinates = store_coordinates
    except Exception as e:
        coordinates = None

    # set variable to write
    results = (region+';'+stype+';'+sname+';'+address+';'+tel+';'+email+';'+coordinates['href'][35:])
     
    #write data to file
    f = open('C:/Users/Wesley Barnes/Desktop/SparScrapedData.csv', 'a+')
    f.write('\n')
    f.write(results)
    f.close()
    print(results)
    print('-----------Fetching Next--------------')

    # Random delays before calling next url to prevent being blocked
    delays = [7, 4, 6, 2, 10, 19]
    delay = np.random.choice(delays)
    time.sleep(delay)
