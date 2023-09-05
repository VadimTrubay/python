-- 6. Знайти список студентів у певній групі.

SELECT gr.name as [group], s.fullname as name
FROM students s
LEFT JOIN groups gr ON gr.id = s.group_id
WHERE gr.id = 1
ORDER BY name
