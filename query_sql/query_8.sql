SELECT AVG(grades.grade) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE subjects.teacher_id = {teacher_id};
