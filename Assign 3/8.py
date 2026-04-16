'''
basic library management system that allows users 
to search, borrow, and return books with logic to prevent 
re-borrowing already borrowed books.
'''
import os

class Library:
    def __init__(self, filename="library.txt"): #assigning filename directly in the constructor for better encapsulation
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: 
                pass # Create the file if it doesn't exist

    def search_book(self, title):
        try:
            with open(self.filename, "r") as f: # Search for the book by title (case-insensitive)
                for line in f:
                    if title.lower() in line.lower(): #turning to lower case
                        return line.strip()
            return None # Return None if no match found
        except Exception as e:
            print(f"Error searching: {e}")

    def update_book_status(self, full_title, borrow=True): #borrow=True for borrowing, False for returning
        books = []
        found = False
        updated = False
        
        try:
            with open(self.filename, "r") as f: # Read all lines to find the book and update its status
                lines = f.readlines()

            for line in lines:
                if not line.strip(): continue
                t, a, b = line.strip().split("|") #format of stored data Title|Author|BorrowedStatus
                
                # Use exact match for the full title to ensure the right book is updated
                if t.lower() == full_title.lower():
                    found = True
                    # Check current status before updating
                    if borrow and b == "True":
                        print(f"Error: '{t}' is already borrowed.")
                    elif not borrow and b == "False":
                        print(f"Error: '{t}' is already in the library.")
                    else:
                        b = "True" if borrow else "False"
                        updated = True # Mark as updated to trigger file rewrite
                
                books.append(f"{t}|{a}|{b}\n")
            
            if updated:
                with open(self.filename, "w") as f:
                    f.writelines(books)
                status = "borrowed" if borrow else "returned"
                print(f"Success: You have {status} '{full_title}'.")
            elif not found:
                print("Error: Book not found in the database.")
                
        except Exception as e:
            print(f"Error updating file: {e}")

# --- Execution ---
lib = Library()

""" causing problem
# Pre-writing data if empty for testing
if os.stat("library.txt").st_size == 0:
    with open("library.txt", "w") as f:
        f.write("The Great Gatsby|F. Scott Fitzgerald|False\n")
        f.write("1984|George Orwell|False\n")
        f.write("Howls Moving Castle|Diana Wynne Jones|False\n")
        f.write("The Hobbit|J.R.R. Tolkien|False\n")
        f.write("To Kill a Mockingbird|Harper Lee|False\n")
"""

print("--- Library System ---")
search_term = input("Enter book title to search: ")
result = lib.search_book(search_term)

if result:
    # Split the result to get the actual full title from the file
    full_title, author, status = result.split("|") #line 36
    print(f"Found: {full_title} by {author} (Borrowed: {status})")
    
    action = input("Would you like to (B)orrow or (R)eturn? ").upper()
    if action == 'B': #borrowing
        lib.update_book_status(full_title, borrow=True)
    elif action == 'R': #returning
        lib.update_book_status(full_title, borrow=False)
else:
    print("Sorry, we don't have that book.")