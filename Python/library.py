# Book class definition
class Book:
    
    # Constructor to initialize book details
    def __init__(self, book_id, title, author, is_available):
        self.book_id = book_id          # stores book ID
        self.title = title              # stores book title
        self.author = author            # stores book author
        self.is_available = is_available  # stores availability status (True/False)

    # Method to issue the book
    def issue_book(self):
        # Check if the book is available
        if self.is_available:
            self.is_available = False   # mark book as issued
            print(f"{self.title} Book issued successfully")
        else:
            print(f"{self.title} Book is already issued")

    # Method to return the book
    def return_book(self):
        # Check if the book was issued
        if not self.is_available:
            self.is_available = True    # mark book as available
            print(f"{self.title} Book returned successfully")
        else:
            print(f"{self.title} Book was not issued")

    # Method to display book details
    def show_details(self):
        print("Book Id:", self.book_id)
        print("Book Title:", self.title)
        print("Book Author:", self.author)
        print("Available (T/F):", self.is_available)


# Creating an object of Book class
Book1 = Book(1, 'Dictionary', 'xyz', True)

# Calling methods using the object
Book1.show_details()     # display initial details
Book1.issue_book()      # issue the book
Book1.show_details()    # display details after issuing
Book1.return_book()     # return the book
Book1.show_details()    # display final details
