import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконуємо запит
cursor.execute("""
    SELECT groups.group_name, AVG(grades.grade) as average_grade
    FROM groups
    JOIN students ON groups.group_id = students.group_id
    JOIN grades ON students.student_id = grades.student_id
    WHERE grades.subject_id = 1
    GROUP BY groups.group_id;
""")

# Отримуємо результат
results = cursor.fetchall()
for row in results:
    print(row[0], row[1])  # Виводимо назву групи та середній бал

# Закриваємо з'єднання
conn.close()
