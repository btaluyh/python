import urllib
from bs4 import *

url= 'http://www.met.yildiz.edu.tr/getOneAnnounce.php?id=610'
url3= 'http://www.bioeng.yildiz.edu.tr/getOneAnnounce.php?id=297'

def duyuru (url):


    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    count = 0

    divs = soup('div')


    for res in divs:

        if count == 1:
            count = count + 1
            print 'Tarih: %s' %res.text
        if count == 0:
            count = count + 1
            print 'Baslik: %s' %res.text

        if res.txt == 0:
            return 'heey'
        else:           
            print res.text

            

count = 605

while count < 1000:
    count = count + 1
    url5= 'http://www.met.yildiz.edu.tr/getOneAnnounce.php?id=%d' %count
    duyuru(url5)





##html = urllib.urlopen(url).read()
##
##soup = BeautifulSoup(html, 'html.parser')
##
##count = 0
##
##divs = soup('div')
##
##
##for res in divs:
##    print res.text
##

    
