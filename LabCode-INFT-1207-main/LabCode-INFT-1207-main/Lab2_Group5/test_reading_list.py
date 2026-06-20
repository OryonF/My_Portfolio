import csv
import unittest
from Lab2_Oryon_Jayce import add_book, list_books, search_book, delete_book


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        # Test adding a book
        add_book("Super_Coolbros", "Nintenfake", 1991)
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        # important to know that when the data has been entered in the csv file
        # it becomes a string regards of it's past data type.
        self.assertIn(["Super_Coolbros", "Nintenfake", "1991"], rows)

    # Tests that the search function returns values properly
    def test_search_book(self):
        """Test searching for an existing book."""
        output_result = search_book("Super_Coolbros")  # Now it returns a value
        expected_output = "Found: Title: Super_Coolbros, Author: Nintenfake, Year: 1991"
        self.assertEqual(output_result, expected_output, "Book not found")

    # Tests that books are listed properly
    def test_list_books(self):
        output_result = list_books()
        books = []
        with open("books.csv", mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                books.append(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
        expected_output =  "\n".join(books)
        self.assertEqual(output_result, expected_output)

    # Tests that "delete me" book is deleted
    def test_delete_books(self):
        add_book("Delete me", "Test author", 2025)
        delete_book("Delete me")
        result = search_book("Delete me")
        self.assertEqual(result, "Book not found")

    # Tests that null title is not taken as input
    def test_null_title(self):
        self.assertEqual(add_book("", "test null title", 2025),
                         "Input cannot be null.")

    # Tests that null author is not taken as input
    def test_null_author(self):
        self.assertEqual(add_book("test null author", "", 2025),
                         "Input cannot be null.")

    # Tests that null year is not taken as input
    def test_null_year(self):
        self.assertEqual(add_book("test null year", "test null year author", ""),
                         "Input cannot be null.")

    # Tests that the year is not taken as input if it's not a digit
    def test_year_not_numeric(self):
        self.assertEqual(add_book("test alpha year", "test alpha year author", "year"),
                         "Year must be a digit.")

    # Tests that the year 2026 is not taken as input
    def test_year_high(self):
        self.assertEqual(add_book("test year too high", "year too high author", 2026),
                         "Please enter a valid year.")

    # Tests that the year -500 is not taken as input
    def test_year_low(self):
        self.assertEqual(add_book("test year too low", "year too low author", -500),
                         "Please enter a valid year.")


if __name__ == '__main__':
    unittest.main()