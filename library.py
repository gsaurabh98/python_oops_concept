class Library:

    def __init__(self,listOfBooks):
        self.availableBook = listOfBooks
    #decorator has been used below, because we are not using self.
    @staticmethod
    def inputs():
        print '\nPress 1 to show available books'
        print 'Press 2 to borrow the books'
        print 'Press 3 to return the books'
        print 'Press 4 to exit\n'

    def displayAvailableBooks(self):
        print '\nAvailabe Books:'
        for books in self.availableBook:
            print books

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBook:
            print 'You have borrowed: ' ,requestedBook
            self.availableBook.remove(requestedBook)
        else:
            print 'Sorry we dont have this book'

    def addBook(self,returnedBook):
        if returnedBook not in self.availableBook:
            if returnedBook in self.availableBook:
                self.availableBook.append(returnedBook)
                print 'You have added new book: ', returnedBook
            else:
                print 'Please return the correct book'
        else:
            print 'we already have this book'

class Customer():

    def requestBook(self):
        print 'Enter the book name you want to borrow'
        self.book = raw_input()
        return self.book

    def returnBook(self):
        print 'Enter the book name you want to return'
        self.book = raw_input()
        return self.book


library = Library(['English', 'Hindi', 'Maths', 'Science', 'Art'])
customer = Customer()
while True:
    library.inputs()
    userChoice = raw_input('Enter the choices.\n')
    while not userChoice.isdigit():
        print 'You have entered a string'
        library.inputs()
        userChoice = raw_input('Please enter the Numbers.\n')
    if userChoice == '1':
        library.displayAvailableBooks()
    elif userChoice == '2':
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == '3':
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == '4':
        print 'Bye', exit()
    else:
        print 'Wrong Input!'


