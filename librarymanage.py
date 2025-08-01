# Library Management System

class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "borrowed" if self.borrowed else "Available"
        return F"{self.title} by {self.author} is {status}"
    
class library :
    def __init__(self):
        self.books = []

    def addbooks(self,title,author):
        self.books.append(book(title, author))
        print(f"{title} added to the library .")

    def viewbooks(self):
        if not self.books:
            print("no books in Library")
        else:
            print("Library Collection")
            for index, book in enumerate(self.books,1):
                print(f"{index}. {book}")

    def borrowbook (self,title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.borrowed:
                book.borrowed = True
                print(f"you borrowed {book.title}")
                return
            print(f"book {title} is not available")

    def returnbook(self,title):
        for book in self.books:
            if book.title.lower()==title.lower() and not book.borrowed:
                book.borrowed = False
                print(f"you returned {book.title}")
                return
            print(f"book {title} was not borrowed")


def main():
    lib = library()
    while True:
        print("\n📖 Library Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input('enter your choice (1-5): ')

        if choice == '1':
            title = input("enter the title of book ")
            author = input("Enter author name: ")
            lib.addbooks(title, author)
        elif choice =='2':
            lib.viewbooks()
        elif choice == '3':
            title = input('enter the book you want to borrow: ')
            lib.borrowbook(title)
        elif choice == '4':
            title = input("enter the book title you want to return: ")
            lib.returnbook(title)
        elif choice == '5':
            print("exiting library system .")
            break
        else:
            print("invalid choice. ")

if __name__ == "__main__":
    main()            
               


                                       
          