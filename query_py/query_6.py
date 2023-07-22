import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT subjects.subject_name
    FROM subjects
    WHERE subjects.teacher_id = 1;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    print(row[0])  # Виводимо назву курсу, який читає викладач

# Закриваємо з'єднання
conn.close()
