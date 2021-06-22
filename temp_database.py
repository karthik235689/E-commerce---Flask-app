import sqlite3

conn = sqlite3.connect('database.db')

conn.execute("INSERT INTO users VALUES (1,'karthik','karthik23052001@gmail.com','katakam','karthik','maruthinagar','kothapet','500036','hyderabad','telangana','India','7382909540')")

conn.commit()
conn.close()