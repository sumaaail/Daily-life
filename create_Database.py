import sqlite3

conn = sqlite3.connect('database.db')
print("open database successfully")

c = conn.cursor()
# c.execute('CREATE TABLE students(ID int NOT NULL, NAME TEXT NOT NULL, AGE int NOT NULL, ADDRESS CHAR(50))')
# c.execute('CREATE TABLE user(uid INTEGER PRIMARY KEY AUTOINCREMENT, uname varchar(20) NOT NULL , pwd varchar(20) NOT NULL, phone varchar(20))')
# c.execute('CREATE TABLE fav(favid INTEGER PRIMARY KEY AUTOINCREMENT, uid int NOT NULL, fav MESSAGE_TEXT )')
c.execute('CREATE TABLE news(title MESSAGE_TEXT , text MESSAGE_TEXT )')

print("Table created")

conn.close()