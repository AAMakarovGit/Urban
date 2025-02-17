import sqlite3

def initiate_db():
    connection= sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection= sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",(username,email,age,1000))
    connection.commit()
    connection.close()

def is_included(username):
    user=True
    connection= sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    user=cursor.execute("SELECT * FROM Users WHERE username=?",(username,))
    if user.fetchone() is None:
        user=False
    connection.close()
    return user