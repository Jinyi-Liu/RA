import pandas as pd
import numpy as np
import pickle
'''
In [1]: import dateutil.parser as dparser

In [18]: dparser.parse("monkey 2010-07-10 love banana",fuzzy=True)
Out[18]: datetime.datetime(2010, 7, 10, 0, 0)
'''

from bs4 import BeautifulSoup
import urllib.request
import pickle
import pandas as pd

file_type = 'DEF+14A'
file_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={" \
           "}&dateb=20151231&owner=exclude&count=40&search_text= "

with open('data/pre_url.pk', 'rb') as fp:
    urls_set = pickle.load(fp)

f=open('urls_date.txt','a+')
urls_date = []
for urls in urls_set:
    _urls = [url for url in urls if url.startswith('/Archives')]
    for url in _urls:  # To get the 10-k file
        page = urllib.request.urlopen('https://sec.gov' + url)
        soup = BeautifulSoup(page, 'html.parser')
        date = soup.select('#formDiv > div.formContent > div:nth-child(1) > div:nth-child(2)')[0].next
        year = pd.to_datetime(date).year
        urls_date.append(date)
        if year < 2002 or year > 2015:
            continue
        urls_date.append(date)
        f.write(date)
        f.write('\n')


#with open('data/def14a_url_final_date.pk', 'wb') as fp:
#    pickle.dump(urls_date, fp)
