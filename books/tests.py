# books/tests.py
# This file contains unit tests for the books app.
from django.test import TestCase
from .models import Book

# Create your tests here.
class BookModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Book.objects.create(
            title="Generation P",
            author="Victor Pelevin",
            genre="classic",
            book_type="hardcover",
            price=19.99,
        )
    def setUp(self):
        # Set up a sample book for testing
        self.book = Book.objects.create(
            title="Trainspotting",
            author="Irvine Welsh",
            genre="classic",
            book_type="hardcover",
            price=8.99,
        )

    def test_book_title(self):
        # Test if the book’s title is initialized as expected
        book = Book.objects.get(id=1)    # Get a book object to test
        # Get the metadata for the 'title' field and use it to query its data
        field_label = book._meta.get_field('title').verbose_name     
        self.assertEqual(field_label, 'title')       # Compare the value to the expected result

    def test_author_max_length(self):
           # Test that maximum length of the author field is 128 characters
           book = Book.objects.get(id=1)
           # Get the metadata for the 'author' field and use it to query its max_length
           max_length = book._meta.get_field('author').max_length
           self.assertEqual(max_length, 128)    # Compare the value to the expected result

    def test_book_creation(self):
        # Test that the book was created successfully
        self.assertEqual(self.book.title, "Trainspotting")
        self.assertEqual(self.book.author, "Irvine Welsh")
        self.assertEqual(self.book.price, 8.99)
        self.assertEqual(self.book.genre, "classic")
        self.assertEqual(self.book.book_type, "hardcover")

    def test_book_str_method(self):
        # Test the string representation of the book
        self.assertEqual(str(self.book), "Trainspotting by Irvine Welsh")
