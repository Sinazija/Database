import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT AVG(grades.grade) as average_grade
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.subject_id
    WHERE subjects.teacher_id = 1;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    print(row[0])  # Виводимо середній бал викладача зі своїх предметів

# Закриваємо з'єднання
conn.close()
