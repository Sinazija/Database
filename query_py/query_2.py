import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT students.student_id, students.first_name, students.last_name, AVG(grades.grade) as average_grade
    FROM students
    JOIN grades ON students.student_id = grades.student_id
    WHERE grades.subject_id = 1
    GROUP BY students.student_id
    ORDER BY average_grade DESC
    LIMIT 1;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    # Виводимо ID, ім'я, прізвище та середній бал студента
    print(row[0], row[1], row[2], row[3])

# Закриваємо з'єднання
conn.close()
