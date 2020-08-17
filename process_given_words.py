from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime

html_from = './txt2html_files'
html_read = './read_html'
html_with_keywords = './with_keywords'


def read_html_names(txt):
    f_open = open(txt, 'r')
    temp = f_open.readlines()
    return [item[:-1] for item in temp]


all_files = os.listdir(html_from)
all_files.sort()
all_files = [item for item in all_files if item.endswith('_0.html')]

processed_files = open(html_with_keywords + '/' + 'keyword1.txt', 'r').readlines()
processed_files = processed_files[::3]
processed_files1 = open(html_with_keywords + '/' + 'keyword2.txt', 'r').readlines()
processed_files1 = processed_files1[::3]
processed_files = [item[:-1] for item in processed_files+processed_files1]

checked_files = os.listdir(html_read)
checked_files.sort()
checked_files = [item for item in checked_files if item.endswith('_0.html')]

processing_files = list(set.difference(set(all_files), set.union(set(processed_files), set(checked_files))))
processing_files.sort()

# keywords = ['[0-9a-zA-Z\.\,]+ votes per share'] keyword1
keywords = [' 5 votes','five votes',]
# processing_files =['67517_0.html']
for file in processing_files:
    data = open(html_from + '/' + file)
    handle = data.read()
    soup = BeautifulSoup(handle, 'lxml')
    soup_doc = soup.find('document')
    if not soup_doc:
        soup_doc = soup
    all_text = ' '.join(soup_doc.get_text().split())
    dual_set = []
    words_set = []
    f = open(html_with_keywords + '/' + 'keyword2.txt', 'a', encoding='UTF-8')
    for keyword in keywords:
        reg = re.compile(keyword, re.IGNORECASE)
        given_keyword_exist = reg.findall(all_text)
        if given_keyword_exist:
            words_set.append(given_keyword_exist)
            dual_set.append(True)
        else:
            dual_set.append(False)
    if len(dual_set) > 0 and (np.array(dual_set) == True).any():
        f.write(file)
        f.write('\n')
        for word in words_set[0]:
            f.write(word)
            f.write('\t')
        f.write('\n\n')
    f.close()
    print(file)
