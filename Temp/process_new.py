from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime
import win32file
win32file._setmaxstdio(4096)
raw_path = './txtfile'
process_new = './process_new'
_files = os.listdir(raw_path)
_files.sort()
n = 150 # 每组n个文件来多线程
# file='12208_0.txt'


def load_raw(raw_data_path, file_name):
    return open(raw_data_path + '/' + file_name).read()


def to_write(to_write_path, file_name):
    return open(to_write_path + '/' + file_name, 'w', encoding='UTF-8')


def find_tag(soup, tag):
    return soup.find_all(tag)


def process_small_tag(soup, tag):
    temp = soup.find_all(tag)[1:]
    temp = [item.get_text() for item in temp]
    temp = list(set(temp))
    return temp


def get_one_vote(files):
    key_word = 'one vote'
    for file in files:
        f = to_write(process_new, file)
        handle = load_raw(raw_path, file)
        soup = BeautifulSoup(handle, 'lxml')
        # 查找p td div标签
        _p = process_small_tag(soup, 'p')
        _td = process_small_tag(soup, 'td')
        _div = soup.find_all('div')
        # 判断是否one vote在这些标签文本中
        _set = []
        for item in _div:
            if type(item) != str:
                tempTrue = [_ for _ in item.descendants if key_word in _]
                _set.extend(tempTrue)
            elif 'one vote' in item:
                _set.extend([item])

        temp_p = [item for item in _p if key_word in item]
        temp_td = [item for item in _td if key_word in item]

        # 提取这些含有one vote标签中的文本
        _set.extend(temp_p)
        _set.extend(temp_td)
        _set = [item.strip().strip('\n\r') for item in _set if len(item) < 10000]
        # 去掉重复的
        _set = list(set(_set))
        # 将文本set中的内容写入对应txt文件
        for item in _set:
            f.write(item)
            f.write('\n')
        f.close()


processed_file = os.listdir(process_new)
processed_file.sort()
not_processed = list(set.difference(set(_files), set(processed_file)))
not_processed.sort()

# thre = [_files[i:i + n] for i in range(0, len(_files), n)]
_files = not_processed+['13573_0.txt','13573_3.txt']
thre = [_files[i:i + n] for i in range(0, len(_files), n)]

threads = []
for i in range(10):
    _ = threading.Thread(target=get_one_vote, args=[thre[i]])
    threads.append(_)

if __name__ == '__main__':
    for thr in threads:
        thr.start()
    thr.join()
    print("all over %s" % ctime())
