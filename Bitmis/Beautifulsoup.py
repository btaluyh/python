import urllib

from bs4 import *

url= 'http://python-data.dr-chuck.net/comments_319130.html'

links = list()


html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

count = 0

spans = soup('span')

for span in spans:
    print int(span.contents[0])

    count = count + int(span.contents[0])

    
##    print span.attrs


##    print span.get('href', None)


    
print count
