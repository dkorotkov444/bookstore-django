# books/urls.py
from django.urls import path
from .views import books

app_name = 'books'

urlpatterns = [
    path('', books, name='books'),
]