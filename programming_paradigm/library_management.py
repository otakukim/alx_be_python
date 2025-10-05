class Book:
    def __init__(self, title, author):
        """Initialize the book with title and author, and set it as available."""
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []  # Changed to _books to match test

    def add_book(self, book):
        """Add a Book object to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.is_checked_out:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Return a list of titles of available books."""
        return [book.title for book in self._books if not book.is_checked_out]

