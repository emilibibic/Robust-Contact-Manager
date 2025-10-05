# contact_manager.py

class DuplicateContactError(Exception):
    """Custom exception for duplicate contact entries."""
    pass


contacts = {}


def add_contact(name, phone):
    """Adds a new contact. Raises DuplicateContactError if contact already exists."""
    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Finds and prints a contact's phone number. Handles KeyError if not found."""
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
    """Main loop for the Contact Manager program."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            try:
                add_contact(name, phone)
            except DuplicateContactError as e:
                print(e)

        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)

        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        elif choice == 4:
            print("Exiting Contact Manager.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
