import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT students.student_id, students.first_name, students.last_name, grades.grade, grades.date_received
    FROM students
    JOIN grades ON students.student_id = grades.student_id
    WHERE students.group_id = 1 AND grades.subject_id = 1;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    # Виводимо ID, ім'я, прізвище, оцінку та дату отримання оцінки
    print(row[0], row[1], row[2], row[3], row[4])

# Закриваємо з'єднання
conn.close()
