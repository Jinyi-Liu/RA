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


def get_one_vote(files):
    dict_handle = {}
    dict_data = {}
    for file in files:
        f = open(test + '/' + 'test' + file, 'w', encoding='UTF-8')
        data = open(path + '/' + file)
        handle = data.read()
        soup = BeautifulSoup(handle, 'lxml')
        reg = re.compile('.*one vote*.')
        tag = soup.find_all(text=reg)

        _set = [' '.join(item.split()) for item in tag if len(tag) < 10000]
        # 去掉重复的
        _set = list(set(_set))
        # 将文本set中的内容写入对应txt文件
        for item in _set:
            f.write(item)
            f.write('\n')
        f.close()


processed_file = os.listdir(test)[1:]
processed_file = [item[4:] for item in processed_file]
processed_file.sort()
not_processed = list(set.difference(set(_files), set(processed_file)))
not_processed.sort()

# thre = [_files[i:i + n] for i in range(0, len(_files), n)]
_files = not_processed
thre = [_files[i:i + n] for i in range(0, len(_files), n)]

threads = []
for i in range(12):
    _ = threading.Thread(target=get_one_vote, args=[thre[i]])
    threads.append(_)

if __name__ == '__main__':
    for thr in threads:
        thr.start()
    thr.join()
    print("all over %s" % ctime())
