import sqlite3
from datetime import datetime
import faker
from random import randint, choice

GROUPS = 3
STUDENTS = 30
SUBJECTS = 5
TEACHERS = 3
MARKS = 20


def generate_fake_data(students, teachers):
    fake_groups = [111, 222, 333]
    fake_students = []
    fake_subjects = ['Python_Core', 'Python_Web', 'Python_Data_Science', 'C', 'C#']
    fake_teachers = []
    fake_marks = [2, 3, 4, 5]
    fake_data = faker.Faker('en-US')

    for _ in range(students):
        fake_students.append(fake_data.name())

    for _ in range(teachers):
        fake_teachers.append(fake_data.name())

    return fake_students, fake_teachers, fake_groups, fake_marks, fake_subjects


def prepare_data(students, teachers, groups, marks, subjects):
    for_groups = []
    for_teachers = []
    for_subjects = []
    for_students = []
    for_marks = []

    for group in groups:
        for_groups.append((group,))
    for teacher in teachers:
        for_teachers.append((teacher,))
    for subject in subjects:
        for_subjects.append((subject, randint(1, TEACHERS)))
    for student in students:
        for_students.append((student, randint(1, GROUPS)))
    for month in range(1, 10 + 1):

        for student_id in range(1, STUDENTS + 1):
            for i in range(1, 10 + 1):
                m_date = datetime(2023, randint(1, 12), randint(1, 28)).date()
                for_marks.append((student_id, randint(1, SUBJECTS), choice(marks), m_date))
    return for_students, for_teachers, for_groups, for_marks, for_subjects


def insert_data_to_db(students, teachers, groups, marks, subjects):
    with sqlite3.connect('students_sqlite.db') as con:
        cur = con.cursor()
        sql_to_groups = """INSERT INTO groups(name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(name)
                                VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_students = """INSERT INTO students(name, group_id)
                                VALUES(?,?)"""
        cur.executemany(sql_to_students, students)

        sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                                VALUES(?,?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, created_at)
                                VALUES(?,?,?,?)"""
        cur.executemany(sql_to_marks, marks)
        
        con.commit()


if __name__ == '__main__':
    students, teachers, groups, marks, subjects = generate_fake_data(STUDENTS, TEACHERS)
    students, teachers, groups, marks, subjects = prepare_data(students, teachers, groups, marks, subjects)
    insert_data_to_db(students, teachers, groups, marks, subjects)
    print('Success inserting data to database')