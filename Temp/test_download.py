import requests
import pickle
import re

download_source = input()
with open(download_source, 'rb') as fp:
    urls = pickle.load(fp)

prefix = input('Prefix?')
if prefix=='T':
    url_prefix = 'https://sec.gov'
else:
    url_prefix = ''
code_pre = re.findall('\d+', urls[0])[0]
i = 0
for url in urls:
    code_now = re.findall('\d+', url)[0]
    if code_pre != code_now:
        i = 0
    r = requests.get(url_prefix + url)
    with open("./def14a/{}_{}.html".format(code_now,i), 'wb') as f:
        f.write(r.content)
    i += 1
    code_pre = code_now


