class Book:
    """Represents a single book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books and supports basic library operations."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books._
