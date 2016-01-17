import urllib
import json

url = raw_input('Enter location: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_190860.json'

uh = urllib.urlopen(url)
print "Retrieving {}".format(url)

data = uh.read()
print "Retrieved {} characters".format(len(data))

info = json.loads(data)

total = 0
tally = 0
for item in info['comments']:
  tally += 1
  total += int(item['count'])

print "Count: {}".format(tally)
print "Sum: {}".format(total)