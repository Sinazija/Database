import sqlite3

# Підключення до бази даних або створення нової бази даних, якщо вона не існує
conn = sqlite3.connect('mydatabase.db')

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# SQL-запит для створення таблиці студентів
create_students_table_query = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    group_id INTEGER NOT NULL
);
"""

cursor.execute(create_students_table_query)

# SQL-запит для створення таблиці груп
create_groups_table_query = """
CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY,
    group_name TEXT NOT NULL
);
"""

cursor.execute(create_groups_table_query)

# SQL-запит для створення таблиці викладачів
create_teachers_table_query = """
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
"""

cursor.execute(create_teachers_table_query)

# SQL-запит для створення таблиці предметів
create_subjects_table_query = """
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
);
"""

cursor.execute(create_subjects_table_query)

# SQL-запит для створення таблиці оцінок
create_grades_table_query = """
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    grade REAL NOT NULL,
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
);
"""

cursor.execute(create_grades_table_query)

# Закриття курсора та збереження змін в базі даних
cursor.close()
conn.commit()

# Закриття з'єднання з базою даних
conn.close()
