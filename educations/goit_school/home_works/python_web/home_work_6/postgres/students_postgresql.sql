-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups(
id SERIAL PRIMARY KEY,
name VARCHAR(30));

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers(
id SERIAL PRIMARY KEY,
name VARCHAR(30));

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects(
id SERIAL PRIMARY KEY,
name VARCHAR(30),
teacher_id INT,
FOREIGN KEY (teacher_id) REFERENCES teachers (id)
ON DELETE SET NULL
ON UPDATE CASCADE);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students(
id SERIAL PRIMARY KEY,
name VARCHAR(35),
group_id INT,
FOREIGN KEY (group_id) REFERENCES groups (id)
ON DELETE SET NULL
ON UPDATE CASCADE);

-- Table: marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks(
id SERIAL PRIMARY KEY,
student_id INT,
subject_id INT,
mark INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
FOREIGN KEY (student_id) REFERENCES students (id),
FOREIGN KEY (subject_id) REFERENCES subjects (id)
ON DELETE SET NULL
);
