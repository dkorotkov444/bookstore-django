# sales/utils.py
# This file contains utility functions for the sales app.
# It is used to define functions that can be reused across the sales app.

from books.models import Book

# Function retrieved book title by ID
def get_booktitle_from_id(val):
    try:
        return Book.objects.get(id=val).title
    except Book.DoesNotExist:
        return "Unknown Book"