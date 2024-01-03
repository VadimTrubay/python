from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/postgres")
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete="CASCADE"))


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    group_id = Column(Integer, ForeignKey('groups.id', ondelete="CASCADE"))


class Marks(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"))
    subjects_id = Column(Integer, ForeignKey('subjects.id', ondelete="CASCADE"))
    mark = Column(Integer)
    created_at = Column(Date)


Base.metadata.create_all(engine)
Base.metadata.bind = engine
