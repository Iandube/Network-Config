# INFO-1298 Python
# Project 1
# Author: Ian Dube
# This Program implements a personal book library system.
from datetime import date
current_year = date.today().year


Library = {
    "1984": {
        "Author": "George Orwell",
        "year": 1949,
        "isbn": "9780451524935"
},
    "Dune": {
        "Author": "Frank Herbert",
        "year": 1965,
        "isbn": "9780441172719"
},
    "The Hobbit": {
        "Author": "J.R.R. Tolkien",
        "year": 1937,
        "isbn": "9780547928227"
    },
}

def add_book(Library, current_year):
    book_name = input("Please enter the Book name you would like to add: ")
    if book_name in Library:
        print("This book is already in the library. ")
        return
    elif book_name == "":
        print("The book name can't be blank.")
        return
    else:
        author = input("What is the Author's name?: ")
    if author == "":
        print("The Authors name can't be blank.")
        return
    else:
        pub_year = int(input("What is the publication year?: "))
    if pub_year <1000 or pub_year > current_year + 1:
        print("Please enter a valid date.")
        return
    else:
        isbn = int(input("What is the isbn of the book?: "))
        isbnlength = str(isbn)
    if len(isbnlength) <10:
        print("The isbn must be 10 or more")
        return
    elif isbnlength =="":
        print("isbn can't be blank")
    else:
        choice = input("Is all this information correct?: \nY/N ")
    if choice == "Y":
        Library[book_name] = {
            "Author": author,
            "Publication Year": pub_year,
            "isbn": isbn
        }
        print("The book has been added.")
        return
    else:
        print("The book has not been added.")
        return
def update_Author(Library):
    book_title = input("What book would you like to change the author of?: ")
    if book_title not in Library:
        print("This book is not in the library.")
        return
    else:
        author_change = input("What is the author you would like to change it to?: ")
    if author_change == "":
        print("The author name can't be blank.")
        return
    else: 
        Library[book_title]["Author"] = author_change
        print("The author has been successfully changed.")
        return
def update_year(Library, current_year):
    book_check = input("What is the book you would like to change?: ")
    if book_check not in Library:
        print("The book is not in the library.")
        return
    else:
        year_change = int(input("What year would you like to change it to?: "))
        if year_change <1000 or year_change > current_year + 1:
            print("This is not a valid date.")
            return
        else:
            Library[book_check]["year"] = year_change
            print("The Book's year has been changed.")
            return
def title_search(Library):
    book_search = input("What is the title of the book you would like to search for?: ")
    if book_search not in Library:
        print("This book is not in the Library.")
        return
    else:
        print("Here is the Book you were looking for.")
        print(Library[book_search])
        return
def delete_book(Library):
    book_search = input("What book would you like to delete?: ")
    if book_search not in Library:
        print("The book is not in the library or is already deleted.")
        return
    else:
        verification = input("Are you sure you want to delete this book?\n Y/N: ")
    if verification =="Y":
        del Library[book_search]
        print("Book Has been Deleted")
        return
    else:
        print("Deletion Cancelled.")
        return
def book_sort(Library):
    print("Books sorted by title:")
    for title in sorted(Library):
        print("Title:", title)
        print("Author:", Library[title]["Author"])
        print("year:", Library[title]["year"])
        print("isbn:", Library[title]["isbn"])
        print("")
    return
        


while True:
    print("Library Menu:")
    print("1. Add a book")
    print("2. Update a book’s author")
    print("3. Update a book’s publication year")
    print("4. Search for a book by title")
    print("5. Delete a book")
    print("6. Display all books (sorted by title)")
    print("7. Exit")

    user_choice = input("Choose an option (1-7): ")

    if user_choice == "1":
        add_book(Library, current_year)

    elif user_choice == "2":
        update_Author(Library)

    elif user_choice == "3":
        update_year(Library, current_year)

    elif user_choice == "4":
        title_search(Library)

    elif user_choice == "5":
        delete_book(Library)

    elif user_choice == "6":
        book_sort(Library)
    
    elif user_choice == "7":
        verification = input("Are you sure you would like to exit? \nY/N: ")
        if verification =="Y":
            print("Thank you for your time.")
            break
        else:
            continue
    
    else:
        print("This is not a valid option, please select a different option.")
