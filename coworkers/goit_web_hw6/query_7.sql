-- 7. Знайти оцінки студентів у окремій групі з певного предмета.

SELECT gr.name as [group], d.name as discipline, s.fullname as name,
       g.grade as grade, g.date_of as date
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN groups gr ON gr.id = s.group_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE gr.id = 3 AND d.id = 1
ORDER BY date
