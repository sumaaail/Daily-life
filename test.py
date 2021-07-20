import sqlite3
from flask import jsonify
conn = sqlite3.connect('database.db')
c = conn.cursor()
print('connected successfully')
# print([0 == len(''.join(node)) for node in c.execute("SELECT pwd FROM user WHERE uid = 5")])
data = []
# for row in c.execute("SELECT pwd FROM user WHERE uid = 5"):
#     data.append(row)
# print(jsonify(data))
print('xhr' in [node[0] for node in c.execute("SELECT uname FROM user ")])
conn.commit()
print('inserted successfully')
conn.close()

