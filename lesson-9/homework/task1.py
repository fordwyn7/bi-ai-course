class BookNotFoundException(Exception):
    """Exception raised when a book is not found in the library."""
    def __init__(self, message="Book not found in the library."):
        self.message = message
        super().__init__(self.message)

class BookAlreadyBorrowedException(Exception):
    """Exception raised when a book is already borrowed."""
    def __init__(self, message="Book is already borrowed by another user."):
        self.message = message
        super().__init__(self.message)

class MemberLimitExceededException(Exception):
    """Exception raised when a member exceeds the borrowing limit."""
    def __init__(self, message="Member has exceeded the borrowing limit."):
        self.message = message
        super().__init__(self.message)

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = True

    def __repr__(self):
        return f"Book({self.book_id}, {self.title}, {self.author}, Available: {self.available})"
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __repr__(self):
        return f"Member({self.name}, Borrowed Books: {len(self.borrowed_books)})"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.borrowed_books = {}
        self.borrow_limit = 3

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book_id] = {"title": title, "author": author, "available": True}

    def add_member(self, member_id, name):
        if member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member_id] = {"name": name, "borrowed_books": []}

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise KeyError("Member not found.")
        if book_id not in self.books:
            raise BookNotFoundException()
        if not self.books[book_id]["available"]:
            raise BookAlreadyBorrowedException()
        if len(self.members[member_id]["borrowed_books"]) >= self.borrow_limit:
            raise MemberLimitExceededException()

        self.books[book_id]["available"] = False
        self.members[member_id]["borrowed_books"].append(book_id)
        self.borrowed_books[book_id] = member_id

    def return_book(self, member_id, book_id):
        if book_id not in self.borrowed_books or self.borrowed_books[book_id] != member_id:
            raise BookNotFoundException("This book was not borrowed by this member.")
        
        self.books[book_id]["available"] = True
        self.members[member_id]["borrowed_books"].remove(book_id)
        del self.borrowed_books[book_id]

Library = Library()
Library.add_book("1", "1984", "George Orwell")
Library.add_member("101", "Alice")
try:
    Library.borrow_book("101", "1")
    print("Book borrowed successfully.")
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(f"Error: {e.message}")
try:
    Library.return_book("101", "1")
    print("Book returned successfully.")
except BookNotFoundException as e:
    print(f"Error: {e.message}")