#Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book): 
        def __init__(self, title, author, format_, file_size):
            super().__init__(title, author)
            self.file_size = file_size    
            self.format = format_

        def __str__(self):
           return f"{self.title} by {self.author}, {self.file_size}MB in {self.format} format"

class PrintBook(Book):
        def __init__(self, title, author, pages):
            super().__init__(title, author)
            self.pages = pages

        def __str__(self):
            return f"{self.title} by {self.author} with {self.pages} pages"

class Library(Book):
        def __init__(self):
            self.books = []

        def add_book(self, book):
            self.books.append(book)

        def list_books(self):
            for book in self.books:
                print(book)
