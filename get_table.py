from bs4 import BeautifulSoup
import numpy as np
import re
import os
from re import sub

html_path = './txt2html_files'
# file = '1023128_0.html'
file ='230557_0.html'
data = open(html_path + '/' + file)
handle = data.read()
soup = BeautifulSoup(handle, 'lxml')
soup = soup.find('document')
# table = soup.find_all('table')

# tags = [tag for tag in table if 'group (10 persons) (O)' in tag.get_text()]

reg = re.compile('SECURITY\W+OWNERSHIP\W+OF\W+MANAGEMENT\W+AND\W+CERTAIN\W+BENEFICIAL\W+OWNERS')
start = soup.find_all('div',text=reg)
test = start[-1]
for tag in test.find_next_siblings('table'):
    print(tag.get_text())
    break
