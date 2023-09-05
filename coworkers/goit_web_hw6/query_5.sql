-- 5. Знайти які курси читає певний викладач.

SELECT t.fullname as name, d.name as discipline
FROM teachers t
LEFT JOIN disciplines d ON d.teacher_id = t.id
WHERE t.id = 1
