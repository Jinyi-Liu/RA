import requests
import pandas as pd
import datetime as dt
'''
data = pd.read_excel('naocan.xlsx')
data['CIK'] = data['CIK'].astype(int)
data['FileDate'] = pd.TimedeltaIndex(data['FileDate'], unit='d') + dt.datetime(1900, 1, 1)
data['FileDate'] = data['FileDate'].dt.date

data = data.sort_values(['CIK', 'FileDate'])

CIK = sorted(list(set(data['CIK'].values)))

for code in CIK[13:26]:
    _urls = data.loc[data['CIK'] == code]['URL'].values
    i = 0
    for _url in _urls:
        r = requests.get(_url)
        with open("./txt2html_files/{}_{}.html".format(code, i), 'wb') as f:
            f.write(r.content)
        i += 1
    print(code)
'''
temp = open('10k_pre_url.txt','r')
pre_url = temp.readlines(temp)