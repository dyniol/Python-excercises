import sqlite3
 
 
def connect_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
    "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

 
def insert_db(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                   (title, author, year, isbn))
    connection.commit()
    connection.close()
     
     
def view_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows
 
 
def search_db(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                   (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows
 
 
def delete_db(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()
 
 
def update_db(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author, year, isbn, id))
    connection.commit()
    connection.close()
 
 
#insert_db('Visual Thinking', 'Willemien Brand', 2017, 9789063694531)
#insert_db('Manhood', 'Cath Tate', 2014, 9781909396395)
#insert_db('Wine Folly', 'Madeline Puckette', 2018, 9780525533894)
#update_db(4, 'MacOSX', 'Gaff', 2020, 123456)