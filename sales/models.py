# salespersons/models.py
# This file defines the Salesperson model for the bookstore application.
from django.db import models
from books.models import Book

# Sale model
class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)  # Number of books sold (of the same type within a transaction)
    amount = models.DecimalField(max_digits=10, decimal_places=2)               # Total sale amount for the transaction
    date_created = models.DateTimeField(auto_now_add=True)                      # Date of sale - will be automatically set to the current date

    def __str__(self):
        return f"ID: {self.id}, book: {self.book.title}, quantity: {self.quantity}, amount: $ {self.amount}"
