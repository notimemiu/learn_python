import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
data = urllib.urlopen(url).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

print sum([int(count.text) for count in counts])
