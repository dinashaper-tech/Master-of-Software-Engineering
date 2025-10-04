import sqlite3
from database import setup_database, get_connection

def add_student():
    name = input("Enter student name: ")
    major = input("Enter major: ")
    intake = input("Enter intake: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Student (Name, Major, Intake) VALUES (?, ?, ?)", (name, major, intake))
    conn.commit()
    conn.close()
    print("Student added successfully!")

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Student WHERE StudentID=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

def add_teacher():
    name = input("Enter teacher name: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Teacher (Name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print("Teacher added successfully!")

def view_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Teacher")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def delete_teacher():
    teacher_id = input("Enter Teacher ID to delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Teacher WHERE TeacherID=?", (teacher_id,))
    conn.commit()
    conn.close()
    print("Teacher deleted successfully!")

def main():
    setup_database()
    while True:
        print("\nYoobee")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Add Teacher")
        print("5. View Teachers")
        print("6. Delete Teacher")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            add_teacher()
        elif choice == "5":
            view_teachers()
        elif choice == "6":
            delete_teacher()
        elif choice == "0":
            break
        else:
            print("Invalid choice, add correct code")

if __name__ == "__main__":
    main()
