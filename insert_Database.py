import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
print('connected successfully')

# c.execute("INSERT INTO fav(uid, fav)  VALUES (1, 'I love eating hamburger')")
# c.execute("INSERT INTO fav(uid, fav)  VALUES (1, 'I love jin bao')")
# c.execute("INSERT INTO fav(uid, fav)  VALUES (1, 'I hate eating southeast foot')")
# c.execute("INSERT INTO fav(uid, fav)  VALUES (1, 'xhr is stupid')")
# c.execute("INSERT INTO fav(uid, fav)  VALUES (2, 'ggg')")
# c.execute("DELETE FROM news")

for row in c.execute("SELECT * FROM news"):
    print(row)

conn.commit()
print('inserted successfully')
conn.close()