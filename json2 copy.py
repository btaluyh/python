import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_319131.json'
data = urllib.urlopen(url).read()

info = json.loads(data)

count = 0
for a in info:
    print a


for i in info['comments']  :

    print i['count']

    count = count + int(i['count'])


print 'Total sum : ' , count
