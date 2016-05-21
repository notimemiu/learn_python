import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')

while count >= 0:
    print 'Retrieving: ', url
    count = int(count) - 1
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[int(position) - 1].get('href', None)
    #print 'Retrieving:', url
