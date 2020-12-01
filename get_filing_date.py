from bs4 import BeautifulSoup
import urllib.request
import pickle
import pandas as pd

file_type = 'DEF+14A'
file_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={" \
           "}&dateb=20151231&owner=exclude&count=40&search_text= "



with open('data/pre_url.pk', 'rb') as fp:
    urls_set = pickle.load(fp)


urls_date = []
for urls in urls_set:
    f = open('urls_date.txt', 'a+')
    _urls = [url for url in urls if url.startswith('/Archives')]
    for url in _urls:  # To get the 10-k file
        page = urllib.request.urlopen('https://sec.gov' + url)
        soup = BeautifulSoup(page, 'html.parser')
        date = soup.select('#formDiv > div.formContent > div:nth-child(1) > div:nth-child(2)')[0].next
        year = pd.to_datetime(date).year
        if year < 2002 or year > 2015:
            continue
        print(date)
        f.write(date)
        f.write('\n')
    f.close()


