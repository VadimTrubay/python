-- 12. Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT gr.name as [group], d.name as discipline, s.fullname as student,  g.grade as grade, g.date_of as date
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
WHERE d.id = 3 AND gr.id = 2  
     AND  date = (SELECT MAX(g.date_of) FROM grades g
     JOIN  students s ON s.id = g.student_id
     WHERE discipline_id = 3 AND group_id = 2)
