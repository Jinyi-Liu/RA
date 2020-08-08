from bs4 import BeautifulSoup
import bs4
import re
import numpy as np
import os

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()

keyword_ = 'outstanding'
tag_search = 'div'


def get_tag_with_keyword_in_text(tags, keyword):
    return [tag for tag in tags if re.search(keyword, tag.get_text(), re.IGNORECASE)]


def get_contents(all_tags, keyword):
    """
    tag_contents: to store the contents in tags which have keyword
    tags_with_interest: to store the tags which have key word
    keyword: like ['as a group','as a Group'] but this situation is solved by re.IGNORECASE which will ignore the case.
    """
    tags_with_interest = []
    tag_contents = []
    # To get the tags with keyword in their text
    if type(keyword) != list:
        tags_with_interest.extend(get_tag_with_keyword_in_text(all_tags, keyword))
    else:
        for keyword_sole in keyword:
            tags_with_interest.extend(get_tag_with_keyword_in_text(all_tags, keyword_sole))
    #
    for tag in tags_with_interest:
        temp = []
        for child_tag in tag:
            if type(child_tag) == bs4.element.NavigableString:
                temp.append(child_tag)
            else:
                temp.append(child_tag.get_text())
        tag_contents.extend(temp)
    return tag_contents


def tag_with_no_defined_tag(tag_descendants_names, processing_tags, not_wanted_tags):
    """
    tag_descendants_names: len(*) == 0 i.e. no child.
    * == processing_tags: not having the descendant tag with the same name as the processing tag.
    * == not_wanted_tags: not having the descendant tag with the name as something like <p> <tr> which
                          will be processed separately.
    """
    if len(tag_descendants_names) == 0:
        return True
    for _tag in [processing_tags, not_wanted_tags]:
        if (tag_descendants_names == _tag).any():
            return False
    return True


def get_paragraph_with_keyword(soup, tag_search, keyword):
    """
    tags: All the tags with name "tag_search"
    tag_descendants_names: Given a tag like <div>(1) it may have children <div>(2) so the list "tags" will
                           saved twice the contents in <div>(2). So the code will search all the descendants of
                           <div>(1) to make sure it has no <div> descendant. "tag_descendants_names" is the list
                           containing all the descendants'name of <div>(1)
    """
    tags = soup.find_all(tag_search)
    if tag_search == 'div':
        div_tags_with_no_p = []
        for tag in tags:
            tag_descendants_names = []
            for _ in tag.descendants:
                tag_descendants_names.append(_.name)
            # To vectoring the list and using == method
            tag_descendants_names = np.array(list(set(tag_descendants_names)))
            # Delete div tag with children (p tags) in it so as to not search repeatedly
            if tag_with_no_defined_tag(tag_descendants_names, processing_tags='div', not_wanted_tags='p'):
                div_tags_with_no_p.append(tag)
        tag_contents = get_contents(div_tags_with_no_p, keyword)
    else:
        tag_contents = get_contents(tags, keyword)

    return ' '.join(''.join(tag_contents).split())


'''
Extract the outstanding shares from a given html file
'''
pre_name = 16918
files = [item for item in html_files if str(pre_name) + '_' in item]
file = '16918_0.html'
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
    p_text = get_paragraph_with_keyword(soup, 'p', keyword=keyword)
    div_text = get_paragraph_with_keyword(soup, 'div', keyword=keyword)
    # re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:.\d{2})?')
    m = re.compile(r"(\d[\d\s.,]*)\s*?(?:[^%\d])")

    re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:\.\d{2})?|\d{3}(?:\.\d{2})')
    print(re_num.findall(p_text)[:100])
    print(m.findall(p_text))
    print(re_num.findall(div_text)[:5])
    print(file)


