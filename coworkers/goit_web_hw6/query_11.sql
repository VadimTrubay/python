-- 11. Середній бал, який певний викладач ставить певному студентові.

SELECT t.fullname as teacher, s.fullname as student,
       ROUND(AVG(g.grade), 2) as avg_grade, COUNT(g.grade) as count_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
JOIN students s ON s.id = g.student_id
WHERE s.id = 13 AND t.id = 1
