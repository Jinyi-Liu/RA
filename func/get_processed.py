import pandas as pd
import numpy

data_path = r'C:\Users\jinyi\Desktop\\'
data = pd.read_excel(data_path + 'checking_.xlsx')

T_data = data.loc[data['Dual'] == 'T']
tbd_data = data.loc[data['Dual'] == '?']

all_data = pd.concat([T_data, tbd_data])


def CIK():
    return sorted(list(set(all_data.CIK)))
