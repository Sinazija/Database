import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Зчитуємо SQL-запит з файла query_5.sql та підставляємо значення змінної teacher_id
with open('query_5.sql', 'r') as file:
    # Припустимо, що шукаємо курси для викладача з ID=1
    sql_query = file.read().format(teacher_id=1)

# Виконуємо SQL-запит
cursor.execute(sql_query)

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    print(row[0], row[1])  # Виводимо ID та назву курсу

# Закриваємо з'єднання
conn.close()
