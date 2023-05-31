# Define the knowledge base
books = {
    "001": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "ISBN": "978-0743273565",
        "publisher": "Scribner"
    },
    "002": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "ISBN": "978-0446310789",
        "publisher": "J. B. Lippincott & Co."
    },
    "003": {
        "title": "1984",
        "author": "George Orwell",
        "ISBN": "978-0451524935",
        "publisher": "Signet Classics"
    }
}

# Define the rules
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    ISBN = input("Enter book ISBN: ")
    publisher = input("Enter book publisher: ")
    books[book_id] = {"title": title, "author": author, "ISBN": ISBN, "publisher": publisher}
    print("Book added successfully.")

def view_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        print(f"Title: {books[book_id]['title']}")
        print(f"Author: {books[book_id]['author']}")
        print(f"ISBN: {books[book_id]['ISBN']}")
        print(f"Publisher: {books[book_id]['publisher']}")
    else:
        print("Book not found.")

def search_book():
    query = input("Enter search query: ")
    found_books = []
    for book_id, book in books.items():
        if query in book.values():
            found_books.append(book_id)
    if found_books:
        for book_id in found_books:
            print(f"Title: {books[book_id]['title']}")
            print(f"Author: {books[book_id]['author']}")
            print(f"ISBN: {books[book_id]['ISBN']}")
            print(f"Publisher: {books[book_id]['publisher']}")
    else:
        print("No books found.")

def delete_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        del books[book_id]
        print("Book deleted successfully.")
    else:
        print("Book not found.")

# Create the expert system
def expert_system():
    while True:
        print("Welcome to the library!")
        print("Enter 1 to add a book.")
        print("Enter 2 to view a book.")
        print("Enter 3 to search for a book.")
        print("Enter 4 to delete a book.")
        print("Enter 5 to exit.")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Test the system
expert_system()

'''
This code implements a simple library management system using a knowledge base and a set of rules. It allows users to add books, view book details, search for books, and delete books from the library. Let's go through the code step by step:

1. The code starts by defining a dictionary called `books`, which serves as the knowledge base. Each book in the library is represented by a unique book ID, and the corresponding details such as title, author, ISBN, and publisher are stored in nested dictionaries.

2. Four functions are defined to implement the rules of the library management system:
   - `add_book()` prompts the user to enter book details and adds the book to the `books` dictionary using the provided book ID as the key.
   - `view_book()` asks the user to input a book ID and displays the details of the corresponding book if it exists in the `books` dictionary.
   - `search_book()` prompts the user to enter a search query and searches for books in the `books` dictionary that match the query. It then displays the details of the found books.
   - `delete_book()` asks the user to enter a book ID and removes the corresponding book from the `books` dictionary if it exists.

3. The `expert_system()` function acts as the main driver of the library management system. It continuously displays a menu and prompts the user to choose an option. Depending on the chosen option, it calls the corresponding function to perform the desired action.

4. Inside the `expert_system()` function, a while loop runs indefinitely until the user chooses to exit by entering "5". The loop repeatedly displays the menu, takes user input, and performs the corresponding action based on the chosen option.

5. When the user selects an option, the appropriate function is called to carry out the requested operation.

6. The `expert_system()` function also handles an invalid choice by displaying an error message and asking the user to try again.

7. Finally, the `expert_system()` function is called to start the library management system.

The code provides a basic interactive interface for users to add, view, search, and delete books from the library. It utilizes a dictionary as a knowledge base to store and retrieve book details based on user actions.
'''