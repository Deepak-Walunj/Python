#library management

class Library:
    no_books=0
    reserve_books_count=0
    no_borrow_count=0
    books={}
    reserve_books={}
    borrow_books={}
    

    def __init__(self,name):
        self.b_name=name
        if self.b_name in Library.books:
            Library.books[self.b_name]+=1
        else:
            Library.books[self.b_name]=1
        Library.no_books+=1

    @staticmethod
    def proper_input(prompt):
        while True:
            user_input=input(prompt)
            if user_input:
                return user_input
            else:
                print('Input cannot be empty, enter valid input')

    @staticmethod
    def show():
            print(f"Currently the library has {Library.no_books} books:")
            for book,count in Library.books.items():
                print(f"{book}:{count}copies")
    
    @staticmethod
    def show_reserve_books():
        print(f"Currently the library has {Library.reserve_books_count} reserved books:")
        for book,user in Library.reserve_books.items():
                print(f"{book}:reserved for {", ".join(user)}")

    @staticmethod
    def show_borrow_books():
        print(f"Currently the library has lended {Library.no_borrow_count} books:")
        for book,user in Library.borrow_books.items():
                print(f"{book}:borrowed by {" ,".join(user)}")

    @staticmethod
    def search(name):
        if name in Library.books:
            return f"Yes the book is present in the Library with {Library.books[name]} copies "
        else:
            return f"The book is not present in the library"

    @staticmethod
    def delete(name):
        if name in Library.books:
            if Library.books[name]>1:
                Library.books[name]-=1
                Library.no_books-=1
            elif Library.books[name]==1:
                Library.books.pop(name)
                Library.no_books-=1
            print(f"{name} deleted successfully")
        else:
            print("Book doesnt exist")
        Library.show()

    @staticmethod
    def borrow(name,c_name):
        if name in Library.books:
            if Library.books[name]>1:
                print(f"borrowed successfully {name} by {c_name}")
                Library.books[name]-=1
            elif Library.books[name]==1:
                print(f"borrowed successfully {name} by {c_name}")
                Library.books.pop(name)
            Library.no_books-=1
        else:
            print('Book is not available')
            
        if name in Library.borrow_books:
            Library.borrow_books[name].append(c_name)
        else:
            Library.borrow_books[name]=[c_name]
        Library.no_borrow_count+=1
        Library.show_borrow_books()
        Library.show()

    @staticmethod
    def Return(name,c_name):
        if name in Library.borrow_books and c_name in Library.borrow_books[name]:
            if name in Library.books:
                Library.books[name]+=1
            else:
                Library.books[name]=1
            Library.no_books+=1
            Library.borrow_books[name].remove(c_name)
            if not Library.borrow_books[name]:
                Library.borrow_books.pop(name)            
            Library.no_borrow_count-=1
        else:
            print("We havent lended this book ")
        Library.show()
        Library.show_borrow_books()

    @staticmethod
    def reserve(b_name,c_name):
        if b_name in Library.books:
            print(f'The book {b_name} is available and is kept reserved for {c_name}')
            if Library.books[b_name]>1:
                Library.books[b_name]-=1
            elif Library.books[b_name]==1:
                Library.books.pop(b_name)
            Library.no_books-=1
        else:
            print("the book is currently unavailable but will be kept reserved and handed once available")
        if b_name in Library.reserve_books:
            Library.reserve_books[b_name].append(c_name)
        else:
            Library.reserve_books[b_name]=[c_name]
        Library.reserve_books_count+=1
        Library.show_reserve_books()
        Library.show()

    @staticmethod
    def renew(b_name,c_name):
        if b_name in Library.borrow_books:
            if c_name in Library.borrow_books[b_name]:
                print(f"Book {b_name} renewed for {c_name}")
            else:
                print(f"{c_name} havent borrowed book {b_name}")
        else:
            print(f'Library hasnt lended {b_name} yet')
            

def main(): 
    while(True):
        try:
            n=int(input("Press\n1)Add a Book to catalog.\n2)Remove a Book from catalog.\n3)Search for a Book by title\n4)Borrow a book from the library.\n5)Return a borrowed Book.\n6)Reserve a Book that are currently checkable or unavailable.\n7)Renew a Book: Extend the borrowing period for a checked-out book.\n8)List All Books of library catalog.\n9)List Books currently available for borrowing.\n10)List Borrowed Books that are currently borrowed.\n11)To exit.\n"))
            if n not in range(12):
                print("Enter between 1-11")
                continue
        except ValueError:
            print("Invalid input ")
            continue
        if n==11:
            print("Thankyou")
            break

        elif n==1:
            while(True):
                n=Library(Library.proper_input("Enter the books to be added into the catalog\n"))
                while True:
                    try:
                        a=int(input("Done with adding? If done press 0 otherwise press 1\n"))
                        if a not in range(2):
                            print("Enter either 0 or 1.")
                        else:
                            break
                    except ValueError:
                        print('Invalid input.Again start from the beginning')
                        continue
                if a==0:
                    break
            Library.show()

        elif n==3:
            try:
                name=Library.proper_input("Enter name of the book you want to search\n")
                if name.isdigit():
                    raise ValueError("Enter a valid book name")
                print(Library.search(name))
            except ValueError:
                print("Enter a valid book name ")

        elif n==2:
            try:
                name=Library.proper_input("Enter the name of book to be deleted\n")
                if name.isdigit():
                    raise ValueError("Enter a valid book name")
                Library.delete(name)
            except ValueError:
                print('Enter a valid book name')

        elif n==4:
            try:
                name=Library.proper_input("Enter the name of the book you want to borrow\n")
                cust_name=Library.proper_input('Enter your name ')
                if name.isdigit():
                    raise ValueError('Enter a valid book name')
                if cust_name.isdigit():
                    raise ValueError('Enter name')                
                Library.borrow(name,cust_name)
            except ValueError:
                print("Enter a valid book name")

        elif n==5:
            try:
                name=Library.proper_input('Enter the name of the book to be returned\n')
                if name.isdigit():
                    raise ValueError('Enter a valid book name')
                Library.Return(name)
            except ValueError:
                print('Enter a valid book name ')

        elif n==6:
            try:
                name=Library.proper_input('Enter the name of the book to be reserved\n')
                cust_name=Library.proper_input("Enter your name\n")
                if name.isdigit():
                    raise ValueError('Enter a valid book name')
                if cust_name.isdigit():
                    raise ValueError('Enter a valid name')
                Library.reserve(name,cust_name)    
            except ValueError:
                print('Enter a valid book name ')

        elif n==7:
            try:
                name=Library.proper_input("Enter the name of the book to be renewed\n")
                cust_name=Library.proper_input("Enter your name\n")
                if name.isdigit():
                    raise ValueError('Enter a valid book name')               
                if cust_name.isdigit():
                    raise ValueError('Enter a valid name')
                Library.renew(name,cust_name)              
            except ValueError:
                print("Enter a valid book name")

        elif n==8:
            Library.show()
            Library.show_borrow_books()
            Library.show_reserve_books()    

        elif n==9:
            Library.show()

        elif n==10:
            Library.show_borrow_books()

if __name__=="__main__":
    main()

