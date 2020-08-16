from bs4 import BeautifulSoup
import re
import numpy as np
import os
from re import sub

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()
re_seq = re.compile('\d+')
outstanding_limit = 20000


def get_tag_with_keyword_in_text(tags, keyword):
    if keyword == 'one (1) vote':
        keyword = '.*one \(\d+\) vote*.'
    if len(tags) == 0:
        return []
    tags_text = [' '.join(tag.get_text().split()) for tag in tags]
    if tags[0].name == 'tr':
        index = 0
        tags_index = []
        for (tag_text, tag) in zip(tags_text, tags):
            if re.search(keyword, tag_text, re.IGNORECASE):  # Locate the tag which contains keyword from its text
                tags_index.append(index)
            index += 1
        tags_return = []
        for index in tags_index:
            if index >= 1:
                tags_return.extend(tags_text[index-1:index+2])  # Get the previous and the next tag.
            else:
                tags_return.extend(tags_text[index:index+2])  # Special case.
        return tags_return
    else:
        # Not tr tag.
        return [tag_text for tag_text in tags_text if re.search(keyword, tag_text, re.IGNORECASE)]


def get_contents(all_tags, keyword):
    """
    tag_contents: to store the contents in tags which have keyword
    tags_with_interest: to store the tags which have key word
    keyword: like ['as a group','as a Group'] but this situation is solved by re.IGNORECASE which will ignore the case.
    """
    tags_with_interest = []
    # To get the tags with keyword in their text
    if type(keyword) != list:
        tags_with_interest.extend(get_tag_with_keyword_in_text(all_tags, keyword))
    else:
        for keyword_sole in keyword:
            tags_with_interest.extend(get_tag_with_keyword_in_text(all_tags, keyword_sole))

    return tags_with_interest


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


def get_paragraph_with_keyword(soup_para, tag_search, keyword):
    """
    tags: All the tags with name "tag_search"
    """
    tags = soup_para.find_all(tag_search)

    tags_contents = get_contents(tags, keyword)

    return tags_contents


def return_whether_outstanding_share(outstanding_num):
    for _ in outstanding_num:
        if float(sub(r'[^\d.]', '', _)) < outstanding_limit:
            return False
    return True


def get_value(num_with_comma):
    if num_with_comma == '*':
        return 0
    else:
        return float(sub(r'[^\d.]', '', num_with_comma))


def return_whether_as_a_group(outstanding_num, CIK):
    CIK_list_5 = [1050825]  # as a group table like 1,285,403 2,547,716	 7.2 19,870,718 20.4 42,743
    CIK_list_6 = [1090727]
    iter_as_a_group_num = iter(outstanding_num)
    share_num = iter_as_a_group_num.__next__()
    if CIK in CIK_list_5:
        if len(outstanding_num) >= 3 and get_value(outstanding_num[-2]) <= 101:
            return True
        elif len(outstanding_num) >= 3 and get_value(outstanding_num[-1]) <= 101:
            return True
        elif len(outstanding_num) == 2 and get_value(outstanding_num[0])>outstanding_limit and get_value(outstanding_num[1])<=105:
            return True
        else:
            return False
    elif len(outstanding_num) >= 3 and get_value(outstanding_num[-1]) <= 101:
        return True

    while True:
        try:
            per_num = iter_as_a_group_num.__next__()
            if per_num == '*' or share_num == '*':
                return True
            elif get_value(share_num) >= outstanding_limit and get_value(per_num) <= 101:
                return True
            else:
                share_num = iter_as_a_group_num.__next__()
        except StopIteration:
            return False



pre_name = 6948
def return_condition(CIK, tag_type=None, outstanding_num=None):
    index = False
    CIK_list = [356080, 357294]
    CIK_list_1 = [717954, 778164, 788329, 789933, 805792, 807707, 808461, 811828, 826821, 859139, 860413, 861058,
                  863456, 867773, 872589]  # outstanding 2 types
    CIK_list_2 = [796735, 858452, 859735, 880117, 1100395, 1134061, 1439404]  # outstanding 3 types
    CIK_list_3 = [887733, 911177, 922487, 923877, 924940, 944136, 1012620, 1070534, 109483, 1095996, 1099358, 1142417,
                  1166691, 1232241, 1288469, 1288776,3116]  # 2 types and 3 types
    CIK_list_5 = [1061069, 1112263, 1344154, 1528356]  # 2\3\4 types
    CIK_list_4 = [928658, 1232241, 1463833, 1468174, 1481792, 1514514, 1541401]  # more than 4 types
    # Below search for ownership percent
    if tag_type == 'tr' and return_whether_as_a_group(outstanding_num, CIK):
        return True  # stands for continue

    if CIK in CIK_list_4:
        if len(outstanding_num) >= 4 and return_whether_outstanding_share(outstanding_num):
            index = True
    elif CIK in CIK_list_5:
        if len(outstanding_num) == 2 or (len(outstanding_num) == 4) or len(outstanding_num) == 5:
            index = True
    elif CIK in CIK_list_3:
        if len(outstanding_num) == 2 or (
                len(outstanding_num) == 3 and return_whether_outstanding_share(outstanding_num)):
            index = True
    elif CIK in CIK_list_2:
        if len(outstanding_num) == 3:
            index = True
    else:
        if len(outstanding_num) >= 2 and return_whether_outstanding_share(outstanding_num):
            index = True
    return index


def print_num(tag_text, re_method, tag_type=None):
    """
    Need more modification!
    """
    return_list = []
    for _ in tag_text:
        outstanding_num = re_method.findall(_)
        if len(outstanding_num) >= 1:
            if tag_type == 'tr':
                if return_condition(pre_name, tag_type, outstanding_num):
                    return_list.append(outstanding_num)
            else:
                outstanding_num = [item for item in outstanding_num if
                                   float(sub(r'[^\d.]', '', item)) > outstanding_limit]
                if return_condition(pre_name, tag_type, outstanding_num):
                    return_list.append(outstanding_num)
    return return_list


def to_float(share_list):
    total_list = []
    search_max_list = []
    for _list in share_list:
        _num_list = []
        for _num in _list:
            float_num = float(sub(r'[^\d.]', '', _num))
            _num_list.append(float_num)
            search_max_list.append(float_num)
        total_list.append(_num_list)
    return total_list, search_max_list


def delete_duplicate(tag_list):
    temp = []
    for _ in tag_list:
        if _ not in temp:
            temp.append(_)
    return temp


def get_seq(file_name):
    return int(re_seq.findall(file_name)[1])


'''
Extract the outstanding shares from a given html file
'''
files = [item for item in html_files if item.startswith(str(pre_name) + '_')]
files.sort(key=get_seq)


def write_to_file(num_list, file_to_write):
    for _ in num_list:
        file_to_write.write(_)
        file_to_write.write('\t')

#files=['5133_1.html']


for file in files:
    data = open(html_path + '/' + file)
    handle = data.read()
    soup = BeautifulSoup(handle, 'lxml')
    soup = soup.find('document')

    keyword_share = 'outstanding'
    keyword_tr = 'as a group'
    # keyword_1023128 = 'All current executive officers and directors as a'
    keyword_1053112 = "All executive officers and directors"

    p_text = get_paragraph_with_keyword(soup, 'p', keyword=keyword_share)
    div_text = get_paragraph_with_keyword(soup, 'div', keyword=keyword_share)
    tr_text = get_paragraph_with_keyword(soup, 'tr', keyword=[keyword_tr, keyword_1053112])

    re_num = re.compile('\d{1,3}(?:,\d{3})+(?:\.\d{2})?|\d{3}(?:\.\d{2})|\d{1,3}(?:\.\d{1,2})')
    re_tr = re.compile('\d{1,3}(?:,\d{3})+(?:\.\d{2})?|\d{3}(?:\.\d{2})|\d{1,3}(?:\.\d{1,2})|100|\*')
    f = open('./for_copy/{}.txt'.format(str(pre_name)), 'a')

    as_a_group_list = delete_duplicate(print_num(tr_text, re_tr, tag_type='tr'))
    # Get outstanding share.
    p_list = print_num(p_text, re_num, tag_type='p')
    div_list = print_num(div_text, re_num, tag_type='div')
    str_share_list = delete_duplicate(p_list + div_list)
    float_share_list, max_list = to_float(str_share_list)
    max_list.sort(reverse=True)

    out_share_list=[]
    for _, __ in zip(float_share_list, str_share_list):
        if max_list[0] in _:
            out_share_list = __
            break
    if len(out_share_list) >= 1:
        write_to_file(out_share_list, f)
    if len(as_a_group_list) >= 1:
        write_to_file(as_a_group_list[0], f)
        if len(as_a_group_list) >= 2:
            write_to_file(as_a_group_list[1], f)
    f.write(file)
    f.write('\n')
    # print_num(tr_asa_text,re_num,f,tag_type='tr')
    f.close()
    print(file)

