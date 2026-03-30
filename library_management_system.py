# library system 
import os 
import json
import datetime

class Book:
    def __init__(self,book_id,author,title,quntity):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.quantity = quntity

    # to conver list to string
    def to_dict(self):
        return{
            'book_id' : self.book_id,
            'author' : self.author,
            'title' : self.title,
            'quantity' : self.quantity,
            }

    @staticmethod
    def from_dict(data):
        """Create Book object from dictionary."""
        book = Book(data["book_id"], data["title"], data["author"], data["quantity"])
        return book
    

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} (Total: {self.quantity}"

class library:

    def __init__(self,books_file = 'library.json'):
        self.books_file = books_file
        self.books = []
        self.load_data()

    
    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file,'r') as f:

                book_data = json.load(f)
                self.books = [Book.from_dict(b) for b in book_data]


    def save_data(self):
        """Save books and transactions to JSON files."""
        with open(self.books_file, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)



    
    #add book
    def add_book(self,book_id,author,title,quantity=1):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += quantity
                print(f"Added one more copies , title is {title},and total quantity is {book.quantity}")
                self.save_data()
                return

        new_book = Book(book_id, title, author, quantity)
        self.books.append(new_book)
        print(f"✅ Book '{title}' added successfully.")
        self.save_data()
        
    # remove book
    def remove_book(self,bid):
        for book in self.books:
            if book.book_id == bid:
                self.books.remove(book)
                print(f"🗑️ Book '{book.title}' removed from library.")
                self.save_data()
                return

            else:
                print("not found book")
                return


    def view_all_books(self):
        for book in self.books:
            print(f"===============  Here is All book and Author Name ===========")
            print(f"{book}")
    

    def search_book(self,keyword):
        keyword = keyword.lower()
        result = [b for b in self.books if keyword in b.title.lower()or keyword in b.author.lower()]


        if result:

            for i in result:
                print(i)
        else :
            print("not found any author or book")

    def issued_book(self,username,bookid):
        for book in self.books:
            if book.book_id == bookid:
                print("=== Book is Available ==")
                issue_days = datetime.date.today().isoformat()
                self.save_data()
                print(f"📘 Book '{book.title}' issued to {username}.")
                return
            
            else:
                 
                print(f"❌ No copies available for '{book.title}'.")
                return
        print("==== Not Found Book ==")

def main():

    lib = library()
    
    while True:
        print("\n" + "="*50)
        print("         📚 LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. Issue Book")
        print("5. View All Books")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            try:
                book_id = input("Enter book id   ")
                author = input("Enter author     ")
                title  = input("Enter title of book   ")
                quantity = int(input("Enter quantity of book   "))
                lib.add_book(book_id,author,title,quantity)
            except ValueError as ve:
                print("❌ Qunatity is number")
        
        elif choice == '2':
            bid = input("Enter book id for remove   ")
            lib.remove_book(bid)
        
        elif choice == '3':
            s_book = input("Enter author or title of book whose you search   ")
            lib.search_book(s_book)

        elif choice == '4':
            lib.view_all_books()
            u_name = input("Enter your name   ")
            bid = input("Enter bid for issued  ")
            lib.issued_book(u_name,bid)
        
        elif choice == '5':
            lib.view_all_books()


        elif choice == '6':
            print(f"Thank for joing library")
            break
        else:
            print("Wrong input enter vaild number of choice")

if __name__ == '__main__':
    main()