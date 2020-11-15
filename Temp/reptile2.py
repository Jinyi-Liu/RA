from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import pickle
import datetime as dt

data = pd.read_excel('tocheck.xlsx')
data['CIK'] = data['CIK'].astype(int)
data['FileDate'] = pd.TimedeltaIndex(data['FileDate'], unit='d') + dt.datetime(1900, 1, 1)
data['FileDate'] = data['FileDate'].dt.date

url_ = data['URL'].values
url_set = [item[:-4]+"-index.htm" for item in url_]
data.insert(5,'url',url_set)
data = data.sort_values(['CIK','FileDate'])
# data.to_excel('tocheck_2.xlsx',index=False)

# urlpage = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={" \
#          "}&type=DEF+14A&dateb=&owner=exclude&count=100&search_text= "

CIK = sorted(list(set(data['CIK'].values)))
# 读取html
url_ = "https://www.sec.gov/Archives/edgar/data/2034/0001188112-13-002937.txt"

page = urllib.request.urlopen(url_)
soup = BeautifulSoup(page, 'lxml')

# data = soup.select("#formDiv > div > table > tr:nth-child(2) >td:nth-child(3) > a")
# [item.get('href') for item in data]

soup.find_all("div")

for code in CIK[26:]:
    _urls = data.loc[data['CIK']==code]['URL'].values
    _temp = []
    for _url in _urls:
        page = urllib.request.urlopen(_url)
        soup = BeautifulSoup(page, 'lxml')
        _temp.append(soup)

    f = open('txtfile/{}.txt'.format(code),'w')
    f.write(temp[0])
    break