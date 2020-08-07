from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime
import re
import win32file
win32file._setmaxstdio(4096)
path = './txtfile'
testing = './preprocess'
test = './test2'

files = os.listdir(path)
file = '12208_0.txt'

f = open(testing+'/'+file, 'w', encoding='UTF-8')
data = open(path + '/' + file)
# Parse txt file with lxml
handle = data.read()
soup = BeautifulSoup(handle, 'lxml')
reg = re.compile('.*one vote*.')
tag = soup.find_all(text=reg)

# 查找p td div标签
_p = soup.find_all('p')
_td = soup.find_all('td')
_div = soup.find_all('div')
# 判断是否one vote在这些标签文本中
_set = []
for item in _div:
    if type(item) != str:
        # tempTrue = [True if 'one vote' in _ else False for _ in item.descendants]
        tempTrue = [_ for _ in item.descendants if 'one vote' in _]
        _set.extend(tempTrue)
    elif 'one vote' in item:
        _set.extend([item])


temp_p = [item.get_text() for item in _p if 'one vote' in item.get_text()]
temp_td = [item.get_text() for item in _td if 'one vote' in item.get_text()]

# 提取这些含有one vote标签中的文本
_set.extend(temp_p)
_set.extend(temp_td)
_set = [item.strip().strip('\n') for item in _set if len(item) < 10000]
# 去掉重复的
_set = list(set(_set))
# 将文本set中的内容写入对应txt文件
for item in _set:
    f.write(item)
    f.write('\n')
f.close()
