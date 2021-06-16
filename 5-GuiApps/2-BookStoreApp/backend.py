import sqlite3
 
class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connection.commit()
    
    def insert_db(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                    (title, author, year, isbn))
        self.connection.commit()        
        
    def view_db(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        return rows    
    
    def search_db(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows    
    
    def delete_db(self, id):
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        self.connection.commit()    
    
    def update_db(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                    (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()