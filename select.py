# import shutil
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import numpy as np
import threading
from time import ctime

path = './txtfile'
prepath = './preprocess'
test = './test2'
sole = './sole'
_files = os.listdir(path)
_files.sort()

sole_files=[item for item in _files if item[-6:]=='_0.txt']

for file in sole_files:
    pass
   # shutil.copyfile(test+'/'+file, sole+'/'+file[5:-6]+'.txt')