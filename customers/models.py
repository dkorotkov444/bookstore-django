# customers/models.py
# This file defines the Customer model for the bookstore application.

from django.db import models

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    notes = models.TextField(blank=True, null=True)     # Any notes the customer wants to make

    def __str__(self):
        return self.name