from bs4 import BeautifulSoup
import bs4
import re
import os

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()

'''
Extract the outstanding shares from a given html file
'''
pre_name = 16160
files = [item for item in html_files if str(pre_name)+'_' in item]
file='16160_1.html'
for file in files:
    data = open(html_path + '/' + file)
    handle = data.read()
    soup = BeautifulSoup(handle, 'lxml')
    soup = soup.find('document')
    '''
    Solved:
    tag <p> with something like <font>****</font> in it.
    16160
    '''
    p = soup.find_all('p')
    _p = [item for item in p if 'outstanding' in item.get_text()]
    p_content = []
    for p_tag in _p:
        temp = []
        for child_tag in p_tag:
            if type(child_tag) == bs4.element.NavigableString:
                temp.append(child_tag)
            else:
                temp.append(child_tag.get_text())
        p_content.extend(temp)
    p_text = ' '.join(''.join(p_content).split())
    re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:\.\d{2})?')

