import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

print sum([int(tag.contents[0]) for tag in tags])
#sum = 0
#for tag in tags:
    #sum = sum + int(tag.contents[0])
#print sum 
