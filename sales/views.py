# sales/views.py
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Sale
from .forms import SalesSearchForm
from .utils import get_chart, explore_querysets


# Create your views here.
# Function-based view to display homepage
def home(request):
    return render(request, 'sales/home.html')

# Function-based view records()
@login_required
def records(request):
    sales_df = None                 # Initialize the variable sales_df to None
    chart = None                    # Initialize the variable chart to None

    # Check if the button is clicked
    if request.method =='POST':
        form = SalesSearchForm(request.POST)        # Create an instance of the SalesSearchForm class and assign it to the variable form
        # Read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        #--- DEBUG --- Display in terminal
        print (book_title, chart_type)

        # Apply filter to extract sales data for the selected book title
        qs =Sale.objects.filter(book__title=book_title)
        if qs.exists():          # If data found, convert the queryset to pandas DataFrame
            sales_df = pd.DataFrame(qs.values())
            sales_df['book_id']=book_title          # Directly overwrite book_id with book_title since we already have the book title
            # Rename 'book_id' to 'Book Title' and 'id' to 'Sale ID' (or any others)
            sales_df.rename(columns={'book_id': 'Book Title', 'id': 'Sale ID'}, inplace=True)
            sales_df=sales_df.to_html(index=False)             # Convert the DataFrame to HTML format for rendering in the template, removing line numbers (index=False)

            # Generate chart
            chart = get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)

            # --- DEBUG --- EXPOLRE QUERYSETS ---
            explore_querysets()       # Call the function to explore querysets and understand the output of different queryset methods

    else:
        form = SalesSearchForm()       # If the button is not clicked, create an instance of the SalesSearchForm class and assign it to the variable form

    # Create a context dictionary to pass the form and sales_df variables to the template
    context = {
        'form': form,
        'sales_df': sales_df,
        'chart': chart
    }        

    # Render the 'sales/records.html' template with the context dictionary and return the resulting HttpResponse object
    return render(request, 'sales/records.html', context)