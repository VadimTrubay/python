-- 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.fullname as name, ROUND(AVG(g.grade), 2) as avg_grade,
       COUNT(g.grade) as [count] 
FROM grades g
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 5
