import urllib
import json

url = raw_input('Enter location: ')
data = urllib.urlopen(url).read()

info = json.loads(data)
print sum ([int(item['count']) for item in info['comments']])
