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

# Python 3.4 used, pip installs done below:
# easy_install pip
# python -m pip install --upgrade pip
# pip install BeautifulSoup4
# python -m pip install requests

# Step 1: Go to this link: https://www.spar.co.za/store-finder, click "search" to load all stores
# Step 2: Download the actual HTML website as a file (save as)
# Step 3: Run the code below on its own first to pull all the urls from the page - update your custom link below for your file name and location

# code: html = urlopen("file:///C:/Users/Wesley%20Barnes/Desktop/SPAR%20-%20Store%20Finder.html") # Insert your URL to extract
# code: bsObj = BeautifulSoup(html.read());

# code: for link in bsObj.find_all('a'):
# code:   #print(link.get('href'))

# Step 4: Copy all the links into a spreadsheet, filter/remove all the unwanted data so that you have a file with all
# the url's of each store. Each in a single line, and save as csv file. Example of your line 1: https://www.spar.co.za/Home/Store-View/SPAR-1000-Hills-KwaZulu-Natal
# Step 5: Save the file as: AllSparURLS.csv (update link location below at "f = open"
# Step 6: Comment out above code between step 3 and 4, and run the code below.


f = open('C:/Users/Wesley Barnes/Desktop/SparURLS.csv', 'r') #text file containing the URLS

for line in f:

    # Select a random user agent from file for header every time a new url is called
    def get_random_ua():
        random_ua = ''
        ua_file = 'C:/Users/Wesley Barnes/Desktop/ua_file.txt'
        try:
            with open(ua_file) as f:
                lines = f.readlines()
            if len(lines) > 0:
                prng = np.random.RandomState()
                index = prng.permutation(len(lines) - 1)
                idx = np.asarray(index, dtype=np.integer)[0]
                random_proxy = lines[int(idx)]
        except Exception as ex:
            print('Exception in random_ua')
            print(str(ex))
        finally:
            return random_ua

    #get the reandomly selected header
    user_agent = get_random_ua()

    #change the header so it looks like your a different user
    headers = {
        'user-agent': user_agent,
    }
    # ? ? r = requests.get('http://spar.co.za', headers=headers)#

    #get the next URL from the file to run
    page = urllib.request.urlopen(line)

    #soup fetched content of the page/url
    soup = BeautifulSoup(page, 'html.parser')

    # find the store name
    store_name = soup.find("div", {"class": "store-header"})
    name = store_name.text.strip()
    f = open('C:/Users/Wesley Barnes/Desktop/ScrapedData.csv', 'a+')
    f.write('\n')
    f.write(str(name))
    f.close()
    print(name)

    # find the store coordinates
    store_coordinates = soup.findAll('div', attrs={'class': 'links'})
    for div in store_coordinates:
        f = open('C:/Users/Wesley Barnes/Desktop/ScrapedData.csv', 'a+')
        f.write('\n')
        f.write(str(div.a['href'][35:]))
        f.close()
        print(div.a['href'][35:])

    # Random delays before calling next url to look more human
    delays = [7, 4, 6, 2, 10, 19]
    delay = np.random.choice(delays)
    time.sleep(delay)
