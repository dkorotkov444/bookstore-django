# sales/views.py
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sale
from .forms import SalesSearchForm


# Create your views here.
# Function-based view to display homepage
def home(request):
    return render(request, 'sales/home.html')

# Function-based view records()
@login_required
def records(request):
    form = SalesSearchForm()        # Create an instance of the SalesSearchForm class and assign it to the variable form

    # Check if the button is clicked
    if request.method =='POST':
        # Read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        #--- DEBUG --- Display in terminal
        print (book_title, chart_type)

    # --- DEBUG --- Explore querysets
    print ('Exploring querysets:')
    print ('\nCase 1: Output of Sale.objects.all()')
    qs=Sale.objects.all()
    for item in qs:
        print (item)

    print ('\nCase 2: Output of Sale.objects.filter(book__title=book_title)')
    qs =Sale.objects.filter(book__title=book_title)
    for item in qs:
        print (item)

    print ('\nCase 3: Output of qs.values')
    for item in qs.values():
        print (item)

    print ('\nCase 4: Output of qs.values_list()')
    for item in qs.values_list():
        print (item)

    print ('\nCase 5: Output of Sale.objects.get(id=1)')
    obj = Sale.objects.get(id=1)
    for field in obj._meta.fields:
        print (f'{field.name}: {getattr(obj, field.name)}')
    # -------------------------------------------------------------------------------------------

    context = {'form': form}        # Create a context dictionary with the key 'form' and the value of the form instance

    # Render the 'sales/records.html' template with the context dictionary and return the resulting HttpResponse object
    return render(request, 'sales/records.html', context)