SELECT DISTINCT subjects.subject_id, subjects.subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.teacher_id = {teacher_id};
