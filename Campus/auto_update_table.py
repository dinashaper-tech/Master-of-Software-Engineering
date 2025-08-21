# You can add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address. 
# Insert two sample records into Students, then display all rows from both the Users and Students tables.

# import sqlite3

# create connection
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# create Users table
cur.execute("CREATE TABLE Users (UserID INTEGER, UserName TEXT)")

# create Students table
cur.execute("CREATE TABLE Students (Stu_ID INTEGER, Stu_name TEXT, Stu_address TEXT)")

# create trigger
cur.execute("""
CREATE TRIGGER insert_user_after_student
AFTER INSERT ON Students
BEGIN
    INSERT INTO Users (UserID, UserName)
    VALUES (NEW.Stu_ID, NEW.Stu_name);
END;
""")


cur.executemany("INSERT INTO Students VALUES (?, ?, ?)", [
    (1, "Alice", "123 Main St"),
    (2, "Bob", "456 Oak Ave")
])

# display Users 
print("Users Table:")
for row in cur.execute("SELECT * FROM Users"):
    print(row)

# display Students
print("\nStudents Table:")
for row in cur.execute("SELECT * FROM Students"):
    print(row)

conn.close()
