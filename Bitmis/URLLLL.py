##import urllib
##
##fhand = urllib.urlopen ("http://www.wom.works")
##
##
##for line in fhand:
##
##        print line.strip()
##
##
import socket
import re


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break

    for content in data :
        m = re.findall("^C.+?:", content)

        if not m == []:
            print m

    
    

mysock.close()
