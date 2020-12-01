"""
We think all that companies in T or preferred type are dual-class companies.
"""

import pandas as pd
import os
import re
import pickle
def14 = os.listdir('def14a_final')


with open('data/def14a_url_final.pk','rb') as fp:
    check = pickle.load(fp)



data_path = r'C:\Users\jinyi\Desktop\\'
data_txt = pd.read_excel(data_path + 'checking_txt.xlsx')
data_html = pd.read_excel(data_path + 'checking_html.xlsx')

data_txt.iloc[:, 3] = data_txt.iloc[:, 3].str.upper()
data_html.iloc[:, 3] = data_html.iloc[:, 3].str.upper()

tbd_txt = data_txt.loc[data_txt['Dual'] != 'F']
tbd_html = data_html.loc[data_html['Dual'] != 'F']


all_data = pd.concat([tbd_html.iloc[:,:4], tbd_txt.iloc[:,:4]])
all_data.sort_values(by=['CIK'],inplace=True)


def CIK_all():
    return sorted(list(set(all_data.CIK)))



