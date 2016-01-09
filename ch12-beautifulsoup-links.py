# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter: ')
count = raw_input('Count: ')
position = raw_input('Position: ')

# url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Esha.html"
# count = 7
# position = 18

i = 0
while i < int(count):
  i += 1
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)

  # Retrieve all of the anchor tags
  tags = soup('a')
  url = tags[int(position)-1].get('href', None)

# just the name
print "{}".format(re.findall("_by_(.+)\.html$", tags[int(position)-1].get('href', None))[0])
