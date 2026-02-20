# bookstore/views.py

from django.shortcuts import render, redirect               # Django functions for rendering templates and redirecting
from django.contrib.auth import authenticate, login         # Django authentication libraries   
from django.contrib.auth.forms import AuthenticationForm    # Django Form for authentication

# Function-based view for handling login requests
def login_view(request):  
    error_message = None            # Default error message for invalid login          
    form = AuthenticationForm()     # Create an instance of the AuthenticationForm class

    if request.method == 'POST':        # Check if the request method is POST
        form = AuthenticationForm(request, data=request.POST)       # Create an instance of the AuthenticationForm class with the POST data
        if form.is_valid():                                         # Check if the form is valid
            username = form.cleaned_data.get('username')            # Get the username from the cleaned data
            password = form.cleaned_data.get('password')            # Get the password from the cleaned data
            user = authenticate(username=username, password=password)   # Authenticate the user
            if user is not None:                                    # i.e. the user is authenticated
                login(request, user)                                # Use pre-defined Django function to login
                return redirect('sales:records')                    # Redirect to a success page.
        else:
            error_message = 'Invalid username or password.'     # Set error message for invalid login
    
    # Prepare data to send from view to template
    context ={                                             
        'form': form,                               # send the form data
        'error_message': error_message              # and the error_message
    }

    # Load the login page using "context" information
    return render(request, 'auth/login.html', context) 