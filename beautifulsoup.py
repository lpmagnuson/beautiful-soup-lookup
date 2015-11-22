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
      directlink = str(link[0])
      directlink = "http://suncat.csun.edu" + directlink[36:]
    except IndexError, e:
      directlink = "nolink"
    try:
      link = soup.find_all("td", class_="bibInfoData")
      pubinfo = str(link[2])
      pubinfo = pubinfo[24:-7]
    except IndexError, e:
      pubinfo = "nopub"
    try:
      briefcit = soup.find_all("span", class_="briefcitTitle")
      bestmatch = str(briefcit[0])
      sep = "&"
      bestmatch = bestmatch.split(sep, 1)[0]
      bestmatch = "http://suncat.csun.edu/" + bestmatch[39:]
    except IndexError, e:
      bestmatch = "nomatch"
    csv_out.writerow([pubinfo,directlink,bestmatch])
finally:  
  f.close()