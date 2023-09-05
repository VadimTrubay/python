--
-- File generated with SQLiteStudio v3.3.3 on Пн Лис 22 20:49:31 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;
-- Table: disciplines
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL,
    teacher_id REFERENCES teachers (id)
);
-- Table: groups
DROP TABLE IF EXISTS [groups];
CREATE TABLE [groups] (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING UNIQUE
);
-- Table: ratings
DROP TABLE IF EXISTS ratings;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    discipline_id REFERENCES disciplines (id),
    date_of DATE NOT NULL,
    grade INTEGER NOT NULL
);
-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname STRING UNIQUE NOT NULL,
    group_id REFERENCES [groups] (id)
);
-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname STRING UNIQUE NOT NULL
);
COMMIT TRANSACTION;
PRAGMA foreign_keys = on;