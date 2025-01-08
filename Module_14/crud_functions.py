import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    
    ''')
    connection.commit()
def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products ")
    users = cursor.fetchall()
    connection.commit()
    return users


# initiate_db()
# get_all_products()
# connection.commit()
# connection.close()