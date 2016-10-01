from bs4 import *
import urllib

num = int()
url = urllib.urlopen(raw_input('Enter URL - '))

soup = BeautifulSoup(url, "html.parser")
tags = soup('span')

for tag in tags:
  data = tag.contents[0]
  num += int(data)

print num
