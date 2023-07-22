import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT AVG(grades.grade) as average_grade
    FROM grades;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    print(row[0])  # Виводимо середній бал на потоці

# Закриваємо з'єднання
conn.close()
