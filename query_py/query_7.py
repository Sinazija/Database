import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT students.student_id, students.first_name, students.last_name
    FROM students
    WHERE students.group_id = 1;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    # Виводимо ID, ім'я та прізвище студентів у групі
    print(row[0], row[1], row[2])

# Закриваємо з'єднання
conn.close()
