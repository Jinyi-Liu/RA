from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import csv

# data = pd.read_excel('tocheck.xlsx')
# data['CIK'] = data['CIK'].astype(int)
# urlpage = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=DEF+14A&dateb=&owner=exclude&count=100&search_text="
#CIK = sorted(list(set(data['CIK'].values)))

urlpage = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=10-k&dateb=20151231&owner=exclude&count=40&search_text="
i = 0
_url_set = []
# 读取到第386
CIK = [1575828]
for code in CIK[:]:
    # 获取网页内容，把 HTML 数据保存在 page 变量中
    page = urllib.request.urlopen(urlpage.format(code))
    # 用 Beautiful Soup 解析 html 数据
    # 并保存在 soup 变量里
    soup = BeautifulSoup(page, 'html.parser')
    # 在表格中查找数据
    table = soup.find('table', attrs={'class': 'tableFile2'})
    results = table.find_all('a')
    for q in results:
        _url = q.get('href')
        _url_set.append(_url)
    i += 1
    print(i)

