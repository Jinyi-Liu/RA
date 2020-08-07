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
    '''
    f_test = open('test.txt', 'w')
    for child in p_content:
        p_text = ' '.join(''.join(child).split())
        f_test.write(p_text)
        f_test.write('\n\r')
    f_test.close()
    p_text = ' '.join(''.join(p_content).split())
    f_test = open('test.txt','w')
    f_test.write(p_text)
    f_test.close()
    '''
    p_text = ' '.join(''.join(p_content).split())
    ###
    #reg = re.compile('.*outstanding*.')
    #tag = soup.find_all(text=reg)
    #pre = [' '.join(item.split()) for item in tag]
    re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:\.\d{2})?')
    print(file)
    print(re_num.findall(p_text)[:8])
    #num = [re_num.findall(tag_item) for tag_item in tag]
    #num = [item for item in num if len(item)>5]
    '''
    num_list = []
    for item in num:
        num_list.extend(item)
    print(file)
    print(num_list)
    '''
