#Week 5 Activity 7: Applying inheritance and encapsulation techniques, with detailed explanations for each syntax element, class, method, and the overall project.

class LibraryItem:
    def __init__(self, title, author):
        self._title = title      # protected attribute
        self._author = author

    def display_details(self):
        pass   # to be overridden


# inherits from LibraryItem
class Book(LibraryItem):
    def display_details(self):
        print(f"Book: {self._title} by {self._author}")


# inherits from LibraryItem
class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self._issue_frequency = issue_frequency

    def display_details(self):
        print(f"Magazine: {self._title} by {self._author}, "
              f"Issue: {self._issue_frequency}")


# to manage items
class Library:
    def __init__(self):
        self._items = []   # list to store items

    def add_item(self, item):
        self._items.append(item)

    def display_all_items(self):
        for item in self._items:
            item.display_details()


lib = Library()
lib.add_item(Book("1984", "George Orwell"))
lib.add_item(Magazine("Time", "Various", "Weekly"))
lib.display_all_items()

