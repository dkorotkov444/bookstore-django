# sales/urls.py
from django.urls import path
from .views import records

app_name = 'sales'

urlpatterns = [
    path('', records, name='records'),
]