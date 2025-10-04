'''
Week 2 - Activity 7 : Develop a basic HR project using OO 

You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
Requirements:
Create at least two Employee objects with different data.
Call the display_info() method to show each employee’s details.
Call the give_raise() method to increase an employee’s salary and display the updated amount.
 '''

class Employee:

    def __init__(self,name,salary,job):
        self.name = name
        self.salary = salary
        self.job = job
        Employee.employees.append(self)

    employees = []
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"Job : {self.job}")
        print("\n")
    
    def salary_increase(self, increase):
       self.salary = self.salary + increase
       return self.name, self.salary, self.job
        
 
    
if __name__ == "__main__":

 employee1 = Employee("John", 5000, "Software Engineer")
 employee2 = Employee("Gim", 10000, "Senior Software Engineer")
 
 for emp in Employee.employees:
    emp.display_info()

 
 updated_salary1 =  employee1.salary_increase(1000)
 print(updated_salary1)
 updated_salary2 = employee2.salary_increase(2000)
 print(updated_salary2) 

    
