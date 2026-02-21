# sales/urls.py
from django.urls import path
from .views import home, records

app_name = 'sales'

urlpatterns = [
    path('', home, name='home'),
    path('sales/', records, name='sales_records'),
]