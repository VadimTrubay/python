from sqlalchemy.orm import joinedload
from models import session, Groups, Teachers, Subjects, Students, Marks
from sqlalchemy import func, desc, and_


# 5 студентов с наибольшим средним баллом по всем предметам
def select_1():
    select = session.query(Students.name, func.round(func.avg(Marks.mark), 2).label('avg_mark'), Subjects.name). \
        select_from(Students, Marks, Subjects). \
        filter(Marks.subjects_id == Subjects.id, Students.id == Marks.student_id). \
        group_by(Students.name, Subjects.name). \
        order_by(desc('avg_mark')). \
        limit(5).all()
    print(select)


# 1 студент с наивысшим средним баллом по одному предмету
def select_2():
    select = session.query(Students.name, func.round(func.avg(Marks.mark), 2).label('avg_mark'), Subjects.name). \
        select_from(Students, Marks, Subjects). \
        filter(Marks.subjects_id == Subjects.id, Students.id == Marks.student_id, Subjects.name == 'Python_Core'). \
        group_by(Students.name, Subjects.name). \
        order_by(desc('avg_mark')). \
        limit(1).all()
    print(select)

# средний балл в группе по одному предмету
def select_3():
    select = session.query(Subjects.name, Groups.name, func.round(func.avg(Marks.mark), 2).
                           label('avg_mark')).  \
        select_from(Students, Marks, Subjects, Groups). \
        join(Marks, Marks.subjects_id == Subjects.id). \
        join(Students, Students.group_id == Groups.id). \
        join(Students, Students.id == Marks.student_id). \
        filter(Subjects.name == 'Python_Core'). \
        filter(Groups.name == 222). \
        group_by(Students.name).\
        order_by(desc('avg_mark')).\
        limit(1).all()
    print(select)


# средний балл в группе по одному предмету
def select_3():
    select = session.query(Groups.name, func.round(func.avg(Marks.mark), 2).label('avg_mark'), Subjects.name). \
        select_from(Subjects, Groups, Marks, Students). \
        filter(Marks.subjects_id == Subjects.id, Students.group_id == Groups.id, Subjects.name == 'Python_Web',
               Groups.name == '111', Students.id == Marks.student_id). \
        group_by(Groups.name, Subjects.name, Students.name).first()
    print(select)


# Средний балл в потоке
def select_4():
    select = session.query(func.round(func.avg(Marks.mark), 2).label('avg_mark')). \
        select_from(Marks).all()
    print(select)


#Какие курсы читает преподаватель
def select_5():
    select = session.query(Teachers.name, Subjects.name). \
        select_from(Teachers, Subjects). \
        filter(Teachers.id == Subjects.teacher_id, Teachers.name == 'Francis Ellis').all()
    print(select)


# Список студентов в группе
def select_6():
    select = session.query(Students.name, Groups.name). \
        select_from(Students, Groups). \
        filter(Students.group_id == Groups.id, Groups.name == '222').all()
    print(select)


# Оценки студентов в группе по предмету
def select_7():
    select = session.query(Groups.name, Students.name, Marks.mark, Subjects.name). \
        select_from(Groups, Students, Marks, Subjects). \
        filter(Marks.subjects_id == Subjects.id, Students.group_id == Groups.id, Groups.name == '333', Subjects.name == 'C', Marks.student_id == Students.id).\
        order_by(Students.name).all()
    print(select)


# Средний балл, который ставит преподаватель
def select_8():
    select = session.query(Teachers.name, func.round(func.avg(Marks.mark), 2).label('avg_mark')). \
        select_from(Marks, Teachers). \
        filter(Subjects.id == Marks.subjects_id, Subjects.teacher_id == Teachers.id).\
        group_by(Teachers.name).all()
    print(select)


# Список курсов, которые посещает студент
def select_9():
    select = session.query(Subjects.name, Students.name). \
        select_from(Subjects, Students, Marks). \
        filter(Students.id == Marks.student_id, Subjects.id == Marks.subjects_id, Students.name == 'Richard Schmitt').\
        group_by(Subjects.name, Students.name).all()
    print(select)


#Список курсов, которые студенту читает преподаватель
def select_10():
    select = session.query(Students.name, Teachers.name, Subjects.name). \
        select_from(Subjects, Students, Teachers). \
        filter(Students.id == Marks.student_id, Subjects.id == Marks.subjects_id, Students.name == 'Richard Schmitt', Teachers.name == 'Francis Ellis', Subjects.teacher_id == Teachers.id).\
        group_by(Students.name, Teachers.name, Subjects.name).all()
    print(select)


#Средний балл, который преподаватель ставит студенту
def select_11():
    select = session.query(Students.name, func.round(func.avg(Marks.mark), 2).label('avg_mark')). \
        select_from(Subjects, Students, Teachers, Marks). \
        filter(Students.id == Marks.student_id, Subjects.id == Marks.subjects_id, Students.name == 'Richard Schmitt', Teachers.name == 'Francis Ellis', Subjects.teacher_id == Teachers.id).\
        group_by(Students.name).all()
    print(select)


#Оценки студентов в группе по предмету на последнем занятии
def select_12():
    select = session.query(Students.name, Marks.mark). \
        select_from(Subjects, Students, Marks, Groups). \
        filter(Students.group_id == Groups.id, Groups.name == '222', Subjects.name == 'Python_Core', Marks.student_id == Students.id).\
        group_by(Students.name, Marks.mark).all()
    print(select)


if __name__ == '__main__':
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()
    select_11()
    select_12()
