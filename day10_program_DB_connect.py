
import sqlite3 as li
con=li.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute(''' CREATE TABLE Cars( id INT, name TEXT, price INT)''')
print('table Cars creaated.')
cur.execute("INSERT INTO Cars VALUES(1,'aulto',517424)")
cur.execute("INSERT INTO Cars VALUES(2,'jeep',617424)")
cur.execute("INSERT INTO Cars VALUES(3,'sift',789542)")
cur.execute("INSERT INTO Cars VALUES(4,'Volvo',787424)")


con.commit()
print("values in table car inserted.")
