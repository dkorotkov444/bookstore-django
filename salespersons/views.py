# salespersons/views.py
from django.shortcuts import render

# Create your views here.
def salesperson(request):
    return render(request, 'salespersons/salesperson.html')
