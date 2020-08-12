import pandas as pd
import numpy as np
import os
import shutil

file = 'searching.xlsx'
html_from = './txt2html_files'
html_to   = './Dual_html'
html_files = os.listdir(html_from)

data = pd.read_excel(file)

dual = data[np.logical_or((data['Dual']=='T').values , (data['Dual']=='t').values) ]
dual_CIK = list(set(dual['CIK'].values))
dual_CIK.sort()

f = open('./with_keywords/keyword1.txt','r')
data = f.readlines()
data = data[::3]
data = [item[:-1] for item in data]
for CIK in dual_CIK:
    files = [item for item in data if item.endswith(str(CIK) + '_')]
    for file in data[8:]:
        shutil.copyfile(html_from+'/'+ file, html_to + '/' + file)


