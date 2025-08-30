class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade

    # method using private attribute
    def is_pass(self):
        return self.__grade == 'A'


# class to show public and protected
class GraduateStudent(Student):
    def show_details(self):
        print("Name:", self.name)   # public
        print("Age:", self._age)    # protected



s = Student("Ali", 20)
print(s.name)         # public
print(s._age)         # protected (discouraged)
print(s.get_grade())  # private via method
print(s.is_pass())    # private via method

g = GraduateStudent("Sara", 24)
g.show_details()

# Encapsulation means keeping data safe by controlling access.
# Public: free to use
# Protected: use only inside class or subclasses
# Private: hidden, only class methods can use
