# sales/utils.py
# This file contains utility functions for the sales app.
# It is used to define functions that can be reused across the sales app.
from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from books.models import Book
from .models import Sale

# Function retrieved book title by ID
def get_booktitle_from_id(val):
    try:
        return Book.objects.get(id=val).title
    except Book.DoesNotExist:
        return "Unknown Book"

# Function to convert a matplotlib graph to a format that can be rendered in HTML templates
def get_graph():
   buffer = BytesIO()       # Create a BytesIO buffer for the image         
   # Create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')
   buffer.seek(0)       # Set cursor to the beginning of the stream

   image_png=buffer.getvalue()          # Retrieve the content of the file
   graph=base64.b64encode(image_png)    # Encode the bytes-like object
   graph=graph.decode('utf-8')          # Decode to get the string as output

   buffer.close()       # Free up the memory of buffer
   return graph         # Return the graph in a format that can be rendered in HTML templates

# Function to generate different types of charts based on user input
#       - chart_type: user input,
#       - data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    # AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(6,3))        # Specify figure size

    # Select chart_type based on user input from the form
    if chart_type == '#1':
        # Plot bar chart between date on x-axis and quantity on y-axis
        plt.bar(data['date_created'], data['quantity'])

    elif chart_type == '#2':
        # Generate pie chart based on the amount. The book titles are sent from the view as labels
        labels=kwargs.get('labels')
        plt.pie(data['amount'], labels=labels)

    elif chart_type == '#3':
        # Plot line chart based on date on x-axis and amount on y-axis
        plt.plot(data['date_created'], data['amount'])
    else:
        print ('Unknown chart type')

    plt.tight_layout()      # Specify layout details
    chart =get_graph()      # Render the graph to file
    return chart  

# Function to explore querysets and understand the output of different queryset methods
def explore_querysets(book_title):
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
