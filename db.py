import mysql.connector

c4db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123'
  ,    database='Connect4'
)

cursorObj = c4db.cursor()
'''cursorObj.execute("CREATE DATABASE Connect4")'''

'''cursorObj.execute("CREATE TABLE User_Accounts (name VARCHAR(255), board_Color VARCHAR(255), coin_Color VARCHAR(255))")'''
cursorObj.execute("INSERT INTO User_Accounts VALUES('Player', 'Blue', 'Red');")
cursorObj.execute('SELECT * FROM User_Accounts')