
class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"This is a {self.name}."



class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


def multiply(x, y):
    return x * y



if __name__ == "__main__":
    
    square = Square(5)
    print(square.display())
    print("Area:", square.area())
