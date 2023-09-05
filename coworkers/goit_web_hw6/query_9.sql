-- 9. Знайти список курсів, які відвідує студент.

SELECT s.fullname as student, d.name as discipline
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id 
JOIN students s ON s.id = g.student_id
WHERE s.id = 4
GROUP BY discipline
ORDER BY discipline
