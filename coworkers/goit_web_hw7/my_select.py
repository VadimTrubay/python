from sqlalchemy import func, desc, select, and_
from prettytable import from_db_cursor
from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


def select_1():
    """
     -- 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

        SELECT s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        GROUP BY s.id 
        ORDER BY avg_grade DESC
        LIMIT 5;
    """
    result = session.query(
        Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student)\
        .group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

def select_2():
    """
    -- 2. Знайти студента із найвищим середнім балом з певного предмета.

        SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN disciplines d ON d.id = g.discipline_id 
        WHERE d.id = 5
        GROUP BY s.id
        ORDER BY avg_grade DESC
        LIMIT 1;
    """
    result = session.query(
        Discipline.name,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Discipline)\
        .filter(Discipline.id == 5)\
        .group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).limit(1).first()
    return result

def select_3():
    """
    -- 3. Знайти середній бал у групах з певного предмета.

        SELECT gr.name as [group], d.name as discipline, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN disciplines d ON d.id = g.discipline_id
        LEFT JOIN [groups] gr ON gr.id = s.group_id 
        WHERE d.id = 1
        GROUP BY gr.id
        ORDER BY avg_grade DESC;
    """
    result = session.query(
        Group.name.label('group'),
        Discipline.name.label('discipline'),
        func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Discipline).join(Group)\
        .filter(Discipline.id == 1)\
        .group_by(Group.id, Discipline.name).order_by(desc('avg_grade')).all()
                    
    return result

def select_4():
    """
    -- 4. Знайти середній бал на потоці (по всій таблиці оцінок).

        SELECT ROUND(AVG(g.grade), 2) as avg_grade, COUNT(grade) as count_grade
        FROM grades g
    """
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade'),
        func.count(Grade.grade).label('count_grade'))\
        .select_from(Grade).all()
    return result

def select_5():
    """
    -- 5. Знайти які курси читає певний викладач.

        SELECT t.fullname as name, d.name as discipline
        FROM teachers t
        LEFT JOIN disciplines d ON d.teacher_id = t.id
        WHERE t.id = 1
    """
    result = session.query(
        Teacher.fullname.label('name'), Discipline.name.label('discipline'))\
        .select_from(Teacher). join(Discipline).filter(Teacher.id == 1).all()
    return result

def select_6():
    """
    -- 6. Знайти список студентів у певній групі.

        SELECT gr.name as [group], s.fullname as name
        FROM students s
        LEFT JOIN groups gr ON gr.id = s.group_id
        WHERE gr.id = 1
        ORDER BY name
    """
    result = session.query(
        Group.name.label('group'), Student.fullname.label('name'))\
        .select_from(Student).join(Group).filter(Group.id == 1)\
        .order_by('name').all()
    return result

def select_7():
    """
    -- 7. Знайти оцінки студентів у окремій групі з певного предмета.

        SELECT gr.name as [group], d.name as discipline, s.fullname as name,
            g.grade as grade, g.date_of as date
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN groups gr ON gr.id = s.group_id
        LEFT JOIN disciplines d ON d.id = g.discipline_id
        WHERE gr.id = 3 AND d.id = 1
        ORDER BY date
    """
    result = session.query(
        Group.name. label('group'), Discipline.name.label('disccipline'),
        Student.fullname.label('name'), Grade.grade.label('grade'),
        Grade.date_of.label('date'))\
        .select_from(Grade).join(Student).join(Group).join(Discipline)\
        .filter(and_(Group.id == 3, Discipline.id == 1)).order_by('date').all()
    return result

def select_8():
    """
    -- 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.

        SELECT t.fullname as name, ROUND(AVG(g.grade), 2) as avg_grade,
            COUNT(g.grade) as [count] 
        FROM grades g
        LEFT JOIN disciplines d ON d.id = g.discipline_id
        LEFT JOIN teachers t ON t.id = d.teacher_id
        WHERE t.id = 5
    """
    result = session.query(
        Teacher.fullname.label('teacher'),
        func.round(func.avg(Grade.grade), 2).label('avg_grade'),
        func.count(Grade.grade).label('count'))\
        .select_from(Grade).join(Discipline).join(Teacher)\
        .filter(Teacher.id == 2).group_by('teacher').one()
    return result

def select_9():
    """
    -- 9. Знайти список курсів, які відвідує студент.

        SELECT s.fullname as student, d.name as discipline
        FROM disciplines d
        JOIN grades g ON g.discipline_id = d.id 
        JOIN students s ON s.id = g.student_id
        WHERE s.id = 4
        GROUP BY discipline
        ORDER BY discipline
    """
    result = session.query(
        Student.fullname.label('student'),
        Discipline.name.label('discipline'))\
        .select_from(Discipline).join(Grade).join(Student)\
        .filter(Student.id == 4).group_by('discipline', 'student')\
        .order_by('discipline').all()
    return result

def select_10():
    """
    -- 10. Список курсів, які певному студенту читає певний викладач.

        SELECT s.fullname as student, t.fullname as teacher, d.name as discipline
        FROM disciplines d
        JOIN grades g ON g.discipline_id = d.id
        JOIN students s ON s.id = g.student_id
        JOIN teachers t ON t.id = d.teacher_id
        WHERE s.id = 4 AND t.id = 2
        GROUP BY discipline
        ORDER BY discipline    
    """
    result = session.query(
        Student.fullname.label('student'),
        Teacher.fullname.label('teacher'),
        Discipline.name.label('discipline'))\
        .select_from(Discipline).join(Grade).join(Student).join(Teacher)\
        .filter(and_(Student.id == 4, Teacher.id == 2))\
        .group_by('discipline', 'student', 'teacher').order_by('discipline').all()
    return result

def select_11():
    """
    -- 11. Середній бал, який певний викладач ставить певному студентові.

        SELECT t.fullname as teacher, s.fullname as student,
            ROUND(AVG(g.grade), 2) as avg_grade, COUNT(g.grade) as count_grade
        FROM grades g
        JOIN disciplines d ON d.id = g.discipline_id
        JOIN teachers t ON t.id = d.teacher_id
        JOIN students s ON s.id = g.student_id
        WHERE s.id = 13 AND t.id = 1
    """
    result = session.query(
        Teacher.fullname.label('teacher'),
        Student.fullname.label('student'),
        func.round(func.avg(Grade.grade), 2).label('avg_grade'),
        func.count(Grade.grade))\
        .select_from(Grade).join(Discipline).join(Student).join(Teacher)\
        .filter(and_(Student.id == 13, Teacher.id == 4))\
        .group_by('student', 'teacher').one()    
    return result
    
def select_12():
    """
    -- Оцінки студентів у певній групі з певного предмета на останньому занятті.
    select s.id, s.fullname, g.grade, g.date_of
    from grades g
    join students s on s.id = g.student_id
    where g.discipline_id = 3 and s.group_id = 3 and g.date_of = (
        select max(date_of)
        from grades g2
        join students s2 on s2.id = g2.student_id
        where g2.discipline_id = 3 and s2.group_id = 3
    );
    :return:
    """
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(
        Grade.discipline_id == 3, Student.group_id == 3
    )).scalar_subquery())

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date_of)\
                    .select_from(Grade)\
                    .join(Student)\
                    .filter(and_(
                        Grade.discipline_id == 3, Student.group_id == 3,
                        Grade.date_of == subquery
                    )).all()
    return result


# if __name__ == '__main__':
#     # print(select_1())
#     # print()
#     # print(select_one_new())
#     # print(select_2())
#     print()
#     print(select_11())

#     # print(select_12())
#     # print(from_db_cursor(select_one_new()))
