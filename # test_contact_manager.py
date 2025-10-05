# test_contact_manager.py

import unittest
import contact_manager
from contact_manager import DuplicateContactError


class TestContactManager(unittest.TestCase):

    def setUp(self):
        """Reset contacts dictionary before each test."""
        contact_manager.contacts.clear()

    def test_add_contact(self):
        """Test adding a new contact successfully."""
        contact_manager.add_contact("Alice", "555-1234")
        self.assertIn("Alice", contact_manager.contacts)
        self.assertEqual(contact_manager.contacts["Alice"], "555-1234")

    def test_find_existing_contact(self):
        """Test finding an existing contact."""
        contact_manager.contacts["Bob"] = "555-5678"
        # Capture printed output using context manager
        with self.assertLogs() as log:
            contact_manager.find_contact("Bob")
        # Check if the contact info was printed (output format)
        self.assertIn("Bob: 555-5678", log.output[0])

    def test_find_nonexistent_contact(self):
        """Test finding a non-existent contact does not crash."""
        try:
            contact_manager.find_contact("Charlie")
        except Exception as e:
            self.fail(f"find_contact() raised an unexpected exception: {e}")

    def test_delete_existing_contact(self):
        """Test deleting an existing contact."""
        contact_manager.contacts["David"] = "555-4321"
        contact_manager.delete_contact("David")
        self.assertNotIn("David", contact_manager.contacts)

    def test_delete_nonexistent_contact(self):
        """Test deleting a non-existent contact doesn't crash."""
        try:
            contact_manager.delete_contact("Eve")
        except Exception as e:
            self.fail(f"delete_contact() raised an unexpected exception: {e}")

    def test_add_duplicate_contact(self):
        """Test adding a duplicate contact raises DuplicateContactError."""
        contact_manager.contacts["Frank"] = "555-8765"
        with self.assertRaises(DuplicateContactError):
            contact_manager.add_contact("Frank", "555-9999")


if __name__ == "__main__":
    unittest.main()
