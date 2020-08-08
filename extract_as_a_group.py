from bs4 import BeautifulSoup
import bs4
import re
import numpy as np
import os

html_path = './txt2html_files'
html_files = os.listdir(html_path)
html_files.sort()

keyword = ['as a group', 'as a Group']
tag_search = 'tr'

