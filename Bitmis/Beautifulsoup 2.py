import urllib

from bs4 import *



url= 'http://python-data.dr-chuck.net/known_by_Fikret.html'


m= 0

while m != 7:
    
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    links = soup('a')

    count = 0

    m = m +1
    


    for link in links:

        print count, '. isim'
        print link.get('href', None)
        
        count = count + 1

       
        
        
        if count == :

            url = link.get('href', None)
            break





    ##    print int(span.contents[0])co


    


    
