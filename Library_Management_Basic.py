class Book:
    '''Book class contains all necessary details related to the book'''
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Issued: {self.is_issued}")

class Member:
    '''Member class is built for tracking members in the library'''
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def display_info(self):
        print(f"Name: {self.name}, Member ID: {self.member_id}")

class Library:
    '''Library class manages the entire library'''
    def __init__(self):
        self.books = []
        self.members = []
        self.borrows = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def remove_member(self, member_id):
        member = self.find_member(member_id)
        if member:
            # If the member has borrowed books, return all borrowed books
            if member_id in self.borrows:
                for isbn in self.borrows[member_id]:
                    book = self.find_book(isbn)
                    if book:
                        book.is_issued = False  # Mark the book as not issued
                del self.borrows[member_id]

            # Remove the member from the members list
            self.members.remove(member)
            print(f"Member '{member.name}' and all associated borrow records have been removed.")
        else:
            print(f"Member with ID {member_id} does not exist.")

    def issue_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        # Checking for member and book that match condition or if none of them match
        if member and book and not book.is_issued:
            book.is_issued = True
            if member_id not in self.borrows:
                self.borrows[member_id] = []
            self.borrows[member_id].append(isbn)
            print(f"Book '{book.title}' issued to member '{member.name}'.")
        else:
            print("Issue failed. Either the book is already issued or the member/book does not exist.")

    def return_book(self, member_id, isbn):
        if member_id in self.borrows and isbn in self.borrows[member_id]:
            book = self.find_book(isbn)
            # Checking if book is borrowed by member and getting book details
            if book:
                book.is_issued = False
                self.borrows[member_id].remove(isbn)
                print(f"Book '{book.title}' returned by member with ID {member_id}.")
            else:
                print("Return failed. Book not found.")
        else:
            print("Return failed. Loan record not found.")

    def find_book(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def find_member(self, member_id):
        return next((member for member in self.members if member.member_id == member_id), None)

    def display_books(self):
        for book in self.books:
            book.display_info()

    def display_members(self):
        for member in self.members:
            member.display_info()

    def display_borrows(self):
        for member_id, books in self.borrows.items():
            book_titles = [self.find_book(isbn).title for isbn in books]
            print(f"Member ID: {member_id}, Books: {', '.join(book_titles)}")

# Sample usage
if __name__ == "__main__":
    library = Library()

    # Add books
    print("\nAdding books to the library...")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "2345678901")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "3456789012")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display books
    print("\nDisplaying all books in the library:")
    library.display_books()

    # Add members
    print("\nAdding members to the library...")
    member1 = Member("Alice Johnson", "1")
    member2 = Member("Bob Smith", "2")
    member3 = Member("Charlie Brown", "3")
    library.add_member(member1)
    library.add_member(member2)
    library.add_member(member3)

    # Display members
    print("\nDisplaying all members of the library:")
    library.display_members()

    # Issue books
    print("\nIssuing books to members...")
    library.issue_book("1", "1234567890")  # The Great Gatsby to Alice
    library.issue_book("2", "2345678901")  # 1984 to Bob

    # Display borrows
    print("\nDisplaying all current borrows:")
    library.display_borrows()

    # Return books
    print("\nReturning books...")
    library.return_book("1", "1234567890")  # Alice returns The Great Gatsby

    # Display borrows again to verify return
    print("\nDisplaying all current borrows after return:")
    library.display_borrows()

    # Remove a member
    print("\nRemoving a member...")
    library.remove_member("1")  # Remove Alice

    # Display members again to verify removal
    print("\nDisplaying all members after removing one:")
    library.display_members()

    # Display borrows again to verify removal of borrows records for removed member
    print("\nDisplaying all current borrows after member removal:")
    library.display_borrows()


