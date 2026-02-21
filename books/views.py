# books/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView      # Import ListView and DetailView for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin  # Import LoginRequiredMixin to restrict access to authenticated users
from .models import Book

# Create your views here.
class BooksListView(LoginRequiredMixin,ListView):          # Protected class-based view to display a list of books
    model = Book                            # specify the model to use for this view
    template_name = 'books/main.html'       # specify the template to render
    context_object_name = 'books'           # specify the context variable name to use in the template

class BookDetailView(LoginRequiredMixin,DetailView):      # class-based view to display details of a single book
    model = Book                            # specify the model to use for this view
    template_name = 'books/detail.html'     # specify the template to render
    context_object_name = 'book'            # specify the context variable name to use in the template