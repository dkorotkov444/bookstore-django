# books/admin.py
# This file registers the Book model with the Django admin site.
from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
