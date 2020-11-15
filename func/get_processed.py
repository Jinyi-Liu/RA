import pandas as pd
import numpy

data_path = r'C:\Users\jinyi\Desktop\\'
data = pd.read_excel(data_path + 'checking_1011.xlsx')

T_data = data.loc[data['Dual'] == 'T']
tbd_data = data.loc[data['Dual'] == '?']

all_data = pd.concat([T_data, tbd_data])


def CIK_T_tbd():
    return sorted(list(set(all_data.CIK)))


def CIK_T():
    return sorted(list(set(T_data.CIK)))
