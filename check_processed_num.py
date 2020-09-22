import pandas as pd
import numpy as np

data_path = r'C:\Users\jinyi\Desktop\\'
data = pd.read_excel(data_path + 'checking_.xlsx')

T_data = data.loc[data['Dual']=='T']
tbd_data = data.loc[data['Dual']=='?']

all_data = pd.concat([T_data,tbd_data])

all_data.to_excel('T&tdb.xlsx',index=False)
'''
CIK = data.CIK.values
unique_CIK = list(set(CIK))
unique_CIK.sort()

check = data.loc[:, ['CIK', 'Dual']]
check.loc[check['Dual'] == ' ', 'Dual'] = np.nan
not_processed = check.loc[pd.isnull(check)['Dual']]
not_CIK = not_processed.CIK.values
unique_not_CIK = list(set(not_CIK))
unique_not_CIK.sort()

print(len(unique_CIK))
print('Not processed number: {}'.format(len(unique_not_CIK)))
import time
print(time.ctime())
'''
