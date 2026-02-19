# books/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView      # Import ListView and DetailView for class-based views
from .models import Book

# Create your views here.
class BooksListView(ListView):          # class-based view to display a list of books
    model = Book                        # specify the model to use for this view
    template_name = 'books/main.html'   # specify the template to render
    context_object_name = 'books'       # specify the context variable name to use in the template

class BookDetailView(DetailView):      # class-based view to display details of a single book
    model = Book                        # specify the model to use for this view
    template_name = 'books/detail.html' # specify the template to render
    context_object_name = 'book'        # specify the context variable name to use in the template