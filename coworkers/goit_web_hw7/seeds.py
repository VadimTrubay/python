from datetime import date, datetime, timedelta
from random import randint, choice
from faker import Faker
from sqlalchemy import select

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session

'''
Создаем свою ф-цию для получения списка дат, в которые происходит учебный процесс.
Для упрощения выбрасываем только дни, которые попадают на выходные.
'''


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result



'''Функция генерации фейковых данных и заполнения ими БД'''


def fill_data():
    # Не все данные будут динамические. Создаем списки предметов и групп
    disciplines = [
        "Аналітична геометрія",
        "Теорія міри та інтегралу",
        "Математична логіка",
        "Теорія ймовірностей та математична статистика",
        "Лінійна алгебра та геометрія",
        "Теорія функцій комплексної змінної",
        "Функціональний аналіз",
        "Теоретична фізика",
        "Математичний аналіз"
    ]

    groups = ['М4-82', 'ТЙ', 'МА']

    # Создаем объект библиотеки Faker. В качестве параметра передаем local 'uk-UA'
    # Больше - https://faker.readthedocs.io/en/master/locales.html
    fake = Faker('uk-UA')
    number_of_teachers = 5
    number_of_students = 50

    def seed_teachers():
        for _ in range(number_of_teachers):
            teacher = Teacher(fullname=fake.name())
            session.add(teacher)
        session.commit()


    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline,
                        teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(number_of_students):
            student = Student(fullname=fake.name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()

    def seed_grades():
        # дата начала учебного процесса
        start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
        # дата окончания учебного процесса
        end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")
        now = datetime.now()
        if end_date > now:
            end_date = now
        d_range = date_range(start=start_date, end=end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:  # пройдемся по каждой дате
            random_id_discipline = choice(discipline_ids)
            random_ids_student = [choice(student_ids) for _ in range(5)]
            # проходимся по списку "везучих" студентов, добавляем их в результирующий список
            # и генерируем оценку
            for student_id in random_ids_student:
                grade = Grade(grade=randint(1, 12), date_of=d, student_id=student_id,
                              discipline_id=random_id_discipline)
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == '__main__':
    fill_data()
