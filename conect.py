import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# SQL-запит на вибірку всіх даних з таблиці "students"
cursor.execute("SELECT * FROM students")

# Отримання результату запиту
result = cursor.fetchall()

# Виведення результату
for row in result:
    print(row)

# Закриття курсора та з'єднання з базою даних
cursor.close()
conn.close()
