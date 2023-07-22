SELECT students.student_id, students.first_name, students.last_name, grades.grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE students.group_id = {group_id} AND grades.subject_id = {subject_id};
