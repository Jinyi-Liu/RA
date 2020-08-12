from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime

html_from = './txt2html_files'
html_with_keywords = './with_keywords'


def read_html_names(txt):
    f_open = open(txt, 'r')
    temp = f_open.readlines()
    return [item[:-1] for item in temp]


files = os.listdir(html_from)
files.sort()
files = [item for item in files if item.endswith('_0.html')]

#files = read_html_names('for_test_09azAZ.txt')
#files = files[::2]  # select one in two

keywords = ['[0-9a-zA-Z\.\,]+ votes per share']
file = '5187_0.html'
for file in files:
    data = open(html_from + '/' + file)
    handle = data.read()
    soup = BeautifulSoup(handle, 'lxml')
    soup_doc = soup.find('document')
    if not soup_doc:
        soup_doc = soup
    all_text = ' '.join(soup_doc.get_text().split())
    dual_set = []
    words_set = []
    f = open(html_with_keywords+'/'+'keyword1.txt', 'a', encoding='UTF-8')
    for keyword in keywords:
        reg = re.compile(keyword, re.IGNORECASE)
        given_keyword_exist = reg.findall(all_text)
        if given_keyword_exist:
            words_set.append(given_keyword_exist)
            dual_set.append(True)
        else:
            dual_set.append(False)
    if len(dual_set) > 0 and (np.array(dual_set) == True).all():
        f.write(file)
        f.write('\n')
        for word in words_set[0]:
            f.write(word)
            f.write('\t')
        f.write('\n\n')
    f.close()
    print(file)