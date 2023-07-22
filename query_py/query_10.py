import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT subjects.subject_name
    FROM subjects
    JOIN grades ON subjects.subject_id = grades.subject_id
    WHERE grades.student_id = 1;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    print(row[0])  # Виводимо назву курсу, який відвідує студент

# Закриваємо з'єднання
conn.close()
