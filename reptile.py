from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from func import get_processed
import pickle


CIK = get_processed.CIK()
with open('CIK.txt','wb') as fp:
    pickle.dump(CIK,fp)

with open('CIK.txt','rb') as fp:
    CIK = pickle.load(fp)

urlpage = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={" \
          "}&type=10-k&dateb=20151231&owner=exclude&count=40&search_text= "

f = open('10k_pre_url.txt','a')
urls_set = []
for code in CIK[:]:
    print(code)
    urls = []
    # 获取网页内容，把 HTML 数据保存在 page 变量中
    page = urllib.request.urlopen(urlpage.format(code))
    # 用 Beautiful Soup 解析 html 数据
    # 并保存在 soup 变量里
    soup = BeautifulSoup(page, 'html.parser')
    # 在表格中查找数据
    table = soup.find('table', attrs={'class': 'tableFile2'})
    results = table.find_all('a')
    for q in results:
        url = q.get('href')
        if url.startswith('/Archives'):
            f.write(url)
            f.write('\n')
            urls.append(url)
    urls_set.append(urls)
f.close()



f = open('10k_url.txt','a')
urls_10k = []
for urls in urls_set:
    _urls = [url for url in urls if url.startswith('/Archives')]
    for url in _urls:  # To get the 10-k file
        page = urllib.request.urlopen('https://sec.gov'+url)
        soup = BeautifulSoup(page, 'html.parser')
        # The 10-K page's table is tableFile not like the previous page
        table = soup.find('table', attrs={'class': 'tableFile'})
        results = table.find_all('a')
        a = results[0]
        if not a.get('href').endswith('.txt') or not a.get('href').endswith('.htm'):
            url = results[-1].get('href')
        url = results.get('href')
        print(results)
        f.write(url)
        f.write('\n')
        urls_10k.append(url)
f.close()


