# sales/views.py
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# Function-based view to display homepage
def home(request):
    return render(request, 'sales/home.html')

# Function-based view records()
@login_required
def records(request):
    return render(request, 'sales/records.html')