import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
  address = raw_input('Enter location: ')
  if len(address) < 1 : break

  url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

  uh = urllib.urlopen(url)
  print "Retrieving {}".format(url)

  data = uh.read()
  print "Retrieved {} characters".format(len(data))


  try: js = json.loads(str(data))
  except: js = None
  if 'status' not in js or js['status'] != 'OK':
      print '==== Failure To Retrieve ===='
      print data
      continue

  print "Place id {}".format(js['results'][0]['place_id'])
