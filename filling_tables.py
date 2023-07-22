from faker import Faker
import sqlite3
import random

fake = Faker()

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Генерація даних для таблиць
groups = ["Group A", "Group B", "Group C"]
teachers = [(fake.first_name(), fake.last_name()) for _ in range(5)]
subjects = ["Mathematics", "Physics", "Chemistry",
            "Biology", "History", "English", "Computer Science"]
students_count = random.randint(30, 50)

# Заповнення таблиці "groups"
for group in groups:
    cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group,))

# Заповнення таблиці "teachers"
for teacher in teachers:
    cursor.execute(
        "INSERT INTO teachers (first_name, last_name) VALUES (?, ?)", teacher)

# Заповнення таблиці "subjects"
cursor.execute("SELECT teacher_id FROM teachers")
teacher_ids = [row[0] for row in cursor.fetchall()]
for subject in subjects:
    teacher_id = random.choice(teacher_ids)
    cursor.execute(
        "INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

# Заповнення таблиці "students" та "grades"
for _ in range(students_count):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, len(groups))
    cursor.execute("INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)",
                   (first_name, last_name, group_id))
    student_id = cursor.lastrowid
    for subject_id in range(1, len(subjects) + 1):
        for _ in range(random.randint(1, 20)):
            grade = random.uniform(2, 5)
            date_received = fake.date_between(
                start_date='-6M', end_date='today')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date_received))

# Збереження змін в базі даних та закриття з'єднання
conn.commit()
conn.close()
