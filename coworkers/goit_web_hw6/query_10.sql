-- 10. Список курсів, які певному студенту читає певний викладач.

SELECT s.fullname as student, t.fullname as teacher, d.name as discipline
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id
JOIN students s ON s.id = g.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 4 AND t.id = 2
GROUP BY discipline
ORDER BY discipline
