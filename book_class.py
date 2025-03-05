# Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.publication_year = 2021

# the title, author and publication year of the book.
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
# Add a __repr__ magic method to the Book class.

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.publication_year}')"
    
# Add a __str__ magic method to the Book class that returns a string with     
    def __del__(self):
        print(f"The book {self.title} has been deleted.")

    