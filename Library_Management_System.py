#Write a Library class with no_of_books and books as two instance variables.
#Write a program to create a library from this Library class and 
#show how you can print all books, add a book and get the number of books using different methods. 
#Show that your program doesnt persist the books after the program is stopped!

class Library:

    def __init__(self, no_of_books, books):
        self.books = books
        self.no_books = no_of_books
    
    def add(self,book_name):
        if book_name not in self.books:
            self.books.append(book_name)
            self.no_books += 1

    def show_books(self):
        print(f"The library has {self.no_books} books. The books are : ")
        for book in self.books:
            print(book)

library1 = Library(3, ["Harry Potter", "The Rainbow", "A Lonely Sunday"])
library1.show_books()
library1.add("Beauty and the Beast")
library1.add("Sherlock Holmes")
library1.show_books()    