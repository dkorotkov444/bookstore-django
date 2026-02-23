# sales/views.py
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Sale
from .forms import SalesSearchForm
# from .utils import get_booktitle_from_id


# Create your views here.
# Function-based view to display homepage
def home(request):
    return render(request, 'sales/home.html')

# Function-based view records()
@login_required
def records(request):
    form = SalesSearchForm()        # Create an instance of the SalesSearchForm class and assign it to the variable form
    sales_df = None                 # Initialize the variable sales_df to None

    # Check if the button is clicked
    if request.method =='POST':
        # Read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        #--- DEBUG --- Display in terminal
        print (book_title, chart_type)

        # Apply filter to extract sales data for the selected book title
        qs =Sale.objects.filter(book__title=book_title)
        if qs.exists():          # If data found, convert the queryset to pandas DataFrame
            sales_df = pd.DataFrame(qs.values())

            #sales_df['book_id']=sales_df['book_id'].apply(get_booktitle_from_id)     # Convert book_id to book title using the get_booktitle_from_id function
            sales_df['book_id']=book_title          # Directly overwrite book_id with book_title since we already have the book title
            # Rename 'book_id' to 'Book Title' and 'id' to 'Sale ID' (or any others)
            sales_df.rename(columns={'book_id': 'Book Title', 'id': 'Sale ID'}, inplace=True)

            sales_df=sales_df.to_html(index=False)             # Convert the DataFrame to HTML format for rendering in the template, removing line numbers (index=False)

    # --- Explore querysets ---
    #print ('Exploring querysets:')
    #print ('\nCase 1: Output of Sale.objects.all()')
    #qs=Sale.objects.all()
    #for item in qs:
    #    print (item)

    #print ('\nCase 2: Output of Sale.objects.filter(book__title=book_title)')
    #qs =Sale.objects.filter(book__title=book_title)
    #for item in qs:
    #    print (item)

    #print ('\nCase 3: Output of qs.values')
    #for item in qs.values():
    #    print (item)

    #print ('\nCase 4: Output of qs.values_list()')
    #for item in qs.values_list():
    #    print (item)

    #print ('\nCase 5: Output of Sale.objects.get(id=1)')
    #obj = Sale.objects.get(id=1)
    #for field in obj._meta.fields:
    #    print (f'{field.name}: {getattr(obj, field.name)}')
    # -------------------------------------------------------

    # Create a context dictionary to pass the form and sales_df variables to the template
    context = {
        'form': form,
        'sales_df': sales_df
    }        

    # Render the 'sales/records.html' template with the context dictionary and return the resulting HttpResponse object
    return render(request, 'sales/records.html', context)