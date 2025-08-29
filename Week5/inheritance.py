
class Person:
    def __init__(self, name, age, address, person_id):
        self.name = name
        self.age = age
        self.address = address
        self.person_id = person_id


class Student(Person):
    def __init__(self, name, age, address, person_id, record):
        super().__init__(name, age, address, person_id)
        self.record = record


class Academic(Person):
    def __init__(self, name, age, address, person_id, salary):
        super().__init__(name, age, address, person_id)
        self.salary = salary


class GeneralStaff(Person):
    def __init__(self, name, age, address, person_id, pay_rate):
        super().__init__(name, age, address, person_id)
        self.pay_rate = pay_rate



s = Student("Alice", 20, "123 Street", "S001", "Excellent")
a = Academic("Dr. Bob", 45, "456 Avenue", "A101", 75000)
g = GeneralStaff("Charlie", 38, "789 Blvd", "G501", 25.5)

print(s.name, s.age, s.address, s.person_id, s.record)
print(a.name, a.age, a.address, a.person_id, a.salary)
print(g.name, g.age, g.address, g.person_id, g.pay_rate)




#calls to the parent constructor (Person.__init__) instead of super().

class Student(Person):
    def __init__(self, name, age, address, person_id, record):
        Person.__init__(self, name, age, address, person_id)
        self.record = record


class Academic(Person):
    def __init__(self, name, age, address, person_id, salary):
        Person.__init__(self,name, age, address, person_id)
        self.salary = salary


class GeneralStaff(Person):
    def __init__(self, name, age, address, person_id, pay_rate):
        Person.__init__(self,name, age, address, person_id)
        self.pay_rate = pay_rate



s = Student("Alice", 20, "123 Street", "S001", "Excellent")
a = Academic("Dr. Bob", 45, "456 Avenue", "A101", 75000)
g = GeneralStaff("Charlie", 38, "789 Blvd", "G501", 25.5)

print(s.name, s.age, s.address, s.person_id, s.record)
print(a.name, a.age, a.address, a.person_id, a.salary)
print(g.name, g.age, g.address, g.person_id, g.pay_rate)
