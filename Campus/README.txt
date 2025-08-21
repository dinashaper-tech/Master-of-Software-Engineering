Add new records (adding a new student or teacher)
View existing records (see the list of students or teachers)
Delete records (remove a student or teacher from the system)

Database
Student → StudentID, Name, Major, Intake
Teacher → TeacherID, Name
Subject → SubjectID, Name
Class → ClassID, SubjectID, TeacherID, Time
Student_Class → StudentID, ClassID (this keeps track of which students are in which classes)

Run command
python main.py
