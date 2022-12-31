
import sqlite3 as li
con=li.connect('mtica.db')
cur=con.cursor()
cur.execute("SELECT * FROM Cars")
rows=cur.fetchall()
for row in rows:
    print(row)

##print(" data values printed")

for row in rows:
    print("{0:*<3}|{1:*<15}| {2: >7}". format(row[0],row[1],row[2]))

##print(" data values printed")
