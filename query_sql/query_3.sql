SELECT groups.group_id, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.group_id = students.group_id
JOIN grades ON students.student_id = grades.student_id
WHERE grades.subject_id = {subject_id}
GROUP BY groups.group_id;
