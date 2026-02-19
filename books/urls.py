# books/urls.py
from django.urls import path
from .views import BooksListView

app_name = 'books'

urlpatterns = [
    path('list/', BooksListView.as_view(), name='list'),    # Call .as_view() for class-based views
]