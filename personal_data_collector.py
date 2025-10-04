#Week 2 - Activity 6: Develop an OO project using list of object data types

class ListManipulator:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
   
 
    words = []
    def add_list(self):
        ListManipulator.words.append(("name:",self.name))
        ListManipulator.words.append(("age:",self.age))
        ListManipulator.words.append(("address:",self.address))
        return ListManipulator.words
    
    def promotion_calculate(self, years):
        self.age = self.age + years
        return self.name, self.age, self.address

    
if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")

    data = ListManipulator(name,age,address)
    details = data.add_list()
    print(details)

    years = int(input("Enter your next promotion expected time in years: "))
    updated_list = data.promotion_calculate(years)
    print(updated_list)




