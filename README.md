# Contact Manager – Debugging and Error Handling Project

## Overview
This project demonstrates debugging, exception handling, and unit testing in Python.  
It begins with a **buggy script** (`buggy_contacts.py`) and evolves into a **fully functional and robust contact management program** (`contact_manager.py`) supported by **automated unit tests** (`test_contact_manager.py`).

---

## Files Included
- **buggy_contacts.py** – The original script containing the initial bugs.
- **contact_manager.py** – The corrected and refactored version with improved error handling and input validation.
- **test_contact_manager.py** – Unit tests created using Python’s `unittest` framework to verify that all functions work as intended.

---

## Bugs Identified and Fixed
### 1. KeyError in `find_contact()`
**Problem:** The program crashed when trying to find a contact that did not exist.  
**Fix:** Added a `try/except KeyError` block to handle missing contacts and print `"Contact not found."`.

### 2. KeyError in `delete_contact()`
**Problem:** The program crashed when attempting to delete a non-existent contact.  
**Fix:** Added a `try/except KeyError` block to handle missing contacts gracefully.

### 3. Unhandled Invalid Input
**Problem:** Entering a non-numeric menu choice (like a letter) caused a crash.  
**Fix:** Added a `try/except ValueError` block to validate menu input and display a user-friendly message.

### 4. Duplicate Contact Entries
**Problem:** Adding a contact with an existing name overwrote the previous entry.  
**Fix:** Created a custom exception class `DuplicateContactError` and raised it if the contact already exists.  
The main function now catches this exception and prints a helpful message.

---

## How to Run the Program

1. **Open a terminal or command prompt** in the project folder.
2. Run the main contact manager:
   ```bash
   python contact_manager.py
