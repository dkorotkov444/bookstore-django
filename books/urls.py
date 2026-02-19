# books/urls.py
from django.urls import path
from .views import BooksListView, BookDetailView   # Import the views for listing books and showing book details

app_name = 'books'

urlpatterns = [
    path('list/', BooksListView.as_view(), name='list'),    # Call .as_view() for class-based views
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),  # URL pattern for book details, using primary key (pk)
]