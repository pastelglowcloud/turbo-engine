import urllib.error
import urllib.request
from bs4 import BeautifulSoup

url = input('enter:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
