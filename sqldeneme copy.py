import re

import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: ') :
        continue
    pieces = line.split()
    emails = pieces[1]
    stripper = re.findall(r'@[\w\.-]+', emails)
    for i in stripper:
        print i

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (i, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( i, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (i, ))



conn.commit()



cur.close()

