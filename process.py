from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime
import win32file
win32file._setmaxstdio(4096)
path = './txtfile'
prepath = './preprocess'
test = './test2'
_files = os.listdir(path)
_files.sort()
n = 300  # 每组n个文件来多线程

thre = [_files[i:i + n] for i in range(0, len(_files), n)]

def get_one_vote(files):
    dict_handle = {}
    dict_data = {}
    for file in files:
        # 被写入的
        dict_handle[file] = open(test+'/'+'test'+file,'a', encoding='UTF-8')
    for file in files:
        # 读取txt文件
        data = open(path+'/'+file)
        dict_data[file] = data.read()
    for file in files:
        '''
        # f = open(prepath+'/'+'test'+file, 'a',encoding='UTF-8')
        # processed files储存文件夹
        # f = open(test + '/' + 'test' + file, 'w', encoding='UTF-8')
        # txtfile储存文件夹
        # data = open(path + '/' + file)
        # Parse txt file with lxml
        # handle = data.read()
        '''
        handle = dict_data[file]
        soup = BeautifulSoup(handle, 'lxml')
        reg = re.compile('.*one vote*.')
        tag = soup.find_all(text=reg)
        '''
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
        '''
        _set = [' '.join(item.split()) for item in tag if len(tag) < 10000]
        # 去掉重复的
        _set = list(set(_set))

        # 将文本set中的内容写入对应txt文件
        for item in _set:
            dict_handle[file].write(item)
            dict_handle[file].write('\n')
        dict_handle[file].close()


threads = []
for i in range(12):
    _ = threading.Thread(target=get_one_vote, args=[thre[i]])
    threads.append(_)

if __name__ == '__main__':
    for thr in threads:
        thr.start()
    thr.join()
    print("all over %s" % ctime())
