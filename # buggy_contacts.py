# simple_bug_fixer.py

contacts = {}

def add_contact(name, phone):
    """Adds a new contact to the contacts dictionary."""
    contacts[name] = phone
    print(f"Added {name} to contacts.")

def find_contact(name):
    """Finds and prints the contact's phone number. Handles KeyError if contact not found."""
    try:
        print(f"{name}: {contacts[name]}")
    except KeyError:
        print("Contact not found.")

def delete_contact(name):
    """Deletes a contact. Handles KeyError if contact does not exist."""
    try:
        del contacts[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")

def main():
    """Runs a simple contact manager program with add, find, and delete options."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
