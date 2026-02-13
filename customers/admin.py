# customers/admin.py
# This file registers the Customer model with the Django admin site.

from django.contrib import admin
from .models import Customer

# Register your models here.
admin.site.register(Customer)