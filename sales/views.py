# sales/views.py
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm

# Create your views here.
# Function-based view to display homepage
def home(request):
    return render(request, 'sales/home.html')

# Function-based view records()
@login_required
def records(request):
    form = SalesSearchForm()        # Create an instance of the SalesSearchForm class and assign it to the variable form
    context = {'form': form}        # Create a context dictionary with the key 'form' and the value of the form instance
    # Render the 'sales/records.html' template with the context dictionary and return the resulting HttpResponse object
    return render(request, 'sales/records.html', context)