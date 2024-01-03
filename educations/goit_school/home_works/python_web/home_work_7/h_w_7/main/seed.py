import psycopg2
from datetime import datetime
import faker
from random import randint, choice
from models import session, Groups, Teachers, Subjects, Students, Marks

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
    for group in groups:
        new_group = Groups(name=f"{group}")
        session.add(new_group)
        session.commit()

    for teacher in teachers:
        new_teacher = Teachers(name=f"{teacher}")
        session.add(new_teacher)
        session.commit()

    for subject in subjects:
        new_subject = Subjects(name=f"{subject}", teacher_id=randint(1, TEACHERS))
        session.add(new_subject)
        session.commit()

    for student in students:
        new_student = Students(name=f"{student}", group_id=randint(1, GROUPS))
        session.add(new_student)
        session.commit()

    for month in range(1, 10 + 1):
        for student_id in range(1, STUDENTS + 1):
            for mark in range(1, 10 + 1):
                m_date = datetime(2023, randint(1, 12), randint(1, 28)).date()
                new_marks = Marks(student_id=f"{mark}", subjects_id=randint(1, SUBJECTS), mark=choice(marks), created_at=m_date)
                session.add(new_marks)
                session.commit()


def insert_students_to_db():
    for student in range(30):
        new_student = Students(name=f"{fake_data.name()}")
        session.add(new_student)
        session.commit()


if __name__ == '__main__':
    students, teachers, groups, marks, subjects = generate_fake_data(STUDENTS, TEACHERS)
    prepare_data(students, teachers, groups, marks, subjects)

    print('Success inserting data to database')