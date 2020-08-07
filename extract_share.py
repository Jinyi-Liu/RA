from bs4 import BeautifulSoup
import bs4
import re
import numpy as np
import os

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()

keyword = 'outstanding'
tag_search = 'p'


def get_contents(tags, keyword=keyword):
    tag_contents = []
    _tags = [item for item in tags if keyword in item.get_text()]
    for tag in _tags:
        temp = []
        for child_tag in tag:
            if type(child_tag) == bs4.element.NavigableString:
                temp.append(child_tag)
            else:
                temp.append(child_tag.get_text())
        tag_contents.extend(temp)
    return tag_contents


def tags_with_no_defined_tag(tag_descendants_names, saved_tags, not_saved_tags):
    return len(tag_descendants_names) == 0 or (not (tag_descendants_names == saved_tags).any() and not (
            tag_descendants_names == not_saved_tags).any())


def get_paragraph_with_keyword(soup, tag_search, keyword=keyword):
    tags = soup.find_all(tag_search)
    if tag_search == 'div':
        div_tags_with_no_p = []
        for tag in tags:
            tag_descendants_names = []
            for _ in tag.descendants:
                tag_descendants_names.append(_.name)
            tag_descendants_names = np.array(tag_descendants_names)
            '''
            Delete div tag with children (p tags) in it so as to not search repeatedly
            '''
            if tags_with_no_defined_tag(tag_descendants_names, 'div', 'p'):
                div_tags_with_no_p.append(tag)
        tag_contents = get_contents(div_tags_with_no_p, keyword)
    else:
        tag_contents = get_contents(tags, keyword)

    return ' '.join(''.join(tag_contents).split())


'''
Extract the outstanding shares from a given html file
'''
pre_name = 16160
files = [item for item in html_files if str(pre_name) + '_' in item]
file = '16160_12.html'
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
    p_text = get_paragraph_with_keyword(soup, 'p', 'outstanding')
    div_text = get_paragraph_with_keyword(soup, 'div', keyword)
    re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:\.\d{2})?')
    print(file)
    print(re_num.findall(p_text)[:5])
    print(re_num.findall(div_text)[:5])


