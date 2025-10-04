import sqlite3

def get_connection():
    return sqlite3.connect("school.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT,
        Major TEXT,
        Intake TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Teacher (
        TeacherID INTEGER PRIMARY KEY,
        Name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subject (
        SubjectID INTEGER PRIMARY KEY,
        Name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Class (
        ClassID INTEGER PRIMARY KEY,
        SubjectID INTEGER,
        TeacherID INTEGER,
        Time TEXT,
        FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID),
        FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student_Class (
        StudentID INTEGER,
        ClassID INTEGER,
        PRIMARY KEY (StudentID, ClassID),
        FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
        FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
    )
    """)

    conn.commit()
    conn.close()
