import pandas as pd
from func import get_processed
import numpy as np

all_data = get_processed.all_data
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
