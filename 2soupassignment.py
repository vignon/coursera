from bs4 import *
import urllib

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
num = 0
names = []

for num in range(count):
  print 'Retrieving: {0}'.format(url)
  page = urllib.urlopen(url)
  soup = BeautifulSoup(page, "html.parser")
  tags = soup('a')
  data = tags[pos -1].string
  names.append(data)
  url = tags[pos - 1]['href']
  num += 1

print names[-1]




