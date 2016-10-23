import xml.etree.ElementTree as ET
import re
import urllib

toplam = 0

url = 'http://python-data.dr-chuck.net/comments_319127.xml'

data = urllib.urlopen(url).read()

tree = ET.fromstring(data)

print'this is tree', tree

lst = tree.findall('comments/comment')


for item in lst:
##    print "Name :", item.find('name').text
    print 'Count :', item.find('count').text

    toplam = toplam + int(item.find('count').text)


print toplam
