import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_190856.xml'

uh = urllib.urlopen(url)
print "Retrieving {}".format(url)

data = uh.read()
print "Retrieved {} characters".format(len(data))

tree = ET.fromstring(data)
counts = tree.findall('.//count')

total = 0
tally = 0
for c in counts:
  tally += 1
  total += int(c.text)

print "Count: {}".format(tally)
print "Sum: {}".format(total)