

import string

class Analyzer:
    def __init__(self, d):
        self.d = d

    def length(self):
        return len(self.d)

    def upper(self):
        if isinstance(self.d, str):
            return sum(1 for c in self.d if c.isupper())
        if isinstance(self.d, list):
            return sum(1 for i in self.d if isinstance(i, str) and i.isupper())
        return 0

    def digits(self):
        if isinstance(self.d, str):
            return sum(1 for c in self.d if c.isdigit())
        if isinstance(self.d, list):
            return sum(1 for i in self.d if isinstance(i, str) and i.isdigit())
        return 0

    def specials(self):
        s = set(string.punctuation)
        if isinstance(self.d, str):
            return sum(1 for c in self.d if c in s)
        if isinstance(self.d, list):
            return sum(1 for i in self.d if isinstance(i, str) and i in s)
        return 0


if __name__ == "__main__":
    TEXT = "Hello World! 123"
    a1 = Analyzer(TEXT)
    print("String:", TEXT)
    print("Len:", a1.length())
    print("Upper:", a1.upper())
    print("Digits:", a1.digits())
    print("Specials:", a1.specials())

    l = ["HELLO", "world", "AI", "Python3", "123", "!", 456]
    a2 = Analyzer(l)
    print("\nList:", l)
    print("Len:", a2.length())
    print("Upper:", a2.upper())
    print("Digits:", a2.digits())
    print("Specials:", a2.specials())
