#!/usr/bin/env python
#see http://stackoverflow.com/questions/10069034/iterating-through-multiple-urls-from-txt-file-with-python-beautifulsoup
from bs4 import BeautifulSoup
import urllib
import csv
import re
url_list = []
csv_out = csv.writer(open('output.txt', 'w'), delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
try:
  f = open('advancedtitleauth.txt', 'rb')
  for line in f:
    url_list.append(line)
    r = urllib.urlopen(line).read()
    soup = BeautifulSoup(r)
    try:
      link = soup.find_all("div", class_="bibRecordLink")
      directlink = link[0]
      #todo: figure out a way to parse out the URLs so they are clickable
    except IndexError, e:
      directlink = "nolink"
    try:
      briefcit = soup.find_all("span", class_="briefcitTitle")
      bestmatch = briefcit[0]
    except IndexError, e:
      bestmatch = "nomatch"
    csv_out.writerow([directlink,bestmatch])
finally:  
  f.close()