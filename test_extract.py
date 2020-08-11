from bs4 import BeautifulSoup
import bs4
import re
import numpy as np
import os

html="""<p style="margin-top:12px;margin-bottom:0px; text-indent:7%"><font face="Times New Roman" size="2">Only holders of record of Class&nbsp;A Stock and Class B Stock on the books of the Company at the close of business on
May&nbsp;31, 2007, the Record Date for eligibility to vote at the Meeting, are entitled to notice of and to vote at the Meeting and at any adjournment thereof. Under arrangements established between the Company and CDN in connection with the
issuance of Constellation CDIs, the holders of Constellation CDIs are entitled to notice of and to attend the Meeting but may only vote at the Meeting as proxy for CDN in the circumstances described above. Except as otherwise required by Delaware
law, the holders of Class&nbsp;A Stock and the holders of Class B Stock vote together as a single class on all matters other than the election of the group of directors who are elected solely by the holders of the Class&nbsp;A Stock. Each holder of
Class&nbsp;A Stock is entitled to one (1)&nbsp;vote for each share of Class&nbsp;A Stock registered in such holder’s name, and each holder of Class B Stock is entitled to ten (10)&nbsp;votes for each </font>
</p>"""
keyword="one (1) vote"
soup = BeautifulSoup(html,'lxml')
ptag = soup.find('p')
t = ptag.get_text()
k = t.split()
text = ' '.join(k)

label = re.search(".*{}*.".format(keyword),' '.join(ptag.get_text().split()))

for tag in ptag:
    print(tag)