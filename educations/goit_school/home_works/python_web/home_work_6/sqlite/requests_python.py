import sqlite3


def execute_query(sql):
    with sqlite3.connect('students_sqlite.db') as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


sql1 = '''/*5 студентов с наибольшим средним баллом по всем предметам.*/
SELECT name, ROUND(AVG(mark), 1) as avg_mark
FROM students, marks
where students.id = marks.student_id 
GROUP BY name
ORDER BY  avg_mark DESC
LIMIT 5;'''

sql2 = '''/*1 студент с наивысшим средним баллом по одному предмету.*/
SELECT students.name, AVG(mark) as avg_mark, subjects.name
FROM marks, students,subjects
where marks.subject_id = subjects.id and students.id = marks.student_id and subjects.name = "Python_Core"
GROUP BY students.name
ORDER BY avg_mark DESC
LIMIT 1;'''

sql3 = '''/*средний балл в группе по одному предмету.*/
SELECT groups.name as N_group, ROUND(AVG(mark), 1) as avg_mark, subjects.name as subject
FROM marks, groups, students, subjects
WHERE marks.subject_id = subjects.id and students.group_id = groups.id and subjects.name = "Python_Core"
and groups.name = 222 and students.id = marks.student_id;'''

sql4 = '''/*Средний балл в потоке.*/
SELECT round(AVG(mark), 1)
FROM marks;'''

sql5 = '''/*Какие курсы читает преподаватель*/
SELECT teachers.name, subjects.name
FROM teachers, subjects
WHERE teachers.id = subjects.teacher_id and teachers.name = 'Angela Morgan';'''

sql6 = '''/*Список студентов в группе.*/
SELECT students.name
FROM groups, students
WHERE students.group_id = groups.id and groups.name = '333'
ORDER BY students.name;'''

sql7 = '''/*Оценки студентов в группе по предмету.*/
SELECT students.name, marks.mark
FROM groups, students, subjects, marks
WHERE students.group_id = groups.id and groups.name = '111' and subjects.name = 'Python_Core' and marks.student_id = students.id
ORDER BY students.name;'''

sql8 = '''/*Средний балл, который ставит преподаватель.*/
SELECT teachers.name as Teachers_name, ROUND(AVG(marks.mark), 1) as avg_mark
FROM groups, students, subjects, marks, teachers
WHERE subjects.id = marks.subject_id  and subjects.teacher_id = teachers.id
GROUP BY teachers.name;'''

sql9 = '''/*Список курсов, которые посещает студент.*/
SELECT subjects.name
FROM subjects, students, marks
WHERE students.id = marks.student_id and subjects.id = marks.subject_id  and students.name = 'Jason Ford'
GROUP BY subjects.name;'''

sql10 = '''/*Список курсов, которые студенту читает преподаватель.*/
SELECT teachers.name, subjects.name
FROM subjects, students, marks, teachers
WHERE students.id = marks.student_id and subjects.id = marks.subject_id  and students.name = 'Jason Ford'
and teachers.name = 'Belinda Smith' and subjects.teacher_id = teachers.id
GROUP BY subjects.name;'''

sql11 = '''/*Средний балл, который преподаватель ставит студенту.*/
SELECT students.name, round(AVG(mark), 1)
FROM groups, students, subjects, marks, teachers 
WHERE students.id = marks.student_id and subjects.id = marks.subject_id  and students.name = 'Jason Ford' 
and teachers.name = 'Angela Morgan' and subjects.teacher_id = teachers.id;'''

sql12 = '''/*Оценки студентов в группе по предмету на последнем занятии*/
SELECT students.name, marks.mark 
FROM groups, students, subjects, marks
WHERE students.group_id = groups.id and groups.name = '222' and subjects.name = 'Python_Core' and marks.student_id = students.id 
GROUP BY students.name;'''

if __name__ == '__main__':
    print(execute_query(sql1))
    print(execute_query(sql2))
    print(execute_query(sql3))
    print(execute_query(sql4))
    print(execute_query(sql5))
    print(execute_query(sql6))
    print(execute_query(sql7))
    print(execute_query(sql8))
    print(execute_query(sql9))
    print(execute_query(sql10))
    print(execute_query(sql11))
    print(execute_query(sql12))
