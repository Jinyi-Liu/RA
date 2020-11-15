import shutil
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime

path = './txtfile'
prepath = './preprocess'
test = './test2'
sole = './processed_sole'
_files = os.listdir(path)
_files.sort()


processed_file = os.listdir(test)[1:]
processed_file = [item[4:] for item in processed_file]
processed_file.sort()

not_processed = set.difference(set(_files), set(processed_file))


sole_processed_files = [item for item in processed_file if item[-6:]=='_0.txt']

q = re.compile(r'\d+')
for file in sole_processed_files:
    shutil.copyfile(test+'/test'+file, sole+'/'+q.findall(file)[0]+'.txt')
