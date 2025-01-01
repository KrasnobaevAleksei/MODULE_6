import sqlite3

# коннект с браузером
connection = sqlite3.connect("not_telegram.db")
# объект типа мышки для указания на ячейки
cursor = connection.cursor()

# траксировать запросы SQL напрямую в базу данных.
# Если запустить код во второй раз, первый запрос на создание таблицы 'Users' будет пропущен,
# так как она уже существует. Это происходит благодаря добавленной проверке 'IF NOT EXISTS',
# которая предотвращает создание дубликатов.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
for i in range(11):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?) ",
                   (f"User{i}", f"example{i}@gmail.com", i*10 , 1000))

for i in range(10):
    if i%2 != 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

for i in range(-2, 12, 3):
        cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?" , (60,))
users = cursor.fetchall()
for user in users:
    print(user)

#сохраняем
connection.commit()
#Закрываем
connection.close()