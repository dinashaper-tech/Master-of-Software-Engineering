
#baseclass
class Person:
    def __init__(self, name, address, age, person_id):
        self.name = name
        self.address = address
        self.age = age
        self.person_id = person_id
    
    def greet(self):
        print(f"Hello, I am {self.name}, and I live at {self.address}.")


#subclass student
class Student(Person):
    def __init__(self, name, address, age, person_id, record):
        super().__init__(name, address, age, person_id)  
        self.record = record

    #overriding the greet method
    def greet(self):
        print(f"Hi, I am {self.name}, a student with record: {self.record}")


#subclass academic
class Academic(Person):
    def __init__(self, name, address, age, person_id, salary):
        super().__init__(name, address, age, person_id)
        self.salary = salary

    #overriding the greet method
    def greet(self):
        print(f"Good day, I am Dr. {self.name}, earning {self.salary}.")


#subclass generalStaff
class GeneralStaff(Person):
    def __init__(self, name, address, age, person_id, pay_rate):
        super().__init__(name, address, age, person_id)
        self.pay_rate = pay_rate

    #overriding the greet method
    def greet(self):
        print(f"Hello, I am {self.name}, my pay rate is {self.pay_rate} per hour.")



student = Student("Alice", "123 Street", 20, "S001", "Excellent")
academic = Academic("Bob", "456 Avenue", 45, "A101", 75000)
general_staff = GeneralStaff("Charlie", "789 Blvd", 38, "G501", 25.5)


student.greet()
academic.greet()
general_staff.greet()
