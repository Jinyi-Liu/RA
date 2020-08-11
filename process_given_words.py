from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime

html_from = './txt2html_files'


def read_html_names(txt):
    f_open = open(txt, 'r')
    temp = f_open.readlines()
    return [item[:-1] for item in temp]
# files = os.listdir(html_from)
# files.sort()
# files = [item for item in files if item.endswith('_0.html')]

processed_1 = read_html_names('dual_all.txt')
already_processed_1 = read_html_names('dual_1.txt')

processing_1 = list(set.difference(set(processed_1),set(already_processed_1)))

# re.compile('[0-9a-zA-Z\.\,]+ votes')
# keywords = ['entitled to one vote', 'entitled to \d+(?:\.)?\d+ votes']
keywords = ['entitled to [0-9a-zA-Z\.\,]+ votes']
file = '5187_0.html'
for file in processed_1:
    data = open(html_from + '/' + file)
    handle = data.read()
    soup = BeautifulSoup(handle, 'lxml')
    soup_doc = soup.find('document')
    if not soup_doc:
        soup_doc = soup
    all_text = ' '.join(soup_doc.get_text().split())
    dual_set = []
    words_set = []
    f = open('for_test_09azAZ.txt', 'a', encoding='UTF-8')
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
        f.write('\n')
    f.close()
    print(file)