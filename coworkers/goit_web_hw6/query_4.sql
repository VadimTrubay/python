-- 4. Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT ROUND(AVG(g.grade), 2) as avg_grade, COUNT(grade) as count_grade
FROM grades g
