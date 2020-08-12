from bs4 import BeautifulSoup
import bs4
import re
import numpy as np
import os

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()

keyword_ = 'one (1) vote'


# tag_search = 'div'


def get_tag_with_keyword_in_text(tags, keyword):
    if keyword == 'one (1) vote':
        keyword = '.*one \(\d+\) vote*.'
    if len(tags) == 0:
        return []
    if tags[0].name == 'tr':
        tr_list = []
        tag_iter = iter(tags)
        while True:
            try:
                tag = tag_iter.__next__()
                if re.search(keyword, ' '.join(tag.get_text().split()), re.IGNORECASE):
                    tr_list.extend([tag, tag_iter.__next__()])
            except StopIteration:
                return tr_list
    return [tag for tag in tags if re.search(keyword, ' '.join(tag.get_text().split()), re.IGNORECASE)]


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
        tag_contents.append(tag.get_text())
        '''
        temp = []
        for child_tag in tag:
            if type(child_tag) == bs4.element.NavigableString:
                temp.append(child_tag)
            else:
                temp.append(child_tag.get_text())
        tag_contents.extend(temp)
        '''
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

    tag_contents_list = [' '.join(''.join(tag_contents_sole).split()) for tag_contents_sole in tag_contents]
    return tag_contents_list


from re import sub
def return_whether_outstanding_share(outstanding_num):
    for _ in outstanding_num:
        if float(sub(r'[^\d.]', '', _)) < 100000:
            return False
    return True

def return_whether_as_a_group(outstanding_num):
    percent_num=0
    for _ in outstanding_num:
        if float(sub(r'[^\d.]', '', _)) <= 101:
            percent_num+=1
    if percent_num >=2:
        return True
    else:
        return False

def return_condition(CIK,tag_type=None,outstanding_num=[]):
    index = False
    CIK_list = [356080, 357294]
    CIK_list_1 = [717954]
    if CIK in CIK_list:
        if tag_type == 'tr':
            len_nums = len(outstanding_num)
            if len_nums == 6 or len_nums == 8:
                index = True  # stands for continue
        else:
            if len(outstanding_num) == 2 and return_whether_outstanding_share(outstanding_num):
                index = True
    if CIK in CIK_list_1:
        if tag_type == 'tr':
            if return_whether_as_a_group(outstanding_num):
                index = True  # stands for continue
        else:
            if len(outstanding_num) == 2:
                index = True
    return index


def print_num(tag_text, re_method, write_text=None, tag_type=None):
    """
    Need more modification!
    """
    for _ in tag_text:
        outstanding_num = re_method.findall(_)
        if len(outstanding_num) >= 1:
            # if len(outstanding_num) == 2 or len(outstanding_num) == 4:
            if tag_type == 'tr':
                print(tag_type)
                '''
                356080:
                if len(outstanding_num)!=6:
                    if len(outstanding_num) != 8:  
                        continue
                '''

                if return_condition(pre_name, tag_type, outstanding_num):
                    for num in outstanding_num:
                        write_text.write(num)
                        write_text.write('\t')
                    print(outstanding_num)
            else:
                print(tag_type)
                '''
                356080:
                if len(outstanding_num) == 2 and ',' in outstanding_num[0]:  
                '''
                outstanding_num = [item for item in outstanding_num if float(sub(r'[^\d.]', '', item))>100000]
                if return_condition(pre_name,tag_type,outstanding_num):
                    print(outstanding_num)
                    for num in outstanding_num:
                        write_text.write(num)
                        write_text.write('\t')
                    #write_text.write('\n')
                else:
                    pass


'''
Extract the outstanding shares from a given html file
'''
pre_name = 717954
keyword_ = 'outstanding'
files = [item for item in html_files if item.startswith(str(pre_name) + '_')]

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
    keyword_ = 'outstanding'
    p_text = get_paragraph_with_keyword(soup, 'p', keyword=keyword_)
    div_text = get_paragraph_with_keyword(soup, 'div', keyword=keyword_)
    # re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:.\d{2})?')
    # m = re.compile(r"(\d[\d\s.,]*)\s*?(?:[^%\d])")
    tr_text = get_paragraph_with_keyword(soup, 'tr', keyword='as a group')

    re_num = re.compile('\d{1,3}(?:\,\d{3})+(?:\.\d{2})?|\d{3}(?:\.\d{2})|\d{1,3}(?:\.\d{1,2})')
    f = open('./for_copy/{}.txt'.format(str(pre_name)), 'a')
    print_num(p_text, re_num, f, tag_type='p')
    print_num(div_text, re_num, f, tag_type='div')
    print_num(tr_text, re_num, f, tag_type='tr')
    f.write(file)
    f.write('\n')
    f.close()

    # print(re_num.findall(p_text)[:100])
    # print(m.findall(p_text))
    # print(re_num.findall(div_text)[:5])
    print(file)
