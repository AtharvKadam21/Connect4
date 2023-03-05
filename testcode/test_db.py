import mysql.connector
import os

os.system("grant all privileges on *.* to 'root'@'localhost' with grant option;")

c4db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='connect4'
)

cursor = c4db.cursor()
cursor.execute("INSERT INTO connect4.user_accounts VALUES('Playr', 'Blue', 'Red');")
cursor.execute('SELECT * FROM user_accounts')
res=cursor.fetchall()
print(res)