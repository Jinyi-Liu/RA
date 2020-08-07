import shutil
import os
import re

txt_path = './txtfile'
html_path = './txt2html_files'

txt_files = os.listdir(txt_path)

for txt_file in txt_files:
    shutil.copyfile(txt_path+'/'+txt_file, html_path+'/'+txt_file[:-3]+'html')
