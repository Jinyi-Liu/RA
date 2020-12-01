from bs4 import BeautifulSoup
import urllib.request
import pickle
import pandas as pd
import re
import os

def14_path = r'C:\Users\Jinyi\PycharmProjects\RA\def14a\def14a_final_2'
def14 = os.listdir(def14_path)
re_code_date = re.compile('[\d]+_[\d]+')

filenames = sorted(def14,key = lambda x:int(re_code_date.findall(x)[0]))

q = [re_code_date.findall(i)[0].split('_') for i in def14]
code = [i[0] for i in q]
date = [i[1] for i in q]
_1 = {'CIK': code, 'FileDate': date}
_1 = pd.DataFrame(_1)
_1.iloc[:, 1] = pd.to_datetime(_1['FileDate'])
_1['CIK'] = _1['CIK'].astype(str).astype(int)
final = _1.copy()
with open('data/def14a_url_final.pk', 'rb') as fp:
    q = pickle.load(fp)

data_path = r'C:\Users\jinyi\Desktop\\'
data_txt = pd.read_excel(data_path + 'checking_txt.xlsx')
data_html = pd.read_excel(data_path + 'checking_html.xlsx')

data_txt.iloc[:, 3] = data_txt.iloc[:, 3].str.upper()
data_html.iloc[:, 3] = data_html.iloc[:, 3].str.upper()

tbd_txt = data_txt.loc[data_txt['Dual'] != 'F']
tbd_txt = tbd_txt.rename({'FileDate': 'FileDate_txt'}, axis=1)
tbd_html = data_html.loc[data_html['Dual'] != 'F']
tbd_html = tbd_html.rename({'FileDate': 'FileDate_html'}, axis=1)
all_data = pd.merge(tbd_html.iloc[:, :4], tbd_txt.iloc[:, :4], how='outer')
all_data.sort_values(by=['CIK', 'FileDate'], inplace=True)

c = pd.merge(all_data, final, how='outer', on='CIK')
delta = abs(c['FileDate_x'] - c['FileDate_y']) < pd.to_timedelta('3d')
check = c.loc[delta]
check = check.rename({'FileDate_x': 'FileDate_pre', 'FileDate_y': 'FileDate_new'}, axis=1)

check1 = pd.merge(check, final, how='outer', left_on=['CIK', 'FileDate_new'], right_on=['CIK', 'FileDate'])
check1.FileDate_new=[x if x!=z else z for (x,z) in zip(check1.FileDate_pre.values, check1.FileDate.values)]
check1.loc[pd.isnull(check1.FileDate_new),'FileDate_new'] = check1.loc[pd.isnull(check1.FileDate_new),'FileDate']
check1.sort_values(['CIK','FileDate_new'],inplace=True)

check2 = pd.merge(check1, tbd_html, how='outer', left_on=['CIK', 'FileDate_new'], right_on=['CIK', 'FileDate_html'])
check2.sort_values(['CIK','FileDate_pre'],inplace=True)
check3 = pd.merge(check2, tbd_txt.iloc[:, :4], how='outer', left_on=['CIK', 'FileDate_new'],right_on=['CIK', 'FileDate_txt'])
check3.sort_values(['CIK','FileDate_new'],inplace=True)
check3.reset_index(drop=True,inplace=True)
check3 = check3.drop(['Dual_y','CompanyName_y','FileDate_html','Dual','FileDate_txt','CompanyName'],axis=1)
check3 = check3.drop(check3.loc[pd.isnull(check3.FileDate)].index)
check3['newHYPER'] = [def14_path+'\\'+filename for filename in filenames]
check3.to_excel('check_final.xlsx', index=False)
for code in all_data.CIK:
    tbd = all_data.loc[all_data['CIK'] == code, 'FileDate']
    tbd.values[0]
