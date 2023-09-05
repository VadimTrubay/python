-- 5 �������� �� ��������� ������� ����� � ��� ��������.
SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.fullname, s.id
ORDER BY avg_grade DESC
LIMIT 5;

--1 ������� �� �������� ������� ����� � ������ ��������.
SELECT d.name, s.fullname, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 1
GROUP BY s.fullname, d.name
ORDER BY avg_grade DESC
LIMIT 1;

--������� ��� � ���� �� ������ ��������.
SELECT d.name, gr.name, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3
GROUP BY gr.name, d.name
ORDER BY avg_grade DESC;

--������� ��� � ������.
SELECT round(avg(g.grade), 2) AS avg_grade 
FROM grades g;

--�� ����� ���� ��������.
SELECT d.id, t.fullname, d.name 
FROM teachers t 
LEFT JOIN disciplines d ON t.id = d.teacher_id
WHERE t.id = 3;

--������ �������� � ����.
SELECT s.id, s.fullname, gr.name
FROM students s 
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 3;

--������ �������� � ���� � ��������.
SELECT s.id, d.name, gr.name, s.fullname, g.grade, g.date_of  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3 AND gr.id = 3;

--������ �������� � ���� � �������� �� ���������� ������.
SELECT g.date_of 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE g.discipline_id = 2 AND gr.id = 3
ORDER BY g.date_of DESC 
LIMIT 1;

SELECT s.id, d.name, gr.name, s.fullname, g.grade, g.date_of  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3 AND gr.id = 3 AND g.date_of = (SELECT g.date_of 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE g.discipline_id = 3 AND gr.id = 3
ORDER BY g.date_of DESC 
LIMIT 1);

-- ������ �����, �� ����� �������
SELECT d.name, s.fullname 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE g.student_id = 1
GROUP BY d.name;

--������ �����, �� �������� ���� ��������.
SELECT s.fullname, t.fullname, d.name 
FROM grades g  
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1 AND g.student_id = 1
GROUP BY d.name;

--������� ���, ���� �������� ������� ��������
SELECT DISTINCT s.fullname, t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g  
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1 AND s.id = 3
GROUP BY s.fullname;

--������� ���, ���� ������� ��������
SELECT t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g  
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
GROUP BY t.fullname;

SELECT *
FROM grades g  
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id;
