import json
import urllib



url = 'https://api.import.io/store/connector/f56836d6-1abf-41c4-b2a0-ef90fc929cf6/_query?input=webpage/url:http%3A%2F%2Fmet.yildiz.edu.tr%2Fduyurular.php&&_apikey=306c8f942cf14564bf50a17fd8f32c29bf03689fc36321f73b2d067813d1a0636d9745d2507088493cca854d3e62864b554b16142834b3e02d580f772e78a904264f5bb6ba43e0a5797cd441fa05858d'
data = urllib.urlopen(url).read()


info = json.loads(data)



#for a in info:
#    print a




for b in info['results']:
    print b['my_column']
    

for a in info:
    print a
