# Create a class Book with attributes title, author, and pages. Instantiate three different books and display their details.

class Books:
    def __init__(self, book_name, author, pages):
        self.bookname = book_name
        self.bookauthor = author
        self.pages = pages

    def showBooks(self):
        print(f"The Title of Book is {self.bookname}")
        print(f"The Author Of Book {self.bookname} is {self.bookauthor} with pages of {self.pages}")


b = Books("one Piece", "Echioro Oda", "1157")
b.showBooks()