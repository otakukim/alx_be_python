# library_system.py

# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library Class
class Library:
    def __init__(self):
        self.books = []  # a list to store Book, EBook, or PrintBook objects

    def add_book(self, book):
        # Ensure the added object is a Book or subclass of Book
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()

    # Create different types of books
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add them to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books
    my_library.list_books()

if __name__ == "__main__":
    main()

