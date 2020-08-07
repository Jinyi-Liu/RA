from bs4 import BeautifulSoup
import bs4
import re
import os

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()

keyword='outstanding'

def get_paragraph_with_keyword(soup, tag, keyword=keyword):
    tags = soup.find_all(tag)
    _tags = [item for item in tags if keyword in item.get_text()]
    tag_contents = []
    for tag in _tags:
        temp = []
        for child_tag in tag:
            if type(child_tag) == bs4.element.NavigableString:
                temp.append(child_tag)
            else:
                temp.append(child_tag.get_text())
        tag_contents.extend(temp)
    return ' '.join(''.join(tag_contents).split())

'''
Extract the outstanding shares from a given html file
'''
pre_name = 16160
files = [item for item in html_files if str(pre_name)+'_' in item]
file='16160_2.html'
for file in files:
    data = open(html_path + '/' + file)
    handle = data.read()
    soup = BeautifulSoup(handle, 'lxml')
    soup = soup.find('document')
    '''
    Solved:
    tag <p> with something like <font>****</font> in it.
    Example: 16160_1.html
    '''
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
    '''
    p_text = get_paragraph_with_keyword(soup,'p','outstanding')

    re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:\.\d{2})?')
    test = re_num.findall(p_text)

    div = soup.find_all('div')
    _div = [item for item in div if 'outstanding' in item.get_text()]




t = get_paragraph_with_keyword(soup, 'div',keyword)
re_num.findall(t)
    print(file)
    print(test)
