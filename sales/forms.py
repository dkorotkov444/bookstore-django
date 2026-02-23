# sales/forms.py

from django import forms
from .models import Sale

# Specify choices for the chart type as a tuple of tuples, where each inner tuple contains a value and a human-readable name
CHART__CHOICES = (
   ('#1', 'Bar chart'),
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

# Class-based Form imported from Django forms
class SalesSearchForm(forms.Form): 
   book_title= forms.CharField(max_length=128)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)