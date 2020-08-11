import pandas as pd
import numpy as np
import os
import shutil

file = 'searching.xlsx'
html_from = './read_html'
html_to   = './Dual_html'
html_files = os.listdir(html_from)

data = pd.read_excel(file)

dual = data[np.logical_or((data['Dual']=='T').values , (data['Dual']=='t').values) ]
dual_CIK = list(set(dual['CIK'].values))
dual_CIK.sort()


for CIK in dual_CIK:
    files = [item for item in html_files if item.startswith(str(CIK) + '_')]
    for file in files:
        shutil.copyfile(html_from+'/'+ file, html_to + '/' + file)


